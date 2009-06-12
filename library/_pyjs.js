
function pyjs_args_merge(func, star_args, dstar_args, args)
{
    var call_args;

    if (star_args) {
        if (!pyjslib.isIteratable(star_args)) {
            throw (pyjslib.TypeError(func.__name__ + "() arguments after * must be a sequence" + pyjslib.repr(star_args)));
        }
        if (star_args.l != null && star_args.l.constructor == Array) {
            call_args = args.concat(star_args.l);
        } else {
            call_args = Array();
            var __i = star_args.__iter__();
            var i = 0;
            try {
                while (true) {
                    call_args[i]=__i.next();
                    i++;
                }
            } catch (e) {
                if (e != pyjslib.StopIteration) {
                    throw e;
                }
            }
            call_args = args.concat(call_args);
        }
    }
    else
    {
        call_args = args;
    }
    if (dstar_args) {
        if (pyjslib.get_pyjs_classtype(dstar_args) != 'Dict') {
            throw (pyjslib.TypeError(func.__name__ + "() arguments after ** must be a dictionary " + pyjslib.repr(dstar_args)));
        }
        var __i = dstar_args.__iter__();
        try {
            while (true) {
                var i = __i.next();
                if (pyjs_options.arg_kwarg_multiple_values && typeof call_args[0][i] != 'undefined') {
                    pyjs__exception_func_multiple_values(func.__name__, i);
                }
                call_args[0][i] = dstar_args.__getitem__(i)
            }
        } catch (e) {
            if (e != pyjslib.StopIteration) {
                throw e;
            }
        }

    }
    return call_args;
}

function pyjs_kwargs_function_call(func, star_args, dstar_args, args)
{
    args = pyjs_args_merge(func, star_args, dstar_args, args);
    if (func.parse_kwargs) {
        args = func.parse_kwargs.apply(null, args);
    } else if (pyjs_options.arg_kwarg_unexpected_keyword && args.length > 0) {
        for (var i in args[0]) {
            pyjs__exception_func_unexpected_keyword(func.__name__, i);
        }
    }
    return func.apply(null, args);
}

function pyjs_kwargs_method_call(obj, method_name, star_args, dstar_args, args)
{
    var method = obj[method_name];
    args = pyjs_args_merge(method, star_args, dstar_args, args);
    if (method.parse_kwargs)
    {
        args = method.parse_kwargs.apply(null, args);
    } else if (pyjs_options.arg_kwarg_unexpected_keyword && args.length > 0) {
        for (var i in args[0]) {
            pyjs__exception_func_unexpected_keyword(method.__name__, i);
        }
    }
    return method.apply(obj, args);
}

function pyjs__exception_func_param(func_name, minargs, maxargs, nargs) {
    if (minargs == maxargs) {
        switch (minargs) {
            case 0:
                var msg = func_name + "() takes no arguments (" + nargs + " given)";
                break;
            case 1:
                msg = func_name + "() takes exactly " + minargs + " argument (" + nargs + " given)";
                break;
            default:
                msg = func_name + "() takes exactly " + minargs + " arguments (" + nargs + " given)";
        };
    } else if (nargs > maxargs) {
        if (maxargs == 1) {
            msg  = func_name + "() takes at most " + maxargs + " argument (" + nargs + " given)";
        } else {
            msg = func_name + "() takes at most " + maxargs + " arguments (" + nargs + " given)";
        }
    } else if (nargs < minargs) {
        if (minargs == 1) {
            msg = func_name + "() takes at least " + minargs + " argument (" + nargs + " given)";
        } else {
            msg = func_name + "() takes at least " + minargs + " arguments (" + nargs + " given)";
        }
    } else {
        return;
    }
    //throw msg
    throw pyjslib.TypeError(String(msg));
}

