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

function pyjs_kwargs_function_call(func, args)
{
    return func.apply(null, func.parse_kwargs.apply(null, args));
}

function pyjs_kwargs_method_call(obj, method_name, args)
{
    var method = obj[method_name];
    return method.apply(obj, method.parse_kwargs.apply(null, args));
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

