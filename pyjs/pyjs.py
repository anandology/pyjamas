#!/usr/bin/env python
from types import StringType

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


import compiler
from compiler import ast
import os
import copy

# this is the python function used to wrap native javascript
NATIVE_JS_FUNC_NAME = "JS"

class Klass:

    klasses = {}

    def __init__(self, name):
        self.name = name
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
    if name[2:10] == 'pyjamas.':
        return "__"+name[10:]
    if name[2:10] == 'pyjamas_':
        return "__"+name[10:]
    if name[:8] == 'pyjamas.':
        return name[8:]
    return name

class Translator:

    def __init__(self, module_name, raw_module_name, src, debug, mod, output):

        if module_name:
            self.module_prefix = module_name + "_"
        else:
            self.module_prefix = ""
        self.raw_module_name = raw_module_name
        src = src.replace("\r\n", "\n")
        src = src.replace("\n\r", "\n")
        src = src.replace("\r",   "\n")
        self.src = src.split("\n")
        self.debug = debug
        self.imported_modules = set()
        self.imported_js = set()
        self.top_level_functions = set()
        self.top_level_classes = set()
        self.top_level_vars = set()
        self.output = output
        self.imported_classes = {}
        self.method_imported_globals = set()
        self.method_self = None
        self.nextTupleAssignID = 1

        if self.debug:
            haltException = self.module_prefix + "HaltException"
            print >>self.output, 'function ' + haltException + '() {'
            print >>self.output, '  this.message = "Program Halted";'
            print >>self.output, '  this.name = "' + haltException + '";'
            print >>self.output, '}'
            print >>self.output, ''
            print >>self.output, haltException + ".prototype.toString = function()"
            print >>self.output, '{'
            print >>self.output, 'return this.name + ": \\"" + this.message + "\\"";'
            print >>self.output, '}'

            isHaltFunction = self.module_prefix + "IsHaltException"
            print >>self.output, 'function ' + isHaltFunction + '(s) {'
            print >>self.output, '  var suffix="HaltException";'
            print >>self.output, '  if (s.length < suffix.length) {'
            print >>self.output, '    return false;'
            print >>self.output, '  } else {'
            print >>self.output, '    return s.substring(suffix.length, (s.length - suffix.length)) == suffix;'
            print >>self.output, '  }'
            print >>self.output, '}'

        for child in mod.node:
            if isinstance(child, ast.Function):
                self.top_level_functions.add(child.name)
            elif isinstance(child, ast.Class):
                self.top_level_classes.add(child.name)

        for child in mod.node:
            if isinstance(child, ast.Function):
                self._function(child, False)
            elif isinstance(child, ast.Class):
                self._class(child)
            elif isinstance(child, ast.Import):
                importName = child.names[0][0]
                if importName == '__pyjamas__': # special module to help make pyjamas modules loadable in the python interpreter
                    pass
                elif importName.endswith('.js'):
                   self.imported_js.add(importName)
                else:
                   self.imported_modules.add(strip_py(importName))
            elif isinstance(child, ast.From):
                if child.modname == '__pyjamas__': # special module to help make pyjamas modules loadable in the python interpreter
                    pass
                else:
                    self.imported_modules.add(child.modname)
                    self._from(child)
            elif isinstance(child, ast.Discard):
                self._discard(child, None)
            elif isinstance(child, ast.Assign):
                self._assign(child, None, True)
            elif isinstance(child, ast.AugAssign):
                self._augassign(child, None)
            else:
                raise TranslationError("unsupported type (in __init__)", child)

        # Initialize all classes for this module
        for className in self.top_level_classes:
            print >> self.output, "__"+strip_py(self.module_prefix)+className+"_initialize();"

    def _default_args_handler(self, node, arg_names, current_klass):
        if len(node.defaults):
            default_pos = len(arg_names) - len(node.defaults)
            if arg_names and arg_names[0] == self.method_self:
                default_pos -= 1
            for default_node in node.defaults:
                if isinstance(default_node, ast.Const):
                    default_value = self._const(default_node)
                elif isinstance(default_node, ast.Name):
                    default_value = self._name(default_node)
                elif isinstance(default_node, ast.UnarySub):
                    default_value = self._unarysub(default_node, current_klass)
                else:
                    raise TranslationError("unsupported type (in _method)", default_node)

                default_name = arg_names[default_pos]
                default_pos += 1
                print >>self.output, "    if (typeof %s == 'undefined') %s=%s;" % (default_name, default_name, default_value)

    def _varargs_handler(self, node, varargname, arg_names, current_klass):
        print >>self.output, "    var", varargname, '= new pyjslib_List([]);'
        print >>self.output, "    for(var __va_arg="+str(len(arg_names))+"; __va_arg < arguments.length; __va_arg++) {"
        print >>self.output, "        var __arg = arguments[__va_arg];"
        print >>self.output, "        "+varargname+".append(__arg);"
        print >>self.output, "    }"

    def _kwargs_parser(self, node, function_name, arg_names, current_klass):
        if len(node.defaults) or node.kwargs:
            default_pos = len(arg_names) - len(node.defaults)
            if arg_names and arg_names[0] == self.method_self:
                default_pos -= 1
            print >>self.output, function_name+'.parse_kwargs = function (', ", ".join(["__kwargs"]+arg_names), ") {"
            for default_node in node.defaults:
                default_value = self.expr(default_node, current_klass)
