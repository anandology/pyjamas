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
import hashlib
import logging

import pyjs

if pyjs.pyjspth is None:
    LIBRARY_PATH = os.path.abspath(os.path.dirname(__file__))
else:
    LIBRARY_PATH = os.path.join(pyjs.pyjspth, "pyjs", "src", "pyjs")

# this is the python function used to wrap native javascript
NATIVE_JS_FUNC_NAME = "JS"

JS_RESERVED_WORDS = frozenset((
    'abstract',
    'as',
    'boolean',
    'break',
    'byte',
    'case',
    'catch',
    'char',
    'class',
    'continue',
    'const',
    'debugger',
    'default',
    'delete',
    'do',
    'double',
    'else',
    'enum',
    'export',
    'extends',
    'false',
    'final',
    'finally',
    'float',
    'for',
    'function',
    'goto',
    'if',
    'implements',
    'import',
    'in',
    'instanceof',
    'int',
    'interface',
    'is',
    'long',
    'namespace',
    'native',
    'new',
    'null',
    'package',
    'private',
    'protected',
    'public',
    'return',
    'short',
    'static',
    'super',
    'switch',
    'synchronized',
    'this',
    'throw',
	'throws',
    'transient',
    'true',
    'try',
    'typeof',
    'use',
    'var',
    'void',
    'volatile',
    'while',
    'with',
    ))

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
                           "type",
                           "pow",
                           "hex",
                           "oct",
                           "round",
                           "divmod",
                           "all",
                           "any",
                           "callable",
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

PYJSLIB_BUILTIN_MAPPING = {\
    'True' : 'true',
    'False': 'false',
    'None': 'null',
    'super': 'pyjslib._super',
}

SCOPE_KEY = 0

# Variable names that should be remapped in functions/methods
# arguments -> arguments_
# arguments_ -> arguments__
# etc.
pyjs_vars_remap_names = [\
    'arguments', 'default', 'this', 'var',
]
pyjs_vars_remap = []
for a in pyjs_vars_remap_names:
    pyjs_vars_remap.append(re.compile('^%s$' % a))

# Attributes that should be remapped in classes
pyjs_attrib_remap_names = [\
    'name', 'prototype', 'call', 'apply', 'constructor', 
    # Specific for IE6:
    'default',
]
pyjs_attrib_remap = []
for a in pyjs_attrib_remap_names:
    pyjs_attrib_remap.append(re.compile('(.*(^|[.]))(%s_*)(([.].*)|$)' % a))

re_return = re.compile(r'\breturn\b')
class __Pyjamas__(object):
    console = "console"

    def JS(self, node):
        if isinstance(node.args[0], ast.Const):
            if re_return.search(node.args[0].value):
                self.has_js_return = True
            return node.args[0].value, not re_return.search(node.args[0].value) is None
        else:
            raise TranslationError(
                "native js functions only support constant strings",
                node.node, self.module_name)

    def wnd(self, node):
        if len(node.args) != 0:
            raise TranslationError(
                "native wnd function doesn't support arguments",
                node.node, self.module_name)
        return '$wnd', False

    def doc(self, node):
        if len(node.args) != 0:
            raise TranslationError(
                "native doc function doesn't support arguments",
                node.node, self.module_name)
        return '$doc', False
__pyjamas__ = __Pyjamas__()

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
    def __init__(self, message, node, module_name=''):
        if node:
            lineno = node.lineno
        else:
            lineno = "Unknown"
        self.message = "%s line %s:\n%s\n%s" % (module_name, lineno, message, node)

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

