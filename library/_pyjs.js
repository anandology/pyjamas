function pyjs_extend(klass, base) {
    function klass_object_inherit() {}
    klass_object_inherit.prototype = base.prototype;
    klass_object = new klass_object_inherit();
    for (var i in base.prototype.__class__) {
        v = base.prototype.__class__[i];
        if (typeof v == "function" && (v.class_method || v.static_method || v.unbound_method))
        {
            klass_object[i] = v;
        }
    }

    function klass_inherit() {}
    klass_inherit.prototype = klass_object;
    klass.prototype = new klass_inherit();
    klass_object.constructor = klass;
    klass.prototype.__class__ = klass_object;

    for (var i in base.prototype) {
        v = base.prototype[i];
        if (typeof v == "function" && v.instance_method)
        {
            klass.prototype[i] = v;
        }
    }
}

function pyjs_kwargs_call(obj, func, star_args, args)
{
    var call_args;

    if (star_args)
    {
        if (!pyjslib.isIteratable(star_args))
        {
            throw (pyjslib.TypeError(func.__name__ + "() arguments after * must be a sequence" + pyjslib.repr(star_args)));
        }
        call_args = Array();
        var __i = star_args.__iter__();
        var i = 0;
        try {
            while (true) {
                call_args[i]=__i.next();
                i++;
            }
        } catch (e) {
            if (e != StopIteration) {
                throw e;
            }
        }

        if (args)
        {
            var n = star_args.length;
            for (var i=0; i < args.length; i++) {
                call_args[n+i]=args[i];
            }
        }
    }
    else
    {
        call_args = args;
    }
    return func.apply(obj, call_args);
}

function pyjs_kwargs_function_call(func, star_args, args)
{
    return pyjs_kwargs_call(null, func, star_args, args);
}

function pyjs_kwargs_method_call(obj, method_name, star_args, args)
{
    var method = obj[method_name];
    if (method.parse_kwargs)
    {
        args = method.parse_kwargs.apply(null, args);
    }
    return pyjs_kwargs_call(obj, method, star_args, args);
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

var str = String;