function pyjs__exception_func_multiple_values(func_name, key) {
    //throw func_name + "() got multiple values for keyword argument '" + key + "'";
    throw pyjslib.TypeError(String(func_name + "() got multiple values for keyword argument '" + key + "'"));
}

function pyjs__exception_func_unexpected_keyword(func_name, key) {
    //throw func_name + "() got an unexpected keyword argument '" + key + "'";
    throw pyjslib.TypeError(String(func_name + "() got an unexpected keyword argument '" + key + "'"));
}

function pyjs__exception_func_class_expected(func_name, class_name, instance) {
        if (typeof instance == 'undefined') {
            instance = 'nothing';
        } else if (instance.__is_instance__ == null) {
            instance = "'"+String(instance)+"'";
        } else {
            instance = String(instance);
        }
        //throw "unbound method "+func_name+"() must be called with "+class_name+" class as first argument (got "+instance+" instead)";
        throw pyjslib.TypeError(String("unbound method "+func_name+"() must be called with "+class_name+" class as first argument (got "+instance+" instead)"));
}

function pyjs__exception_func_instance_expected(func_name, class_name, instance) {
        if (typeof instance == 'undefined') {
            instance = 'nothing';
        } else if (instance.__is_instance__ == null) {
            instance = "'"+String(instance)+"'";
        } else {
            instance = String(instance);
        }
        //throw "unbound method "+func_name+"() must be called with "+class_name+" instance as first argument (got "+instance+" instead)";
        throw pyjslib.TypeError(String("unbound method "+func_name+"() must be called with "+class_name+" instance as first argument (got "+instance+" instead)"));
}

function pyjs__bind_method(klass, func_name, func, parse_kwargs) {
    func.__name__ = func.func_name = func_name;
    func.__class__ = klass;
    func.prototype = func;
    if (typeof parse_kwargs != 'undefined') func.parse_kwargs = parse_kwargs;
    return func;
}
function pyjs__instancemethod(klass, func_name, func, parse_kwargs) {
    var fn = function () {
        var _this = this;
        var argstart = 0;
        if (this.__is_instance__ !== true && arguments.length > 0) {
            _this = arguments[0];
            argstart = 1;
        }
        var args = new Array(_this);
        for (var a=argstart;a < arguments.length; a++) args.push(arguments[a]);
        if (pyjs_options.arg_is_instance) {
            if (_this.__is_instance__ === true) {
                if (pyjs_options.arg_instance_type) return func.apply(this, args);
                for (var c in _this.__mro__) {
                    var cls = _this.__mro__[c];
                    if (cls == klass) {
                        return func.apply(this, args);
                    }
                }
            }
            pyjs__exception_func_instance_expected(func_name, klass.__name__, _this);
        }
        return func.apply(this, args);
    };
    func.__name__ = func.func_name = func_name;
    func.__class__ = klass;
    if (typeof parse_kwargs != 'undefined') func.parse_kwargs = parse_kwargs;
    return fn;
}

function pyjs__staticmethod(klass, func_name, func, parse_kwargs) {
    func.__name__ = func.func_name = func_name;
    func.__class__ = klass;
    if (typeof parse_kwargs != 'undefined') func.parse_kwargs = parse_kwargs;
    return func;
}

function pyjs__classmethod(klass, func_name, func, parse_kwargs) {
    var fn = function () {
        if (pyjs_options.arg_is_instance && this.__is_instance__ !== true && this.__is_instance__ !== false) pyjs__exception_func_instance_expected(func_name, klass.__name__);
        var args = new Array(this.prototype);
        for (var a=0;a < arguments.length; a++) args.push(arguments[a]);
        return func.apply(this, args);
    };
    func.__name__ = func.func_name = func_name;
    func.__class__ = klass;
    if (typeof parse_kwargs != 'undefined') func.parse_kwargs = parse_kwargs;
    return fn;
}

function pyjs__subclasses__(cls_obj) {
    return cls_obj.__sub_classes__;
}