class Translator:

    decorator_compiler_options = {\
        'Debug': ('debug', True),
        'noDebug': ('debug', False),
        'PrintStatements': ('print_statements', True),
        'noPrintStatements': ('print_statements', False),
        'FunctionArgumentChecking': ('function_argument_checking', True),
        'noFunctionArgumentChecking': ('function_argument_checking', False),
        'AttributeChecking': ('attribute_checking', True),
        'noAttributeChecking': ('attribute_checking', False),
        'BoundMethods': ('bound_methods', True),
        'noBoundMethods': ('bound_methods', False),
        'SourceTracking': ('source_tracking', True),
        'noSourceTracking': ('source_tracking', False),
        'LineTracking': ('line_tracking', True),
        'noLineTracking': ('line_tracking', False),
        'StoreSource': ('store_source', True),
        'noStoreSource': ('store_source', False),
    }

    def __init__(self, mn, module_name, raw_module_name, src, mod, output,
                 dynamic=0, findFile=None,
                 debug = False,
                 print_statements=True,
                 function_argument_checking=True,
                 attribute_checking=True,
                 bound_methods=True,
                 source_tracking=True,
                 line_tracking=True,
                 store_source=True,
                ):

        if module_name:
            self.module_prefix = module_name + "."
        else:
            self.module_prefix = ""
        self.module_name = module_name
        self.raw_module_name = raw_module_name
        src = src.replace("\r\n", "\n")
        src = src.replace("\n\r", "\n")
        src = src.replace("\r",   "\n")
        self.src = src.split("\n")

        self.output = output
        self.dynamic = dynamic
        self.findFile = findFile
        # compile options
        self.debug = debug
        self.print_statements = print_statements
        self.function_argument_checking = function_argument_checking
        self.attribute_checking = attribute_checking
        self.bound_methods = bound_methods
        self.source_tracking = source_tracking
        self.line_tracking = line_tracking
        self.store_source = store_source

        self.imported_modules = []
        self.imported_js = set()
        self.local_prefix = None
        self.track_lines = {}
        self.stacksize_depth = 0
        self.option_stack = []
        self.lookup_stack = [{}]
        self.indent_level = 0
        self.__unique_ids__ = {}

        for v in PYJSLIB_BUILTIN_FUNCTIONS:
            # rename reserved words, pyjslib has to handle this internally
            if v in JS_RESERVED_WORDS:
                vf = v + '_'
            else:
                vf = v
            self.add_lookup("builtin", v, "pyjslib." + vf)
        for v in PYJSLIB_BUILTIN_CLASSES:
            self.add_lookup("builtin", v, "pyjslib." + v)
        for k in PYJSLIB_BUILTIN_MAPPING.keys():
            self.add_lookup("builtin", k, PYJSLIB_BUILTIN_MAPPING[k])

        if '.' in module_name:
            vdec = ''
        else:
            if module_name in JS_RESERVED_WORDS:
                raise TranslationError(
                    "reserved word used for top-level module %r" % module_name,
                    mod, self.module_name)

            vdec = 'var '
        print >>self.output, self.spacing() + "/* start module: %s */" % module_name
        print >>self.output, self.spacing() + '%s%s = $pyjs.loaded_modules["%s"] = function (__mod_name__) {' % (vdec, module_name, module_name)

        print >>self.output, self.spacing() + "if("+module_name+".__was_initialized__) return %s;"% module_name
        print >>self.output, self.spacing() + module_name+".__was_initialized__ = true;"
        print >>self.output, self.spacing() + "if (__mod_name__ == null) __mod_name__ = '%s';" % (mn)
        lhs = "%s.__name__" % raw_module_name
        self.add_lookup('variable', '__name__', lhs)
        print >>self.output, self.spacing() + "var __name__ = %s = __mod_name__;" % (lhs)
        if self.source_tracking:
            print >> self.output, self.spacing() + "%s.__track_lines__ = new Array();" % raw_module_name

        save_output = self.output
        self.output = StringIO()

        decl = mod_var_name_decl(raw_module_name)
        if decl:
            print >>self.output, self.spacing() + decl

        if self.attribute_checking and not raw_module_name in ['sys', 'pyjslib']:
            attribute_checking = True
            print >>self.output, self.indent() + 'try {'
        else:
            attribute_checking = False

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
                self._import(child, None, True, True)
            elif isinstance(child, ast.From):
                self._from(child, None, True, True)
            elif isinstance(child, ast.Discard):
                self._discard(child, None)
            elif isinstance(child, ast.Assign):
                self._assign(child, None, True)
            elif isinstance(child, ast.AugAssign):
                self._augassign(child, None, True)
            elif isinstance(child, ast.If):
                self._if(child, None, True)
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
            elif isinstance(child, ast.TryFinally):
                self._tryFinally(child, None, True)
            elif isinstance(child, ast.Raise):
                self._raise(child, None)
            elif isinstance(child, ast.Stmt):
                self._stmt(child, None, True)
            else:
                raise TranslationError(
                    "unsupported type (in __init__)",
                    child, self.module_name)

        captured_output = self.output.getvalue()
        self.output = save_output
        if self.source_tracking and self.store_source:
            for l in self.track_lines.keys():
                print >> self.output, self.spacing() + '''%s.__track_lines__[%d] = "%s";''' % (raw_module_name, l, self.track_lines[l].replace('"', '\"'))
        print >>self.output, captured_output,

        if attribute_checking:
            print >> self.output, self.spacing() + "} catch (pyjs_attr_err) {throw pyjslib._errorMapping(pyjs_attr_err)};"

        print >> self.output, self.spacing() + "return this;"
        print >> self.output, self.spacing() + "}; /* end %s */"  % module_name
        print >>self.output, self.spacing() + "$pyjs.modules_hash['"+module_name+"'] = $pyjs.loaded_modules['"+module_name+"'];"
        print >> self.output, "\n"
        print >>self.output, self.spacing(), "/* end module: %s */" % module_name
        print >> self.output, "\n"

        # print out the deps and check for wrong imports
        if self.imported_modules:
            print >> self.output, '/*'
            print >> self.output, 'PYJS_DEPS: %s' % self.imported_modules
            print >> self.output, '*/'

    def uniqid(self, prefix = ""):
        if not self.__unique_ids__.has_key(prefix):
            self.__unique_ids__[prefix] = 0
        self.__unique_ids__[prefix] += 1
        return "%s%06d" % (prefix, self.__unique_ids__[prefix])

    def spacing(self):
        return "\t" * self.indent_level

    def indent(self):
        spacing = self.spacing()
        self.indent_level += 1
        return spacing

    def dedent(self):
        if self.indent_level == 0:
            raise TranslationError("Dedent error", None, self.module_name)
        self.indent_level -= 1
        return self.spacing()

    def push_options(self):
        self.option_stack.append((\
            self.debug, self.print_statements, self.function_argument_checking,
            self.attribute_checking, self.bound_methods,
            self.source_tracking, self.line_tracking, self.store_source,
        ))
    def pop_options(self):
        (\
            self.debug, self.print_statements, self.function_argument_checking,
            self.attribute_checking, self.bound_methods,
            self.source_tracking, self.line_tracking, self.store_source,
        ) = self.option_stack.pop()

    def parse_decorators(self, node):
        staticmethod = False
        classmethod = False
        for d in node.decorators:
            if isinstance(d, ast.Getattr):
                if isinstance(d.expr, ast.Name):
                    if d.expr.name == 'compiler':
                        # Special case: compiler option
                        if self.decorator_compiler_options.has_key(d.attrname):
                            setattr(self, self.decorator_compiler_options[d.attrname][0], self.decorator_compiler_options[d.attrname][1])
                        else:
                            raise TranslationError(
                                "Unknown compiler option '%s'" % d.attrname, node, self.module_name)
                    else:
                        raise TranslationError(
                            "Unknown decorator '%s'" % d.attrname, node, self.module_name)
                else:
                    raise TranslationError(
                        "Unknown decorator '%s'" % d.attrname, node, self.module_name)
            elif isinstance(d, ast.Name):
                if d.name == 'staticmethod':
                    staticmethod = True
                elif d.name == 'classmethod':
                    classmethod = True
                else:
                    raise TranslationError(
                        "Unknown decorator '%s'" % d.name, node, self.module_name)
            else:
                raise TranslationError(
                    "Unknown decorator '%s'" % d, node, self.module_name)
        return (staticmethod, classmethod)

    def remap_regex(self, re_list, *words):
        dbg = 0
        if words[0] == 'name': dbg = 1
        if dbg: print 'remap_regex words:', words
        mapped = []
        single_word = False
        if len(words) == 1:
            if isinstance(words[0], list) or \
               isinstance(words[0], tuple):
                words = words[0]
            else:
                single_word = True
        for word in words:
            if dbg: print 'remap_regex word:', word
            for r in re_list:
                if dbg: print 'remap_regex r:', r
                if r.match(word):
                    word = word + '_'
                    break
            mapped.append(word)
        if dbg: print 'remap_regex mapped:', mapped
        if single_word:
            return mapped[0]
        return mapped

    def vars_remap(self, word):
        for r in pyjs_vars_remap:
            if r.match(word):
                return word + "_"
        return word

    def attrib_remap(self, word):
        for r in pyjs_attrib_remap:
            m = r.match(word)
            if m:
                m = m.groups()
                word = m[0] + m[2] + '_' + m[3]
        return word

    def push_lookup(self, scope = None):
        if not scope:
            scope = {}
        self.lookup_stack.append(scope)

    def pop_lookup(self):
        return self.lookup_stack.pop()

    def add_lookup(self, name_type, pyname, jsname, depth = -1):
        if name_type == 'variable':
            if jsname.find('.') >= 0:
                jsname = self.attrib_remap(jsname)
            else:
                jsname = self.vars_remap(jsname)
        else:
            jsname = self.attrib_remap(jsname)
        self.lookup_stack[depth][pyname] = (name_type, pyname, jsname)
        return jsname

    def lookup(self, name):
        # builtin
        # import
        # class
        # function
        # variable
        name_type = None
        pyname = name
        jsname = None
        max_depth = depth = len(self.lookup_stack) - 1
        while depth >= 0:
            if self.lookup_stack[depth].has_key(name):
                name_type, pyname, jsname = self.lookup_stack[depth][name]
                break
            depth -= 1
        return (name_type, pyname, jsname, depth, max_depth == depth and not name_type is None)

    def scopeName(self, name, depth, local):
        if local:
            return name
        while depth >= 0:
            scopeName = self.lookup_stack[depth].get(SCOPE_KEY, None)
            if scopeName is not None:
                return scopeName + name
            depth -= 1
        return self.modpfx() + name

    def local_js_vars_decl(self, ignore_py_vars):
        names = []
        for name in self.lookup_stack[-1].keys():
            nametype = self.lookup_stack[-1][name][0]
            pyname = self.lookup_stack[-1][name][1]
            jsname = self.lookup_stack[-1][name][2]
            if (     not jsname.find('.') >= 0
                 and not pyname in ignore_py_vars
                 and not nametype in ['__pyjamas__', '__javascript__']
               ):
                names.append(jsname)
        if len(names) > 0:
            return self.spacing() + "var %s;" % ','.join(names)
        return ''

    def add_imported_module(self, importName):
        names = importName.split(".")
        if not importName in self.imported_modules:
            self.imported_modules.append(importName)
        if importName.endswith('.js'):
            return
        # Add all parent modules
        _importName = ''
        for name in names:
            _importName += name
            if not _importName in self.imported_modules:
                self.imported_modules.append(_importName)
            _importName += '.'

    def md5(self, node):
        return hashlib.md5(self.raw_module_name + str(node.lineno) + repr(node)).hexdigest()

    def track_lineno(self, node, module=False):
        if self.source_tracking and node.lineno:
            if module:
                print >> self.output, self.spacing() + "$pyjs.track.module='%s';" % self.raw_module_name
            if self.line_tracking:
                print >> self.output, self.spacing() + "$pyjs.track.lineno=%d;" % node.lineno
                #print >> self.output, self.spacing() + "if ($pyjs.track.module!='%s') debugger;" % self.raw_module_name
            if self.store_source:
                self.track_lines[node.lineno] = self.get_line_trace(node)

    def track_call(self, call_code, lineno=None):
        if self.debug:
            dbg = self.uniqid("pyjs_dbg_")
            mod = self.raw_module_name
            call_code = """\
(function(){\
var %(dbg)s_retry = 0;
try{var %(dbg)s_res=%(call_code)s;}catch(%(dbg)s_err){
    if (%(dbg)s_err.__name__ != 'StopIteration') {
        var save_stack = $pyjs.__last_exception_stack__;
        sys.save_exception_stack();
        var pyjs_msg = "";

        try {
            pyjs_msg = "\\n" + sys.trackstackstr();
        } catch (s) {};
        $pyjs.__last_exception_stack__ = save_stack;
        if (pyjs_msg !== $pyjs.debug_msg) {
            alert("Module %(mod)s at line %(lineno)s :\\n" + %(dbg)s_err + pyjs_msg);
            $pyjs.debug_msg = pyjs_msg;
            debugger;
        }
    }
    switch (%(dbg)s_retry) {
        case 1:
            %(dbg)s_res=%(call_code)s;
            break;
        case 2:
            break;
        default:
            throw %(dbg)s_err;
    }
}return %(dbg)s_res})()""" % locals()
        return call_code

    def func_args(self, node, function_name, bind_type, args, stararg, dstararg):
        if bind_type == 'static':
            bind_type = 0
        elif bind_type == 'bound':
            bind_type = 1
        elif bind_type == 'class':
            bind_type = 2
        else:
            raise TranslationError("Unknown bind type: %s" % bind_type, node)
        args = repr(args)[1:]
        org_args = args
        if dstararg:
            args = "'%s',%s" % (dstararg, args)
        else:
            args = "null,%s" % args
        if stararg:
            args = "'%s',%s" % (stararg, args)
        else:
            args = "null,%s" % args
        args = '[' + args
        # remove any empty tail
        if args.endswith(',]'):
            args = args[:-2] + ']'
        if function_name is None:
            print >>self.output, "\t, %d, %s);" % (bind_type, args)
        else:
            print >>self.output, self.spacing() + "%s.__bind_type__ = %s;" % (function_name, bind_type)
            print >>self.output, self.spacing() + "%s.__args__ = %s;" % (function_name, args)

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

        print >> output, self.indent() + """\
if (this.__is_instance__ === true) {\
"""
        if arg_names:
            print >> output, self.spacing() + """\
var %s = this;\
""" % arg_names[0]

        if node.varargs:
            self._varargs_handler(node, varargname, maxargs1)

        if node.kwargs:
            print >> output, self.spacing() + """\
var %s = arguments.length >= %d ? arguments[arguments.length-1] : arguments[arguments.length];\
""" % (kwargname, maxargs1)
            s = self.spacing()
            print >> output, """\
%(s)sif (typeof %(kwargname)s != 'object' || %(kwargname)s.__is_instance__ !== true || %(kwargname)s.__name__ != 'Dict') {\
""" % locals()
            if node.varargs:
                print >> output, """\
%(s)s\tif (typeof %(kwargname)s != 'undefined') %(varargname)s.l.push(%(kwargname)s);\
""" % locals()
            print >> output, """\
%(s)s\t%(kwargname)s = arguments[arguments.length+1];
%(s)s}\
""" % locals()

        if self.function_argument_checking:
            print >> output, self.spacing() + """\
if ($pyjs.options.arg_count && %s) pyjs__exception_func_param(arguments.callee.__name__, %d, %s, arguments.length+1);\
""" % (argcount1, minargs2, maxargs2str)

        print >> output, self.dedent() + """\
} else {\
"""
        self.indent()

        if arg_names:
            print >> output, self.spacing() + """\
var %s = arguments[0];\
""" % arg_names[0]
        arg_idx = 0
        for arg_name in arg_names[1:]:
            arg_idx += 1
            print >> output, self.spacing() + """\
%s = arguments[%d];\
""" % (arg_name, arg_idx)

        if node.varargs:
            self._varargs_handler(node, varargname, maxargs2)

        if node.kwargs:
            print >> output, self.spacing() + """\
var %s = arguments.length >= %d ? arguments[arguments.length-1] : arguments[arguments.length];\
""" % (kwargname, maxargs2)
            s = self.spacing()
            print >> output, """\
%(s)sif (typeof %(kwargname)s != 'object' || %(kwargname)s.__is_instance__ !== true || %(kwargname)s.__name__ != 'Dict') {\
""" % locals()
            if node.varargs:
                print >> output, """\
%(s)s\tif (typeof %(kwargname)s != 'undefined') %(varargname)s.l.push(%(kwargname)s);\
""" % locals()
            print >> output, """\
%(s)s\t%(kwargname)s = arguments[arguments.length+1];
%(s)s}\
""" % locals()

        if self.function_argument_checking:
            print >> output, """\
%sif ($pyjs.options.arg_is_instance && self.__is_instance__ !== true) pyjs__exception_func_instance_expected(arguments.callee.__name__, arguments.callee.__class__.__name__, self);
%sif ($pyjs.options.arg_count && %s) pyjs__exception_func_param(arguments.callee.__name__, %d, %s, arguments.length);\
""" % (self.spacing(), self.spacing(), argcount2, minargs2, maxargs2str)

        print >> output, self.dedent() + "}"

        if arg_names and self.function_argument_checking:
            print >> output, """\
%(s)sif ($pyjs.options.arg_instance_type) {
%(s)s\tif (%(self)s.prototype.__md5__ !== '%(__md5__)s') {
%(s)s\t\tif (!pyjslib._isinstance(%(self)s, arguments.callee.__class__)) {
%(s)s\t\t\tpyjs__exception_func_instance_expected(arguments.callee.__name__, arguments.callee.__class__.__name__, %(self)s);
%(s)s\t\t}
%(s)s\t}
%(s)s}\
""" % {'s': self.spacing(), 'self': arg_names[0], '__md5__': current_klass.__md5__}

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
            print >> output, self.spacing() + """\
if ($pyjs.options.arg_count && %s) pyjs__exception_func_param(arguments.callee.__name__, %d, %s, arguments.length);\
""" % (argcount, minargs, maxargsstr)

        if node.varargs:
            self._varargs_handler(node, varargname, maxargs)

        if node.kwargs:
            print >> output, self.spacing() + """\
var %s = arguments.length >= %d ? arguments[arguments.length-1] : arguments[arguments.length];\
""" % (kwargname, maxargs)
            s = self.spacing()
            print >> output, """\
%(s)sif (typeof %(kwargname)s != 'object' || %(kwargname)s.__is_instance__ !== true || %(kwargname)s.__name__ != 'Dict') {\
""" % locals()
            if node.varargs:
                print >> output, """\
%(s)s\tif (typeof %(kwargname)s != 'undefined') %(varargname)s.l.push(%(kwargname)s);\
""" % locals()
            print >> output, """\
%(s)s\t%(kwargname)s = arguments[arguments.length+1];
%(s)s}\
""" % locals()


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
    if ($pyjs.options.arg_is_instance && this.__is_instance__ !== true && this.__is_instance__ !== false) pyjs__exception_func_class_expected(arguments.callee.__name__, arguments.callee.__class__.__name__);
    if ($pyjs.options.arg_count && %s) pyjs__exception_func_param(arguments.callee.__name__, %d, %s, arguments.length);\
