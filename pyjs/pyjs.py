#!/usr/bin/env python
# Copyright 2006 James Tauber and contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import sys
from types import StringType
import compiler
from compiler import ast
import os
import copy
from cStringIO import StringIO
import re

# the standard location for builtins (e.g. pyjslib) can be
# over-ridden by changing this.  it defaults to sys.prefix
# so that on a system-wide install of pyjamas the builtins
# can be found in e.g. {sys.prefix}/share/pyjamas
#
# over-rides can be done by either explicitly modifying
# pyjs.prefix or by setting an environment variable, PYJSPREFIX.

prefix = sys.prefix

if os.environ.has_key('PYJSPREFIX'):
    prefix = os.environ['PYJSPREFIX']

# pyjs.path is the list of paths, just like sys.path, from which
# library modules will be searched for, for compile purposes.
# obviously we don't want to use sys.path because that would result
# in compiling standard python modules into javascript!

path = [os.path.abspath('')]

if os.environ.has_key('PYJSPATH'):
    for p in os.environ['PYJSPATH'].split(os.pathsep):
        p = os.path.abspath(p)
        if os.path.isdir(p):
            path.append(p)

# this is the python function used to wrap native javascript
NATIVE_JS_FUNC_NAME = "JS"

UU = ""

PYJSLIB_BUILTIN_FUNCTIONS=("cmp",
                           "map",
                           "filter",
                           "dir",
                           "getattr",
                           "setattr",
                           "hasattr",
                           "delattr",
                           "int",
                           "float",
                           "str",
                           "repr",
                           "range",
                           "len",
                           "hash",
                           "abs",
                           "ord",
                           "chr",
                           "enumerate",
                           "min",
                           "max",
                           "bool",
                           "super",
                           "type",
                           "pow",
                           "hex",
                           "oct",
                           "round",
                           "divmod",
                           "all",
                           "any",
                           "isinstance")

PYJSLIB_BUILTIN_CLASSES=("BaseException",
                         "Exception",
                         "StandardError",
                         "StopIteration",
                         "AttributeError",
                         "TypeError",
                         "KeyError",
                         "LookupError",
                         "NameError",
                         "ValueError",
                         "IndexError",
                         "list",
                         "dict",
                         "object",
                         "tuple",
                        )

# XXX HACK!
pyjs_builtin_remap = { \
    'list': 'List',
    'dict': 'Dict',
    'tuple': 'Tuple',
    'super': '_super',
}

# XXX: this is a hack: these should be dealt with another way
# however, console is currently the only global name which is causing
# problems.
PYJS_GLOBAL_VARS=("console")

# This is taken from the django project.
# Escape every ASCII character with a value less than 32.
JS_ESCAPES = (
    ('\\', r'\x5C'),
    ('\'', r'\x27'),
    ('"', r'\x22'),
    ('>', r'\x3E'),
    ('<', r'\x3C'),
    ('&', r'\x26'),
    (';', r'\x3B')
    ) + tuple([('%c' % z, '\\x%02X' % z) for z in range(32)])

def escapejs(value):
    """Hex encodes characters for use in JavaScript strings."""
    for bad, good in JS_ESCAPES:
        value = value.replace(bad, good)
    return value

def uuprefix(name, leave_alone=0):
    name = name.split(".")
    name = name[:leave_alone] + map(lambda x: "__%s" % x, name[leave_alone:])
    return '.'.join(name)

class Klass:

    klasses = {}

    def __init__(self, name, name_):
        self.name = name
        self.name_ = name_
        self.klasses[name] = self
        self.functions = set()

    def set_base(self, base_name):
        self.base = self.klasses.get(base_name)

    def add_function(self, function_name):
        self.functions.add(function_name)


class TranslationError(Exception):
    def __init__(self, message, node):
        self.message = "line %s:\n%s\n%s" % (node.lineno, message, node)

    def __str__(self):
        return self.message

def strip_py(name):
    return name

def mod_var_name_decl(raw_module_name):
    """ function to get the last component of the module e.g.
        pyjamas.ui.DOM into the "namespace".  i.e. doing
        "import pyjamas.ui.DOM" actually ends up with _two_
        variables - one pyjamas.ui.DOM, the other just "DOM".
        but "DOM" is actually local, hence the "var" prefix.

        for PyV8, this might end up causing problems - we'll have
        to see: gen_mod_import and mod_var_name_decl might have
        to end up in a library-specific module, somewhere.
    """
    name = raw_module_name.split(".")
    if len(name) == 1:
        return ''
    child_name = name[-1]
    return "var %s = %s;\n" % (child_name, raw_module_name)

def gen_mod_import(parentName, importName, dynamic=1):
    #pyjs_ajax_eval("%(n)s.cache.js", null, true);
    return """
    pyjslib.import_module(sys.loadpath, '%(p)s', '%(n)s', %(d)d, false);
    track.module='%(p)s';
    """ % ({'p': parentName, 'd': dynamic, 'n': importName}) + \
    mod_var_name_decl(importName)