function pyjs__mro_merge(seqs) {
    var res = new Array();
    var i = 0;
    var cand = null;
    function resolve_error(candidates) {
        //throw "Cannot create a consistent method resolution order (MRO) for bases " + candidates[0].__name__ + ", "+ candidates[1].__name__;
        throw (pyjslib.TypeError("Cannot create a consistent method resolution order (MRO) for bases " + candidates[0].__name__ + ", "+ candidates[1].__name__));
    }
    for (;;) {
        var nonemptyseqs = new Array();
        for (var j = 0; j < seqs.length; j++) {
            if (seqs[j].length > 0) nonemptyseqs.push(seqs[j]);
        }
        if (nonemptyseqs.length == 0) return res;
        i++;
        var candidates = new Array();
        for (var j = 0; j < nonemptyseqs.length; j++) {
            cand = nonemptyseqs[j][0];
            candidates.push(cand);
            var nothead = new Array();
            for (var k = 0; k < nonemptyseqs.length; k++) {
                for (var m = 1; m < nonemptyseqs[k].length; m++) {
                    if (cand == nonemptyseqs[k][m]) {
                        nothead.push(nonemptyseqs[k]);
                    }
                }
            }
            if (nothead.length != 0)
                cand = null; // reject candidate
            else
                break;
        }
        if (cand == null) {
            resolve_error(candidates);
        }
        res.push(cand);
        for (var j = 0; j < nonemptyseqs.length; j++) {
            if (nonemptyseqs[j][0] == cand) {
                nonemptyseqs[j].shift();
            }
        }
    }
}

function pyjs__class_instance(class_name, module_name) {
    if (typeof module_name == 'undefined') module_name = typeof __mod_name__ == 'undefined' ? '__main__' : __mod_name__;
    var cls_fn = function(){
        var instance = cls_fn.__new__.apply(null, [cls_fn]);
        if (instance.__init__) {
            if (instance.__init__.apply(instance, arguments) != null) {
                //throw '__init__() should return None';
                throw pyjslib.TypeError('__init__() should return None');
            }
        }
        return instance;
    }
    cls_fn.__name__ = class_name;
    cls_fn.__module__ = module_name;
    cls_fn.toString = function() { return (this.__is_instance__ === true ? "instance of " : "class ") + (this.__module__?this.__module__ + "." : "") + this.__name__;}
    return cls_fn;
}

