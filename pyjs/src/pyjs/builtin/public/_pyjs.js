
function pyjs_kwargs_call(obj, func, star_args, dstar_args, args)
{
    if (obj !== null) {
        func = obj[func];
    }

    // Merge dstar_args into args[0]
    if (dstar_args) {
        if (pyjslib.get_pyjs_classtype(dstar_args) != 'Dict') {
            throw (pyjslib.TypeError(func.__name__ + "() arguments after ** must be a dictionary " + pyjslib.repr(dstar_args)));
        }
        var __i = dstar_args.__iter__();
        try {
            while (true) {
                var i = __i.next();
                if ($pyjs.options.arg_kwarg_multiple_values && typeof args[0][i] != 'undefined') {
                    pyjs__exception_func_multiple_values(func.__name__, i);
                }
                args[0][i] = dstar_args.__getitem__(i)
            }
        } catch (e) {
            if (e != pyjslib.StopIteration) {
                throw e;
            }
        }

    }

    // Append star_args to args
    if (star_args) {
        if (!pyjslib.isIteratable(star_args)) {
            throw (pyjslib.TypeError(func.__name__ + "() arguments after * must be a sequence" + pyjslib.repr(star_args)));
        }
        if (star_args.l != null && star_args.l.constructor == Array) {
            args = args.concat(star_args.l);
        } else {
            var call_args = Array();
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
            args = args.concat(call_args);
        }
    }

    // Now convert args to call_args
    // args = __kwargs, arg1, arg2, ...
    // _args = arg1, arg2, arg3, ... [*args, [**kwargs]]
    var _args = [];

    // Get function/method arguments
    if (typeof func.__args__ != 'undefined') {
        var __args__ = func.__args__;
    } else {
        var __args__ = new Array(null, null);
    }

    var a, aname, _idx , idx;
    _idx = idx = 1;
    if (obj === null) {
        if (func.__is_instance__ === false) {
            // Skip first argument in __args__
            _idx ++;
        }
    } else {
        if (typeof obj.__is_instance__ == 'undefined' && typeof func.__is_instance__ != 'undefined' && func.__is_instance__ === false) {
            // Skip first argument in __args__
            _idx ++;
        } else if (func.__bind_type__ > 0) {
            if (typeof args[1] == 'undefined' || obj.__is_instance__ !== false || args[1].__is_instance__ !== true) {
                // Skip first argument in __args__
                _idx ++;
            }
        }
    }
    for (++_idx; _idx < __args__.length; _idx++, idx++) {
        aname = __args__[_idx];
        a = args[0][aname];
        if (typeof args[idx] == 'undefined') {
            _args.push(a);
            delete args[0][aname];
        } else {
            if (typeof a != 'undefined') pyjs__exception_func_multiple_values(func.__name__, aname);
            _args.push(args[idx]);
        }
    }

    // Append the left-over args
    for (;idx < args.length;idx++) {
            _args.push(args[idx]);
    }

    if (__args__[1] === null) {
        // Check for unexpected keyword
        for (var kwname in args[0]) {
            pyjs__exception_func_unexpected_keyword(func.__name__, kwname);
        }
    } else {
        _args.push(pyjslib.Dict(args[0]));
    }
    return func.apply(obj, _args);
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
    if (typeof pyjslib.TypeError == 'function') {
        throw pyjslib.TypeError(String(msg));
    }
    throw msg
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

function pyjs__bind_method(klass, func_name, func, bind_type, args) {
    func.__name__ = func.func_name = func_name;
    func.__bind_type__ = bind_type;
    func.__args__ = args;
    func.__class__ = klass;
    func.prototype = func;
    return func;
}
function pyjs__instancemethod(klass, func_name, func, bind_type, args) {
    var fn = function () {
        var _this = this;
        var argstart = 0;
        if (this.__is_instance__ !== true && arguments.length > 0) {
            _this = arguments[0];
            argstart = 1;
        }
        var args = new Array(_this);
        for (var a=argstart;a < arguments.length; a++) args.push(arguments[a]);
        if ($pyjs.options.arg_is_instance) {
            if (_this.__is_instance__ === true) {
                if ($pyjs.options.arg_instance_type) return func.apply(this, args);
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
    func.__bind_type__ = bind_type;
    func.__args__ = args;
    func.__class__ = klass;
    return fn;
}

function pyjs__staticmethod(klass, func_name, func, bind_type, args) {
    func.__name__ = func.func_name = func_name;
    func.__bind_type__ = bind_type;
    func.__args__ = args;
    func.__class__ = klass;
    return func;
}

function pyjs__classmethod(klass, func_name, func, bind_type, args) {
    var fn = function () {
        if ($pyjs.options.arg_is_instance && this.__is_instance__ !== true && this.__is_instance__ !== false) pyjs__exception_func_instance_expected(func_name, klass.__name__);
        var args = new Array(this.prototype);
        for (var a=0;a < arguments.length; a++) args.push(arguments[a]);
        return func.apply(this, args);
    };
    func.__name__ = func.func_name = func_name;
    func.__bind_type__ = bind_type;
    func.__args__ = args;
    func.__class__ = klass;
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
}, 1, ['cls']);
    }
    if (cls_fn['__init__'] == null) {
        cls_fn['__init__'] = pyjs__bind_method(cls_fn, '__init__', function () {
    if (this.__is_instance__ === true) {
        var self = this;
        if ($pyjs.options.arg_count && arguments.length != 0) pyjs__exception_func_param(arguments.callee.__name__, 1, 1, arguments.length+1);
    } else {
        var self = arguments[0];
        if ($pyjs.options.arg_is_instance && self.__is_instance__ !== true) pyjs__exception_func_instance_expected(arguments.callee.__name__, arguments.callee.__class__.__name__, self);
        if ($pyjs.options.arg_count && arguments.length != 1) pyjs__exception_func_param(arguments.callee.__name__, 1, 1, arguments.length);
    }
    if ($pyjs.options.arg_instance_type) {
        if (arguments.callee !== arguments.callee.__class__[arguments.callee.__name__]) {
            if (!pyjslib._isinstance(self, arguments.callee.__class__.slice(1))) {
                pyjs__exception_func_instance_expected(arguments.callee.__name__, arguments.callee.__class__.__name__, self);
            }
        }
    }
}, 0, ['self']);
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
    cls_fn.__args__ = cls_fn.__init__.__args__;
    return cls_fn;
}

/* creates a class, derived from bases, with methods and variables */
function pyjs_type(clsname, bases, methods)
{
    var cls_instance = pyjs__class_instance(clsname);
    var obj = new Object;
    for (var i in methods) {
        if (typeof methods[i] == 'function') {
            obj[i] = pyjs__instancemethod(cls_instance, i, methods[i], methods[i].__bind_type__, methods[i].__args__);
        } else {
            obj[i] = methods[i];
        }
    }
    return pyjs__class_function(cls_instance, obj, bases);
}

