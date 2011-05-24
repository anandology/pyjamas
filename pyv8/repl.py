import sys
from IPython.iplib import InteractiveShell, softspace
from IPython.Shell import IPShellEmbed, make_IPython, ipapi, kill_embedded, ultraTB
from traceback import print_exc
from StringIO import StringIO

from pyjs import translator

class REPL(object):
    def __init__(self, compiler, linker, translator_arguments,
                 jsglobal, jscontext):
        self.compiler = compiler
        self.linker = linker
        self.translator_arguments = translator_arguments
        self.jsglobal = jsglobal
        self.jscontext = jscontext
        self.jscontext.eval(js_interactive_func)
        self.jscontext.eval(set_main)
        
    def __call__(self):
        """
        Start read-eval-print loop
        """
        self.shell = V8ShellEmbed(argv='')
        self.shell.IP._set_js_int(self)
        self.shell.set_banner(self.shell.IP.BANNER + '\n\n' + banner)
        self.shell.IP.hooks.generate_prompt = generate_prompt
        locs = dict(
            shell = self,
            jsctxt = self.jscontext,
            jsglob = self.jsglobal
            )
        self.shell(local_ns=locs)
        
    def translate(self, src):
        output = StringIO()
        tree = self.compiler.parse(src)
        t = InteractiveTranslator(self.compiler,
                       'main', 'main', src, tree, output,
                       **self.translator_arguments)
        jssrc = output.getvalue()
        output.close()
        return jssrc, t.imported_modules, t.imported_js
    
    def eval(self, code, print_result=False):
        try:
            res = self.jscontext.eval(code)
            if print_result:
                print res
        except Exception, e:
            print e
        return 0
        
js_interactive_func = """
function runinteractive (f, ctxt)
{
   return f(ctxt);
}"""

set_main = """
var __main__ = $pyjs.loaded_modules['main'];
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
        try:
            jscode, imppy, impjs = self._js_int.translate(source)
            self.code_to_run = jscode
        except Exception, e:
            print_exc()
            return None

        if self._show_js:
            print "\n Translated JS:\n" + jscode + "\n"
        # now actually execute the code object
        if self._js_int.eval(jscode) == 0:
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
        

class InteractiveTranslator(translator.Translator):
    def __init__(self, compiler,
                 module_name, module_file_name, src, mod, output,
                 dynamic=0, findFile=None, **kw):

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
        
        self.set_compile_options(kw)

        self.future_division = False
        
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
        self.w(self.spacing() + "var %s = ctxt;" % self.js_module_name)

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