class Translator:

    def __init__(self, mn, module_name, raw_module_name, src, debug, mod, output,
                 dynamic=0, optimize=False, findFile=None,
                 function_argument_checking=True, attribute_checking=True,
                 source_tracking=True, store_source=True):

        if module_name:
            self.module_prefix = module_name + "."
        else:
            self.module_prefix = ""
        self.raw_module_name = raw_module_name
        src = src.replace("\r\n", "\n")
        src = src.replace("\n\r", "\n")
        src = src.replace("\r",   "\n")
        self.src = src.split("\n")
        self.debug = debug
        self.imported_modules = []
        self.imported_modules_as = []
        self.imported_js = set()
        self.top_level_functions = set()
        self.top_level_classes = set()
        self.top_level_vars = set()
        self.local_arg_stack = [[]]
        self.output = output
        self.imported_classes = {}
        self.method_imported_globals = set()
        self.method_self = None
        self.nextTupleAssignID = 1
        self.dynamic = dynamic
        self.optimize = optimize
        self.findFile = findFile
        self.function_argument_checking = function_argument_checking
        self.attribute_checking = attribute_checking
        self.source_tracking = source_tracking
        self.store_source = store_source
        self.local_prefix = None

        if module_name.find(".") >= 0:
            vdec = ''
        else:
            vdec = 'var '
        print >>self.output, UU+"%s%s = function (__mod_name__) {" % (vdec, module_name)

        print >>self.output, "    if("+module_name+".__was_initialized__) return;"
        print >>self.output, "    "+UU+module_name+".__was_initialized__ = true;"
        print >>self.output, UU+"if (__mod_name__ == null) __mod_name__ = '%s';" % (mn)
        print >>self.output, UU+"%s.__name__ = __mod_name__;" % (raw_module_name)
        if self.source_tracking:
            print >> self.output, UU+"%s.__track_lines__ = new Array();" % raw_module_name

        decl = mod_var_name_decl(raw_module_name)
        if decl:
            print >>self.output, decl

        self.track_lines = {}

        save_output = self.output
        buffered_output = StringIO()
        self.output = buffered_output
        
        if self.attribute_checking:
            print >>self.output, 'try {'
        for child in mod.node:
            if isinstance(child, ast.Function):
                self.top_level_functions.add(child.name)
            elif isinstance(child, ast.Class):
                self.top_level_classes.add(child.name)

        mod.lineno = 1
        self.track_lineno(mod, True)
        for child in mod.node:
            self.has_js_return = False
            self.track_lineno(child)
            if isinstance(child, ast.Function):
                self._function(child, False)
            elif isinstance(child, ast.Class):
                self._class(child)
            elif isinstance(child, ast.Import):
                importName = child.names[0][0]
                importAs = child.names[0][1]
                if importName == '__pyjamas__': # special module to help make pyjamas modules loadable in the python interpreter
                    pass
                elif importName.endswith('.js'):
                    self.imported_js.add(importName)
                else:
                    self.add_imported_module(strip_py(importName))
                    if importAs:
                        tnode = ast.Assign([ast.AssName(importAs, "OP_ASSIGN", child.lineno)], ast.Name(strip_py(importName), child.lineno), child.lineno)
                        self._assign(tnode, None, True)
            elif isinstance(child, ast.From):
                if child.modname == '__pyjamas__': # special module to help make pyjamas modules loadable in the python interpreter
                    pass
                else:
                    self.add_imported_module(child.modname)
                    self._from(child)
            elif isinstance(child, ast.Discard):
                self._discard(child, None)
            elif isinstance(child, ast.Assign):
                self._assign(child, None, True)
            elif isinstance(child, ast.AugAssign):
                self._augassign(child, None)
            elif isinstance(child, ast.If):
                self._if(child, None)
            elif isinstance(child, ast.For):
                self._for(child, None)
            elif isinstance(child, ast.While):
                self._while(child, None)
            elif isinstance(child, ast.Subscript):
                self._subscript_stmt(child, None)
            elif isinstance(child, ast.Global):
                self._global(child, None)
            elif isinstance(child, ast.Printnl):
               self._print(child, None)
            elif isinstance(child, ast.Print):
               self._print(child, None)
            elif isinstance(child, ast.TryExcept):
                self._tryExcept(child, None, True)
            elif isinstance(child, ast.Raise):
                self._raise(child, None)
            elif isinstance(child, ast.Stmt):
                self._stmt(child, None)
            else:
                raise TranslationError("unsupported type (in __init__)", child)

        # Initialize all classes for this module
        #print >> self.output, "__"+self.modpfx()+\
        #          "classes_initialize = function() {\n"
        #for className in self.top_level_classes:
        #    print >> self.output, "\t"+UU+self.modpfx()+"__"+className+"_initialize();"
        #print >> self.output, "};\n"
        if self.attribute_checking:
            print >> self.output, "} catch (pyjs_attr_err) {pyjslib._attr_err_check(pyjs_attr_err)};"

        self.output = save_output
        if self.source_tracking and self.store_source:
            for l in self.track_lines.keys():
                print >> self.output, UU+'''%s.__track_lines__[%d] = "%s";''' % (raw_module_name, l, self.track_lines[l].replace('"', '\"'))

        print >> self.output, buffered_output.getvalue()
        print >> self.output, "return this;\n"
        print >> self.output, "}; /* end %s */ \n"  % module_name

    def module_imports(self):
        return self.imported_modules + self.imported_modules_as

    def add_local_arg(self, varname):
        local_vars = self.local_arg_stack[-1]
        if varname not in local_vars:
            local_vars.append(varname)

    def add_imported_module(self, importName):

        if importName in self.imported_modules:
            return
        self.imported_modules.append(importName)
        name = importName.split(".")
        if len(name) != 1:
            # add the name of the module to the namespace,
            # but don't add the short name to imported_modules
            # because then the short name would be attempted to be
            # added to the dependencies, and it's half way up the
            # module import directory structure!
            child_name = name[-1]
            self.imported_modules_as.append(child_name) 
        print >> self.output, gen_mod_import(self.raw_module_name,
                                             strip_py(importName),
                                             self.dynamic)
    def track_lineno(self, node, module=False):
        if self.source_tracking and node.lineno:
            if module:
                print >> self.output, "track.module='%s';" % self.raw_module_name
            print >> self.output, "track.lineno=%d;" % node.lineno
            #print >> self.output, "if (track.module!='%s') debugger;" % self.raw_module_name
            self.track_lines[node.lineno] = self.get_line_trace(node)

    def track_call(self, call_code):
        if self.debug:
            call_code = """\
(function(){\
var pyjs_dbg_retry = 0;
try{var pyjs_dbg_res=%s;}catch(pyjs_dbg_err){
    if (pyjs_dbg_err.name != 'StopIteration') {
        debugger;
    }
    switch (pyjs_dbg_retry) {
        case 1:
            pyjs_dbg_res=%s;
            break;
        case 2:
            break;
        default:
            throw pyjs_dbg_err;
    }
}return pyjs_dbg_res})()""" % (call_code, call_code)
        return call_code

    def _instance_method_init(self, node, arg_names, varargname, kwargname,
                              current_klass, output=None):
        output = output or self.output
        maxargs1 = len(arg_names) - 1
        maxargs2 = len(arg_names)
        minargs1 = maxargs1 - len(node.defaults)
        minargs2 = maxargs2 - len(node.defaults)
        if node.kwargs:
            maxargs1 += 1
            maxargs2 += 1
        maxargs1str = "%d" % maxargs1
        maxargs2str = "%d" % maxargs2
        if node.varargs:
            argcount1 = "arguments.length < %d" % minargs1
            maxargs1str = "null"
        elif minargs1 == maxargs1:
            argcount1 = "arguments.length != %d" % minargs1
        else:
            argcount1 = "(arguments.length < %d || arguments.length > %d)" % (minargs1, maxargs1)
        if node.varargs:
            argcount2 = "arguments.length < %d" % minargs2
            maxargs2str = "null"
        elif minargs2 == maxargs2:
            argcount2 = "arguments.length != %d" % minargs2
        else:
            argcount2 = "(arguments.length < %d || arguments.length > %d)" % (minargs2, maxargs2)

        print >> output, """\
    if (this.__is_instance__ === true) {\
"""
        #var %s = (arguments.callee.instance == null ? this : arguments.callee.instance);
        if arg_names:
            print >> output, """\
        var %s = this;\
""" % arg_names[0]

        if node.kwargs:
            print >> output, """\
        var %s = arguments.length >= %d ? arguments[arguments.length-1] : arguments[arguments.length];\
""" % (kwargname, maxargs1)

        if node.varargs:
            self._varargs_handler(node, varargname, maxargs1)

        if self.function_argument_checking:
            print >> output, """\
        if (pyjs_options.arg_count && %s) pyjs__exception_func_param(arguments.callee.__name__, %d, %s, arguments.length+1);\
""" % (argcount1, minargs2, maxargs2str)

        print >> output, """\
    } else {\
"""
        if arg_names:
            print >> output, """\
        var %s = arguments[0];\
""" % arg_names[0]
        arg_idx = 0
        for arg_name in arg_names[1:]:
            arg_idx += 1
            print >> output, """\
        %s = arguments[%d];\
""" % (arg_name, arg_idx)

        if node.kwargs:
            print >> output, """\
        var %s = arguments.length >= %d ? arguments[arguments.length-1] : arguments[arguments.length];\
""" % (kwargname, maxargs2)

        if node.varargs:
            self._varargs_handler(node, varargname, maxargs2)

        if self.function_argument_checking:
            print >> output, """\
        if (pyjs_options.arg_is_instance && self.__is_instance__ !== true) pyjs__exception_func_instance_expected(arguments.callee.__name__, arguments.callee.__class__.__name__, self);
        if (pyjs_options.arg_count && %s) pyjs__exception_func_param(arguments.callee.__name__, %d, %s, arguments.length);\
""" % (argcount2, minargs2, maxargs2str)

        print >> output, """\
    }\
"""
        if self.function_argument_checking:
            print >> output, """\
    if (pyjs_options.arg_instance_type) {
        if (arguments.callee !== arguments.callee.__class__[arguments.callee.__name__]) {
            if (!pyjs___isinstance(self, arguments.callee.__class__.slice(1))) {
                pyjs__exception_func_instance_expected(arguments.callee.__name__, arguments.callee.__class__.__name__, self);
            }
        }
    }\
"""

    def _static_method_init(self, node, arg_names, varargname, kwargname,
                            current_klass, output=None):
        output = output or self.output
        maxargs = len(arg_names)
        minargs = maxargs - len(node.defaults)
        maxargsstr = "%d" % maxargs
        if node.kwargs:
            maxargs += 1
        if node.varargs:
            argcount = "arguments.length < %d" % minargs
            maxargsstr = "null"
        elif minargs == maxargs:
            argcount = "arguments.length != %d" % minargs
        else:
            argcount = "(arguments.length < %d || arguments.length > %d)" % (minargs, maxargs)
        if self.function_argument_checking:
            print >> output, """\
    if (pyjs_options.arg_count && %s) pyjs__exception_func_param(arguments.callee.__name__, %d, %s, arguments.length);\
""" % (argcount, minargs, maxargsstr)

        if node.kwargs:
            print >> output, """\
        var %s = arguments.length >= %d ? arguments[arguments.length-1] : arguments[arguments.length];\
""" % (kwargname, maxargs)

        if node.varargs:
            self._varargs_handler(node, varargname, maxargs)

    def _class_method_init(self, node, arg_names, varargname, kwargname,
                           current_klass, output=None):
        output = output or self.output
        maxargs = max(0, len(arg_names) -1)
        minargs = max(0, maxargs - len(node.defaults))
        maxargsstr = "%d" % (maxargs+1)
        if node.kwargs:
            maxargs += 1
        if node.varargs:
            argcount = "arguments.length < %d" % minargs
            maxargsstr = "null"
        elif minargs == maxargs:
            argcount = "arguments.length != %d" % minargs
            maxargsstr = "%d" % (maxargs)
        else:
            argcount = "(arguments.length < %d || arguments.length > %d)" % (minargs, maxargs)
        if self.function_argument_checking:
            print >> output, """\
    if (pyjs_options.arg_is_instance && this.__is_instance__ !== true && this.__is_instance__ !== false) pyjs__exception_func_class_expected(arguments.callee.__name__, arguments.callee.__class__.__name__);
    if (pyjs_options.arg_count && %s) pyjs__exception_func_param(arguments.callee.__name__, %d, %s, arguments.length);\
""" % (argcount, minargs+1, maxargsstr)

        print >> output, """\
    var %s = this.prototype;\
""" % (arg_names[0],)

        if node.kwargs:
            print >> output, """\
        var %s = arguments.length >= %d ? arguments[arguments.length-1] : arguments[arguments.length];\
""" % (kwargname, maxargs)

        if node.varargs:
            self._varargs_handler(node, varargname, maxargs)

    def _default_args_handler(self, node, arg_names, current_klass, kwargname,
                              output=None):
        output = output or self.output
        if node.kwargs and (len(arg_names) > 0):
            # This is necessary when **kwargs in function definition
            # and the call didn't pass the parse_kwargs() of this function.
            # See libtest testKwArgsInherit
            # This is not completely safe: if the last element in arguments 
            # is an dict and the corresponding argument shoud be a dict and 
            # the kwargs should be empty, the kwars gets incorrectly the 
            # dict and the argument becomes undefined.
            # E.g.
            # def fn(a = {}, **kwargs): pass
            # fn({'a':1}) -> a gets undefined and kwargs gets {'a':1}
            revargs = arg_names[0:]
            revargs.reverse()
            print >> output, """\
    if (typeof %s == 'undefined') {
        %s = pyjslib.Dict({});
       \
""" % (kwargname, kwargname),
            for v in revargs:
                print >> output, """\
if (typeof %s != 'undefined') {
            if (pyjslib.get_pyjs_classtype(%s) == 'Dict') {
                %s = %s;
                %s = arguments[%d];
            }
        } else\
""" % (v, v, kwargname, v, v, len(arg_names)),
            print >> output, """\
{
        }
    }\
"""
        if len(node.defaults):
            default_pos = len(arg_names) - len(node.defaults)
            for default_node in node.defaults:
                default_value = self.expr(default_node, current_klass)
                default_name = arg_names[default_pos]
                default_pos += 1
                print >> output, "    if (typeof %s == 'undefined') %s=%s;" % (default_name, default_name, default_value)

    def _varargs_handler(self, node, varargname, start):
        if node.kwargs:
            end = "arguments.length-1"
            start -= 1
        else:
            end = "arguments.length"
        print >> self.output, """\
        var %s = pyjslib.Tuple();
        for (var pyjs__va_arg = %d; pyjs__va_arg < %s; pyjs__va_arg++) {
            var pyjs__arg = arguments[pyjs__va_arg];
            %s.append(pyjs__arg);
        }\
""" % (varargname, start, end, varargname)

    def __varargs_handler(self, node, varargname, arg_names, current_klass, loop_var = None):
        print >>self.output, "    var", varargname, '= new pyjslib.Tuple();'
        print >>self.output, "    for(",
        if loop_var is None:
            loop_var = "pyjs__va_arg"
            print >>self.output, "var "+loop_var+"="+str(len(arg_names)),
        print >>self.output, """\
; %(loop_var)s < arguments.length; %(loop_var)s++) {
        var pyjs__arg = arguments[%(loop_var)s];
        %(varargname)s.append(pyjs__arg);
    }\
""" % {'varargname': varargname, 'loop_var': loop_var}

    def _kwargs_parser(self, node, function_name, arg_names, current_klass, method_ = False):
        default_pos = len(arg_names) - len(node.defaults)
        if not method_:
            print >>self.output, function_name+'.parse_kwargs = function (', ", ".join(["__kwargs"]+arg_names), ") {"
        else:
            print >>self.output, ", function (", ", ".join(["__kwargs"]+arg_names), ") {"
        for arg_name in arg_names:
            if self.function_argument_checking:
                print >>self.output, """\
    if (typeof %(arg_name)s == 'undefined') {
        %(arg_name)s=__kwargs.%(arg_name)s;
        delete __kwargs.%(arg_name)s;
    } else if (pyjs_options.arg_kwarg_multiple_values && typeof __kwargs.%(arg_name)s != 'undefined') {
        pyjs__exception_func_multiple_values('%(function_name)s', '%(arg_name)s');
    }\
""" % {'arg_name': arg_name, 'function_name': function_name}
            else:
                print >>self.output, "    if (typeof %s == 'undefined')"%(arg_name)
                print >>self.output, "        %s=__kwargs.%s;"% (arg_name, arg_name)

        if self.function_argument_checking and not node.kwargs:
            print >>self.output, """\
    if (pyjs_options.arg_kwarg_unexpected_keyword) {
        for (var i in __kwargs) {
            pyjs__exception_func_unexpected_keyword('%(function_name)s', i);
        }
    }\
""" % {'function_name': function_name}

        # Always add all remaining arguments. Needed for argument checking _and_ if self != this;
        print >>self.output, "    var __r = "+"".join(["[", ", ".join(arg_names), "]"])+";"
        print >>self.output, """\
    for (var pyjs__va_arg = %d;pyjs__va_arg < arguments.length;pyjs__va_arg++) {
        __r.push(arguments[pyjs__va_arg]);
    }
""" % (len(arg_names)+1,)
        if node.kwargs:
            print >>self.output, "    __r.push(pyjslib.Dict(__kwargs));"
        print >>self.output, "    return __r;"
        if not method_:
            print >>self.output, "};"
        else:
            print >>self.output, "});"

    def _function(self, node, local=False):
        source_tracking = save_source_tracking = self.source_tracking
        save_has_js_return = self.has_js_return
        self.has_js_return = False
        if node.decorators:
            for d in node.decorators:
                if d.name == "noSourceTracking":
                    source_tracking = False
        self.source_tracking = source_tracking

        if local:
            function_name = node.name
            self.add_local_arg(function_name)
        else:
            function_name = UU + self.modpfx() + node.name

        arg_names = list(node.argnames)
        normal_arg_names = list(arg_names)
        if node.kwargs:
            kwargname = normal_arg_names.pop()
        else:
            kwargname = None
        if node.varargs:
            varargname = normal_arg_names.pop()
        else:
            varargname = None
        declared_arg_names = list(normal_arg_names)
        #if node.kwargs: declared_arg_names.append(kwargname)

        function_args = "(" + ", ".join(declared_arg_names) + ")"
        print >>self.output, "%s = function%s {" % (function_name, function_args)
        self._static_method_init(node, declared_arg_names, varargname, kwargname, None)
        self._default_args_handler(node, declared_arg_names, None, kwargname)

        local_arg_names = normal_arg_names + declared_arg_names

        if node.kwargs:
            local_arg_names.append(kwargname)
        if node.varargs:
            local_arg_names.append(varargname)

        # stack of local variable names for this function call
        self.local_arg_stack.append(local_arg_names)

        save_output = self.output
        self.output = StringIO()
        if self.source_tracking:
            print >>self.output, "track={module:'%s',lineno:%d};trackstack.push(track);" % (self.raw_module_name, node.lineno)
        self.track_lineno(node, True)
        for child in node.code:
            self._stmt(child, None)
        if self.source_tracking and self.has_js_return:
            self.source_tracking = False
            self.output = StringIO()
            for child in node.code:
                self._stmt(child, None)
        captured_output = self.output.getvalue()
        self.output = save_output
        print >>self.output, captured_output,

        # remove the top local arg names
        self.local_arg_stack.pop()

        # we need to return null always, so it is not undefined
        lastStmt = [p for p in node.code][-1]
        if not isinstance(lastStmt, ast.Return):
            if self.source_tracking:
                print >>self.output, "trackstack.pop();track=trackstack.pop();trackstack.push(track);"
            # FIXME: check why not on on self._isNativeFunc(lastStmt)
            if not self._isNativeFunc(lastStmt):
                print >>self.output, "    return null;"

        print >>self.output, "};"
        print >>self.output, "%s.__name__ = '%s';\n" % (function_name, node.name)

        self._kwargs_parser(node, function_name, normal_arg_names, None)
        self.has_js_return = save_has_js_return
        self.source_tracking = save_source_tracking


    def _return(self, node, current_klass):
        expr = self.expr(node.value, current_klass)
        # in python a function call always returns None, so we do it
        # here too
        self.track_lineno(node)
        if self.source_tracking:
            print >>self.output, "var pyjs__ret = " + expr + ";"
            print >>self.output, "trackstack.pop();track=trackstack.pop();trackstack.push(track);"
            print >>self.output, "    return pyjs__ret;"
        else:
            print >>self.output, "    return " + expr + ";"


    def _break(self, node, current_klass):
        print >>self.output, "    break;"


    def _continue(self, node, current_klass):
        print >>self.output, "    continue;"


    re_return = re.compile(r'\breturn\b')
    def _callfunc(self, v, current_klass):

        if isinstance(v.node, ast.Name):
            if v.node.name == NATIVE_JS_FUNC_NAME:
                if isinstance(v.args[0], ast.Const):
                    if self.re_return.search(v.args[0].value):
                        self.has_js_return = True
                    return v.args[0].value
                else:
                    raise TranslationError("native js functions only support constant strings",v.node)
            elif v.node.name in self.top_level_functions:
                call_name = self.modpfx() + v.node.name
            elif v.node.name in self.top_level_classes:
                call_name = self.modpfx() + v.node.name
            elif self.imported_classes.has_key(v.node.name):
                call_name = self.imported_classes[v.node.name] + '.' + v.node.name
            elif v.node.name in PYJSLIB_BUILTIN_FUNCTIONS:
                name = pyjs_builtin_remap.get(v.node.name, v.node.name)
                call_name = 'pyjslib.' + name
            elif v.node.name in PYJSLIB_BUILTIN_CLASSES:
                name = pyjs_builtin_remap.get(v.node.name, v.node.name)
                call_name = 'pyjslib.' + name
            elif v.node.name == "callable":
                call_name = "pyjslib.isFunction"
            elif v.node.name in self.local_arg_stack[-1] and \
                 len(self.local_arg_stack) == 1:
                call_name = self.modpfx() + v.node.name
            elif v.node.name in self.top_level_vars:
                call_name = self.modpfx() + v.node.name
            else:
                call_name = v.node.name
            call_args = []
        elif isinstance(v.node, ast.Getattr):
            attr_name = v.node.attrname

            if isinstance(v.node.expr, ast.Name):
                call_name = self._name2(v.node.expr, current_klass, attr_name)
                call_args = []
            elif isinstance(v.node.expr, ast.Getattr):
                call_name = self._getattr2(v.node.expr, current_klass, attr_name)
                call_args = []
            elif isinstance(v.node.expr, ast.CallFunc):
                call_name = self._callfunc(v.node.expr, current_klass) + "." + v.node.attrname
                call_args = []
            elif isinstance(v.node.expr, ast.Subscript):
                call_name = self._subscript(v.node.expr, current_klass) + "." + v.node.attrname
                call_args = []
            elif isinstance(v.node.expr, ast.Const):
                call_name = self.expr(v.node.expr, current_klass) + "." + v.node.attrname
                call_args = []
            else:
                raise TranslationError("unsupported type (in _callfunc)", v.node.expr)
        elif isinstance(v.node, ast.CallFunc):
            call_name = self._callfunc(v.node, current_klass)
            call_args = []
        elif isinstance(v.node, ast.Subscript):
            call_name = self._subscript(v.node, current_klass)
            call_args = []
        else:
            raise TranslationError("unsupported type (in _callfunc)", v.node)

        call_name = strip_py(call_name)

        kwargs = []
        star_arg_name = None
        if v.star_args:
            star_arg_name = self.expr(v.star_args, current_klass)
        dstar_arg_name = None
        if v.dstar_args:
            dstar_arg_name = self.expr(v.dstar_args, current_klass)

        for ch4 in v.args:
            if isinstance(ch4, ast.Keyword):
                kwarg = ch4.name + ":" + self.expr(ch4.expr, current_klass)
                kwargs.append(kwarg)
            else:
                arg = self.expr(ch4, current_klass)
                call_args.append(arg)

        if kwargs:
            fn_args = ", ".join(['{' + ', '.join(kwargs) + '}']+call_args)
        else:
            fn_args = ", ".join(['{}']+call_args)

        if kwargs or star_arg_name or dstar_arg_name:
            if not star_arg_name:
                star_arg_name = 'null'
            if not dstar_arg_name:
                dstar_arg_name = 'null'
            try: call_this, method_name = call_name.rsplit(".", 1)
            except ValueError:
                # Must be a function call ...
                call_code = ("pyjs_kwargs_function_call("+call_name+", "
                                  + star_arg_name 
                                  + ", " + dstar_arg_name
                                  + ", ["+fn_args+"]"
                                  + ")")
            else:
                call_code = ("pyjs_kwargs_method_call("+call_this+", '"+method_name+"', "
                                  + star_arg_name 
                                  + ", " + dstar_arg_name
                                  + ", ["+fn_args+"]"
                                  + ")")
        else:
            call_code = call_name + "(" + ", ".join(call_args) + ")"
        return self.track_call(call_code)

    def _print(self, node, current_klass):
        if self.optimize:
            return
        call_args = []
        for ch4 in node.nodes:
            arg = self.expr(ch4, current_klass)
            call_args.append(arg)
        print >>self.output, self.track_call("pyjslib.printFunc([%s], %d);" % (', '.join(call_args), int(isinstance(node, ast.Printnl))))

    def _tryExcept(self, node, current_klass, top_level=False):

        pyjs_try_err = 'pyjs_try_err'
        if self.source_tracking:
            if top_level:
                print >>self.output, "{"
            print >>self.output, "var pyjs__trackstack_size = trackstack.length;"
        if self.attribute_checking:
            print >>self.output, "    try {try {"
        else:
            print >>self.output, "    try {"

        for stmt in node.body.nodes:
            self._stmt(stmt, current_klass)
        if self.attribute_checking:
            print >> self.output, "    } catch (pyjs_attr_err) {pyjslib._attr_err_check(pyjs_attr_err)}} catch(%s) {" % pyjs_try_err
        else:
            print >> self.output, "    } catch(%s) {" % pyjs_try_err
        print >> self.output, "        sys.__last_exception__ = {error: %s, module: %s, try_lineno: %s};" % (pyjs_try_err, self.raw_module_name, node.lineno)
        if self.source_tracking:
            print >>self.output, """\
sys.save_exception_stack();
if (trackstack.length > pyjs__trackstack_size) {
    trackstack = trackstack.slice(0,pyjs__trackstack_size);
    track = trackstack.slice(-1)[0];
}
track.module='%s';""" % self.raw_module_name
            if top_level:
                print >>self.output, "}"


        self.add_local_arg(pyjs_try_err)
        else_str = "        "
        for handler in node.handlers:
            lineno = handler[2].nodes[0].lineno
            expr = handler[0]
            as_ = handler[1]
            if as_:
                errName = as_.name
            else:
                errName = 'err'

            if not expr:
                print >> self.output, "%s{" % else_str
            else:
                if expr.lineno:
                    lineno = expr.lineno
                l = []
                if isinstance(expr, ast.Tuple):
                    for x in expr.nodes:
                        l.append("(%s.__name__ == %s.__name__)" % (pyjs_try_err, self.expr(x, current_klass)))
                else:
                    l = [ "%s.__name__ == %s.__name__" % (pyjs_try_err, self.expr(expr, current_klass)) ]
                print >> self.output, "%sif (%s) {" % (else_str, "||".join(l))
            print >> self.output, "               sys.__last_exception__.except_lineno = %d;" % lineno
            tnode = ast.Assign([ast.AssName(errName, "OP_ASSIGN", lineno)], ast.Name(pyjs_try_err, lineno), lineno)
            self._assign(tnode, current_klass, top_level)
            for stmt in handler[2]:
                self._stmt(stmt, current_klass)
            print >> self.output, "        }",
            else_str = "else "

        if node.else_ != None:
            print >>self.output, "    } finally {"
            for stmt in node.else_:
                self._stmt(stmt, current_klass)
        print >>self.output, "    }"

    # XXX: change use_getattr to True to enable "strict" compilation
    # but incurring a 100% performance penalty. oops.
    def _getattr(self, v, current_klass, use_getattr=False):
        attr_name = v.attrname
        if isinstance(v.expr, ast.Name):
            obj = self._name(v.expr, current_klass, return_none_for_module=True)
            if obj == None and v.expr.name in self.module_imports():
                # XXX TODO: distinguish between module import classes
                # and variables.  right now, this is a hack to get
                # the sys module working.
                #if v.expr.name == 'sys':
                return v.expr.name+'.'+attr_name
            if not use_getattr or attr_name == '__class__' or \
                    attr_name == '__name__':
                return obj + "." + attr_name
            return "pyjslib.getattr(%s, '%s')" % (obj, attr_name)
        elif isinstance(v.expr, ast.Getattr):
            return self._getattr(v.expr, current_klass) + "." + attr_name
        elif isinstance(v.expr, ast.Subscript):
            return self._subscript(v.expr, self.modpfx()) + "." + attr_name
        elif isinstance(v.expr, ast.CallFunc):
            return self._callfunc(v.expr, self.modpfx()) + "." + attr_name
        else:
            raise TranslationError("unsupported type (in _getattr)", v.expr)


    def modpfx(self):
        return strip_py(self.module_prefix)
        
    def _name(self, v, current_klass, top_level=False,
              return_none_for_module=False):

        if not hasattr(v, 'name'):
            name = v.attrname
        else:
            name = v.name
        if name == 'ilikesillynamesfornicedebugcode':
            print top_level, current_klass, repr(v)
            print self.top_level_vars
            print self.top_level_functions
            print self.local_arg_stack
            print "error..."

        local_var_names = None
        las = len(self.local_arg_stack)
        if las > 0:
            local_var_names = self.local_arg_stack[-1]

        if name == "True":
            return "true"
        elif name == "False":
            return "false"
        elif name == "None":
            return "null"
        elif name == '__name__' and current_klass is None:
            return self.modpfx() + name
        elif name == self.method_self:
            return "this"
        elif name in self.top_level_functions:
            return UU+self.modpfx() + name
        elif name in self.method_imported_globals:
            return UU+self.modpfx() + name
        elif not current_klass and las == 1 and name in self.top_level_vars:
            return UU+self.modpfx() + name
        elif name in local_var_names:
            if self.local_prefix:
                return self.local_prefix + "." + name
            else:
                return name
        elif self.imported_classes.has_key(name):
            return UU+self.imported_classes[name] + '.' + name
        elif name in self.top_level_classes:
            return UU+self.modpfx() + name
        elif name in self.module_imports() and return_none_for_module:
            return None
        elif name in PYJSLIB_BUILTIN_CLASSES:
            return "pyjslib." + pyjs_builtin_remap.get( name, name )
        elif current_klass:
            if name not in local_var_names and \
               name not in self.top_level_vars and \
               name not in PYJS_GLOBAL_VARS and \
               name not in self.top_level_functions:

                cls_name = current_klass
                if hasattr(cls_name, "name"):
                    cls_name_ = cls_name.name_
                    cls_name = cls_name.name
                else:
                    cls_name_ = current_klass + "_" # XXX ???
                name = UU+cls_name_ + "." + name
                if name == 'listener':
                    name = 'listener+' + name
                return name

        return name

    def _name2(self, v, current_klass, attr_name):
        obj = v.name

        if obj in self.method_imported_globals:
            call_name = UU+self.modpfx() + obj + "." + attr_name
        elif self.imported_classes.has_key(obj):
            call_name = UU+self.imported_classes[obj] + "." + obj + "." + attr_name
        elif obj in self.module_imports():
            call_name = obj + "." + attr_name
        else:
            call_name = UU+self._name(v, current_klass) + "." + attr_name

        return call_name


    def _getattr2(self, v, current_klass, attr_name):
        if isinstance(v.expr, ast.Getattr):
            call_name = self._getattr2(v.expr, current_klass, v.attrname + "." + attr_name)
        elif isinstance(v.expr, ast.Name) and v.expr.name in self.module_imports():
            call_name = UU+v.expr.name + '.' +v.attrname+"."+attr_name
        else:
            obj = self.expr(v.expr, current_klass)
            call_name = obj + "." + v.attrname + "." + attr_name

        return call_name

    def _class(self, node):
        class_name = self.modpfx() + uuprefix(node.name, 1)
        current_klass = Klass(class_name, class_name)
        init_method = None
        for child in node.code:
            if isinstance(child, ast.Function):
                current_klass.add_function(child.name)
                if child.name == "__init__":
                    init_method = child
        if len(node.bases) == 0:
            base_classes = [("object", "pyjslib.object")]
        else:
            base_classes = []
            for node_base in node.bases:
                if isinstance(node_base, ast.Name):
                    node_base_name = node_base.name
                    if self.imported_classes.has_key(node_base.name):
                        base_class = self.imported_classes[node_base.name] + '.' + node_base.name
                    else:
                        #base_class = self.modpfx() + node_base.name
                        base_class = self._name(node_base, None)
                elif isinstance(node_base, ast.Getattr):
                    # the bases are not in scope of the class so do not
                    # pass our class to self._name
                    node_base_name = node_base.attrname
                    base_class = self._name(node_base.expr, None) + \
                                 "." + node_base.attrname
                else:
                    raise TranslationError("unsupported type (in _class)", node_base)
                base_classes.append((node_base_name, base_class))
            current_klass.set_base(base_classes[0][1])

        if not init_method:
            init_method = ast.Function([], "__init__", ["self"], [], 0, None, [])

        if node.name in ['object', 'pyjslib.Object', 'pyjslib.object']:
            base_classes = []
        local_prefix = 'cls_definition'
        self.local_prefix = None
        print >>self.output, UU+class_name + """ = (function(){
    var cls_instance = pyjs__class_instance('%s');
    var %s = new Object();""" % (node.name, local_prefix,)

        for child in node.code:
            if isinstance(child, ast.Pass):
                pass
            elif isinstance(child, ast.Function):
                self.local_prefix = None
                self._method(child, current_klass, class_name, class_name, local_prefix)
            elif isinstance(child, ast.Assign):
                self.local_prefix = local_prefix
                self.add_local_arg(child.nodes[0].name)
                print >>self.output, "    %s.%s = %s" % (local_prefix, child.nodes[0].name, self.expr(child.expr, current_klass))
            elif isinstance(child, ast.Discard) and isinstance(child.expr, ast.Const):
                # Probably a docstring, turf it
                pass
            else:
                raise TranslationError("unsupported type (in _class)", child)
        print >>self.output, """\
    return pyjs__class_function(cls_instance, cls_definition, 
                                new Array(""" + ",".join(map(lambda x: x[1], base_classes)) + """));
})();"""

    def classattr(self, node, current_klass):
        self._assign(node, current_klass, True)

    def _raise(self, node, current_klass):
        if node.expr2:
            raise TranslationError("More than one expression unsupported",
                                   node)
        print >> self.output, "throw (%s);" % self.expr(
            node.expr1, current_klass)

    def _method(self, node, current_klass, class_name, class_name_, local_prefix):
        # reset global var scope
        self.method_imported_globals = set()

        arg_names = list(node.argnames)

        source_tracking = save_source_tracking = self.source_tracking
        save_has_js_return = self.has_js_return
        self.has_js_return = False
        classmethod = False
        staticmethod = False
        if node.decorators:
            for d in node.decorators:
                if d.name == "classmethod":
                    classmethod = True
                elif d.name == "staticmethod":
                    staticmethod = True
                elif d.name == "noSourceTracking":
                    source_tracking = False
        self.source_tracking = source_tracking
        if node.name == '__new__':
            staticmethod = True

        if (classmethod or staticmethod) and len(arg_names) > 0:
            self.method_self = arg_names[0]
        else:
            self.method_self = None
        self.method_self = None

        normal_arg_names = arg_names[0:]
        if node.kwargs:
            kwargname = normal_arg_names.pop()
        else:
            kwargname = None
        if node.varargs:
            varargname = normal_arg_names.pop()
        else:
            varargname = None
        declared_arg_names = list(normal_arg_names)
        #if node.kwargs: declared_arg_names.append(kwargname)

        if staticmethod:
            function_args = "(" + ", ".join(declared_arg_names) + ")"
        else:
            function_args = "(" + ", ".join(declared_arg_names[1:]) + ")"

        fexpr = node.name
        print >>self.output, "    "+local_prefix + '.' + node.name + " = pyjs__bind_method(cls_instance, '"+node.name+"', function" + function_args + " {"
        if staticmethod:
            self._static_method_init(node, declared_arg_names, varargname, kwargname, current_klass)
        elif classmethod:
            self._class_method_init(node, declared_arg_names, varargname, kwargname, current_klass)
        else:
            self._instance_method_init(node, declared_arg_names, varargname, kwargname, current_klass)

        # default arguments
        self._default_args_handler(node, declared_arg_names, current_klass, kwargname)

        local_arg_names = normal_arg_names + declared_arg_names

        if node.kwargs:
            local_arg_names.append(kwargname)
        if node.varargs:
            local_arg_names.append(varargname)


        # stack of local variable names for this function call
        self.local_arg_stack.append(local_arg_names)

        save_output = self.output
        self.output = StringIO()
        if self.source_tracking:
            print >>self.output, "track={module:%s, lineno:%d};trackstack.push(track);" % (self.raw_module_name, node.lineno)
        self.track_lineno(node, True)
        for child in node.code:
            self._stmt(child, current_klass)
        if self.source_tracking and self.has_js_return:
            self.source_tracking = False
            self.output = StringIO()
            for child in node.code:
                self._stmt(child, None)
        captured_output = self.output.getvalue()
        self.output = save_output
        print >>self.output, captured_output,


        # we need to return null always, so it is not undefined
        lastStmt = [p for p in node.code][-1]
        if not isinstance(lastStmt, ast.Return):
            if self.source_tracking:
                print >>self.output, "trackstack.pop();track=trackstack.pop();trackstack.push(track);"
            if not self._isNativeFunc(lastStmt):
                print >>self.output, "    return null;"

        # remove the top local arg names
        self.local_arg_stack.pop()

        print >>self.output, "}"

        if staticmethod:
            self._kwargs_parser(node, fexpr, normal_arg_names, current_klass, True)
        else:
            self._kwargs_parser(node, fexpr, normal_arg_names[1:], current_klass, True)

        self.method_self = None
        self.method_imported_globals = set()
        self.has_js_return = save_has_js_return
        self.source_tracking = save_source_tracking

    def _isNativeFunc(self, node):
        if isinstance(node, ast.Discard):
            if isinstance(node.expr, ast.CallFunc):
                if isinstance(node.expr.node, ast.Name) and \
                       node.expr.node.name == NATIVE_JS_FUNC_NAME:
                    return True
        return False

    def _stmt(self, node, current_klass):
        self.track_lineno(node)

        if isinstance(node, ast.Return):
            self._return(node, current_klass)
        elif isinstance(node, ast.Break):
            self._break(node, current_klass)
        elif isinstance(node, ast.Continue):
            self._continue(node, current_klass)
        elif isinstance(node, ast.Assign):
            self._assign(node, current_klass)
        elif isinstance(node, ast.AugAssign):
            self._augassign(node, current_klass)
        elif isinstance(node, ast.Discard):
            self._discard(node, current_klass)
        elif isinstance(node, ast.If):
            self._if(node, current_klass)
        elif isinstance(node, ast.For):
            self._for(node, current_klass)
        elif isinstance(node, ast.While):
            self._while(node, current_klass)
        elif isinstance(node, ast.Subscript):
            self._subscript_stmt(node, current_klass)
        elif isinstance(node, ast.Global):
            self._global(node, current_klass)
        elif isinstance(node, ast.Pass):
            pass
        elif isinstance(node, ast.Function):
            self._function(node, True)
        elif isinstance(node, ast.Printnl):
           self._print(node, current_klass)
        elif isinstance(node, ast.Print):
           self._print(node, current_klass)
        elif isinstance(node, ast.TryExcept):
            self._tryExcept(node, current_klass)
        elif isinstance(node, ast.Raise):
            self._raise(node, current_klass)
        else:
            raise TranslationError("unsupported type (in _stmt)", node)


    def get_start_line(self, node, lineno):
        if node:
            if hasattr(node, "lineno") and node.lineno != None and node.lineno < lineno:
                lineno = node.lineno
            if hasattr(node, 'getChildren'):
                for n in node.getChildren():
                    lineno = self.get_start_line(n, lineno)
        return lineno

    def get_line_trace(self, node):
        lineNum1 = "Unknown"
        srcLine = ""
        if hasattr(node, "lineno"):
            if node.lineno != None:
                lineNum2 = node.lineno
                lineNum1 = self.get_start_line(node, lineNum2)
                srcLine = self.src[min(lineNum1, len(self.src))-1].strip()
                if lineNum1 < lineNum2:
                    srcLine += ' ... ' + self.src[min(lineNum2, len(self.src))-1].strip()
                srcLine = srcLine.replace('\\', '\\\\')
                srcLine = srcLine.replace('"', '\\"')
                srcLine = srcLine.replace("'", "\\'")

        return self.raw_module_name + ".py, line " \
               + str(lineNum1) + ":"\
               + "\\n" \
               + "    " + srcLine

    def _augassign(self, node, current_klass):
        v = node.node
        if isinstance(v, ast.Getattr):
            # XXX HACK!  don't allow += on return result of getattr.
            # TODO: create a temporary variable or something.
            lhs = self._getattr(v, current_klass, False)
        else:
            lhs = self._name(node.node, current_klass)
        op = node.op
        rhs = self.expr(node.expr, current_klass)
        print >>self.output, "    " + lhs + " " + op + " " + rhs + ";"


    def _assign(self, node, current_klass, top_level = False):
        if len(node.nodes) != 1:
            tempvar = '__temp'+str(node.lineno)
            tnode = ast.Assign([ast.AssName(tempvar, "OP_ASSIGN", node.lineno)], node.expr, node.lineno)
            self._assign(tnode, current_klass, top_level)
            for v in node.nodes:
               tnode2 = ast.Assign([v], ast.Name(tempvar, node.lineno), node.lineno)
               self._assign(tnode2, current_klass, top_level)
            return

        local_var_names = None
        if len(self.local_arg_stack) > 0:
            local_var_names = self.local_arg_stack[-1]

        def _lhsFromAttr(v, current_klass):
            attr_name = v.attrname
            if isinstance(v.expr, ast.Name):
                obj = v.expr.name
                lhs = self._name(v.expr, current_klass) + "." + attr_name
            elif isinstance(v.expr, ast.Getattr):
                lhs = self._getattr(v, current_klass)
            elif isinstance(v.expr, ast.Subscript):
                lhs = self._subscript(v.expr, current_klass) + "." + attr_name
            else:
                raise TranslationError("unsupported type (in _assign)", v.expr)
            return lhs

        def _lhsFromName(v, top_level, current_klass):
            if top_level:
                if current_klass:
                    lhs = UU+current_klass.name_ + "." + v.name
                else:
                    self.top_level_vars.add(v.name)
                    vname = self.modpfx() + v.name
                    if not self.modpfx() and v.name not in\
                           self.method_imported_globals:
                        lhs = "var " + vname
                    else:
                        lhs = UU + vname
                    self.add_local_arg(v.name)
            else:
                if v.name in local_var_names:
                    lhs = v.name
                elif v.name in self.method_imported_globals:
                    lhs = self.modpfx() + v.name
                else:
                    lhs = "var " + v.name
                    self.add_local_arg(v.name)
            return lhs

        dbg = 0
        v = node.nodes[0]
        if isinstance(v, ast.AssAttr):
            lhs = _lhsFromAttr(v, current_klass)
            if v.flags == "OP_ASSIGN":
                op = "="
            else:
                raise TranslationError("unsupported flag (in _assign)", v)

        elif isinstance(v, ast.AssName):
            lhs = _lhsFromName(v, top_level, current_klass)
            if v.flags == "OP_ASSIGN":
                op = "="
            else:
                raise TranslationError("unsupported flag (in _assign)", v)
        elif isinstance(v, ast.Subscript):
            if v.flags == "OP_ASSIGN":
                obj = self.expr(v.expr, current_klass)
                if len(v.subs) != 1:
                    raise TranslationError("must have one sub (in _assign)", v)
                idx = self.expr(v.subs[0], current_klass)
                value = self.expr(node.expr, current_klass)
                print >>self.output, "    " + self.track_call(obj + ".__setitem__(" + idx + ", " + value + ");")
                return
            else:
                raise TranslationError("unsupported flag (in _assign)", v)
        elif isinstance(v, (ast.AssList, ast.AssTuple)):
            uniqueID = self.nextTupleAssignID
            self.nextTupleAssignID += 1
            tempName = "__tupleassign" + str(uniqueID) + "__"
            print >>self.output, "    var " + tempName + " = " + \
                                 self.expr(node.expr, current_klass) + ";"
            for index,child in enumerate(v.getChildNodes()):
                rhs = self.track_call(tempName + ".__getitem__(" + str(index) + ")")

                if isinstance(child, ast.AssAttr):
                    lhs = _lhsFromAttr(child, current_klass)
                elif isinstance(child, ast.AssName):
                    lhs = _lhsFromName(child, top_level, current_klass)
                elif isinstance(child, ast.Subscript):
                    if child.flags == "OP_ASSIGN":
                        obj = self.expr(child.expr, current_klass)
                        if len(child.subs) != 1:
                            raise TranslationError("must have one sub " +
                                                   "(in _assign)", child)
                        idx = self.expr(child.subs[0], current_klass)
                        value = self.expr(node.expr, current_klass)
                        print >>self.output, "    " + self.track_call(obj + ".__setitem__(" \
                                           + idx + ", " + rhs + ");")
                        continue
                print >>self.output, "    " + lhs + " = " + rhs + ";"
            return
        else:
            raise TranslationError("unsupported type (in _assign)", v)

        rhs = self.expr(node.expr, current_klass)
        if dbg:
            print "b", repr(node.expr), rhs
        print >>self.output, "    " + lhs + " " + op + " " + rhs + ";"


    def _discard(self, node, current_klass):
        
        if isinstance(node.expr, ast.CallFunc):
            if isinstance(node.expr.node, ast.Name) and node.expr.node.name == NATIVE_JS_FUNC_NAME:
                if len(node.expr.args) != 1:
                    raise TranslationError("native javascript function %s must have one arg" % NATIVE_JS_FUNC_NAME, node.expr)
                if not isinstance(node.expr.args[0], ast.Const):
                    raise TranslationError("native javascript function %s must have constant arg" % NATIVE_JS_FUNC_NAME, node.expr)
                raw_js = node.expr.args[0].value
                if self.re_return.search(raw_js):
                    self.has_js_return = True
                print >>self.output, raw_js
            else:
                expr = self._callfunc(node.expr, current_klass)
                print >>self.output, "    " + expr + ";"

        elif isinstance(node.expr, ast.Const):
            if node.expr.value is not None: # Empty statements generate ignore None
                print >>self.output, self._const(node.expr)
        else:
            raise TranslationError("unsupported type (in _discard)", node.expr)


    def _if(self, node, current_klass):
        for i in range(len(node.tests)):
            test, consequence = node.tests[i]
            if i == 0:
                keyword = "if"
            else:
                keyword = "else if"

            self._if_test(keyword, test, consequence, current_klass)

        if node.else_:
            keyword = "else"
            test = None
            consequence = node.else_

            self._if_test(keyword, test, consequence, current_klass)


    def _if_test(self, keyword, test, consequence, current_klass):
        if test:
            expr = self.expr(test, current_klass)

            print >>self.output, "    " + keyword + " (" + self.track_call("pyjslib.bool(" + expr + ")")+") {"
        else:
            print >>self.output, "    " + keyword + " {"

        if isinstance(consequence, ast.Stmt):
            for child in consequence.nodes:
                self._stmt(child, current_klass)
        else:
            raise TranslationError("unsupported type (in _if_test)", consequence)

        print >>self.output, "    }"


    def _from(self, node):
        for name in node.names:
            # look up "hack" in AppTranslator as to how findFile gets here
            module_name = node.modname + "." + name[0]
            try:
                ff = self.findFile(module_name + ".py")
            except Exception:
                ff = None
            if ff:
                self.add_imported_module(module_name)
            else:
                self.imported_classes[name[0]] = node.modname
            if name[1]:
                tnode = ast.Assign([ast.AssName(name[1], "OP_ASSIGN", node.lineno)], ast.Name(module_name, node.lineno), node.lineno)
                self._assign(tnode, None, True)


    def _compare(self, node, current_klass):
        lhs = self.expr(node.expr, current_klass)

        if len(node.ops) != 1:
            raise TranslationError("only one ops supported (in _compare)", node)

        op = node.ops[0][0]
        rhs_node = node.ops[0][1]
        rhs = self.expr(rhs_node, current_klass)

        if op == "==":
            return self.track_call("pyjslib.eq(%s, %s)" % (lhs, rhs))
        if op == "in":
            return self.track_call(rhs + ".__contains__(" + lhs + ")")
        elif op == "not in":
            return "!" + self.track_call(rhs + ".__contains__(" + lhs + ")")
        elif op == "is":
            op = "==="
        elif op == "is not":
            op = "!=="

        return "(" + lhs + " " + op + " " + rhs + ")"


    def _not(self, node, current_klass):
        expr = self.expr(node.expr, current_klass)

        return "!(" + expr + ")"

    def _or(self, node, current_klass):
        expr = "("+(") || (".join([self.expr(child, current_klass) for child in node.nodes]))+')'
        return expr

    def _and(self, node, current_klass):
        expr = "("+(") && (".join([self.expr(child, current_klass) for child in node.nodes]))+")"
        return expr

    def _for(self, node, current_klass):
        assign_name = ""
        assign_tuple = ""

        # based on Bob Ippolito's Iteration in Javascript code
        if isinstance(node.assign, ast.AssName):
            assign_name = node.assign.name
            self.add_local_arg(assign_name)
            if node.assign.flags == "OP_ASSIGN":
                op = "="
        elif isinstance(node.assign, ast.AssTuple):
            op = "="
            i = 0
            for child in node.assign:
                child_name = child.name
                if assign_name == "":
                    assign_name = "temp_" + child_name
                self.add_local_arg(child_name)
                assign_tuple += """
                var %(child_name)s %(op)s """ % locals()
                assign_tuple += self.track_call("""%(assign_name)s.__getitem__(%(i)i);
                """ % locals())
                i += 1
        else:
            raise TranslationError("unsupported type (in _for)", node.assign)

        if isinstance(node.list, ast.Name):
            list_expr = self._name(node.list, current_klass)
        elif isinstance(node.list, ast.Getattr):
            list_expr = self._getattr(node.list, current_klass)
        elif isinstance(node.list, ast.CallFunc):
            list_expr = self._callfunc(node.list, current_klass)
        elif isinstance(node.list, ast.Subscript):
            list_expr = self._subscript(node.list, current_klass)
        elif isinstance(node.list, ast.Const):
            list_expr = self._const(node.list)
        elif isinstance(node.list, ast.Const):
            list_expr = self._const(node.list)
        elif isinstance(node.list, ast.List):
            list_expr = self._list(node.list, current_klass)
        elif isinstance(node.list, ast.Slice):
            list_expr = self._slice(node.list, current_klass)
        else:
            raise TranslationError("unsupported type (in _for)", node.list)

        lhs = "var " + assign_name
        iterator_name = "__" + assign_name

        if self.source_tracking:
            print >>self.output, "var pyjs__trackstack_size=trackstack.length;"
        print >>self.output, """
        var %(iterator_name)s = """ % locals() + self.track_call("%(list_expr)s.__iter__();" % locals()) + """
        try {
            while (true) {
                %(lhs)s %(op)s""" % locals(),
        print >>self.output, self.track_call("%(iterator_name)s.next();"% locals())
        print >>self.output, """\
                %(assign_tuple)s
        """ % locals()
        for node in node.body.nodes:
            self._stmt(node, current_klass)
        print >>self.output, """
            }
        } catch (e) {
            if (e.__name__ != pyjslib.StopIteration.__name__) {
                throw e;
            }
        }
        """ % locals()
        if self.source_tracking:
            print >>self.output, """if (trackstack.length > pyjs__trackstack_size) {
    trackstack = trackstack.slice(0,pyjs__trackstack_size);
    track = trackstack.slice(-1)[0];
}
track.module='%s';""" % self.raw_module_name


    def _while(self, node, current_klass):
        test = self.expr(node.test, current_klass)
        print >>self.output, "    while (" + self.track_call("pyjslib.bool(" + test + ")") + ") {"
        if isinstance(node.body, ast.Stmt):
            for child in node.body.nodes:
                self._stmt(child, current_klass)
        else:
            raise TranslationError("unsupported type (in _while)", node.body)
        print >>self.output, "    }"


    def _const(self, node):
        if isinstance(node.value, int):
            return str(node.value)
        elif isinstance(node.value, float):
            return str(node.value)
        elif isinstance(node.value, basestring):
            v = node.value
            if isinstance(node.value, unicode):
                v = v.encode('utf-8')
            return  "String('%s')" % escapejs(v)
        elif node.value is None:
            return "null"
        else:
            raise TranslationError("unsupported type (in _const)", node)

    def _unaryadd(self, node, current_klass):
        return self.expr(node.expr, current_klass)

    def _unarysub(self, node, current_klass):
        return "-" + self.expr(node.expr, current_klass)

    def _add(self, node, current_klass):
        return self.expr(node.left, current_klass) + " + " + self.expr(node.right, current_klass)

    def _sub(self, node, current_klass):
        return self.expr(node.left, current_klass) + " - " + self.expr(node.right, current_klass)

    def _div(self, node, current_klass):
        return self.expr(node.left, current_klass) + " / " + self.expr(node.right, current_klass)

    def _mul(self, node, current_klass):
        return self.expr(node.left, current_klass) + " * " + self.expr(node.right, current_klass)

    def _mod(self, node, current_klass):
        if isinstance(node.left, ast.Const) and isinstance(node.left.value, StringType):
           #self.imported_js.add("sprintf.js") # Include the sprintf functionality if it is used
           #return "sprintf("+self.expr(node.left, current_klass) + ", " + self.expr(node.right, current_klass)+")"
           return self.track_call("pyjslib.sprintf("+self.expr(node.left, current_klass) + ", " + self.expr(node.right, current_klass)+")")
        return self.expr(node.left, current_klass) + " % " + self.expr(node.right, current_klass)

    def _power(self, node, current_klass):
        return "Math.pow("+self.expr(node.left, current_klass) + "," + self.expr(node.right, current_klass) + ")"

    def _invert(self, node, current_klass):
        return "~" + self.expr(node.expr, current_klass)

    def _bitand(self, node, current_klass):
        return " & ".join([self.expr(child, current_klass) for child in node.nodes])

    def _bitshiftleft(self, node, current_klass):
        return self.expr(node.left, current_klass) + " << " + self.expr(node.right, current_klass)

    def _bitshiftright(self, node, current_klass):
        return self.expr(node.left, current_klass) + " >>> " + self.expr(node.right, current_klass)

    def _bitxor(self,node, current_klass):
        return " ^ ".join([self.expr(child, current_klass) for child in node.nodes])

    def _bitor(self, node, current_klass):
        return " | ".join([self.expr(child, current_klass) for child in node.nodes])

    def _subscript(self, node, current_klass):
        if node.flags == "OP_APPLY":
            if len(node.subs) == 1:
                return self.track_call(self.expr(node.expr, current_klass) + ".__getitem__(" + self.expr(node.subs[0], current_klass) + ")")
            else:
                raise TranslationError("must have one sub (in _subscript)", node)
        else:
            raise TranslationError("unsupported flag (in _subscript)", node)

    def _subscript_stmt(self, node, current_klass):
        if node.flags == "OP_DELETE":
            print >>self.output, "    " + self.track_call(self.expr(node.expr, current_klass) + ".__delitem__(" + self.expr(node.subs[0], current_klass) + ");")
        else:
            raise TranslationError("unsupported flag (in _subscript)", node)

    def _list(self, node, current_klass):
        return self.track_call("new pyjslib.List([" + ", ".join([self.expr(x, current_klass) for x in node.nodes]) + "])")

    def _dict(self, node, current_klass):
        items = []
        for x in node.items:
            key = self.expr(x[0], current_klass)
            value = self.expr(x[1], current_klass)
            items.append("[" + key + ", " + value + "]")
        return self.track_call("new pyjslib.Dict([" + ", ".join(items) + "])")

    def _tuple(self, node, current_klass):
        return self.track_call("new pyjslib.Tuple([" + ", ".join([self.expr(x, current_klass) for x in node.nodes]) + "])")

    def _lambda(self, node, current_klass):
        if node.varargs:
            raise TranslationError("varargs are not supported in Lambdas", node)
        if node.kwargs:
            raise TranslationError("kwargs are not supported in Lambdas", node)
        res = StringIO()
        arg_names = list(node.argnames)
        function_args = ", ".join(arg_names)
        for child in node.getChildNodes():
            expr = self.expr(child, None)
        print >> res, "function (%s){" % function_args
        self._default_args_handler(node, arg_names, None, None,
                                   output=res)
        print >> res, 'return %s;}' % expr
        return res.getvalue()

    def _slice(self, node, current_klass):
        if node.flags == "OP_APPLY":
            lower = "null"
            upper = "null"
            if node.lower != None:
                lower = self.expr(node.lower, current_klass)
            if node.upper != None:
                upper = self.expr(node.upper, current_klass)
            return  "pyjslib.slice(" + self.expr(node.expr, current_klass) + ", " + lower + ", " + upper + ")"
        else:
            raise TranslationError("unsupported flag (in _slice)", node)

    def _global(self, node, current_klass):
        for name in node.names:
            self.method_imported_globals.add(name)

    def expr(self, node, current_klass):
        if isinstance(node, ast.Const):
            return self._const(node)
        # @@@ not sure if the parentheses should be here or in individual operator functions - JKT
        elif isinstance(node, ast.Mul):
            return " ( " + self._mul(node, current_klass) + " ) "
        elif isinstance(node, ast.Add):
            return " ( " + self._add(node, current_klass) + " ) "
        elif isinstance(node, ast.Sub):
            return " ( " + self._sub(node, current_klass) + " ) "
        elif isinstance(node, ast.Div):
            return " ( " + self._div(node, current_klass) + " ) "
        elif isinstance(node, ast.Mod):
            return self._mod(node, current_klass)
        elif isinstance(node, ast.Power):
            return self._power(node, current_klass)
        elif isinstance(node, ast.UnaryAdd):
            return self._unaryadd(node, current_klass)
        elif isinstance(node, ast.UnarySub):
            return self._unarysub(node, current_klass)
        elif isinstance(node, ast.Not):
            return self._not(node, current_klass)
        elif isinstance(node, ast.Or):
            return self._or(node, current_klass)
        elif isinstance(node, ast.And):
            return self._and(node, current_klass)
        elif isinstance(node, ast.Invert):
            return self._invert(node, current_klass)
        elif isinstance(node, ast.Bitand):
            return "("+self._bitand(node, current_klass)+")"
        elif isinstance(node,ast.LeftShift):
            return self._bitshiftleft(node, current_klass)
        elif isinstance(node, ast.RightShift):
            return self._bitshiftright(node, current_klass)
        elif isinstance(node, ast.Bitxor):
            return "("+self._bitxor(node, current_klass)+")"
        elif isinstance(node, ast.Bitor):
            return "("+self._bitor(node, current_klass)+")"
        elif isinstance(node, ast.Compare):
            return self._compare(node, current_klass)
        elif isinstance(node, ast.CallFunc):
            return self._callfunc(node, current_klass)
        elif isinstance(node, ast.Name):
            return self._name(node, current_klass)
        elif isinstance(node, ast.Subscript):
            return self._subscript(node, current_klass)
        elif isinstance(node, ast.Getattr):
            attr = self._getattr(node, current_klass)
            if self.attribute_checking and attr.find('.') >= 0:
                if attr.find('(') < 0 and not self.debug:
                    attr = "("+attr+"===undefined?(function(){throw new TypeError('"+attr+" is undefined')})():"+attr+")"
                else:
                    attr_ = attr
                    if self.source_tracking or self.debug:
                        _source_tracking = self.source_tracking
                        _debug = self.debug
                        self.source_tracking = self.debug = False
                        attr_ = self._getattr(node, current_klass)
                        self.source_tracking = _source_tracking
                        self.debug = _debug
                    attr = "(function(){var pyjs__testval="+attr+";return (pyjs__testval===undefined?(function(){throw new TypeError('"+attr_.replace("'", "\\'")+" is undefined')})():pyjs__testval)})()"
            return attr
        elif isinstance(node, ast.List):
            return self._list(node, current_klass)
        elif isinstance(node, ast.Dict):
            return self._dict(node, current_klass)
        elif isinstance(node, ast.Tuple):
            return self._tuple(node, current_klass)
        elif isinstance(node, ast.Slice):
            return self._slice(node, current_klass)
        elif isinstance(node, ast.Lambda):
            return self._lambda(node, current_klass)
        else:
            raise TranslationError("unsupported type (in expr)", node)