#                if isinstance(default_node, ast.Const):
#                    default_value = self._const(default_node)
#                elif isinstance(default_node, ast.Name):
#                    default_value = self._name(default_node)
#                elif isinstance(default_node, ast.UnarySub):
#                    default_value = self._unarysub(default_node, current_klass)
#                else:
#                    raise TranslationError("unsupported type (in _method)", default_node)

                default_name = arg_names[default_pos]
                print >>self.output, "    if (typeof %s == 'undefined')"%(default_name)
                print >>self.output, "        %s=__kwargs.%s;"% (default_name, default_name)
                default_pos += 1

            #self._default_args_handler(node, arg_names, current_klass)
            if node.kwargs: arg_names += ["pyjslib_Dict(__kwargs)"]
            print >>self.output, "    var __r = "+"".join(["[", ", ".join(arg_names), "]"])+";"
            if node.varargs:
                self._varargs_handler(node, "__args", arg_names, current_klass)
                print >>self.output, "    __r.push.apply(__r, __args.getArray())"
            print >>self.output, "    return __r;"
            print >>self.output, "};"

    def _function(self, node, local=False):
        if local: function_name = node.name
        else: function_name = strip_py(self.module_prefix) + node.name
        arg_names = list(node.argnames)
        normal_arg_names = list(arg_names)
        if node.kwargs: kwargname = normal_arg_names.pop()
        if node.varargs: varargname = normal_arg_names.pop()
        declared_arg_names = list(normal_arg_names)
        if node.kwargs: declared_arg_names.append(kwargname)

        function_args = "(" + ", ".join(declared_arg_names) + ")"
        print >>self.output, "function %s%s {" % (function_name, function_args)
        self._default_args_handler(node, normal_arg_names, None)

        if node.varargs:
            self._varargs_handler(node, varargname, declared_arg_names, None)

        for child in node.code:
            self._stmt(child, None)

        print >>self.output, "}"
        print >>self.output, "\n"

        self._kwargs_parser(node, function_name, normal_arg_names, None)


    def _return(self, node, current_klass):
        expr = self.expr(node.value, current_klass)
        if expr != "null":
            print >>self.output, "    return " + expr + ";"
        else:
            print >>self.output, "    return;"


    def _break(self, node, current_klass):
        print >>self.output, "    break;"


    def _continue(self, node, current_klass):
        print >>self.output, "    continue;"


    def _callfunc(self, v, current_klass):
        if isinstance(v.node, ast.Name):
            if v.node.name in self.top_level_functions:
                call_name = strip_py(self.module_prefix) + v.node.name
            elif v.node.name in self.top_level_classes:
                call_name = strip_py(self.module_prefix) + v.node.name
            elif self.imported_classes.has_key(v.node.name):
                call_name = self.imported_classes[v.node.name] + '_' + v.node.name
            elif v.node.name == "callable":
                call_name = "pyjslib_isFunction"
            elif v.node.name == "map":
                call_name = "pyjslib_map"
            elif v.node.name == "filter":
                call_name = "pyjslib_filter"
            elif v.node.name == "dir":
                call_name = "pyjslib_dir"
            elif v.node.name == "getattr":
                call_name = "pyjslib_getattr"
            elif v.node.name == "setattr":
                call_name = "pyjslib_setattr"
            elif v.node.name == "hasattr":
                call_name = "pyjslib_hasattr"
            elif v.node.name == "int":
                call_name = "pyjslib_int"
            elif v.node.name == "str":
                call_name = "pyjslib_str"
            elif v.node.name == "repr":
                call_name = "pyjslib_repr"
            elif v.node.name == "range":
                call_name = "pyjslib_range"
            elif v.node.name == "len":
                call_name = "pyjslib_len"
            elif v.node.name == "hash":
                call_name = "pyjslib_hash"
            elif v.node.name == "abs":
                call_name = "pyjslib_abs"
            elif v.node.name == "ord":
                call_name = "pyjslib_ord"
            elif v.node.name == "chr":
                call_name = "pyjslib_chr"
            elif v.node.name == "enumerate":
                call_name = "pyjslib_enumerate"
            elif v.node.name == "min":
                call_name = "pyjslib_min"
            elif v.node.name == "max":
                call_name = "pyjslib_max"
            elif v.node.name == "isinstance":
                call_name = "pyjslib_isinstance"
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
        else:
            raise TranslationError("unsupported type (in _callfunc)", v.node)

        call_name = strip_py(call_name)

        kwargs = []
        for ch4 in v.args:
            if isinstance(ch4, ast.Keyword):
                kwarg = ch4.name + ":" + self.expr(ch4.expr, current_klass)
                kwargs.append(kwarg)
            else:
                arg = self.expr(ch4, current_klass)
                call_args.append(arg)

        if kwargs:
            try: call_this, method_name = call_name.rsplit(".", 1)
            except ValueError:
                # Must be a function call ...
                return ("pyjs_kwargs_function_call("+call_name+", "
                                  + "["+", ".join(['{' + ', '.join(kwargs) + '}']+call_args)+"]"
                                  + ")" )
            else:
                return ("pyjs_kwargs_method_call("+call_this+", '"+method_name+"', "
                                  + "["+", ".join(['{' + ', '.join(kwargs) + '}']+call_args)+"]"
                                  + ")")
        else:
            return call_name + "(" + ", ".join(call_args) + ")"

    def _print(self, node, current_klass):
        call_args = []
        for ch4 in node.nodes:
            arg = self.expr(ch4, current_klass)
            call_args.append(arg)

        print >>self.output, "pyjslib_printFunc([", ', '.join(call_args), "],", int(isinstance(node, ast.Printnl)), ");"

    def _tryExcept(self, node, current_klass):
        ok = True
        if len(node.handlers) != 1:
            raise TranslationError("except statements in this form are" +
                                   " not supported", node)

        expr = node.handlers[0][0]
        as_ = node.handlers[0][1]
        if as_:
            errName = as_.name
        else:
            errName = 'err'
        if not ok:
            expr = self.expr(node.handlers[0][0], current_klass)
            import pdb;pdb.set_trace()
            raise TranslationError("only simple try...except statements " +
                                   "supported", node)

        print >>self.output, "    try {"
        for stmt in node.body.nodes:
            self._stmt(stmt, current_klass)
        print >> self.output, "    } catch(%s) {" % errName
        if expr:
            print >> self.output, "   if((%(err)s === %(expr)s)||(pyjslib_isinstance(%(err)s, %(expr)s))){" % dict (err=errName, expr=self.expr(expr, current_klass))
        for stmt in node.handlers[0][2]:
            self._stmt(stmt, current_klass)
        if expr:
            print >> self.output, "}"
        if node.else_ != None:
            print >>self.output, "    } finally {"
            for stmt in node.else_:
                self._stmt(stmt, current_klass)
        print >>self.output, "    }"

    def _getattr(self, v):
        attr_name = v.attrname
        if isinstance(v.expr, ast.Name):
            obj = self._name(v.expr, return_none_for_module=True)
            if obj == None and v.expr.name in self.imported_modules:
                return "__"+v.expr.name+'_'+attr_name+'.prototype.__class__'
            return obj + "." + attr_name
        elif isinstance(v.expr, ast.Getattr):
            return self._getattr(v.expr) + "." + attr_name
        elif isinstance(v.expr, ast.Subscript):
            return self._subscript(v.expr, strip_py(self.module_prefix)) + "." + attr_name
        elif isinstance(v.expr, ast.CallFunc):
            return self._callfunc(v.expr, strip_py(self.module_prefix)) + "." + attr_name
        else:
            raise TranslationError("unsupported type (in _getattr)", v.expr)


    def _name(self, v, return_none_for_module=False):
        if v.name == "True":
            return "true"
        elif v.name == "False":
            return "false"
        elif v.name == "None":
            return "null"
        elif v.name == self.method_self:
            return "this"
        elif v.name in self.method_imported_globals:
            return strip_py(self.module_prefix) + v.name
        elif self.imported_classes.has_key(v.name):
            return "__" + self.imported_classes[v.name] + '_' + v.name + ".prototype.__class__"
        elif v.name in self.top_level_classes:
            return "__" + strip_py(self.module_prefix) + v.name + ".prototype.__class__"
        elif v.name in self.imported_modules and return_none_for_module:
            return None
        else:
            return v.name


    def _name2(self, v, current_klass, attr_name):
        obj = v.name

        if obj in self.method_imported_globals:
            call_name = strip_py(self.module_prefix) + obj + "." + attr_name
        elif self.imported_classes.has_key(obj):
            #attr_str = ""
            #if attr_name != "__init__":
            attr_str = ".prototype.__class__." + attr_name
            call_name = "__" + self.imported_classes[obj] + '_' + obj + attr_str
        elif obj in self.imported_modules:
            call_name = obj + "_" + attr_name
        elif obj[0] == obj[0].upper():
            call_name = "__" + strip_py(self.module_prefix) + obj + ".prototype.__class__." + attr_name
        else:
            call_name = self._name(v) + "." + attr_name

        return call_name


    def _getattr2(self, v, current_klass, attr_name):
        if isinstance(v.expr, ast.Getattr):
            call_name = self._getattr2(v.expr, current_klass, v.attrname + "." + attr_name)
        elif isinstance(v.expr, ast.Name) and v.expr.name in self.imported_modules:
            if v.expr.name == 'pyjamas':
                call_name = v.attrname + "_" + attr_name
            else:
                call_name = '__'+v.expr.name + '_' +v.attrname+".prototype.__class__."+attr_name
        else:
            obj = self.expr(v.expr, current_klass)
            call_name = obj + "." + v.attrname + "." + attr_name

        return call_name


    def _class(self, node):
        """
        Handle a class definition.

        In order to translate python semantics reasonably well, the following
        structure is used:

        A special object is created for the class, which inherits attributes
        from the superclass, or Object if there's no superclass.  This is the
        class object; the object which you refer to when specifying the
        class by name.  Static, class, and unbound methods are copied
        from the superclass object.

        A special constructor function is created with the same name as the
        class, which is used to create instances of that class.

        A javascript class (e.g. a function with a prototype attribute) is
        created which is the javascript class of created instances, and
        which inherits attributes from the class object. Bound methods are
        copied from the superclass into this class rather than inherited,
        because the class object contains unbound, class, and static methods
        that we don't necessarily want to inherit.

        The type of a method can now be determined by inspecting its
        static_method, unbound_method, class_method, or instance_method
        attribute; only one of these should be true.

        Much of this work is done in pyjs_extend, is pyjslib.py
        """
        class_name = strip_py(self.module_prefix) + node.name
        current_klass = Klass(class_name)

        init_method = None
        for child in node.code:
            if isinstance(child, ast.Function):
                current_klass.add_function(child.name)
                if child.name == "__init__":
                    init_method = child


        if len(node.bases) == 0:
            base_class = "pyjslib_Object"
        elif len(node.bases) == 1:
            if isinstance(node.bases[0], ast.Name):
                if self.imported_classes.has_key(node.bases[0].name):
                    base_class = self.imported_classes[node.bases[0].name] + '_' + node.bases[0].name
                else:
                    base_class = strip_py(self.module_prefix) + node.bases[0].name
            elif isinstance(node.bases[0], ast.Getattr):
                base_class = self._name(node.bases[0].expr) + "_" + node.bases[0].attrname
            else:
                raise TranslationError("unsupported type (in _class)", node.bases[0])

            current_klass.set_base(base_class)
        else:
            raise TranslationError("more than one base (in _class)", node)

        print >>self.output, "function __" + class_name + "() {"
        # call superconstructor
        #if base_class:
        #    print >>self.output, "    __" + base_class + ".call(this);"
        print >>self.output, "}"

        if not init_method:
            init_method = ast.Function([], "__init__", ["self"], [], 0, None, [])
            #self._method(init_method, current_klass, class_name)

        # Generate a function which constructs the object
        clsfunc = ast.Function([],
           node.name,
           init_method.argnames[1:],
           init_method.defaults,
           init_method.flags,
           None,
           [ast.Discard(ast.CallFunc(ast.Name("JS"), [ast.Const(
#            I attempted lazy initialization, but then you can't access static class members
#            "    if(!__"+base_class+".__was_initialized__)"+
#            "        __" + class_name + "_initialize();\n" +
            "    var instance = new __" + class_name + "();\n" +
            "    if(instance.__init__) instance.__init__.apply(instance, arguments);\n" +
            "    return instance;"
            )]))])

        self._function(clsfunc, False)
        print >>self.output, "function __" + class_name + "_initialize() {"
        print >>self.output, "    if(__"+class_name+".__was_initialized__) return;"
        print >>self.output, "    __"+class_name+".__was_initialized__ = true;"
        cls_obj = "__" + class_name + '.prototype.__class__'

        if class_name == "pyjslib_Object":
            print >>self.output, "    "+cls_obj+" = {};"
        else:
            if base_class and base_class not in ("object", "pyjslib_Object"):
                print >>self.output, "    if(!__"+base_class+".__was_initialized__)"
                print >>self.output, "        __"+base_class+"_initialize();"
                print >>self.output, "    pyjs_extend(__" + class_name + ", __"+base_class+");"
            else:
                print >>self.output, "    pyjs_extend(__" + class_name + ", __pyjslib_Object);"

        print >>self.output, "    "+cls_obj+".__new__ = "+class_name+";"

        for child in node.code:
            if isinstance(child, ast.Pass):
                pass
            elif isinstance(child, ast.Function):
                self._method(child, current_klass, class_name)
            elif isinstance(child, ast.Assign):
                self.classattr(child, current_klass)
            elif isinstance(child, ast.Discard) and isinstance(child.expr, ast.Const):
                # Probably a docstring, turf it
                pass
            else:
                raise TranslationError("unsupported type (in _class)", child)
        print >>self.output, "}"



    def classattr(self, node, current_klass):
        self._assign(node, current_klass, True)

    def _raise(self, node, current_klass):
        if node.expr2:
            raise TranslationError("More than one expression unsupported",
                                   node)
        print >> self.output, "throw (%s);" % self.expr(
            node.expr1, current_klass)

    def _method(self, node, current_klass, class_name):
        # reset global var scope
        self.method_imported_globals = set()

        arg_names = list(node.argnames)

        classmethod = False
        staticmethod = False
        if node.decorators:
            for d in node.decorators:
                if d.name == "classmethod":
                    classmethod = True
                elif d.name == "staticmethod":
                    staticmethod = True

        if staticmethod:
            staticfunc = ast.Function([], class_name+"_"+node.name, node.argnames, node.defaults, node.flags, node.doc, node.code, node.lineno)
            self._function(staticfunc, True)
            print >>self.output, "    __" + class_name + ".prototype.__class__." + node.name + " = " + class_name+"_"+node.name+";";
            print >>self.output, "    __" + class_name + ".prototype.__class__." + node.name + ".static_method = true;";
            return
        else:
            if len(arg_names) == 0:
                raise TranslationError("methods must take an argument 'self' (in _method)", node)
            self.method_self = arg_names[0]

            #if not classmethod and arg_names[0] != "self":
            #    raise TranslationError("first arg not 'self' (in _method)", node)

        normal_arg_names = arg_names[1:]
        if node.kwargs: kwargname = normal_arg_names.pop()
        if node.varargs: varargname = normal_arg_names.pop()
        declared_arg_names = list(normal_arg_names)
        if node.kwargs: declared_arg_names.append(kwargname)

        function_args = "(" + ", ".join(declared_arg_names) + ")"

        if classmethod:
            fexpr = "__" + class_name + ".prototype.__class__." + node.name
        else:
            fexpr = "__" + class_name + ".prototype." + node.name
        print >>self.output, "    "+fexpr + " = function" + function_args + " {"

        # default arguments
        self._default_args_handler(node, normal_arg_names, current_klass)

        if node.varargs:
            self._varargs_handler(node, varargname, declared_arg_names, current_klass)

        for child in node.code:
            self._stmt(child, current_klass)

        print >>self.output, "    };"

        self._kwargs_parser(node, fexpr, normal_arg_names, current_klass)

        if classmethod:
            # Have to create a version on the instances which automatically passes the
            # class as "self"
            altexpr = "__" + class_name + ".prototype." + node.name
            print >>self.output, "    "+altexpr + " = function() {"
            print >>self.output, "        return " + fexpr + ".apply(this.__class__, arguments);"
            print >>self.output, "    };"
            print >>self.output, "    "+fexpr+".class_method = true;"
            print >>self.output, "    "+altexpr+".instance_method = true;"
        else:
            # For instance methods, we need an unbound version in the class object
            altexpr = "__" + class_name + ".prototype.__class__." + node.name
            print >>self.output, "    "+altexpr + " = function() {"
            print >>self.output, "        return " + fexpr + ".call.apply("+fexpr+", arguments);"
            print >>self.output, "    };"
            print >>self.output, "    "+altexpr+".unbound_method = true;"
            print >>self.output, "    "+fexpr+".instance_method = true;"

        if node.kwargs or len(node.defaults):
            print >>self.output, "    "+altexpr + ".parse_kwargs = " + fexpr + ".parse_kwargs;"

        self.method_self = None
        self.method_imported_globals = set()

    def _stmt(self, node, current_klass):
        if self.debug:
            debugStmt = True # initially.
            if isinstance(node, ast.Discard):
                if isinstance(node.expr, ast.CallFunc):
                    if isinstance(node.expr.node, ast.Name) and \
                       node.expr.node.name == NATIVE_JS_FUNC_NAME:
                        # Don't try to debug JS() functions.
                        debugStmt = False
        else:
            debugStmt = False

        if debugStmt:
            print >>self.output, '  try {'

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

        if debugStmt:
            lineNum = "Unknown"
            srcLine = ""
            if hasattr(node, "lineno"):
                if node.lineno != None:
                    lineNum = node.lineno
                    srcLine = self.src[lineNum-1]
                    srcLine = srcLine.replace('\\', '\\\\')
                    srcLine = srcLine.replace('"', '\\"')

            errMsg = "Error in " + self.raw_module_name + ".py, line " \
                   + str(lineNum) + ":"\
                   + "\\n\\n" \
                   + "    " + srcLine \
                   + "\\n\\n"

            haltException = self.module_prefix + "HaltException"
            isHaltFunction = self.module_prefix + "IsHaltException"

            print >>self.output, '  } catch (err) {'
            print >>self.output, '      if (' + isHaltFunction + '(err.name)) {'
            print >>self.output, '          throw err;'
            print >>self.output, '      } else {'
            print >>self.output, '          alert("' + errMsg + '"' \
                                                + '+err.name+": "+err.message'\
                                                + ');'
            print >>self.output, '          debugger;'

            print >>self.output, '          throw new ' + self.module_prefix + "HaltException();"
            print >>self.output, '      }'
            print >>self.output, '  }'


    def _augassign(self, node, current_klass):
        v = node.node
        if isinstance(v, ast.Getattr):
            lhs = self._getattr(v)
        else:
            lhs = self._name(node.node)
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

        def _lhsFromAttr(v):
            attr_name = v.attrname
            if isinstance(v.expr, ast.Name):
                obj = v.expr.name
                lhs = self._name(v.expr) + "." + attr_name
            elif isinstance(v.expr, ast.Getattr):
                lhs = self._getattr(v)
            elif isinstance(v.expr, ast.Subscript):
                lhs = self._subscript(v.expr, current_klass) + "." + attr_name
            else:
                raise TranslationError("unsupported type (in _assign)", v.expr)
            return lhs

        def _lhsFromName(v, top_level, current_klass):
            if top_level:
                if current_klass:
                    lhs = "__" + current_klass.name + ".prototype.__class__." \
                               + v.name
                else:
                    self.top_level_vars.add(v.name)
                    lhs = "var " + strip_py(self.module_prefix) + v.name
            else:
                if v.name in self.method_imported_globals:
                    lhs = strip_py(self.module_prefix) + v.name
                else:
                    lhs = "var " + v.name
            return lhs

        v = node.nodes[0]
        if isinstance(v, ast.AssAttr):
            lhs = _lhsFromAttr(v)
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
                print >>self.output, "    " + obj + ".__setitem__(" + idx + ", " + value + ");"
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
                rhs = tempName + ".__getitem__(" + str(index) + ")"

                if isinstance(child, ast.AssAttr):
                    lhs = _lhsFromAttr(child)
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
                        print >>self.output, "    " + obj + ".__setitem__(" \
                                           + idx + ", " + rhs + ");"
                        continue
                print >>self.output, "    " + lhs + " = " + rhs + ";"
            return
        else:
            raise TranslationError("unsupported type (in _assign)", v)

        rhs = self.expr(node.expr, current_klass)
        print >>self.output, "    " + lhs + " " + op + " " + rhs + ";"


    def _discard(self, node, current_klass):
        if isinstance(node.expr, ast.CallFunc):
            if isinstance(node.expr.node, ast.Name) and node.expr.node.name == NATIVE_JS_FUNC_NAME:
                if len(node.expr.args) != 1:
                    raise TranslationError("native javascript function %s must have one arg" % NATIVE_JS_FUNC_NAME, node.expr)
                if not isinstance(node.expr.args[0], ast.Const):
                    raise TranslationError("native javascript function %s must have constant arg" % NATIVE_JS_FUNC_NAME, node.expr)
                print >>self.output, node.expr.args[0].value
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

            print >>self.output, "    " + keyword + " (" + expr + ") {"
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
            if node.modname == 'pyjamas':
                self.imported_modules.add(name[0])
            elif node.modname[:8] == 'pyjamas.':
                self.imported_classes[name[0]] = node.modname[8:]
            else:
                self.imported_classes[name[0]] = node.modname


    def _compare(self, node, current_klass):
        lhs = self.expr(node.expr, current_klass)

        if len(node.ops) != 1:
            raise TranslationError("only one ops supported (in _compare)", node)

        op = node.ops[0][0]
        rhs_node = node.ops[0][1]
        rhs = self.expr(rhs_node, current_klass)

        if op == "in":
            return rhs + ".__contains__(" + lhs + ")"
        elif op == "not in":
            return "!" + rhs + ".__contains__(" + lhs + ")"
        elif op == "is":
            op = "=="
        elif op == "is not":
            op = "!="

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
            if node.assign.flags == "OP_ASSIGN":
                op = "="
        elif isinstance(node.assign, ast.AssTuple):
            op = "="
            i = 0
            for child in node.assign:
                child_name = child.name
                if assign_name == "":
                    assign_name = "temp_" + child_name

                assign_tuple += """
                var %(child_name)s %(op)s %(assign_name)s.__getitem__(%(i)i);
                """ % locals()
                i += 1
        else:
            raise TranslationError("unsupported type (in _for)", node.assign)

        if isinstance(node.list, ast.Name):
            list_expr = self._name(node.list)
        elif isinstance(node.list, ast.Getattr):
            list_expr = self._getattr(node.list)
        elif isinstance(node.list, ast.CallFunc):
            list_expr = self._callfunc(node.list, current_klass)
        else:
            raise TranslationError("unsupported type (in _for)", node.list)

        lhs = "var " + assign_name
        iterator_name = "__" + assign_name

        print >>self.output, """
        var %(iterator_name)s = %(list_expr)s.__iter__();
        try {
            while (true) {
                %(lhs)s %(op)s %(iterator_name)s.next();
                %(assign_tuple)s
        """ % locals()
        for node in node.body.nodes:
            self._stmt(node, current_klass)
        print >>self.output, """
            }
        } catch (e) {
            if (e != StopIteration) {
                throw e;
            }
        }
        """ % locals()


    def _while(self, node, current_klass):
        test = self.expr(node.test, current_klass)
        print >>self.output, "    while (" + test + ") {"
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
        elif isinstance(node.value, str):
            return "'" + node.value.encode('string_escape') + "'"
            # lkcl: reverting r208.  bug #127
            # erik - string_escape does something necessary, without
            # which quotes inside comments (docstrings) causes a
            # javascript syntax error.  e.g. """ 'hello' """
            s = unicode(node.value, 'utf-8')
            s = repr(s)[2:-1].replace("'", "\\'")
            return "'" + s + "'"
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
           self.imported_js.add("sprintf.js") # Include the sprintf functionality if it is used
           return "sprintf("+self.expr(node.left, current_klass) + ", " + self.expr(node.right, current_klass)+")"
        return self.expr(node.left, current_klass) + " % " + self.expr(node.right, current_klass)

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
                return self.expr(node.expr, current_klass) + ".__getitem__(" + self.expr(node.subs[0], current_klass) + ")"
            else:
                raise TranslationError("must have one sub (in _subscript)", node)
        else:
            raise TranslationError("unsupported flag (in _subscript)", node)

    def _subscript_stmt(self, node, current_klass):
        if node.flags == "OP_DELETE":
            print >>self.output, "    " + self.expr(node.expr, current_klass) + ".__delitem__(" + self.expr(node.subs[0], current_klass) + ");"
        else:
            raise TranslationError("unsupported flag (in _subscript)", node)

    def _list(self, node, current_klass):
        return "new pyjslib_List([" + ", ".join([self.expr(x, current_klass) for x in node.nodes]) + "])"

    def _dict(self, node, current_klass):
        items = []
        for x in node.items:
            key = self.expr(x[0], current_klass)
            value = self.expr(x[1], current_klass)
            items.append("[" + key + ", " + value + "]")
        return "new pyjslib_Dict([" + ", ".join(items) + "])"

    def _tuple(self, node, current_klass):
        return "new pyjslib_Tuple([" + ", ".join([self.expr(x, current_klass) for x in node.nodes]) + "])"

    def _slice(self, node, current_klass):
        if node.flags == "OP_APPLY":
            lower = "null"
            upper = "null"
            if node.lower != None:
                lower = self.expr(node.lower, current_klass)
            if node.upper != None:
                upper = self.expr(node.upper, current_klass)
            return  "pyjslib_slice(" + self.expr(node.expr, current_klass) + ", " + lower + ", " + upper + ")"
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
            return self._name(node)
        elif isinstance(node, ast.Subscript):
            return self._subscript(node, current_klass)
        elif isinstance(node, ast.Getattr):
            return self._getattr(node)
        elif isinstance(node, ast.List):
            return self._list(node, current_klass)
        elif isinstance(node, ast.Dict):
            return self._dict(node, current_klass)
        elif isinstance(node, ast.Tuple):
            return self._tuple(node, current_klass)
        elif isinstance(node, ast.Slice):
            return self._slice(node, current_klass)
        else:
            raise TranslationError("unsupported type (in expr)", node)



