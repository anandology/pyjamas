#!/usr/bin/env python

import sys
import compiler
from optparse import OptionParser
from os.path import join, dirname, basename, abspath, exists
from StringIO import StringIO

import PyV8

from IPython.iplib import InteractiveShell, softspace
from IPython.Shell import IPShellEmbed, make_IPython, ipapi, kill_embedded, ultraTB

from pyv8run import Global

currentdir = abspath(dirname(dirname(__file__)))
currentdir = abspath(dirname(__file__))
pyjspth = abspath(join(dirname(__file__), ".."))
sys.path = [(join(pyjspth, "pyjs", "src"))] + sys.path

import pyjs
from pyjs import translator

class V8InteractiveShell(InteractiveShell):
    _js_int = None
    _is_native = False
    _show_js = False
    def runsource(self, source, filename='<input>', symbol='single'):
        if self._is_native:
            return InteractiveShell.runsource(self, source, filename, symbol)
        source=source.encode(self.stdin_encoding)
        if source[:1] in [' ', '\t']:
            source = 'if 1:\n%s' % source
        try:
            code = self.compile(source, filename, symbol)
        except (OverflowError, SyntaxError, ValueError, TypeError, MemoryError):
            # Case 1
            self.showsyntaxerror(filename)
            return None
        if code is None:
            # Case 2
            return True
        
        # Case 3
        #print "\n Code to translate:\n" + source + "\n"
        if source.startswith('_ip.'):
            # This is IPython Magick stuff. Run in native interpreter:
            return InteractiveShell.runsource(self, source, filename, symbol)
        # Translate
        jscode, imppy, impjs = self._js_int.interactive_translate(source)
        self.code_to_run = jscode
        if self._show_js:
            print "\n Translated JS:\n" + jscode + "\n"
        # now actually execute the code object
        if self._js_int.evaluate(jscode) == 0:
            return False
        else:
            return None
    
    def runcode(self,code_obj):
        old_excepthook,sys.excepthook = sys.excepthook, self.excepthook
        self.sys_excepthook = old_excepthook
        outflag = 1  # happens in more places, so it's easier as default
        try:
            try:
                self.hooks.pre_runcode_hook()
                exec code_obj in self.user_global_ns, self.user_ns
            finally:
                # Reset our crash handler in place
                sys.excepthook = old_excepthook
        except SystemExit:
            self.resetbuffer()
            self.showtraceback()
            warn("Type %exit or %quit to exit IPython "
                 "(%Exit or %Quit do so unconditionally).",level=1)
        except self.custom_exceptions:
            etype,value,tb = sys.exc_info()
            self.CustomTB(etype,value,tb)
        except:
            self.showtraceback()
        else:
            outflag = 0
            if softspace(sys.stdout, 0):
                print
        # Flush out code object which has been run (and source)
        self.code_to_run = None
        return outflag
    
    def _set_js_int(self, js_int):
        self._js_int = js_int
        
    def magic_native(self, p):
        self._is_native = True
        print "Switched to native interpreter"
    
    def magic_pyjs(self, p):
        self._is_native = False
        print "Switched to PyJS/PyV8 interpreter"
        
    def magic_showjs(self, p):
        f = False
        if p.lower() == 'true':
            f = True
        elif p == '1':
            f = True
        elif not p:
            f = True
        self._show_js = f
        if f:
            print "Showing translated JS"
        else:
            print "Not showing translated JS"
            
def generate_prompt(is_continuation):
    """ calculate and return a string with the prompt to display """
    if not is_continuation:
        return '>>> '
    return '... '


class V8ShellEmbed(IPShellEmbed):
    def __init__(self,argv=None,banner='',exit_msg=None,rc_override=None,
                 user_ns=None):
        self.set_banner(banner)
        self.set_exit_msg(exit_msg)
        self.set_dummy_mode(0)
        self.sys_displayhook_ori = sys.displayhook
        try:
            self.sys_ipcompleter_ori = sys.ipcompleter
        except:
            pass # not nested with IPython
        self.IP = make_IPython(argv,rc_override=rc_override,
                               embedded=True,
                               user_ns=user_ns, 
                               shell_class=V8InteractiveShell)
	
        ip = ipapi.IPApi(self.IP)
        ip.expose_magic("kill_embedded",kill_embedded)
        self.sys_displayhook_embed = sys.displayhook
        sys.displayhook = self.sys_displayhook_ori
        sys.excepthook = ultraTB.FormattedTB(color_scheme = self.IP.rc.colors,
                                             mode = self.IP.rc.xmode,
                                             call_pdb = self.IP.rc.pdb)
        self.restore_system_completer()