def translate(file_name, module_name, debug=False, 
              function_argument_checking=True,
              attribute_checking=True, source_tracking=True,
              store_source=True,
             ):
    f = file(file_name, "r")
    src = f.read()
    f.close()
    output = StringIO()
    mod = compiler.parseFile(file_name)
    t = Translator(module_name, module_name, module_name, src, debug, mod, output,
                   function_argument_checking=function_argument_checking,
                   attribute_checking=attribute_checking,
                   source_tracking=source_tracking,
                   store_source=store_source
                  )
    return output.getvalue()


class PlatformParser:
    def __init__(self, platform_dir = "", verbose=True):
        self.platform_dir = platform_dir
        self.parse_cache = {}
        self.platform = ""
        self.verbose = verbose

    def setPlatform(self, platform):
        self.platform = platform

    def parseModule(self, module_name, file_name):

        importing = False
        if not self.parse_cache.has_key(file_name):
            importing = True
            mod = compiler.parseFile(file_name)
            self.parse_cache[file_name] = mod
        else:
            mod = self.parse_cache[file_name]

        override = False
        platform_file_name = self.generatePlatformFilename(file_name)
        if self.platform and os.path.isfile(platform_file_name):
            mod = copy.deepcopy(mod)
            mod_override = compiler.parseFile(platform_file_name)
            self.merge(mod, mod_override)
            override = True

        if self.verbose:
            if override:
                print "Importing %s (Platform %s)" % (module_name, self.platform)
            elif importing:
                print "Importing %s" % (module_name)

        return mod, override

    def generatePlatformFilename(self, file_name):
        (module_name, extension) = os.path.splitext(os.path.basename(file_name))
        platform_file_name = module_name + self.platform + extension

        return os.path.join(os.path.dirname(file_name), self.platform_dir, platform_file_name)

    def merge(self, tree1, tree2):
        for child in tree2.node:
            if isinstance(child, ast.Function):
                self.replaceFunction(tree1, child.name, child)
            elif isinstance(child, ast.Class):
                self.replaceClassMethods(tree1, child.name, child)

        return tree1

    def replaceFunction(self, tree, function_name, function_node):
        # find function to replace
        for child in tree.node:
            if isinstance(child, ast.Function) and child.name == function_name:
                self.copyFunction(child, function_node)
                return
        raise TranslationError("function not found: " + function_name, function_node)

    def replaceClassMethods(self, tree, class_name, class_node):
        # find class to replace
        old_class_node = None
        for child in tree.node:
            if isinstance(child, ast.Class) and child.name == class_name:
                old_class_node = child
                break

        if not old_class_node:
            raise TranslationError("class not found: " + class_name, class_node)

        # replace methods
        for function_node in class_node.code:
            if isinstance(function_node, ast.Function):
                found = False
                for child in old_class_node.code:
                    if isinstance(child, ast.Function) and child.name == function_node.name:
                        found = True
                        self.copyFunction(child, function_node)
                        break

                if not found:
                    raise TranslationError("class method not found: " + class_name + "." + function_node.name, function_node)

    def copyFunction(self, target, source):
        target.code = source.code
        target.argnames = source.argnames
        target.defaults = source.defaults
        target.doc = source.doc # @@@ not sure we need to do this any more