import cStringIO

def translate(file_name, module_name, debug=False):
    f = file(file_name, "r")
    src = f.read()
    f.close()
    output = cStringIO.StringIO()
    mod = compiler.parseFile(file_name)
    t = Translator(module_name, module_name, src, debug, mod, output)
    return output.getvalue()


class PlatformParser:
    def __init__(self, platform_dir = ""):
        self.platform_dir = platform_dir
        self.parse_cache = {}
        self.platform = ""

    def setPlatform(self, platform):
        self.platform = platform

    def parseModule(self, module_name, file_name):
        if self.parse_cache.has_key(file_name):
            mod = self.parse_cache[file_name]
        else:
            print "Importing " + module_name
            mod = compiler.parseFile(file_name)
            self.parse_cache[file_name] = mod

        platform_file_name = self.generatePlatformFilename(file_name)
        if self.platform and os.path.isfile(platform_file_name):
            mod = copy.deepcopy(mod)
            mod_override = compiler.parseFile(platform_file_name)
            self.merge(mod, mod_override)

        return mod

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


class AppTranslator:

    def __init__(self, library_dirs=["../library"], parser=None):
        self.extension = ".py"

        self.library_modules = []
        self.library_dirs = library_dirs

        if not parser:
            self.parser = PlatformParser()
        else:
            self.parser = parser

    def findFile(self, file_name):
        if os.path.isfile(file_name):
            return file_name

        if file_name[:8] == 'pyjamas.': # strip off library name
            if file_name != "pyjamas.py":
                file_name = file_name[8:]
        for library_dir in self.library_dirs:
            full_file_name = os.path.join(os.path.dirname(__file__), library_dir, file_name)
            if os.path.isfile(full_file_name):
                return full_file_name

        raise Exception("file not found: " + file_name)

    def translate(self, module_name, is_app=True, debug=False):

        if module_name not in self.library_modules:
            self.library_modules.append(module_name)

        file_name = self.findFile(module_name + self.extension)

        if is_app:
            module_name_translated = ""
        else:
            module_name_translated = module_name

        output = cStringIO.StringIO()

        f = file(file_name, "r")
        src = f.read()
        f.close()

        mod = self.parser.parseModule(module_name, file_name)
        t = Translator(module_name_translated, module_name, src, debug, mod, output)
        module_str = output.getvalue()

        imported_modules_str = ""
        for module in t.imported_modules:
            if module not in self.library_modules:
                imported_modules_str += self.translate(module, False, debug)
        for js in t.imported_js:
           path = self.findFile(js)
           if os.path.isfile(path):
              print 'Including', js
              imported_modules_str += '\n//\n// BEGIN '+js+'\n//\n'
              imported_modules_str += file(path).read()
              imported_modules_str += '\n//\n// END '+js+'\n//\n'
           else:
              print >>sys.stderr, 'Warning: Unable to find imported javascript:', js

        if module_name == 'pyjamas':
            return imported_modules_str
        return imported_modules_str + module_str

    def translateLibraries(self, library_modules=[], debug=False):
        self.library_modules = library_modules

        imported_modules_str = ""
        for library in self.library_modules:
            imported_modules_str += self.translate(library, False, debug)

        return imported_modules_str


if __name__ == "__main__":
    import sys
    file_name = sys.argv[1]
    if len(sys.argv) > 2:
        module_name = sys.argv[2]
    else:
        module_name = None
    print translate(file_name, module_name),