class PyV8Shell(object):
    js_header = """
var $wnd = new Object();
$wnd.document = new Object();
var $doc = $wnd.document;
var $pyjs = new Object();
$pyjs.__modules__ = {};
$pyjs.modules = {};
$pyjs.modules_hash = {};
$pyjs.loaded_modules = {};
$pyjs.options = new Object();
$pyjs.options.set_all = function (v) {
    $pyjs.options.arg_ignore = v;
    $pyjs.options.arg_count = v;
    $pyjs.options.arg_is_instance = v;
    $pyjs.options.arg_instance_type = v;
    $pyjs.options.arg_kwarg_dup = v;
    $pyjs.options.arg_kwarg_unexpected_keyword = v;
    $pyjs.options.arg_kwarg_multiple_values = v;
};
$pyjs.options.set_all(true);
$pyjs.trackstack = [];
$pyjs.track = {module:'__main__', lineno: 1};
$pyjs.trackstack.push($pyjs.track);
$pyjs.__last_exception_stack__ = null;
$pyjs.__last_exception__ = null;

/*
 * prepare app system vars
 */
$pyjs.platform = 'pyv8';
$pyjs.appname = '<input>';
$pyjs.loadpath = './';    
/*
 *  interactively run functions in module contexts
 */
 function runinteractive (f, ctxt)
 {
    return f(ctxt);
 }
    """
    banner = """
Interactive PyJS/PyV8 shell.

Magic functions:
%native - switch to native python interpreter
%pyjs   - switch to PyJS/PyV8 interpreter
%showjs <true/false> - enable/disable JS printing

Native mode locals:
shell  - PyV8Shell instance
jsctxt - PyV8 context
jsglob - PyV8 globals
    """
    def initialize_translator(self, path=None):
        if not path:
            path = pyjspth
        self.path = path
        self.paths = [join(path, 'pyjs', 'src', 'pyjs', 'lib'),
                      join(path, 'pyjs', 'src', 'pyjs', 'builtin'),
                      join(path, 'library'),
                      ]
        
        parser = OptionParser()
        translator.add_compile_options(parser)
        (options, args) = parser.parse_args()
        self.options = options
        # This seems to be outdated too
        #self.parser = translator.PlatformParser("platform", verbose=False)
        #self.parser.setPlatform("pyv8")
    
    def find_file(self, name, subdir=None):
        for path in self.paths:
            fpath = path
            if subdir:
                fpath = join(fpath, subdir)
            fpath = join(fpath, name)
            if exists(fpath):
                return fpath
        return None
    
    def translate(self, src, module):
        output = StringIO()
        tree = compiler.parse(src)
        t = translator.Translator(compiler,
                       module, module, src, tree, output,
                       debug = self.options.debug,
                       print_statements = self.options.print_statements,
                       function_argument_checking = self.options.function_argument_checking,
                       attribute_checking = self.options.attribute_checking,
                       bound_methods = self.options.bound_methods,
                       descriptors = self.options.descriptors,
                       source_tracking = self.options.source_tracking,
                       line_tracking = self.options.line_tracking,
                       store_source = self.options.store_source,
                       inline_code = self.options.inline_code,
                       operator_funcs = self.options.operator_funcs,
                       number_classes = self.options.number_classes,
                       )
        jssrc = output.getvalue()
        output.close()
        return jssrc, t.imported_modules, t.imported_js
    def interactive_translate(self, src):
        output = StringIO()
        tree = compiler.parse(src)
        t = InteractiveTranslator(compiler,
                       '__main__', '__main__', src, tree, output,
                       debug = self.options.debug,
                       print_statements = self.options.print_statements,
                       function_argument_checking = self.options.function_argument_checking,
                       attribute_checking = self.options.attribute_checking,
                       bound_methods = self.options.bound_methods,
                       descriptors = self.options.descriptors,
                       source_tracking = self.options.source_tracking,
                       line_tracking = self.options.line_tracking,
                       store_source = self.options.store_source,
                       inline_code = self.options.inline_code,
                       operator_funcs = self.options.operator_funcs,
                       number_classes = self.options.number_classes,
                       )
        jssrc = output.getvalue()
        output.close()
        return jssrc, t.imported_modules, t.imported_js        
    
    def compile_pyjs(self):
        self._pyjs = open(self.find_file('_pyjs.js', 'public')).read()
        self.dynamic, imppy, impjs = self.translate('', 'dynamic')
        self.pyjslib, imppy, impjs = self.translate(
            open(self.find_file('pyjslib.py')).read() + "\n" +
            open(self.find_file('pyjslib.py', '__pyv8__')).read(),
            'pyjslib')
        self.sys, imppy, impjs = self.translate(
            open(self.find_file('sys.py')).read(),
            'sys')
        self.string, imppy, impjs = self.translate(
            open(self.find_file('string.py')).read(),
            'string')
        self.main, imppy, impjs = self.translate('', '__main__')

    def initialize_v8(self):
        self.g = Global()
        self.ctxt = PyV8.JSContext(self.g)
        self.g.__context__ = self.ctxt
        self.ctxt.enter()
        self.evaluate(self.js_header)
        self.evaluate(self._pyjs)
        self.evaluate(self.sys)
        self.evaluate(self.dynamic)
        self.evaluate(self.pyjslib)
        self.evaluate(self.main)
        self.evaluate("""$pyjs.loaded_modules['pyjslib']('pyjslib');""")
        self.evaluate("""$pyjs.loaded_modules['__main__']('__main__');""")        
        
    def evaluate(self, code, print_result=False):
        res = self.ctxt.eval(code)
        if print_result:
            print res
        return 0

    def run_ipython(self):
        self.shell = V8ShellEmbed(argv='')
        self.shell.IP._set_js_int(self)
        self.shell.set_banner(self.shell.IP.BANNER + '\n\n' + self.banner)
        self.shell.IP.hooks.generate_prompt = generate_prompt
        locs = dict(
            shell = self,
            jsctxt = self.ctxt,
            jsglob = self.g
            )
        self.shell(local_ns=locs)

    def run(self):
        self.initialize_translator()
        self.compile_pyjs()
        self.initialize_v8()
        self.run_ipython()