def dotreplace(fname):
    path, ext = os.path.splitext(fname)
    return path.replace(".", "/") + ext

class AppTranslator:

    def __init__(self, library_dirs=[], parser=None, dynamic=False,
                 optimize=False, verbose=True, function_argument_checking=True,
                 attribute_checking=True, source_tracking=True,
                 store_source=True,
                ):
        self.extension = ".py"
        self.optimize = optimize
        self.library_modules = []
        self.overrides = {}
        self.library_dirs = path + library_dirs
        self.dynamic = dynamic
        self.verbose = verbose
        self.function_argument_checking = function_argument_checking
        self.attribute_checking = attribute_checking
        self.source_tracking = source_tracking
        self.store_source = store_source

        if not parser:
            self.parser = PlatformParser()
        else:
            self.parser = parser

        self.parser.dynamic = dynamic

    def findFile(self, file_name):
        if os.path.isfile(file_name):
            return file_name

        for library_dir in self.library_dirs:
            file_name = dotreplace(file_name)
            full_file_name = os.path.join(
                os.path.abspath(os.path.dirname(__file__)), library_dir, file_name)
            if os.path.isfile(full_file_name):
                return full_file_name

            fnameinit, ext = os.path.splitext(file_name)
            fnameinit = fnameinit + "/__init__.py"

            full_file_name = os.path.join(
                os.path.abspath(os.path.dirname(__file__)), library_dir, fnameinit)
            if os.path.isfile(full_file_name):
                return full_file_name

        raise Exception("file not found: " + file_name)

    def _translate(self, module_name, is_app=True, debug=False,
                   imported_js=set()):
        if module_name not in self.library_modules:
            self.library_modules.append(module_name)

        file_name = self.findFile(module_name + self.extension)

        output = StringIO()

        f = file(file_name, "r")
        src = f.read()
        f.close()

        mod, override = self.parser.parseModule(module_name, file_name)
        if override:
            override_name = "%s.%s" % (self.parser.platform.lower(),
                                           module_name)
            self.overrides[override_name] = override_name
        if is_app:
            mn = '__main__'
        else:
            mn = module_name
        t = Translator(mn, module_name, module_name,
                       src, debug, mod, output, self.dynamic, self.optimize,
                       self.findFile, function_argument_checking=self.function_argument_checking,
                       attribute_checking = self.attribute_checking,
                       source_tracking = self.source_tracking,
                       store_source = self.store_source,
                      )

        module_str = output.getvalue()
        imported_js.update(set(t.imported_js))
        imported_modules_str = ""
        for module in t.imported_modules:
            if module not in self.library_modules:
                self.library_modules.append(module)
                #imported_js.update(set(t.imported_js))
                #imported_modules_str += self._translate(
                #    module, False, debug=debug, imported_js=imported_js)

        return imported_modules_str + module_str


    def translate(self, module_name, is_app=True, debug=False,
                  library_modules=[]):
        app_code = StringIO()
        lib_code = StringIO()
        imported_js = set()
        self.library_modules = []
        self.overrides = {}
        for library in library_modules:
            if library.endswith(".js"):
                imported_js.add(library)
                continue
            self.library_modules.append(library)
            if self.verbose:
                print 'Including LIB', library
            print >> lib_code, '\n//\n// BEGIN LIB '+library+'\n//\n'
            print >> lib_code, self._translate(
                library, False, debug=debug, imported_js=imported_js)

            print >> lib_code, "/* initialize static library */"
            print >> lib_code, "%s%s();\n" % (UU, library)

            print >> lib_code, '\n//\n// END LIB '+library+'\n//\n'
        if module_name:
            print >> app_code, self._translate(
                module_name, is_app, debug=debug, imported_js=imported_js)
        for js in imported_js:
           path = self.findFile(js)
           if os.path.isfile(path):
              if self.verbose:
                  print 'Including JS', js
              print >> lib_code,  '\n//\n// BEGIN JS '+js+'\n//\n'
              print >> lib_code, file(path).read()
              print >> lib_code,  '\n//\n// END JS '+js+'\n//\n'
           else:
              print >>sys.stderr, 'Warning: Unable to find imported javascript:', js
        return lib_code.getvalue(), app_code.getvalue()

usage = """
  usage: %s file_name [module_name]
"""

def main():
    import sys
    if len(sys.argv)<2:
        print >> sys.stderr, usage % sys.argv[0]
        sys.exit(1)
    file_name = os.path.abspath(sys.argv[1])
    if not os.path.isfile(file_name):
        print >> sys.stderr, "File not found %s" % file_name
        sys.exit(1)
    if len(sys.argv) > 2:
        module_name = sys.argv[2]
    else:
        module_name = None
    print translate(file_name, module_name),

if __name__ == "__main__":
    main()