function pyjs__class_function(cls_fn, prop, bases) {
    if (typeof cls_fn != 'function') throw "compiler error? pyjs__class_function: typeof cls_fn != 'function'";
    var class_name = cls_fn.__name__;
    var class_module = cls_fn.__module__;
    var base_mro_list = new Array()
    for (var i = 0; i < bases.length; i++) {
        if (bases[i].__mro__ != null) {
            base_mro_list.push(new Array().concat(bases[i].__mro__));
        }
    }
    var __mro__ = pyjs__mro_merge(base_mro_list);

    for (var b = __mro__.length-1; b >= 0; b--) {
        var base = __mro__[b];
        for (var p in base) cls_fn[p] = base[p];
    }
    for (var p in prop) cls_fn[p] = prop[p];

    if (prop.__new__ == null) {
        cls_fn.__new__ = pyjs__bind_method(cls_fn, '__new__', function(cls) {
    var instance = function () {};
    instance.prototype = arguments[0].prototype;
    instance = new instance();
    instance.__dict__ = instance.__class__ = instance;
    instance.__is_instance__ = true;
    return instance;
}, function (__kwargs, cls) {
    if (typeof cls == 'undefined') {
        cls=__kwargs.cls;
        delete __kwargs.cls;
    } else if (pyjs_options.arg_kwarg_multiple_values && typeof __kwargs.cls != 'undefined') {
        pyjs__exception_func_multiple_values('__new__', 'cls');
    }
    if (pyjs_options.arg_kwarg_unexpected_keyword) {
        for (var i in __kwargs) {
            pyjs__exception_func_unexpected_keyword('__new__', i);
        }
    }
    var __r = [cls];
    for (var pyjs__va_arg = 2;pyjs__va_arg < arguments.length;pyjs__va_arg++) {
        __r.push(arguments[pyjs__va_arg]);
    }

    return __r;
});

    }
    if (cls_fn['__init__'] == null) {
        cls_fn['__init__'] = pyjs__bind_method(cls_fn, '__init__', function () {
    if (this.__is_instance__ === true) {
        var self = this;
        if (pyjs_options.arg_count && arguments.length != 0) pyjs__exception_func_param(arguments.callee.__name__, 1, 1, arguments.length+1);
    } else {
        var self = arguments[0];
        if (pyjs_options.arg_is_instance && self.__is_instance__ !== true) pyjs__exception_func_instance_expected(arguments.callee.__name__, arguments.callee.__class__.__name__, self);
        if (pyjs_options.arg_count && arguments.length != 1) pyjs__exception_func_param(arguments.callee.__name__, 1, 1, arguments.length);
    }
    if (pyjs_options.arg_instance_type) {
        if (arguments.callee !== arguments.callee.__class__[arguments.callee.__name__]) {
            if (!pyjslib._isinstance(self, arguments.callee.__class__.slice(1))) {
                pyjs__exception_func_instance_expected(arguments.callee.__name__, arguments.callee.__class__.__name__, self);
            }
        }
    }
}, function (__kwargs) {
    var __r = [];
    return __r;
});
    }
    cls_fn.__name__ = class_name;
    cls_fn.__module__ = class_module;
    //cls_fn.__mro__ = pyjslib.List(new Array(cls_fn).concat(__mro__));
    cls_fn.__mro__ = new Array(cls_fn).concat(__mro__);
    cls_fn.prototype = cls_fn;
    cls_fn.__dict__ = cls_fn;
    cls_fn.__is_instance__ = false;
    cls_fn.__super_classes__ = bases;
    cls_fn.__sub_classes__ = new Array();
    for (var i = 0; i < bases.length; i++) {
        (bases[i]).__sub_classes__.push(cls_fn);
    }
    cls_fn.parse_kwargs = function () {
        return cls_fn.__init__.parse_kwargs.apply(null, arguments);
    }
    return cls_fn;
}

/* creates a class, derived from bases, with methods and variables */
function pyjs_type(clsname, bases, methods)
{
    var cls_instance = pyjs__class_instance(clsname);
    var obj = new Object;
    for (var i in methods) {
        if (typeof methods[i] == 'function') {
            obj[i] = pyjs__instancemethod(cls_instance, i, methods[i], methods[i].parse_kwargs);
        } else {
            obj[i] = methods[i];
        }
    }
    return pyjs__class_function(cls_instance, obj, bases);
}

String.prototype.__getitem__ = String.prototype.charAt;
String.prototype.upper = String.prototype.toUpperCase;
String.prototype.lower = String.prototype.toLowerCase;
String.prototype.find=pyjslib.String_find;
String.prototype.join=pyjslib.String_join;
String.prototype.isdigit=pyjslib.String_isdigit;
String.prototype.__iter__=pyjslib.String___iter__;

String.prototype.__replace=String.prototype.replace;
String.prototype.replace=pyjslib.String_replace;

String.prototype.split=pyjslib.String_split;
String.prototype.strip=pyjslib.String_strip;
String.prototype.lstrip=pyjslib.String_lstrip;
String.prototype.rstrip=pyjslib.String_rstrip;
String.prototype.startswith=pyjslib.String_startswith;
String.prototype.endswith=pyjslib.String_endswith;
String.prototype.ljust=pyjslib.String_ljust;
String.prototype.rjust=pyjslib.String_rjust;
String.prototype.center=pyjslib.String_center;

var str = String;