class InteractiveTranslator(translator.Translator):
    def __init__(self, compiler,
                 module_name, module_file_name, src, mod, output,
                 dynamic=0, findFile=None,
                 debug = False,
                 print_statements=True,
                 function_argument_checking=True,
                 attribute_checking=True,
                 bound_methods=True,
                 descriptors=True,
                 source_tracking=True,
                 line_tracking=True,
                 store_source=True,
                 inline_code=True,
                 operator_funcs=True,
                 number_classes=True,
                 create_locals=False,
                ):

        translator.monkey_patch_broken_transformer(compiler)

        self.compiler = compiler
        self.ast = compiler.ast
        self.js_module_name = self.jsname("variable", module_name)
        if module_name:
            self.module_prefix = "$module."
        else:
            self.module_prefix = ""
        self.module_name = module_name
        src = src.replace("\r\n", "\n")
        src = src.replace("\n\r", "\n")
        src = src.replace("\r",   "\n")
        self.src = src.split("\n")

        self.output = output
        self.dynamic = dynamic
        self.findFile = findFile
        # compile options
        self.debug = debug
        self.ignore_debug = False
        self.print_statements = print_statements
        self.function_argument_checking = function_argument_checking
        self.attribute_checking = attribute_checking
        self.bound_methods = bound_methods
        self.descriptors = descriptors
        self.source_tracking = source_tracking
        self.line_tracking = line_tracking
        self.store_source = store_source
        self.inline_bool = inline_code
        self.inline_len = inline_code
        self.inline_eq = inline_code
        self.inline_cmp = inline_code
        self.inline_getitem = inline_code
        self.inline_code = inline_code
        self.create_locals = create_locals
        self.operator_funcs = operator_funcs
        self.number_classes = number_classes
        if self.number_classes:
            self.operator_funcs = True

        self.imported_modules = []
        self.imported_js = []
        self.is_class_definition = False
        self.local_prefix = None
        self.track_lines = {}
        self.stacksize_depth = 0
        self.option_stack = []
        self.lookup_stack = [{}]
        self.indent_level = 0
        self.__unique_ids__ = {}
        self.try_depth = -1
        self.is_generator = False
        self.generator_states = []
        self.state_max_depth = len(self.generator_states)
        self.constant_int = {}
        self.constant_long = {}
        self.top_level = True
        translator.PYJSLIB_BUILTIN_MAPPING['__file__'] = "'%s'" % module_file_name
        self.import_context = "null"
        
        self.w(self.indent() + "runinteractive(function (ctxt) {")
        self.w(self.spacing() + "var $module = ctxt;")
        self.w(self.spacing() + "var __name__ = ctxt.__name__;")

        if self.attribute_checking and not module_name in ['sys', 'pyjslib']:
            attribute_checking = True
            self.w( self.indent() + 'try {')
        else:
            attribute_checking = False

        save_output = self.output
        self.output = StringIO()

        mod.lineno = 1
        self.track_lineno(mod, True)
        for child in mod.node:
            self.has_js_return = False
            self.has_yield = False
            self.is_generator = False
            self.track_lineno(child)
            assert self.top_level
            if isinstance(child, self.ast.Function):
                self._function(child, None)
            elif isinstance(child, self.ast.Class):
                self._class(child)
            elif isinstance(child, self.ast.Import):
                self._import(child, None, True)
            elif isinstance(child, self.ast.From):
                self._from(child, None, True)
            elif isinstance(child, self.ast.Discard):
                self._discard(child, None)
            elif isinstance(child, self.ast.Assign):
                self._assign(child, None)
            elif isinstance(child, self.ast.AugAssign):
                self._augassign(child, None)
            elif isinstance(child, self.ast.If):
                self._if(child, None)
            elif isinstance(child, self.ast.For):
                self._for(child, None)
            elif isinstance(child, self.ast.While):
                self._while(child, None)
            elif isinstance(child, self.ast.Subscript):
                self._subscript_stmt(child, None)
            elif isinstance(child, self.ast.Global):
                self._global(child, None)
            elif isinstance(child, self.ast.Printnl):
               self._print(child, None)
            elif isinstance(child, self.ast.Print):
               self._print(child, None)
            elif isinstance(child, self.ast.TryExcept):
                self._tryExcept(child, None)
            elif isinstance(child, self.ast.TryFinally):
                self._tryFinally(child, None)
            elif isinstance(child, self.ast.Raise):
                self._raise(child, None)
            elif isinstance(child, self.ast.Stmt):
                self._stmt(child, None, True)
            elif isinstance(child, self.ast.AssAttr):
                self._assattr(child, None)
            elif isinstance(child, self.ast.AssName):
                self._assname(child, None)
            elif isinstance(child, self.ast.AssTuple):
                for node in child.nodes:
                    self._stmt(node, None)
            elif isinstance(child, self.ast.Slice):
                self.w( self.spacing() + self._slice(child, None))
            else:
                raise TranslationError(
                    "unsupported type (in __init__)",
                    child, self.module_name)

        captured_output = self.output.getvalue()
        self.output = save_output
        if self.source_tracking and self.store_source:
            for l in self.track_lines.keys():
                self.w( self.spacing() + '''%s.__track_lines__[%d] = "%s";''' % (self.js_module_name, l, self.track_lines[l].replace('"', '\"')), translate=False)
        self.w( self.local_js_vars_decl([]))
        if captured_output.find("@CONSTANT_DECLARATION@") >= 0:
            captured_output = captured_output.replace("@CONSTANT_DECLARATION@", self.constant_decl())
        else:
            self.w( self.constant_decl())
        if captured_output.find("@ATTRIB_REMAP_DECLARATION@") >= 0:
            captured_output = captured_output.replace("@ATTRIB_REMAP_DECLARATION@", self.attrib_remap_decl())
        self.w( captured_output, False)

        if attribute_checking:
            self.w( self.dedent() + "} catch ($pyjs_attr_err) {throw @{{_errorMapping}}($pyjs_attr_err);};")
        self.w( self.dedent() + "}, __main__);")


if __name__ == '__main__':
    PyV8Shell().run()