""" % (argcount, minargs+1, maxargsstr)

        print >> output, """\
    var %s = this.prototype;\
""" % (arg_names[0],)

        if node.varargs:
            self._varargs_handler(node, varargname, maxargs)

        if node.kwargs:
            print >> output, """\
        var %s = arguments.length >= %d ? arguments[arguments.length-1] : arguments[arguments.length];\
""" % (kwargname, maxargs)
            s = self.spacing()
            print >> output, """\
%(s)sif (typeof %(kwargname)s != 'object' || %(kwargname)s.__is_instance__ !== true || %(kwargname)s.__name__ != 'Dict') {\
""" % locals()
            if node.varargs:
                print >> output, """\
%(s)s\tif (typeof %(kwargname)s != 'undefined') %(varargname)s.l.push(%(kwargname)s);\
""" % locals()
            print >> output, """\
%(s)s\t%(kwargname)s = arguments[arguments.length+1];
%(s)s}\
""" % locals()

    def _default_args_handler(self, node, arg_names, current_klass, kwargname,
                              output=None):
        output = output or self.output
        if node.kwargs and (len(arg_names) > 0):
            # This is necessary when **kwargs in function definition
            # and the call didn't pass the pyjs_kwargs_call().
            # See libtest testKwArgsInherit
            # This is not completely safe: if the last element in arguments 
            # is an dict and the corresponding argument shoud be a dict and 
            # the kwargs should be empty, the kwargs gets incorrectly the 
            # dict and the argument becomes undefined.
            # E.g.
            # def fn(a = {}, **kwargs): pass
            # fn({'a':1}) -> a gets undefined and kwargs gets {'a':1}
            revargs = arg_names[0:]
            revargs.reverse()
            print >> output, """\
%(s)sif (typeof %(k)s == 'undefined') {
%(s)s\t%(k)s = pyjslib.Dict({});\
""" % {'s': self.spacing(), 'k': kwargname}
            for v in revargs:
                print >> output, """\
%(s)s\tif (typeof %(v)s != 'undefined') {
%(s)s\t\tif (pyjslib.get_pyjs_classtype(%(v)s) == 'Dict') {
%(s)s\t\t\t%(k)s = %(v)s;
%(s)s\t\t\t%(v)s = arguments[%(a)d];
%(s)s\t\t}
%(s)s\t} else\
""" % {'s': self.spacing(), 'v': v, 'k': kwargname, 'a': len(arg_names)},
            print >> output, """\
{
%(s)s\t}
%(s)s}\
""" % {'s': self.spacing()}
        if len(node.defaults):
            default_pos = len(arg_names) - len(node.defaults)
            for default_node in node.defaults:
                default_value = self.expr(default_node, current_klass)
                default_name = arg_names[default_pos]
                default_pos += 1
                print >> output, self.spacing() + "if (typeof %s == 'undefined') %s=%s;" % (default_name, default_name, default_value)

    def _varargs_handler(self, node, varargname, start):
        if node.kwargs:
            end = "arguments.length-1"
            start -= 1
        else:
            end = "arguments.length"
        print >> self.output, """\
%(s)svar %(v)s = new Array();
%(s)sfor (var pyjs__va_arg = %(b)d; pyjs__va_arg < %(e)s; pyjs__va_arg++) {
%(s)s\tvar pyjs__arg = arguments[pyjs__va_arg];
%(s)s\t%(v)s.push(pyjs__arg);
%(s)s}
%(s)s%(v)s = pyjslib.Tuple(%(v)s);
\
""" % {'s': self.spacing(), 'v': varargname, 'b': start, 'e': end}

    def __varargs_handler(self, node, varargname, arg_names, current_klass, loop_var = None):
        print >>self.output, self.spacing() + "var", varargname, '= new pyjslib.Tuple();'
        print >>self.output, self.spacing() + "for(",
        if loop_var is None:
            loop_var = "pyjs__va_arg"
            print >>self.output, "var "+loop_var+"="+str(len(arg_names)),
        print >>self.output, """\
; %(loop_var)s < arguments.length; %(loop_var)s++) {
%(s)s\tvar pyjs__arg = arguments[%(loop_var)s];
%(s)s\t%(varargname)s.append(pyjs__arg);
%(s)s}\
""" % {'s': self.spacing(), 'varargname': varargname, 'loop_var': loop_var}

    def _kwargs_parser(self, node, function_name, arg_names, current_klass, method_ = False):
        default_pos = len(arg_names) - len(node.defaults)
        if not method_:
            print >>self.output, self.indent() + function_name+'.parse_kwargs = function (', ", ".join(["__kwargs"]+arg_names), ") {"
        else:
            print >>self.output, self.indent() + ", function (", ", ".join(["__kwargs"]+arg_names), ") {"
        print >>self.output, self.spacing() + "var __r = [];"
        print >>self.output, self.spacing() + "var pyjs__va_arg_start = %d;" % (len(arg_names)+1)

        if len(arg_names) > 0:
            print >>self.output, """\
%(s)sif (typeof %(arg_name)s != 'undefined' && this.__is_instance__ === false && %(arg_name)s.__is_instance__ === true) {
%(s)s\t__r.push(%(arg_name)s);
%(s)s\tpyjs__va_arg_start++;""" % {'s': self.spacing(), 'arg_name': arg_names[0]}
            idx = 1
            for arg_name in arg_names:
                idx += 1
                print >>self.output, """\
%(s)s\t%(arg_name)s = arguments[%(idx)d];\
""" % {'s': self.spacing(), 'arg_name': arg_name, 'idx': idx}
            print >>self.output, self.spacing() + "}"

        for arg_name in arg_names:
            if self.function_argument_checking:
                print >>self.output, """\
%(s)sif (typeof %(arg_name)s == 'undefined') {
%(s)s\t%(arg_name)s=__kwargs.%(arg_name)s;
%(s)s\tdelete __kwargs.%(arg_name)s;
%(s)s} else if ($pyjs.options.arg_kwarg_multiple_values && typeof __kwargs.%(arg_name)s != 'undefined') {
%(s)s\tpyjs__exception_func_multiple_values('%(function_name)s', '%(arg_name)s');
%(s)s}\
""" % {'s': self.spacing(), 'arg_name': arg_name, 'function_name': function_name}
            else:
                print >>self.output, self.indent() + "if (typeof %s == 'undefined') {"%(arg_name)
                print >>self.output, self.spacing() + "%s=__kwargs.%s;"% (arg_name, arg_name)
                print >>self.output, self.dedent() + "}"
            print >>self.output, self.spacing() + "__r.push(%s);" % arg_name

        if self.function_argument_checking and not node.kwargs:
            print >>self.output, """\
%(s)sif ($pyjs.options.arg_kwarg_unexpected_keyword) {
%(s)s\tfor (var i in __kwargs) {
%(s)s\t\tpyjs__exception_func_unexpected_keyword('%(function_name)s', i);
%(s)s\t}
%(s)s}\
""" % {'s': self.spacing(), 'function_name': function_name}

        # Always add all remaining arguments. Needed for argument checking _and_ if self != this;
        print >>self.output, """\
%(s)sfor (var pyjs__va_arg = pyjs__va_arg_start;pyjs__va_arg < arguments.length;pyjs__va_arg++) {
%(s)s\t__r.push(arguments[pyjs__va_arg]);
%(s)s}
""" % {'s': self.spacing()}
        if node.kwargs:
            print >>self.output, self.spacing() + "__r.push(pyjslib.Dict(__kwargs));"
        print >>self.output, self.spacing() + "return __r;"
        if not method_:
            print >>self.output, self.dedent() + "};"
        else:
            print >>self.output, self.dedent() + "});"


    def _import(self, node, current_klass, top_level = False, root_level = False):
        # XXX: hack for in-function checking, we should have another
        # object to check our scope
        self._doImport(node.names, current_klass, top_level, root_level, True)

    def _doImport(self, names, current_klass, top_level, root_level, assignBase):
        if root_level:
            modtype = 'root-module'
        else:
            modtype = 'module'
        for importName, importAs in names:
            if importName == '__pyjamas__':
                continue
            if importName.endswith(".js"):
                self.add_imported_module(importName)
                continue
            # "searchList" contains a list of possible module names :
            #   We create the list at compile time to save runtime.
            searchList = []
            context = self.raw_module_name
            if '.' in context:
                # our context lives in a package so it is possible to have a
                # relative import
                package = context.rsplit('.', 1)[0]
                relName = package + '.' + importName
                searchList.append(relName)
                if '.' in importName:
                    searchList.append(relName.rsplit('.', 1)[0])
            # the absolute path
            searchList.append(importName)
            if '.' in importName:
                searchList.append(importName.rsplit('.', 1)[0])

            mod = self.lookup(importName)
            package_mod = self.lookup(importName.split('.', 1)[0])
            if (   mod[0] != 'root-module'
                or (assignBase and not package_mod[0] in ['root-module', 'module'])
               ):
                # the import statement
                stmt = "pyjslib.__import__([%s], '%s', '%s');" % (
                            ', '.join(["'%s'"% n for n in searchList]),
                            importName,
                            self.raw_module_name,
                            )
                print >> self.output, self.spacing() + stmt
                self._lhsFromName(importName, top_level, current_klass, modtype)
                self.add_imported_module(importName)
            if assignBase:
                # get the name in scope
                package_name = importName.split('.')[0]
                if importAs:
                    ass_name = importAs
                else:
                    ass_name = package_name
                lhs = self._lhsFromName(ass_name, top_level, current_klass, modtype)
                if importAs:
                    mod_name = importName
                else:
                    mod_name = ass_name
                stmt = '%s = $pyjs.__modules__.%s;'% (lhs, mod_name)
                print >> self.output, self.spacing() + stmt

    def _from(self, node, current_klass, top_level = False, root_level = False):
        if node.modname == '__pyjamas__':
            # special module to help make pyjamas modules loadable in
            # the python interpreter
            for name in node.names:
                ass_name = name[1] or name[0]
                try:
                    jsname =  getattr(__pyjamas__, name[0])
                    if callable(jsname):
                        self.add_lookup("__pyjamas__", ass_name, name[0])
                    else:
                        self.add_lookup("__pyjamas__", ass_name, jsname)
                except AttributeError, e:
                    #raise TranslationError("Unknown __pyjamas__ import: %s" % name, node)
                    pass
            return
        if node.modname == '__javascript__':
            for name in node.names:
                ass_name = name[1] or name[0]
                self.add_lookup("__javascript__", ass_name, ass_name)
            return
        # XXX: hack for in-function checking, we should have another
        # object to check our scope
        for name in node.names:
            sub = node.modname + '.' + name[0]
            self._doImport(((sub, None),), current_klass, top_level, root_level, False)
            ass_name = name[1] or name[0]
            lhs = self._lhsFromName(ass_name, top_level, current_klass)
            rhs = '.'.join(('$pyjs', '__modules__', node.modname, name[0]))
            print >> self.output, self.spacing() + "%s = %s;" % (lhs, rhs)

    def _function(self, node, local=False):
        self.push_options()
        save_has_js_return = self.has_js_return
        self.has_js_return = False
        if node.decorators:
            self.parse_decorators(node)

        if local:
            function_name = node.name
        else:
            function_name = self.modpfx() + node.name
        function_name = self.add_lookup('function', node.name, function_name)
        self.push_lookup()

        arg_names = []
        for arg in node.argnames:
            arg_names.append(self.add_lookup('variable', arg, arg))
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
        if local:
            vdec = ''
        else:
            vdec = "var %s = " % node.name
            vdec = ""
        print >>self.output, self.indent() + "%s%s = function%s {" % (vdec, function_name, function_args)
        self._static_method_init(node, declared_arg_names, varargname, kwargname, None)
        self._default_args_handler(node, declared_arg_names, None, kwargname)

        local_arg_names = normal_arg_names + declared_arg_names

        if node.kwargs:
            local_arg_names.append(kwargname)
        if node.varargs:
            local_arg_names.append(varargname)

        save_output = self.output
        self.output = StringIO()
        if self.source_tracking:
            print >>self.output, self.spacing() + "$pyjs.track={module:'%s',lineno:%d};$pyjs.trackstack.push($pyjs.track);" % (self.raw_module_name, node.lineno)
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
        print >>self.output, self.local_js_vars_decl(local_arg_names)
        print >>self.output, captured_output,

        # we need to return null always, so it is not undefined
        if node.code.nodes:
            lastStmt = node.code.nodes[-1]
        else:
            lastStmt = None
        if not isinstance(lastStmt, ast.Return):
            if self.source_tracking:
                print >>self.output, self.spacing() + "$pyjs.trackstack.pop();$pyjs.track=$pyjs.trackstack.pop();$pyjs.trackstack.push($pyjs.track);"
            # FIXME: check why not on on self._isNativeFunc(lastStmt)
            if not self._isNativeFunc(lastStmt):
                print >>self.output, self.spacing() + "return null;"

        print >>self.output, self.dedent() + "};"
        print >>self.output, self.spacing() + "%s.__name__ = '%s';\n" % (function_name, node.name)

        self.func_args(node, function_name, 'static', declared_arg_names, varargname, kwargname)

        #self._kwargs_parser(node, function_name, normal_arg_names, None)
        self.has_js_return = save_has_js_return
        self.pop_options()
        self.pop_lookup()


    def _return(self, node, current_klass):
        expr = self.expr(node.value, current_klass)
        # in python a function call always returns None, so we do it
        # here too
        self.track_lineno(node)
        if self.source_tracking:
            print >>self.output, self.spacing() + "var pyjs__ret = " + expr + ";"
            print >>self.output, self.spacing() + "$pyjs.trackstack.pop();$pyjs.track=$pyjs.trackstack.pop();$pyjs.trackstack.push($pyjs.track);"
            print >>self.output, self.spacing() + "return pyjs__ret;"
        else:
            print >>self.output, self.spacing() + "return " + expr + ";"


    def _break(self, node, current_klass):
        print >>self.output, self.spacing() + "break;"


    def _continue(self, node, current_klass):
        print >>self.output, self.spacing() + "continue;"


    def _callfunc(self, v, current_klass):

        if isinstance(v.node, ast.Name):
            name_type, pyname, jsname, depth, is_local = self.lookup(v.node.name)
            if name_type == '__pyjamas__':
                try:
                    raw_js = getattr(__pyjamas__, v.node.name)
                    if callable(raw_js):
                        raw_js, has_js_return = raw_js(v)
                        if has_js_return:
                            self.has_js_return = True
                    return raw_js
                except AttributeError, e:
                    raise TranslationError(
                        "Unknown __pyjamas__ function %s" % pyname,
                         v.node, self.module_name)
            else:
                if name_type is None:
                    # What to do with a (yet) unknown name?
                    # Just nothing...
                    call_name = self.scopeName(v.node.name, depth, is_local)
                else:
                    call_name = jsname
            call_args = []
        elif isinstance(v.node, ast.Getattr):
            if isinstance(v.node.expr, ast.Name):
                attrname = self.attrib_remap(v.node.attrname)
                call_name = self._name2(v.node.expr, current_klass, attrname)
                call_args = []
            elif isinstance(v.node.expr, ast.Getattr):
                call_name = self._getattr2(v.node.expr, current_klass, v.node.attrname)
                call_name = self.attrib_remap(call_name)
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
            elif isinstance(v.node.expr, ast.Slice):
                call_name = self._slice(v.node.expr, current_klass) + "." + v.node.attrname
                call_args = []
            else:
                raise TranslationError(
                    "unsupported type (in _callfunc)", v.node.expr, self.module_name)
        elif isinstance(v.node, ast.CallFunc):
            call_name = self._callfunc(v.node, current_klass)
            call_args = []
        elif isinstance(v.node, ast.Subscript):
            call_name = self._subscript(v.node, current_klass)
            call_args = []
        else:
            raise TranslationError(
                "unsupported type (in _callfunc)", v.node, self.module_name)

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
            if call_name[-1] == ')':
                # Function call, or an entity (...)
                call_this = None
            else:
                try:
                    call_this, method_name = call_name.rsplit(".", 1)
                except ValueError:
                    # Must be a function call ...
                    call_this = None
            if call_this is None:
                call_code = ("pyjs_kwargs_call(null, "+call_name+", "
                                  + star_arg_name 
                                  + ", " + dstar_arg_name
                                  + ", ["+fn_args+"]"
                                  + ")")
            else:
                call_code = ("pyjs_kwargs_call("+call_this+", '"+method_name+"', "
                                  + star_arg_name 
                                  + ", " + dstar_arg_name
                                  + ", ["+fn_args+"]"
                                  + ")")
        else:
            call_code = call_name + "(" + ", ".join(call_args) + ")"
        return self.track_call(call_code, v.lineno)

    def _print(self, node, current_klass):
        if not self.print_statements:
            return
        call_args = []
        for ch4 in node.nodes:
            arg = self.expr(ch4, current_klass)
            call_args.append(arg)
        print >>self.output, self.spacing() + self.track_call("pyjslib.printFunc([%s], %d)" % (', '.join(call_args), int(isinstance(node, ast.Printnl))), node.lineno) + ';'

    def _tryFinally(self, node, current_klass, top_level=False):
        body = node.body
        if not isinstance(node.body, ast.TryExcept):
            body = node
        node.body.final = node.final
        self._tryExcept(body, current_klass, top_level=top_level)

    def _tryExcept(self, node, current_klass, top_level=False):

        self.stacksize_depth += 1
        pyjs_try_err = 'pyjs_try_err'
        if self.source_tracking:
            print >>self.output, self.spacing() + "var pyjs__trackstack_size_%d = $pyjs.trackstack.length;" % self.stacksize_depth
        print >>self.output, self.indent() + "try {"

        for stmt in node.body.nodes:
            self._stmt(stmt, current_klass)
        if hasattr(node, 'else_') and node.else_:
            print >> self.output, self.spacing() + "throw pyjslib.TryElse;"
        print >> self.output, self.dedent() + "} catch(%s) {" % pyjs_try_err
        self.indent()

        if hasattr(node, 'else_') and node.else_:
            print >> self.output, self.indent() + """\
if (%(e)s.__name__ == 'TryElse') {""" % {'e': pyjs_try_err}

            for stmt in node.else_:
                self._stmt(stmt, current_klass)

            print >> self.output, self.dedent() + """} else {"""
            self.indent()
        if self.attribute_checking:
            print >> self.output, self.spacing() + """pyjs_try_err = pyjslib._errorMapping(pyjs_try_err);"""
        print >> self.output, self.spacing() + """\
var %(e)s_name = (typeof %(e)s.__name__ == 'undefined' ? %(e)s.name : %(e)s.__name__ );\
""" % {'e': pyjs_try_err}
        print >> self.output, self.spacing() + "$pyjs.__last_exception__ = {error: %s, module: %s, try_lineno: %s};" % (pyjs_try_err, self.raw_module_name, node.lineno)
        if self.source_tracking:
            print >>self.output, """\
%(s)ssys.save_exception_stack();
%(s)sif ($pyjs.trackstack.length > pyjs__trackstack_size_%(d)d) {
%(s)s\t$pyjs.trackstack = $pyjs.trackstack.slice(0,pyjs__trackstack_size_%(d)d);
%(s)s\t$pyjs.track = $pyjs.trackstack.slice(-1)[0];
%(s)s}
%(s)s$pyjs.track.module='%(m)s';""" % {'s': self.spacing(), 'd': self.stacksize_depth, 'm': self.raw_module_name}

        pyjs_try_err = self.add_lookup('variable', pyjs_try_err, pyjs_try_err)
        if hasattr(node, 'handlers'):
            else_str = self.spacing()
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
                            l.append("(%s_name == %s.__name__)" % (pyjs_try_err, self.expr(x, current_klass)))
                    else:
                        l = [ "%s_name == %s.__name__" % (pyjs_try_err, self.expr(expr, current_klass)) ]
                    print >> self.output, "%sif (%s) {" % (else_str, "||".join(l))
                self.indent()
                print >> self.output, self.spacing() + "$pyjs.__last_exception__.except_lineno = %d;" % lineno
                tnode = ast.Assign([ast.AssName(errName, "OP_ASSIGN", lineno)], ast.Name(pyjs_try_err, lineno), lineno)
                self._assign(tnode, current_klass, top_level)
                for stmt in handler[2]:
                    self._stmt(stmt, current_klass)
                print >> self.output, self.dedent() + "}",
                else_str = "else "

            if node.handlers[-1][0]:
                # No default catcher, create one to fall through
                print >> self.output, "%s{ throw %s; }" % (else_str, pyjs_try_err)
        if hasattr(node, 'else_') and node.else_:
            print >> self.output, self.dedent() + "}",

        if hasattr(node, 'final'):
            print >>self.output, self.dedent() + "} finally {"
            self.indent()
            for stmt in node.final:
                self._stmt(stmt, current_klass)
        print >>self.output, self.dedent()  + "}"
        self.stacksize_depth -= 1

    # XXX: change use_getattr to True to enable "strict" compilation
    # but incurring a 100% performance penalty. oops.
    def _getattr(self, v, current_klass, use_getattr=False):
        attr_name = self.attrib_remap(v.attrname)
        if isinstance(v.expr, ast.Name):
            obj = self._name(v.expr, current_klass, return_none_for_module=True)
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
            raise TranslationError(
                "unsupported type (in _getattr)", v.expr, self.module_name)


    def modpfx(self):
        return strip_py(self.module_prefix)

    def _name(self, v, current_klass, top_level=False,
              return_none_for_module=False):

        if not hasattr(v, 'name'):
            name = v.attrname
        else:
            name = v.name

        name_type, pyname, jsname, depth, is_local = self.lookup(name)
        if name_type is None:
            # What to do with a (yet) unknown name?
            # Just nothing...
            return self.scopeName(name, depth, is_local)
        return jsname

    def _name2(self, v, current_klass, attr_name):
        name_type, pyname, jsname, depth, is_local = self.lookup(v.name)
        if name_type is None:
            jsname = self.scopeName(v.name, depth, is_local)
        return jsname + "." + attr_name

    def _getattr2(self, v, current_klass, attr_name):
        if isinstance(v.expr, ast.Getattr):
            return self._getattr2(v.expr, current_klass, v.attrname + "." + attr_name)
        if isinstance(v.expr, ast.Name):
            name_type, pyname, jsname, depth, is_local = self.lookup(v.expr.name)
            if name_type is None:
                jsname = self.scopeName(v.expr.name, depth, is_local)
            return jsname + '.' +v.attrname+"."+attr_name
        return self.expr(v.expr, current_klass) + "." + v.attrname + "." + attr_name

    def _class(self, node):
        class_name = self.modpfx() + uuprefix(node.name, 1)
        current_klass = Klass(class_name, class_name)
        current_klass.__md5__ = self.md5(node)
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
                    base_class = self._name(node_base, None)
                elif isinstance(node_base, ast.Getattr):
                    # the bases are not in scope of the class so do not
                    # pass our class to self._name
                    node_base_name = node_base.attrname
                    base_class = self.expr(node_base, None)
                else:
                    raise TranslationError(
                        "unsupported type (in _class)",
                        node_base, self.module_name)
                base_classes.append((node_base_name, base_class))
            current_klass.set_base(base_classes[0][1])

        if node.name in ['object', 'pyjslib.Object', 'pyjslib.object']:
            base_classes = []
        local_prefix = 'cls_definition'
        self.local_prefix = None
        class_name = self.add_lookup('class', node.name, class_name)
        print >>self.output, self.indent() + class_name + """ = (function(){
%(s)svar cls_instance = pyjs__class_instance('%(n)s');
%(s)svar %(p)s = new Object();
%(s)s%(p)s.__md5__ = '%(m)s';""" % {'s': self.spacing(), 'n': node.name, 'p': local_prefix, 'm': current_klass.__md5__}

        private_scope = {}
        for child in node.code:
            if isinstance(child, ast.Pass):
                pass
            elif isinstance(child, ast.Function):
                self.local_prefix = None
                self._method(child, current_klass, class_name, class_name, local_prefix)
            elif isinstance(child, ast.Assign):
                self.local_prefix = local_prefix
                self.push_lookup(private_scope)
                self.track_lineno(child, True)
                lhs = "%s.%s" % (local_prefix, child.nodes[0].name)
                lhs = self.add_lookup('attribute', child.nodes[0].name, lhs)
                print >>self.output, self.spacing() + "%s = %s;" % (lhs, self.expr(child.expr, current_klass))
                private_scope = self.pop_lookup()
            elif isinstance(child, ast.Discard) and isinstance(child.expr, ast.Const):
                # Probably a docstring, turf it
                pass
            else:
                raise TranslationError(
                    "unsupported type (in _class)", child, self.module_name)
        print >>self.output, """\
%(s)sreturn pyjs__class_function(cls_instance, cls_definition, 
%(s)s                            new Array(""" % {'s': self.spacing()}  + ",".join(map(lambda x: x[1], base_classes)) + """));
%s})();""" % self.dedent()

    def classattr(self, node, current_klass):
        self._assign(node, current_klass, True)

    def _raise(self, node, current_klass):
        if node.expr3:
            raise TranslationError("More than two expressions unsupported",
                                   node, self.module_name)
        if node.expr1:
            if node.expr2:
                print >> self.output, """
%(s)svar pyjs__raise_expr1 = %(expr1)s;
%(s)svar pyjs__raise_expr2 = %(expr2)s;
%(s)sif (pyjs__raise_expr2 !== null && pyjs__raise_expr1.__is_instance__ === true) {
%(s)s\tthrow (pyjslib.TypeError('instance exception may not have a separate value'))
%(s)s}
%(s)sif (pyjslib.isinstance(pyjs__raise_expr2, pyjslib.Tuple)) {
%(s)s\tthrow (pyjs__raise_expr1.apply(pyjs__raise_expr1, pyjs__raise_expr2.getArray()));
%(s)s} else {
%(s)s\tthrow (pyjs__raise_expr1(pyjs__raise_expr2));
%(s)s}
""" % { 's': self.spacing(),
        'expr1': self.expr(node.expr1, current_klass),
        'expr2': self.expr(node.expr2, current_klass),
      }
            else:
                print >> self.output, self.spacing() + "throw (%s);" % self.expr(
                    node.expr1, current_klass)
        else:
            print >> self.output, self.spacing() + "throw ($pyjs.__last_exception__?$pyjs.__last_exception__.error:pyjslib.TypeError('exceptions must be classes, instances, or strings (deprecated), not NoneType'));"

    def _method(self, node, current_klass, class_name, class_name_, local_prefix):
        self.push_options()
        save_has_js_return = self.has_js_return
        self.has_js_return = False
        if node.decorators:
            staticmethod, classmethod = self.parse_decorators(node)
        else:
            staticmethod = classmethod = False

        if node.name == '__new__':
            staticmethod = True

        self.push_lookup()
        arg_names = []
        for arg in node.argnames:
            arg_names.append(self.add_lookup('variable', arg, arg))

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

        method_name = self.attrib_remap(node.name)
        print >>self.output, self.indent() + local_prefix + '.' + method_name + " = pyjs__bind_method(cls_instance, '"+method_name+"', function" + function_args + " {"
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

        save_output = self.output
        self.output = StringIO()
        if self.source_tracking:
            print >>self.output, self.spacing() + "$pyjs.track={module:%s, lineno:%d};$pyjs.trackstack.push($pyjs.track);" % (self.raw_module_name, node.lineno)
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
        print >>self.output, self.local_js_vars_decl(local_arg_names)
        print >>self.output, captured_output,


        # we need to return null always, so it is not undefined
        if node.code.nodes:
            lastStmt = node.code.nodes[-1]
        else:
            lastStmt = None
        if not isinstance(lastStmt, ast.Return):
            if self.source_tracking:
                print >>self.output, self.spacing() + "$pyjs.trackstack.pop();$pyjs.track=$pyjs.trackstack.pop();$pyjs.trackstack.push($pyjs.track);"
            if not self._isNativeFunc(lastStmt):
                print >>self.output, self.spacing() + "return null;"

        print >>self.output, self.dedent() + "}"

        bind_type = 'bound'
        if staticmethod:
            bind_type = 'static'
        elif classmethod:
            bind_type = 'class'
        self.func_args(node, None, bind_type, declared_arg_names, varargname, kwargname)

        #if staticmethod:
        #    self._kwargs_parser(node, method_name, normal_arg_names, current_klass, True)
        #else:
        #    self._kwargs_parser(node, method_name, normal_arg_names[1:], current_klass, True)

        self.has_js_return = save_has_js_return
        self.pop_options()
        self.pop_lookup()

    def _isNativeFunc(self, node):
        if isinstance(node, ast.Discard):
            if isinstance(node.expr, ast.CallFunc):
                if isinstance(node.expr.node, ast.Name):
                    name_type, pyname, jsname, depth, is_local = self.lookup(node.expr.node.name)
                    if name_type == '__pyjamas__' and jsname == NATIVE_JS_FUNC_NAME:
                        return True
        return False

    def _stmt(self, node, current_klass, top_level = False):
        self.track_lineno(node)

        if isinstance(node, ast.Return):
            self._return(node, current_klass)
        elif isinstance(node, ast.Break):
            self._break(node, current_klass)
        elif isinstance(node, ast.Continue):
            self._continue(node, current_klass)
        elif isinstance(node, ast.Assign):
            self._assign(node, current_klass, top_level)
        elif isinstance(node, ast.AugAssign):
            self._augassign(node, current_klass, top_level)
        elif isinstance(node, ast.Discard):
            self._discard(node, current_klass)
        elif isinstance(node, ast.If):
            self._if(node, current_klass, top_level)
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
            self._tryExcept(node, current_klass, top_level)
        elif isinstance(node, ast.TryFinally):
            self._tryFinally(node, current_klass, top_level)
        elif isinstance(node, ast.Raise):
            self._raise(node, current_klass)
        elif isinstance(node, ast.Import):
            self._import(node, current_klass, top_level)
        elif isinstance(node, ast.From):
            self._from(node, current_klass, top_level)
        else:
            raise TranslationError(
                "unsupported type (in _stmt)", node, self.module_name)


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

    def _augassign(self, node, current_klass, top_level = False):
        def astOP(op):
            if op == "+=":
                return ast.Add
            elif op == "-=":
                return ast.Sub
            elif op == "*=":
                return ast.Mul
            elif op == "/=":
                return ast.Div
            elif op == "%=":
                return ast.Mod
            else:
                raise TranslationError(
                 "unsupported OP (in _augassign)", node, self.module_name)
        v = node.node
        if isinstance(v, ast.Getattr):
            # XXX HACK!  don't allow += on return result of getattr.
            # TODO: create a temporary variable or something.
            lhs = self._getattr(v, current_klass, False)
        elif isinstance(v, ast.Name):
            lhs = self._name(node.node, current_klass)
        elif isinstance(v, ast.Subscript):
            if len(v.subs) != 1:
                raise TranslationError(
                    "must have one sub (in _assign)", v, self.module_name)
            lhs = ast.Subscript(v.expr, "OP_ASSIGN", v.subs)
            expr = v.expr
            subs = v.subs
            if not (isinstance(v.subs[0], ast.Const) or \
                    isinstance(v.subs[0], ast.Name)) or \
               not isinstance(v.expr, ast.Name):
                # There's something complex here.
                # Neither a simple x[0] += ?
                # Nore a simple x[y] += ?
                augexpr = self.uniqid('augexpr')
                augsub = self.uniqid('augsub')
                print >>self.output, self.spacing() + "var " + augsub + " = " + self.expr(subs[0], current_klass) + ";"
                self.add_lookup('variable', augexpr, augexpr)
                print >>self.output, self.spacing() + "var " + augexpr + " = " + self.expr(expr, current_klass) + ";"
                self.add_lookup('variable', augsub, augsub)
                lhs = ast.Subscript(ast.Name(augexpr), "OP_ASSIGN", [ast.Name(augsub)])
                v = ast.Subscript(ast.Name(augexpr), v.flags, [ast.Name(augsub)])
            op = astOP(node.op)
            tnode = ast.Assign([lhs], op((v, node.expr)))
            return self._assign(tnode, current_klass, top_level)
        else:
            raise TranslationError(
                "unsupported type (in _augassign)", v, self.module_name)
        op = node.op
        rhs = self.expr(node.expr, current_klass)
        print >>self.output, self.spacing() + lhs + " " + op + " " + rhs + ";"


    def _lhsFromName(self, name, top_level, current_klass, set_name_type = 'variable'):
        name_type, pyname, jsname, depth, is_local = self.lookup(name)
        if is_local:
            lhs = jsname
            self.add_lookup(set_name_type, name, jsname)
        elif top_level:
            if current_klass:
                #lhs = "var " + name + " = " + current_klass.name_ + "." + name
                lhs = current_klass.name_ + "." + name
            else:
                vname = self.modpfx() + name
                vname = self.add_lookup(set_name_type, name, vname)
                #lhs = "var " + name + " = " + vname
                lhs = vname
        else:
            vname = self.add_lookup(set_name_type, name, name)
            lhs = "var " + vname
            lhs = vname
        return lhs

    def _assign(self, node, current_klass, top_level = False):
        if len(node.nodes) != 1:
            tempvar = '__temp'+str(node.lineno)
            tnode = ast.Assign([ast.AssName(tempvar, "OP_ASSIGN", node.lineno)], node.expr, node.lineno)
            self._assign(tnode, current_klass, top_level)
            for v in node.nodes:
               tnode2 = ast.Assign([v], ast.Name(tempvar, node.lineno), node.lineno)
               self._assign(tnode2, current_klass, top_level)
            return

        def _lhsFromAttr(v, current_klass):
            attr_name = self.attrib_remap(v.attrname)
            if isinstance(v.expr, ast.Name):
                obj = v.expr.name
                lhs = self._name(v.expr, current_klass) + "." + attr_name
            elif isinstance(v.expr, ast.Getattr):
                lhs = self._getattr(v, current_klass)
            elif isinstance(v.expr, ast.Subscript):
                lhs = self._subscript(v.expr, current_klass) + "." + attr_name
            else:
                raise TranslationError(
                    "unsupported type (in _assign)", v.expr, self.module_name)
            return lhs

        dbg = 0
        v = node.nodes[0]
        if isinstance(v, ast.AssAttr):
            rhs = self.expr(node.expr, current_klass)
            lhs = _lhsFromAttr(v, current_klass)
            if v.flags == "OP_ASSIGN":
                op = "="
            else:
                raise TranslationError(
                    "unsupported flag (in _assign)", v, self.module_name)

        elif isinstance(v, ast.AssName):
            rhs = self.expr(node.expr, current_klass)
            lhs = self._lhsFromName(v.name, top_level, current_klass)
            if v.flags == "OP_ASSIGN":
                op = "="
            else:
                raise TranslationError(
                    "unsupported flag (in _assign)", v, self.module_name)
        elif isinstance(v, ast.Subscript):
            if v.flags == "OP_ASSIGN":
                obj = self.expr(v.expr, current_klass)
                if len(v.subs) != 1:
                    raise TranslationError(
                        "must have one sub (in _assign)", v, self.module_name)
                idx = self.expr(v.subs[0], current_klass)
                value = self.expr(node.expr, current_klass)
                print >>self.output, self.spacing() + self.track_call(obj + ".__setitem__(" + idx + ", " + value + ")", v.lineno) + ';'
                return
            else:
                raise TranslationError(
                    "unsupported flag (in _assign)", v, self.module_name)
        elif isinstance(v, (ast.AssList, ast.AssTuple)):
            tempName = self.uniqid("__tupleassign__")
            print >>self.output, self.spacing() + "var " + tempName + " = " + \
                                 self.expr(node.expr, current_klass) + ";"
            for index,child in enumerate(v.getChildNodes()):
                rhs = self.track_call(tempName + ".__getitem__(" + str(index) + ")", v.lineno)

                if isinstance(child, ast.AssAttr):
                    lhs = _lhsFromAttr(child, current_klass)
                elif isinstance(child, ast.AssName):
                    lhs = self._lhsFromName(child.name, top_level, current_klass)
                elif isinstance(child, ast.Subscript):
                    if child.flags == "OP_ASSIGN":
                        obj = self.expr(child.expr, current_klass)
                        if len(child.subs) != 1:
                            raise TranslationError("must have one sub " +
                                                   "(in _assign)",
                                                   child,
                                                   self.module_name)
                        idx = self.expr(child.subs[0], current_klass)
                        value = self.expr(node.expr, current_klass)
                        print >>self.output, self.spacing() + self.track_call(obj + ".__setitem__(" \
                                           + idx + ", " + rhs + ")", v.lineno) + ';'
                        continue
                print >>self.output, self.spacing() + lhs + " = " + rhs + ";"
            return
        else:
            raise TranslationError(
                "unsupported type (in _assign)", v, self.module_name)

        if dbg:
            print "b", repr(node.expr), rhs
        print >>self.output, self.spacing() + lhs + " " + op + " " + rhs + ";"


    def _discard(self, node, current_klass):
        
        if isinstance(node.expr, ast.CallFunc):
            expr = self._callfunc(node.expr, current_klass)
            if isinstance(node.expr.node, ast.Name):
                name_type, pyname, jsname, depth, is_local = self.lookup(node.expr.node.name)
                if name_type == '__pyjamas__' and jsname == NATIVE_JS_FUNC_NAME:
                    print >>self.output, expr
                    return
            print >>self.output, self.spacing() + expr + ";"

        elif isinstance(node.expr, ast.Const):
            # we can safely remove all constants that are discarded,
            # e.g None fo empty expressions after a unneeded ";" or
            # mostly important to remove doc strings
            return
        else:
            raise TranslationError(
                "unsupported type, must be call or const (in _discard)", node.expr,  self.module_name)


    def _if(self, node, current_klass, top_level = False):
        for i in range(len(node.tests)):
            test, consequence = node.tests[i]
            if i == 0:
                keyword = "if"
            else:
                keyword = "else if"

            self.lookup_stack[-1]
            self._if_test(keyword, test, consequence, current_klass, top_level)

        if node.else_:
            keyword = "else"
            test = None
            consequence = node.else_

            self._if_test(keyword, test, consequence, current_klass)


    def _if_test(self, keyword, test, consequence, current_klass, top_level = False):
        if test:
            expr = self.expr(test, current_klass)

            print >>self.output, self.indent() +keyword + " (" + self.track_call("pyjslib.bool(" + expr + ")", test.lineno)+") {"
        else:
            print >>self.output, self.indent() + keyword + " {"

        if isinstance(consequence, ast.Stmt):
            for child in consequence.nodes:
                self._stmt(child, current_klass, top_level)
        else:
            raise TranslationError(
                "unsupported type (in _if_test)", consequence,  self.module_name)

        print >>self.output, self.dedent() + "}"

    def _compare(self, node, current_klass):
        lhs = self.expr(node.expr, current_klass)

        if len(node.ops) != 1:
            raise TranslationError(
                "only one ops supported (in _compare)", node,  self.module_name)

        op = node.ops[0][0]
        rhs_node = node.ops[0][1]
        rhs = self.expr(rhs_node, current_klass)

        if op == "==":
            return self.track_call("pyjslib.eq(%s, %s)" % (lhs, rhs), node.lineno)
        if op == "!=":
            return self.track_call("!pyjslib.eq(%s, %s)" % (lhs, rhs), node.lineno)
        if op == "<":
            return self.track_call("(pyjslib.cmp(%s, %s) == -1)" % (lhs, rhs), node.lineno)
        if op == "<=":
            return self.track_call("(pyjslib.cmp(%s, %s) != 1)" % (lhs, rhs), node.lineno)
        if op == ">":
            return self.track_call("(pyjslib.cmp(%s, %s) == 1)" % (lhs, rhs), node.lineno)
        if op == ">=":
            return self.track_call("(pyjslib.cmp(%s, %s) != -1)" % (lhs, rhs), node.lineno)
        if op == "in":
            return self.track_call(rhs + ".__contains__(" + lhs + ")", node.lineno)
        elif op == "not in":
            return "!" + self.track_call(rhs + ".__contains__(" + lhs + ")", node.lineno)
        if op == "is":
            op = "==="
        if op == "is not":
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
            assign_name = self.add_lookup('variable', node.assign.name, node.assign.name)
            if node.assign.flags == "OP_ASSIGN":
                op = "="
        elif isinstance(node.assign, ast.AssTuple):
            op = "="
            i = 0
            for child in node.assign:
                child_name = child.name
                if assign_name == "":
                    assign_name = "temp_" + child_name
                self.add_lookup('variable', child_name, child_name)
                s = self.spacing()
                assign_tuple += """%(s)svar %(child_name)s %(op)s """ % locals()
                assign_tuple += self.track_call("%(assign_name)s.__getitem__(%(i)i)" % locals(), node.lineno) + ';'
                i += 1
        else:
            raise TranslationError(
                "unsupported type (in _for)", node.assign, self.module_name)

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
            raise TranslationError(
                "unsupported type (in _for)", node.list, self.module_name)

        assign_name = self.add_lookup('variable', assign_name, assign_name)
        lhs = "var " + assign_name
        iterator_name = "__" + assign_name

        if self.source_tracking:
            self.stacksize_depth += 1
            print >>self.output, self.spacing() + "var pyjs__trackstack_size_%d=$pyjs.trackstack.length;" % self.stacksize_depth
        s = self.spacing()
        print >>self.output, """\
%(s)svar %(iterator_name)s = """ % locals() + self.track_call("%(list_expr)s.__iter__()" % locals(), node.lineno) + ';'
        print >>self.output, self.indent() + """try {"""
        print >>self.output, self.indent() + """while (true) {"""
        print >>self.output, self.spacing() + """%(lhs)s %(op)s""" % locals(),
        print >>self.output, self.track_call("%(iterator_name)s.next()"% locals(), node.lineno) + ";"
        print >>self.output, self.spacing() + """%(assign_tuple)s""" % locals()
        for node in node.body.nodes:
            self._stmt(node, current_klass)
        print >>self.output, self.dedent() + "}"
        print >>self.output, self.dedent() + "} catch (e) {"
        self.indent()
        print >>self.output, self.indent() + "if (e.__name__ != 'StopIteration') {"
        print >>self.output, self.spacing() + "throw e;"
        print >>self.output, self.dedent() + "}"
        print >>self.output, self.dedent() + "}"
        if self.source_tracking:
            print >>self.output, """\
%(s)sif ($pyjs.trackstack.length > pyjs__trackstack_size_%(d)d) {
%(s)s\t$pyjs.trackstack = $pyjs.trackstack.slice(0,pyjs__trackstack_size_%(d)d);
%(s)s\t$pyjs.track = $pyjs.trackstack.slice(-1)[0];
%(s)s}
%(s)s$pyjs.track.module='%(m)s';""" % {'s': self.spacing(), 'd': self.stacksize_depth, 'm': self.raw_module_name}
            self.stacksize_depth -= 1

    def _while(self, node, current_klass):
        test = self.expr(node.test, current_klass)
        print >>self.output, "    while (" + self.track_call("pyjslib.bool(" + test + ")", node.lineno) + ") {"
        if isinstance(node.body, ast.Stmt):
            for child in node.body.nodes:
                self._stmt(child, current_klass)
        else:
            raise TranslationError(
                "unsupported type (in _while)", node.body, self.module_name)
        print >>self.output, "    }"


    def _const(self, node):
        if isinstance(node.value, int):
            return str(node.value)
        elif isinstance(node.value, long):
            v = str(node.value)
            if v[-1] == 'L':
                v = v[:-1]
            return v
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
            raise TranslationError(
                "unsupported type (in _const)", node, self.module_name)

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
           return self.track_call("pyjslib.sprintf("+self.expr(node.left, current_klass) + ", " + self.expr(node.right, current_klass)+")", node.lineno)
        return self.expr(node.left, current_klass) + " % " + self.expr(node.right, current_klass)

    def _power(self, node, current_klass):
        return "Math.pow("+self.expr(node.left, current_klass) + "," + self.expr(node.right, current_klass) + ")"

    def _invert(self, node, current_klass):
        return "(" + "~" + self.expr(node.expr, current_klass) + ")"

    def _bitand(self, node, current_klass):
        return "(" + " & ".join([self.expr(child, current_klass) for child in node.nodes]) + ")"

    def _bitshiftleft(self, node, current_klass):
        return "(" + self.expr(node.left, current_klass) + " << " + self.expr(node.right, current_klass) + ")"

    def _bitshiftright(self, node, current_klass):
        return "(" + self.expr(node.left, current_klass) + " >>> " + self.expr(node.right, current_klass) + ")"

    def _bitxor(self,node, current_klass):
        return "(" + " ^ ".join([self.expr(child, current_klass) for child in node.nodes]) + ")"

    def _bitor(self, node, current_klass):
        return "(" + " | ".join([self.expr(child, current_klass) for child in node.nodes]) + ")"

    def _subscript(self, node, current_klass):
        if node.flags == "OP_APPLY":
            if len(node.subs) == 1:
                return self.track_call(self.expr(node.expr, current_klass) + ".__getitem__(" + self.expr(node.subs[0], current_klass) + ")", node.lineno)
            else:
                raise TranslationError(
                    "must have one sub (in _subscript)", node, self.module_name)
        else:
            raise TranslationError(
                "unsupported flag (in _subscript)", node, self.module_name)

    def _subscript_stmt(self, node, current_klass):
        if node.flags == "OP_DELETE":
            print >>self.output, "    " + self.track_call(self.expr(node.expr, current_klass) + ".__delitem__(" + self.expr(node.subs[0], current_klass) + ")", node.lineno) + ';'
        else:
            raise TranslationError(
                "unsupported flag (in _subscript)", node, self.module_name)

    def _list(self, node, current_klass):
        return self.track_call("new pyjslib.List([" + ", ".join([self.expr(x, current_klass) for x in node.nodes]) + "])", node.lineno)

    def _dict(self, node, current_klass):
        items = []
        for x in node.items:
            key = self.expr(x[0], current_klass)
            value = self.expr(x[1], current_klass)
            items.append("[" + key + ", " + value + "]")
        return self.track_call("new pyjslib.Dict([" + ", ".join(items) + "])")

    def _tuple(self, node, current_klass):
        return self.track_call("new pyjslib.Tuple([" + ", ".join([self.expr(x, current_klass) for x in node.nodes]) + "])", node.lineno)

    def _lambda(self, node, current_klass):
        if node.varargs:
            raise TranslationError(
                "varargs are not supported in Lambdas", node, self.module_name)
        if node.kwargs:
            raise TranslationError(
                "kwargs are not supported in Lambdas", node, self.module_name)
        res = StringIO()
        arg_names = list(node.argnames)
        self.push_lookup()
        for arg in arg_names:
            self.add_lookup('variable', arg, arg)
        function_args = ", ".join(arg_names)
        for child in node.getChildNodes():
            expr = self.expr(child, None)
        print >> res, "function (%s){" % function_args
        self._default_args_handler(node, arg_names, None, None,
                                   output=res)
        print >> res, 'return %s;}' % expr
        self.pop_lookup()
        return res.getvalue()

    def _listcomp(self, node, current_klass):
        self.push_lookup()
        resultlist = self.uniqid("listcomp")
        self.add_lookup('variable', resultlist, resultlist)
        save_output = self.output
        self.output = StringIO()
        print >> self.output, "function(){"
        print >> self.output, "var %s = pyjslib.List();" % resultlist

        tnode = ast.Discard(ast.CallFunc(ast.Getattr(ast.Name(resultlist), 'append'), [node.expr], None, None))
        for qual in node.quals[::-1]:
            if len(qual.ifs) > 1:
                raise TranslationError(
                    "unsupported ifs (in _listcomp)", node, self.module_name)
            tassign = qual.assign
            tlist = qual.list
            tbody = ast.Stmt([tnode])
            if len(qual.ifs) == 1:
                tbody = ast.Stmt([ast.If([(qual.ifs[0].test, tbody)], None, qual.ifs[0].lineno)])
            telse_ = None
            tnode = ast.For(tassign, tlist, tbody, telse_, node.lineno)
        self._for(tnode, current_klass)

        print >> self.output, "return %s;}()" % resultlist,
        captured_output = self.output
        self.output = save_output
        self.pop_lookup()
        return captured_output.getvalue()

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
            raise TranslationError(
                "unsupported flag (in _slice)", node, self.module_name)

    def _global(self, node, current_klass):
        for name in node.names:
            name_type, pyname, jsname, depth, is_local = self.lookup(name)
            if name_type is None:
                # Not defined yet.
                name_type = 'variable'
                pyname = name
                jsname = self.scopeName(name, depth, is_local)
            self.add_lookup(name_type, pyname, jsname)

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
        elif isinstance(node, ast.FloorDiv):
            return " pyjslib.int_( " + self._div(node, current_klass) + " ) "
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
            attr_ = attr.split('.')
            attr_left = '.'.join(attr_[:-1])
            attr_right = attr_[-1]
            pdict = {\
                    'attr': attr, 
                    'attr_left': attr_left, 
                    'attr_right': attr_right,
                }
            if self.bound_methods:
                attr_code = """\
(typeof %(attr)s == 'function' && %(attr_left)s.__is_instance__?\
pyjslib.getattr(%(attr_left)s, '%(attr_right)s'):\
%(attr)s)\
"""
            else:
                attr_code = "%(attr)s"
            attr_code = attr_code % pdict
            pdict['attr_code'] = attr_code

            if not self.attribute_checking:
                attr = attr_code
            else:
                if attr.find('(') < 0 and not self.debug:
                    attr = """(%(attr)s===undefined?(function(){throw new TypeError('%(attr)s is undefined')})():%(attr_code)s)""" % pdict
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
        elif isinstance(node, ast.ListComp):
            return self._listcomp(node, current_klass)
        else:
            raise TranslationError(
                "unsupported type (in expr)", node, self.module_name)


def translate(sources, output_file, module_name=None,
              debug=False,
              print_statements = True,
              function_argument_checking=True,
              attribute_checking=True,
              bound_methods=True,
              source_tracking=True,
              line_tracking=True,
              store_source=True,
             ):
    sources = map(os.path.abspath, sources)
    output_file = os.path.abspath(output_file)
    if not module_name:
        module_name, extension = os.path.splitext(os.path.basename(sources[0]))

    trees = []
    tree= None
    for src in sources:
        current_tree = compiler.parseFile(src)
        flags = set()
        f = file(src)
        for l in f:
            if l.startswith('#@PYJS_'):
                flags.add(l.strip()[7:])
        f.close()
        if tree:
            tree = merge(module_name, tree, current_tree, flags)
        else:
            tree = current_tree
    #XXX: if we have an override the sourcefile and the tree is not the same!
    f = file(sources[0], "r")
    src = f.read()
    f.close()
    output = file(output_file, 'w')

    t = Translator(module_name, module_name, module_name, src, tree, output,
                   debug = debug,
                   print_statements = print_statements,
                   function_argument_checking = function_argument_checking,
                   attribute_checking = attribute_checking,
                   bound_methods = bound_methods,
                   source_tracking = source_tracking,
                   line_tracking = line_tracking,
                   store_source = store_source,
                  )
    output.close()
    return t.imported_modules

def merge(module_name, tree1, tree2, flags):
    if 'FULL_OVERRIDE' in flags:
        return tree2
    for child in tree2.node:
        if isinstance(child, ast.Function):
            replaceFunction(tree1, child.name, child)
        elif isinstance(child, ast.Class):
            replaceClassMethods(tree1, child.name, child)
        else:
            raise TranslationError(
                "Do not know how to merge %s" % child, child, module_name)
    return tree1

def replaceFunction(tree, function_name, function_node):
    # find function to replace
    for child in tree.node:
        if isinstance(child, ast.Function) and child.name == function_name:
            copyFunction(child, function_node)
            return
    raise TranslationError(
        "function not found: " + function_name, function_node, None)

def copyFunction(target, source):
    target.code = source.code
    target.argnames = source.argnames
    target.defaults = source.defaults
    target.doc = source.doc # @@@ not sure we need to do this any more

def addCode(target, source):
    target.nodes.append(source)



def replaceClassMethods(tree, class_name, class_node):
    # find class to replace
    old_class_node = None
    for child in tree.node:
        if isinstance(child, ast.Class) and child.name == class_name:
            old_class_node = child
            break

    if not old_class_node:
        raise TranslationError(
            "class not found: " + class_name, class_node, self.module_name)

    # replace methods
    for node in class_node.code:
        if isinstance(node, ast.Function):
            found = False
            for child in old_class_node.code:
                if isinstance(child, ast.Function) and child.name == node.name:
                    found = True
                    copyFunction(child, node)
                    break

            if not found:
                raise TranslationError(
                    "class method not found: " + class_name + "." + node.name,
                    node, self.module_name)
        elif isinstance(node, ast.Assign) and \
             isinstance(node.nodes[0], ast.AssName):
            found = False
            for child in old_class_node.code:
                if isinstance(child, ast.Assign) and \
                    eqNodes(child.nodes, node.nodes):
                    found = True
                    copyAssign(child, node)
            if not found:
                addCode(old_class_node.code, node)
        elif isinstance(node, ast.Pass):
            pass
        else:
            raise TranslationError(
                "Do not know how to merge %s" % node, node, self.module_name)



class PlatformParser:
    def __init__(self, platform_dir = "", verbose=True, chain_plat=None):
        self.platform_dir = platform_dir
        self.parse_cache = {}
        self.platform = ""
        self.verbose = verbose
        self.chain_plat = chain_plat

    def setPlatform(self, platform):
        self.platform = platform

    def parseModule(self, module_name, file_name):

        importing = False
        if not self.parse_cache.has_key(file_name):
            importing = True
            if self.chain_plat:
                mod, override = self.chain_plat.parseModule(module_name,
                                                            file_name)
            else:
                mod = compiler.parseFile(file_name)
            self.parse_cache[file_name] = mod
        else:
            mod = self.parse_cache[file_name]

        override = False
        platform_file_name = self.generatePlatformFilename(file_name)
        if self.platform and os.path.isfile(platform_file_name):
            mod = copy.deepcopy(mod)
            mod_override = compiler.parseFile(platform_file_name)
            if self.verbose:
                print "Merging", module_name, self.platform
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

    def replaceFunction(self, tree, function_name, function_node):
        # find function to replace
        for child in tree.node:
            if isinstance(child, ast.Function) and child.name == function_name:
                self.copyFunction(child, function_node)
                return
        raise TranslationError(
            "function not found: " + function_name,
            function_node, self.module_name)

    def replaceClassMethods(self, tree, class_name, class_node):
        # find class to replace
        old_class_node = None
        for child in tree.node:
            if isinstance(child, ast.Class) and child.name == class_name:
                old_class_node = child
                break

        if not old_class_node:
            raise TranslationError(
                "class not found: " + class_name, class_node, self.module_name)

        # replace methods
        for node in class_node.code:
            if isinstance(node, ast.Function):
                found = False
                for child in old_class_node.code:
                    if isinstance(child, ast.Function) and child.name == node.name:
                        found = True
                        self.copyFunction(child, node)
                        break

                if not found:
                    raise TranslationError(
                        "class method not found: " + class_name + "." + node.name,
                        node, self.module_name)
            elif isinstance(node, ast.Assign) and \
                 isinstance(node.nodes[0], ast.AssName):
                found = False
                for child in old_class_node.code:
                    if isinstance(child, ast.Assign) and \
                        self.eqNodes(child.nodes, node.nodes):
                        found = True
                        self.copyAssign(child, node)
                if not found:
                    self.addCode(old_class_node.code, node)
            elif isinstance(node, ast.Pass):
                pass
            else:
                raise TranslationError(
                    "Do not know how to merge %s" % node,
                    node, self.module_name)

    def copyFunction(self, target, source):
        target.code = source.code
        target.argnames = source.argnames
        target.defaults = source.defaults
        target.doc = source.doc # @@@ not sure we need to do this any more

    def copyAssign(self, target, source):
        target.nodes = source.nodes
        target.expr = source.expr
        target.lineno = source.lineno
        return

    def eqNodes(self, nodes1, nodes2):
        return str(nodes1) == str(nodes2)

def dotreplace(fname):
    path, ext = os.path.splitext(fname)
    return path.replace(".", "/") + ext

class AppTranslator:

    def __init__(self, library_dirs=[], parser=None, dynamic=False,
                 verbose=True,
                 debug=False,
                 print_statements=True,
                 function_argument_checking=True,
                 attribute_checking=True,
                 bound_methods=True,
                 source_tracking=True,
                 line_tracking=True,
                 store_source=True,
                ):
        self.extension = ".py"
        self.print_statements = print_statements
        self.library_modules = []
        self.overrides = {}
        self.library_dirs = path + library_dirs
        self.dynamic = dynamic
        self.verbose = verbose
        self.debug = debug
        self.print_statements = print_statements
        self.function_argument_checking = function_argument_checking
        self.attribute_checking = attribute_checking
        self.bound_methods = bound_methods
        self.source_tracking = source_tracking
        self.line_tracking = line_tracking
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
                    LIBRARY_PATH, library_dir, file_name)
            if os.path.isfile(full_file_name):
                return full_file_name

            fnameinit, ext = os.path.splitext(file_name)
            fnameinit = fnameinit + "/__init__.py"

            full_file_name = os.path.join(
                    LIBRARY_PATH, library_dir, fnameinit)
            if os.path.isfile(full_file_name):
                return full_file_name

        raise Exception("file not found: " + file_name)

    def _translate(self, module_name, debug=False):
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
        t = Translator(mn, module_name, module_name, src, mod, output, 
                       self.dynamic, self.findFile, 
                       debug = self.debug,
                       print_statements = self.print_statements,
                       function_argument_checking = self.function_argument_checking,
                       attribute_checking = self.attribute_checking,
                       bound_methods = self.bound_methods,
                       source_tracking = self.source_tracking,
                       line_tracking = self.line_tracking,
                       store_source = self.store_source,
                      )

        module_str = output.getvalue()
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
            print >> lib_code, "%s();\n" % library

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

def add_compile_options(parser):
    debug_options = {}
    speed_options = {}
    pythonic_options = {}

    parser.add_option("--debug-wrap",
                      dest="debug",
                      action="store_true",
                      help="Wrap function calls with javascript debug code",
                     )
    parser.add_option("--no-debug-wrap",
                      dest="debug",
                      action="store_false",
                     )
    debug_options['debug'] = True
    speed_options['debug'] = False

    parser.add_option("--no-print-statements",
                      dest="print_statements",
                      action="store_false",
                      help="Remove all print statements",
                     )
    parser.add_option("--print-statements",
                      dest="print_statements",
                      action="store_true",
                      help="Generate code for print statements",
                     )
    speed_options['print_statements'] = False

    parser.add_option("--no-function-argument-checking",
                      dest = "function_argument_checking",
                      action="store_false",
                      help = "Do not generate code for function argument checking",
                     )
    parser.add_option("--function-argument-checking",
                      dest = "function_argument_checking",
                      action="store_true",
                      help = "Generate code for function argument checking",
                     )
    speed_options['function_argument_checking'] = False
    pythonic_options['function_argument_checking'] = True

    parser.add_option("--no-attribute-checking",
                      dest = "attribute_checking",
                      action="store_false",
                      help = "Do not generate code for attribute checking",
                     )
    parser.add_option("--attribute-checking",
                      dest = "attribute_checking",
                      action="store_true",
                      help = "Generate code for attribute checking",
                     )
    speed_options['attribute_checking'] = False
    pythonic_options['attribute_checking'] = True

    parser.add_option("--no-bound-methods",
                      dest = "bound_methods",
                      action="store_false",
                      help = "Do not generate code for binding methods",
                     )
    parser.add_option("--bound-methods",
                      dest = "bound_methods",
                      action="store_true",
                      help = "Generate code for binding methods",
                     )
    speed_options['bound_methods'] = False
    pythonic_options['bound_methods'] = True

    parser.add_option("--no-source-tracking",
                      dest = "source_tracking",
                      action="store_false",
                      help = "Do not generate code for source tracking",
                     )
    parser.add_option("--source-tracking",
                      dest = "source_tracking",
                      action="store_true",
                      help = "Generate code for source tracking",
                     )
    debug_options['source_tracking'] = True
    speed_options['source_tracking'] = False
    pythonic_options['source_tracking'] = True

    parser.add_option("--no-line-tracking",
                      dest = "line_tracking",
                      action="store_true",
                      help = "Do not generate code for source tracking on every line",
                     )
    parser.add_option("--line-tracking",
                      dest = "line_tracking",
                      action="store_true",
                      help = "Generate code for source tracking on every line",
                     )
    debug_options['line_tracking'] = True
    pythonic_options['line_tracking'] = True

    parser.add_option("--no-store-source",
                      dest = "store_source",
                      action="store_false",
                      help = "Do not store python code in javascript",
                     )
    parser.add_option("--store-source",
                      dest = "store_source",
                      action="store_true",
                      help = "Store python code in javascript",
                     )
    debug_options['store_source'] = True
    pythonic_options['store_source'] = True


    def set_multiple(option, opt_str, value, parser, **kwargs):
        for k in kwargs.keys():
            setattr(parser.values, k, kwargs[k])

    parser.add_option("-d", "--debug",
                      action="callback",
                      callback = set_multiple,
                      callback_kwargs = debug_options,
                      help="Set all debugging options",
                     )
    parser.add_option("-O",
                      action="callback",
                      callback = set_multiple,
                      callback_kwargs = speed_options,
                      help="Set all options that maximize speed",
                     )
    parser.add_option("--strict",
                      action="callback",
                      callback = set_multiple,
                      callback_kwargs = pythonic_options,
                      help="Set all options that mimic standard python behavior",
                     )
    parser.set_defaults(debug=False,
                        print_statements=True,
                        function_argument_checking = False,
                        attribute_checking = False,
                        bound_methods = True,
                        source_tracking = False,
                        line_tracking = False,
                        store_source = False,
                       )


usage = """
  usage: %prog [options] file...
"""

def main():
    import sys
    from optparse import OptionParser

    parser = OptionParser(usage = usage)
    parser.add_option("-o", "--output", dest="output",
                      help="Place the output into <output>")
    parser.add_option("-m", "--module-name", dest="module_name",
                      help="Module name of output")
    add_compile_options(parser)
    (options, args) = parser.parse_args()

    if len(args)<1:
        parser.error("incorrect number of arguments")

    if not options.output:
        parser.error("No output file specified")
    options.output = os.path.abspath(options.output)

    file_names = map(os.path.abspath, args)
    for fn in file_names:
        if not os.path.isfile(fn):
            print >> sys.stderr, "Input file not found %s" % fn
            sys.exit(1)

    translate(file_names, options.output, options.module_name,
              debug = options.debug,
              print_statements = options.print_statements,
              function_argument_checking = options.function_argument_checking,
              attribute_checking = options.attribute_checking,
              bound_methods = options.bound_methods,
              source_tracking = options.source_tracking,
              line_tracking = options.line_tracking,
              store_source = options.store_source,
    ),

if __name__ == "__main__":
    main()

