#!/usr/bin/env python

import re

func_type = {
    'jsmethod': 0,
    'function': 1,
    'staticmethod': 2,
    'classmethod': 3,
    'wrappermethod': 4,
}

short_names = {
    'module': 'm$',
    'globals': 'g$',
    'locals': 'l$',
    'funcbase': 'f$',
    'builtin': 'B$',
    'constants': 'C$',
    'None': 'N$',
    'True': 'T$',
    'False': 'F$',
    'bool': 'b$',
    'booljs': '_b',
    'fcall': '_f',
    'fcallext': '_fe',
    'mcall': '_m',
    'mcallext': '_me',
}


class Replacement(object):
    re_p = re.compile('''[$]{\s*([0-9]+)(\s*,\s*([^,]+?))+\s*}[$]''')

    def substitute(self, src, names):
        def subs(m):
            indent_level = int(m.group(1))
            args = m.group(0)[:-1].split(',')[1:]
            args = [i.strip() for i in m.group(0)[:-2].split(',')[1:]]
            name, args = args[0], args[1:]
            if name in short_names:
                return short_names[name]
            try:
                repl = getattr(self, 'repl_%s' % name, None)(*args)
            except:
                print 'repl name:', name, args
                raise
            lines = ['%s%s' % (
                '    ' * indent_level,
                line,
            ) for line in repl.split('\n')]
            return "\n".join(lines)
        dst = self.re_p.sub(subs, src)
        for name in names:
            if isinstance(names[name], basestring):
                dst = dst.replace('${%s}' % name, names[name])
        return dst

    def repl_g(self):
        # globals
        return short_names['globals']

    def repl_l(self):
        # locals
        return short_names['locals']
        return 'l$'


    def repl_new_bool(self, value, true, false):
        return self.substitute("""
var v = ${value}.valueOf();
switch (v) {
    case null:
    case false:
    case 0:
    case '':
        return ${false};
    case true:
    case 1:
        return ${true};
}
if (typeof v == 'number' || typeof v == 'string') {
    return ${true};
}
if (${value}['$inst'] === true) {
    var mro$, attr, attrs = ['__nonzero__', '__len__'];
    for (var i = 0; i < attrs.length; i++) {
        attr = attrs[i];
${2, getattribute, mro$, v, ${value}, attr}$
        if (typeof v != "undefined") {
${3, bind_method, v, v, ${value}, _meth_src}$
            v = @{{fcall}}(this, null, v, ${value});
            switch (attr) {
                case '__nonzero__':
                    return v.__v ? ${true} : ${false};
                case '__len__':
                    return v.__v != 0 ? ${true} : ${false};
            }
        }
    }
}
return ${true};""", locals())

    def repl_jsmethod(self):
        return str(func_type['jsmethod'])

    def repl_function(self):
        return str(func_type['function'])

    def repl_classmethod(self):
        return str(func_type['classmethod'])

    def repl_staticmethod(self):
        return str(func_type['staticmethod'])

    def repl_wrappermethod(self):
        return str(func_type['wrappermethod'])

    def repl_call_head(self, skip):
        return self.substitute("""\
var rval, f, star = null, dstar = null, named = null, o = obj,
    args = Array.prototype.slice.call(arguments, ${skip}),
    track_len = $pyjs.trackstack.length;
for (var i = 0; i < args.length; i++) {
    if (typeof args[i] == "undefined") {
        return @{{raise}}($new(@{{TypeError}}, B$str("argument " + i + " is undefined")));
    }
}
if (module !== null && lineno !== null) {
    if (module['__class__'] !== @{{module}}) {
        debugger;
    }
    $pyjs.track.lineno = lineno;
    $pyjs.track.module = module;
    $pyjs.trackstack[track_len] = {'lineno': $pyjs.track.lineno, 'module': $pyjs.track.module};
}
if (typeof o == "undefined") {
    //debugger;
    //return ${0,None}$;
    throw "o == 'undefined'";""", locals())

    def repl_call_method(self):
        return self.substitute("""\
} else if (method !== null) {
    if (method['$inst'] === true) {
        o = method;
    } else if (typeof o['$inst'] == 'boolean') {
        // as in getattr
        var mro$;
${2, getattributes, o, obj, method, null}$
    } else {
        o = o[method];
    }""", locals())

    def repl_call_object(self):
        return self.substitute("""\
}
for (;;) {
    switch (o['__class__']) {
        case @{{function}}:
            f = o;
            break;
        case @{{instancemethod}}:
            f = o['im_func'];
            if (o['im_self'] !== null){
                args = [o['im_self']].concat(args);
            } else if (base !== null) {
                args = [base].concat(args);
            } else if (obj['$inst'] === true) {
                args = [obj].concat(args);
            } else {
                if (args.length > 0 && args[0]['$inst'] === true) {
                    // check if args[0].__class__.__mro__ contains im_class
                    var mro = args[0]['__class__']['__mro__'];
                    for (var j = 0; j < mro.length; j++) {
                        if (mro[j] === o['im_class']) {
                            mro = true;
                            break;
                        }
                    }
                    if (mro !== true) {
                        @{{_issubtype}}(o['im_class'], args[0]);
                        return @{{raise}}($new(@{{TypeError}}, B$str(
                            "unbound method " + f.__name__ + "() " +
                            "must be called with " + _typeof(o['im_class']) +
                            " instance as first argument (got " +
                            _typeof(args[0]) + " instance instead)")));
                    }
                    break;
                }
                return @{{raise}}($new(@{{TypeError}}, B$str(
                    "unbound method " + f.__name__ + "()" +
                    " must be called with " + _typeof(o['im_class']) + 
                    " instance as first argument (got nothing instead)")));
            }
            break;
        default:
            if (typeof o != 'function') {
                return @{{raise}}($new(@{{TypeError}}, B$str("javascript '" + typeof obj + "' object is not callable")));
            }
            if (typeof o['$inst'] === "boolean") {
                obj = o;
                method = '__call__';
                //o = o['__call__'];
                o = @{{_getattr}}(obj, method);
            } else if (o['$inst'] === true) {
                o = @{{_getattr}}(obj, method);
            } else {
                f = o;
                break;
            }
            if (typeof o == "undefined") {
                return @{{raise}}($new(@{{TypeError}}, B$str("'" + _typeof(obj) + "' object is not callable")));
            }
            continue
    }
    break;
}""", locals())

    def repl_call_star_dstar(self):
        return self.substitute("""\
named = args.pop();
dstar = args.pop();
star = args.pop();
if (star !== null) {
    if (star instanceof Array) {
        args = args.concat(star);
    } if (star.__array instanceof Array) {
        args = args.concat(star.__array);
    } else {
        var iter = @{{fcall}}(this, null, @{{iter}}, null, star),
            next = @{{getattr}}(iter, 'next'),
            stopiter = @{{stopiter}},
            v;
        for (;;) {
            @{{stopiter}} = true;
            v = @{{fcall}}(this, null, next, iter);
            @{{stopiter}} = stopiter;
            if (v === @{{StopIter}}) {
                break;
            }
            args.push(v);
        }
    }
    star = null;
}
if (named !== null) {
    var k, d = {};
    k = false;
    for (k in named) {
        d[k] = named[k];
    }
    if (k !== false) {
        if (typeof f.func_args == "undefined") {
            @{{raise}}($new(@{{TypeError}}, B$str("Cannot apply named arguments on javascript function")));
        }
        named = d;
    }
}
if (dstar !== null) {
    if (dstar._length == 0) {
        dstar = null;
    } else {
        if (typeof f.func_args == "undefined") {
            @{{raise}}($new(@{{TypeError}}, B$str("Cannot apply dstar args on javascript function")));
        }
        var k, v, d = {};
        if (dstar.__class__ === @{{dict}}) {
            for (var h in dstar.__object_hash) {
                k = dstar.__object_hash[h]['key'];
                if (typeof k != "string" && k.__class__ != @{{str}}) {
                    @{{raise}}($new(@{{TypeError}}, B$str(f.__name__ + "() keywords must be strings")));
                }
                d[k.valueOf()] = dstar.__object[h];
            }
        } else if (dstar['$inst'] == "undefined") {
            for (var k in dstar) {
                d[k] = dstar[k];
            }
        } else {
            @{{raise}}($new(@{{TypeError}}, B$str("Invalid dstar_args")));
        }
        dstar = d;
    }
}
if (dstar !== null || named !== null) {
    var ndefaults = f.func_defaults ? f.func_defaults.length : 0;
    if (dstar === null) {
        dstar = {};
    } else if (named === null) {
        named = {};
    }
    for (var i = 0; i < f.func_args.length; i++) {
        k = f.func_args[i];
        v = named[k];
        delete named[k];
        if (typeof v == "undefined") {
            v = dstar[k];
            delete dstar[k];
        } else if (typeof dstar[k] != "undefined") {
            @{{raise}}($new(@{{TypeError}}, B$str(f.__name__ + "() got multiple values for keyword argument '" + k + "'")));
        }
        if (typeof v != "undefined") {
            if (i < args.length) {
                @{{raise}}($new(@{{TypeError}}, B$str(f.__name__ + "() got multiple values for keyword argument '" + k + "'")));
            }
            args[i] = v;
        } else if (i >= args.length) {
            if (i < f.func_minargs) {
                @{{raise}}($new(@{{TypeError}}, B$str(f.__name__ + "() takes at least " + f.func_minargs + " non-keyword arguments (" + f.func_args.length + " given)")));
            }
            args[i] = f.func_defaults[ndefaults - (f.func_args.length - i)];
        }
    }
    if (f.func_dstarargs === null) {
        for (var k in dstar) {
            @{{raise}}($new(@{{TypeError}}, B$str(f.__name__ + "() got an unexpected keyword argument '" + k + "'")));
        }
    }
    for (k in named) {
        if (typeof dstar[k] != 'undefined') {
            return @{{raise}}($new(@{{TypeError}}, B$str(f.__name__ + "() got multiple values for keyword argument '" + k + "'")));
        }
        dstar[k] = named[k];
    }
    dstar = $new(@{{dict}}, dstar);
}
""", locals())

    def repl_call_tail(self):
        return self.substitute("""\
if (typeof f.func_args != "undefined") {
    var n_args = args.length;
    if (dstar === null && args.length < f.func_args.length) {
        // Just add defaults
        var n = f.func_args.length - args.length;
        if (n > 0 && f.func_defaults !== null) {
            if (n > f.func_defaults.length) {
                args = args.concat(f.func_defaults.slice(0));
            } else {
                n = f.func_defaults.length - n;
                args = args.concat(f.func_defaults.slice(n));
            }
        }
    }
    if (f.func_args.length != args.length) {
        if (f.func_starargs !== null && f.func_args.length < args.length) {
            if (f.func_args.length == 0) {
                star = args;
                args = [];
            } else {
                star = args.slice(f.func_args.length);
                args.splice(f.func_args.length, args.length - f.func_args.length);
            }
            star = B$tuple(star);
        } else if (f.func_defaults === null || f.func_defaults.length == 0) {
            switch (f.func_args.length) {
                case 0:
                    @{{raise}}($new(@{{TypeError}}, B$str(f.__name__ + "() takes no arguments (" + n_args + " given)")));
                case 1:
                    @{{raise}}($new(@{{TypeError}}, B$str(f.__name__ + "() takes exactly " + f.func_args.length + " argument (" + n_args + " given)")));
                default:
                    @{{raise}}($new(@{{TypeError}}, B$str(f.__name__ + "() takes exactly " + f.func_args.length + " arguments (" + n_args + " given)")));
            }
        } else {
            if (f.func_args.length > args.length) {
                if (f.func_minargs == 1) {
                    @{{raise}}($new(@{{TypeError}}, B$str(f.__name__ + "() takes at least 1 argument (0 given)")));
                } else {
                    @{{raise}}($new(@{{TypeError}}, B$str(f.__name__ + "() takes at least " + f.func_minargs + " arguments (" + n_args + " given)")));
                }
            }
            if (f.func_minargs == 1) {
                @{{raise}}($new(@{{TypeError}}, B$str(f.__name__ + "() takes at most 1 argument (" + n_args + " given)")));
            } else {
                @{{raise}}($new(@{{TypeError}}, B$str(f.__name__ + "() takes at most " + f.func_minargs + " arguments (" + n_args + " given)")));
            }
        }
    }
    if (f.func_starargs !== null) {
        if (star === null) {
            //star = B$tuple([]);
            star = empty_tuple;
        }
        args.push(star);
    }
    if (module !== null && lineno !== null) {
        if (typeof f._module != "undefined" && 
            f._module !== null &&
            typeof f._lineno != "undefined" &&
            f._lineno !== null) {
            $pyjs.track.module = f._module;
            $pyjs.track.lineno = f._lineno;
        }
    }
    if (dstar !== null) {
        args.push(dstar);
        args.push(null); // no named args
    } else if (f.func_dstarargs !== null) {
        dstar = B$dict();
        args.push(dstar);
        args.push(null); // no named args
    }
}
if (typeof obj['$inst'] != "undefined" || typeof obj['func_type'] != "undefined") {
    rval = f.apply(module, args);
} else {
    // obj is an ordinary javascript object
    rval = f.apply(obj, args);
}
if (typeof rval == "undefined") {
    if (typeof f['__name__'] == 'undefined') {
        return ${0,None}$;
    } else {
        @{{raise}}($new(@{{ValueError}}, B$str("return value of call is undefined")));
    }
}
if (module !== null && lineno !== null) {
    $pyjs.track = $pyjs.trackstack[track_len];
    $pyjs.trackstack.splice(track_len, $pyjs.trackstack.length);
    if (typeof $pyjs.track == "undefined" || $pyjs.track.lineno != lineno || $pyjs.track.module !== module) {
        debugger;
    }
}
return rval;""", locals())

    def repl___new__(self, instance, cls, add_dict=True):
        if add_dict is not True:
            if add_dict.lower().strip() == 'false':
                add_dict = False
            else:
                add_dict = True
        if add_dict:
            add_dict = """
if (typeof ${cls} == "undefined") {
    debugger;
}
if (typeof ${cls}['__slots__'] == "undefined" || ${cls}['__slots__'].length > 0) {
    ${instance}['__dict__'] = B$dict();
    ${instance}['$dict'] = ${instance}['__dict__']['__object'];
}"""
        else:
            add_dict = ''
        return self.substitute("""\
var ${instance} = function ( ) {
    var args = Array.prototype.slice.call(arguments);
    if (arguments.callee['__class__'] === @{{instancemethod}}) {
        if (arguments.callee['im_self'] !== null) {
            return @{{fcall}}.apply(this, [this, null, arguments.callee['im_func'], null, arguments.callee['im_self']].concat(args));
        }
    }
    var a = @{{_getattr}}(arguments.callee, '__call__');
    if (typeof a == "undefined") {
        @{{raise}}($new(@{{TypeError}}, B$str("'" + _typeof(arguments.callee) + "' object is not callable")));
    }
    if (args.length >= 3) {
        var len = args.length;
        if ((args[len-3] === null || args[len-3]['__class__'] === @{{tuple}}) &&
            (args[len-2] === null || args[len-3]['__class__'] === @{{dict}}) &&
            (args[len-1] === null || typeof args[len-1]['__class__'] == "undefined")) {
            return @{{fcallext}}.apply(this, [this, null, a, arguments.callee].concat(args));
        }
    }
    return @{{fcall}}.apply(this, [this, null, a, arguments.callee].concat(args));
}
${instance}['toString'] = function ( ) {
    try {
        return @{{mcall}}(this, null, this, '__str__').valueOf();
    } catch (e) {
    }
    try {
        return "<" + this.__class__.__name__ + " instance>";
    } catch (e) {
    }
    return "<instance>";
};
${instance}['$inst'] = true;%(add_dict)s
${instance}['__class__'] = ${cls};""" % locals(), locals())

    def repl_create_instance(self, args, cls, mcall, fcall):
        return self.substitute("""\
var method$, instance, mro$, module = this['__class__'] === @{{module}} ? this : null;
${0, getattribute, mro$, method$, ${cls}, '__new__'}$
if (method$ === B$__new__) {
${1, __new__, instance, ${cls}}$
} else {
    instance = ${fcall}.apply(module, [module, null, method$, ${cls}, ${cls}].concat(${args}));
}
if (instance['$inst'] === true) {
${1, getattribute, mro$, method$, ${cls}, '__init__'}$
    if (method$ !== B$__init__) {
${2, bind_method, method$, method$, instance, _meth_src}$
        var ret = ${fcall}.apply(module, [module, null, method$, null].concat(${args}));
        if (ret !== @{{None}} && ret !== null) {
            if (ret['__class__'] != "undefined") {
                return @{{raise}}($new(@{{TypeError}}, B$str("__init__() should return None, not '" + ret['__class__']['__name__'] + "'")));
            }
            return @{{raise}}($new(@{{TypeError}}, B$str("__init__() should return None")));
        }
    }
}
return instance;""", locals())

    def repl_bind_method(self, dst, src, obj, meth_src):
        return self.substitute("""\
if (${meth_src}['$inst'] === false && ${obj}['__class__'] !== @{{module}} && typeof ${src} != "undefined" && typeof ${src}['$inst'] != "undefined") {
    switch (${dst}['__class__']) {
        case @{{function}}:
${3, __new__, _new_dst$, @{{instancemethod}}}$
            _new_dst$['im_class'] = ${obj}['$inst'] === true ? ${obj}['__class__'] : ${obj};
            _new_dst$['im_func'] = ${dst};
            _new_dst$['im_self'] = ${obj}['$inst'] === true ? ${obj} : null;
            ${dst} = _new_dst$;
            break;
        case @{{staticmethod}}:
            ${dst} = ${dst}['im_func'];
            break;
        case @{{classmethod}}:
${3, __new__, _new_dst$, @{{instancemethod}}}$
            _new_dst$['im_class'] = ${obj}['$inst'] === true ? ${obj}['__class__'] : ${obj};
            _new_dst$['im_func'] = ${dst}['im_func'];
            _new_dst$['im_self'] = ${obj}['$inst'] === true ? ${obj}['__class__'] : ${obj};
            ${dst} = _new_dst$;
            break;
        case @{{bool}}: // Some known to be non-descriptors
        case @{{int}}:
        case @{{long}}:
        case @{{str}}:
            break;
        default:
            // check for __get__ method in ${dst}
            if (${dst}['$inst'] === true) {
                var get$ = @{{_getattr}}(${dst}, '__get__');
                if (typeof get$ != 'undefined') {
                    ${dst} = @{{fcall}}(this, null, get$, ${dst}, ${obj}, ${obj}['__class__']);
                }
            }
            break;
    }
}""", locals())

    def repl_attr_args_validate(self, _self, name):
        return self.substitute("""\
if ($self['$inst'] !== true) {
    @{{raise}}($new(@{{TypeError}}, B$str("can't apply this __getattribute__ to type object")));
}
if (${name}['__class__'] !== @{{str}} && typeof ${name} != 'string') {
    @{{raise}}($new(@{{TypeError}}, B$str("attribute name must be string")));
}""", locals())

    def repl_getattribute(self, mro, dst, src, name, break_after_instance=False):
        if break_after_instance:
            break_after_instance = 'break;\n        '
        else:
            break_after_instance = ''
        return self.substitute("""\
${dst} = [][1];
var ${mro} = ${src}['__mro__'];
var _meth_src = ${src};
switch (${src}['$inst']) {
    case true:
        if (${src}['__class__'] === @{{module}}) {
            ${dst} = ${src}['$dict'][${name}];
            break;
        } else if (${src}['__class__'] === @{{function}}) {
            switch (${name}.charAt(0)) {
                case 'i':
                case '_':
                    ${dst} = ${src}[${name}];
            }
            break;
        }
        var _noraise$ = @{{noraise}};
        var ga;
        ${mro} = ${src}['__class__']['__mro__'];
        for (var mro_i$ = 0; mro_i$ < ${mro}.length - 1; mro_i$++) {
            var _mro$ = ${mro}[mro_i$];
            var ga = _mro$['__getattribute__'];
            if (typeof ga == "undefined") {
                if (typeof _mro$ == "undefined" || typeof _mro$['$dict']['__getattribute__'] == "undefined") {
                    continue;
                }
                ga = _mro$['$dict']['__getattribute__'];
            }
${3, bind_method, ga, ${src}, ${src}, ${src}['__class__']}$
            @{{noraise}} = @{{AttributeError}};
            ${dst} = @{{fcall}}(this, null, ga, _mro$, ${name});
            @{{noraise}} = _noraise$;
            if (${dst} === @{{AttributeError}}) {
                ${dst} = [][1];
            }
            _meth_src = ${src}['__class__'];
            ${src} = ${src}['__class__'];
            break;
        }
        if (typeof ${dst} == "undefined") {
            if (typeof ${src}['$dict'] != "undefined") {
                ${dst} = ${src}['$dict'][${name}];
                if (typeof ${dst} != "undefined") {
                    if (${dst} !== {}[${name}]) {
                        break;
                    }
                    ${dst} = [][1];
                }
            }
            switch (${name}.charAt(0)) {
                case 'i':
                case '_':
                    ${dst} = ${src}[${name}];
            }
            if (typeof ${dst} != "undefined") {
                break;
            }
        }${break_after_instance}
    case false:
        if (typeof ${dst} == "undefined") {
            var _mro$, ga;
            if (${src}['$inst'] === true) {
                _meth_src = ${src}['__class__'];
            } else {
                switch (${name}.charAt(0)) {
                    case 'i':
                    case '_':
                        ${dst} = ${src}[${name}];
                }
                if (typeof ${dst} != "undefined") {
                    break;
                }
                
            }
            if (typeof ${dst} == "undefined") {
                for (var mro_i$ = 0; mro_i$ < ${mro}.length; mro_i$++) {
                    _mro$ = ${mro}[mro_i$];
                    ${dst} = _mro$['$dict'][${name}];
                    if (typeof ${dst} != "undefined") {
                        if (${dst} !== {}[${name}]) {
                            break;
                        }
                        ${dst} = [][1];
                    }
                    switch (${name}.charAt(0)) {
                        case 'i':
                        case '_':
                            ${dst} = _mro$[${name}];
                    }
                    if (typeof ${dst} != "undefined") {
                        break;
                    }
                }
            }
            if (typeof ${dst} == "undefined" && ${name} !== '__get__') {
                for (var mro_i$ = 0; mro_i$ < ${mro}.length - 1; mro_i$++) {
                    _mro$ = ${mro}[mro_i$];
                    if (typeof _mro$['$dict'] == "undefined" || typeof _mro$['$dict']['__getattr__'] == "undefined") {
                        continue;
                    }
                    ga = _mro$['$dict']['__getattr__'];
${5, bind_method, ga, ${src}, ${src}, ${src}['__class__']}$
                    @{{noraise}} = @{{AttributeError}};
                    ${dst} = @{{fcall}}(this, null, ga, _mro$, ${name});
                    @{{noraise}} = _noraise$;
                    if (${dst} === @{{AttributeError}}) {
                        ${dst} = [][1];
                    }
                    // TODO : unbind ${dst} ?
                    break;
                }
            }
        }
        break;
    default:
        ${dst} = ${src}[${name}];
        if (typeof ${dst} == "undefined" && typeof ${src}['$dict'] != "undefined") {
            ${dst} = ${src}['$dict'][${name}];
        }
}""", locals())

    def repl_getattributes(self, dst, src, name, value):
        return self.substitute("""\
var attrname, attrnames, ga, mro, _${src} = ${src};
if (${name} instanceof Array) {
    attrnames = ${name};
} else {
    attrnames = [${name}];
}
find_attr:
for (var attri = 0; attri < attrnames.length; attri++) {
    attrname = attrnames[attri];
    if (typeof attrname != 'string') {
        if (typeof attrname['__s'] != "undefined") {
            attrname = attrname['__s'];
        } else {
            @{{raise}}($new(@{{TypeError}}, B$str("attribute name must be string, not '" + _typeof(attrname) + "'")));
        }
    }
${1, getattribute, mro, ${dst}, _${src}, attrname}$
    if (typeof ${dst} == "undefined") {
        if (_${src}['$inst'] === true && _${src}['__class__'] !== @{{module}} && _${src}['__class__'] !== @{{function}}) {
            if (typeof ${dst} == "undefined") {
                if (${value} === null || typeof ${value} == "undefined") {
                    @{{raise}}($new(@{{AttributeError}}, B$str("'" + _${src}['__class__']['__name__'] + "' object has no attribute '" + attrname + "'")));
                } else {
                    ${dst} = ${value};
                    break find_attr;
                }
            }
        }
        if (${value} === null || typeof ${value} == "undefined") {
            if (_${src}['$inst'] === false) {
                @{{raise}}($new(@{{AttributeError}}, B$str("type object '" + _${src}['__name__'] + "' object has no attribute '" + attrname + "'")));
            }
            @{{raise}}($new(@{{AttributeError}}, B$str(attrname)));
        }
        ${dst} = ${value};
        break find_attr;
    }
    if (attri == attrnames.length - 1) {
${2, bind_method, ${dst}, _${src}, ${src}, _meth_src}$
    } else {
        // check for __get__ method in ${dst}
        if (${dst}['$inst'] === true) {
            var get$ = @{{_getattr}}(${dst}, '__get__');
            if (typeof get$ != 'undefined') {
                ${dst} = @{{fcall}}(this, null, get$, ${dst}, _${src}, _${src}['__class__']);
            }
        }
    }
    ${src} = _${src};
    _${src} = ${dst};
}""", locals())

    def repl_type_class(self, cls, module, clsname, bases, dict):
        return self.substitute("""\
var ${cls},
    mro$ = new Array(),
    _bases = ${bases};
    ${cls} = function () {
        var args = Array.prototype.slice.call(arguments);
        if (args.length >= 3) {
            var len = args.length;
            if ((args[len-3] === null || args[len-3]['__class__'] === @{{tuple}}) &&
                (args[len-2] === null || args[len-3]['__class__'] === @{{dict}}) &&
                (args[len-1] === null || typeof args[len-1]['__class__'] == "undefined")) {
                return $newext.apply(this, [arguments.callee].concat(args));
            }
        }
        return $new.apply(this, [arguments.callee].concat(args));
};
${cls}['$inst'] = false;
${cls}['__name__'] = typeof ${clsname} == "string" ? B$str(${clsname}) : ${clsname};
if (${bases} instanceof Array) {
    ${cls}['__bases__'] = B$tuple(${bases});
} else {
    ${cls}['__bases__'] = ${bases};
    _bases = ${bases}['__array'];
}
if (typeof ${dict}['mro'] != "undefined") {
    // The mro method (?) exists. Use that.
    // TODO
    @{{raise}}(@{{NotImplemented}});
} else {
    for (var i = 0; i < _bases.length; i++) {
        mro$.push(new Array().concat(_bases[i].__mro__));
    }
    ${cls}['__mro__'] = [${cls}].concat(mro_merge(mro$));
}
${cls}['$dict'] = {};
if (${module}['__class__'] !== @{{module}}) {
    debugger;
}
var __module__ = typeof ${module}['$dict'] != "undefined" ? ${module}['$dict']['__name__'] : ${module}['__name__'];
if (typeof __module__ != "undefined") {
    cls['$dict']['__module__'] = __module__;
}
if (typeof ${dict} != "undefined" && ${dict}['__class__'] === @{{dict}}) {
    for (var k in ${dict}.__object) {
        cls['$dict'][k] = ${dict}.__object[k];
    }
}
${cls}['__dict__'] = @{{dictproxy}};
${cls}['__dict__']['__object'] = ${cls}['$dict'];
func(${0,module}$, null, ${cls}, '__call__', ${0, classmethod}$, null, 'args', 'kwargs', null, $newext, true);
${cls}['__class__'] = @{{type}};""", locals())

    def repl_hash(self, obj, dst):
        return self.substitute("""\
if (typeof ${obj}['$inst'] != "undefined") {
    ${dst} = ${obj}[$hash_id_name$];
    if (typeof ${dst} == "undefined") {
        if (${obj}['__class__'] === @{{str}}) {
            ${dst} = ${obj}['__s'].charAt(0) == '#' ? '#string#' + ${obj}['__s'] : ${obj}['__s'];
        } else {
            ${dst} = @{{mcall}}(this, null, ${obj}, '__hash__');
        }
    }
} else if (typeof ${obj} == "string") {
    ${dst} = ${obj}.charAt(0) == '#' ? '#string#' + ${obj} : ${obj};
} else {
    ${dst} = '#' + typeof ${obj} + '#' + ${obj};
}""" % locals(), locals())

    def repl_op_compare(self, op, a, b, val1, val2):
        if op in ['is', 'is_not']:
            return self.substitute("""\
if (${a} === ${b}) {
    return ${val1};
}
if (${a} !== null && ${b} !== null) {
    switch ((${a}.__number__ << 8) | ${b}.__number__) {
        case 0x0101:
            return ${a} == ${b} ? ${val1} : ${val2};
        case 0x0202:
            return $a.__v == $b.__v ? ${val1} : ${val2};
        case 0x0404:
            return @{{long}}['$dict'].__cmp__(${a}, ${b}) == 0 ? ${val1} : ${val2};
    }
}
return ${val2}""" % locals(), locals())

        if op in ['in', 'not_in']:
            return self.substitute("""\
var i, mro$;
${0, getattribute, mro$, i, ${b}, '__contains__'}$
if (typeof i != "undefined") {
${1, bind_method, i, i, ${b}, _meth_src}$
    return @{{fcall}}(this, null, i,  ${b}, ${a}).valueOf() ? ${val1} : ${val2};
}
var __iter__ = @{{iter}}(${b});
var $stopiter = @{{stopiter}}
for (;;) {
    @{{stopiter}} = true;
    i = @{{mcall}}(this, null, __iter__, 'next');
    @{{stopiter}} = $stopiter;
    if (i === @{{StopIter}}) {
        return ${val2};
    }
    if (@{{op_eq}}(i, ${a})) {
        return ${val1};
    }
}
""" % locals(), locals())

        valnull = '${val2}'
        if not '=' in op:
            opis = ''
        elif op == '!=':
            opis = 'if (${a} === ${b}) return ${val2};\n'
            valnull = '${val1}'
        else:
            opis = 'if (${a} === ${b}) return ${val1};\n'
        opis = ''
        return self.substitute("""\
%(opis)sif (${a} !== null && ${b} !== null) {
    switch ((${a}.__number__ << 8) | ${b}.__number__) {
        case 0x0101:
        case 0x0401:
            return ${a}.valueOf() ${op} ${b}.valueOf() ? ${val1} : ${val2};
        case 0x0102:
            return ${a}.valueOf() ${op} ${b}.__v ? ${val1} : ${val2};
        case 0x0201:
            return ${a}.__v ${op} ${b}.valueOf() ? ${val1} : ${val2};
        case 0x0202:
            return ${a}.__v ${op} ${b}.__v ? ${val1} : ${val2};
        case 0x0104:
        case 0x0204:
            ${a} = $new(@{{long}}, ${a}.valueOf());
        case 0x0404:
            if (${a}['__class__'] !== @{{long}}) break;
            return @{{long}}['$dict']['__cmp__'](${a}, ${b}).valueOf() ${op} 0 ? ${val1} : ${val2};
        case 0x0402:
            if (${a}['__class__'] !== @{{long}}) break;
            return @{{long}}['$dict']['__cmp__'](${a}, $new(@{{long}}, ${b}.valueOf())).valueOf() ${op} 0 ? ${val1} : ${val2};
    }
    var v = @{{fcall}}(this, null, @{{cmp}}, null, ${a}, ${b}).valueOf();
    return v === null ? %(valnull)s : (v ${op} 0 ? ${val1} : ${val2});
}
return ${val2};""" % locals(), locals())

    def repl_op_arithmetic(self, op, opname, x, y, i, opfunc=None):
        
        jsop = op
        if opfunc is None:
            opnumber = "x_v %s y_v" % op
        elif opfunc == 'Math.floor':
            jsop = '/'
            opnumber = "%s(x_v %s y_v)" % (opfunc, jsop)
        elif opfunc == 'mod':
            opnumber = "x_v %s y_v" % op
            opnumber = "(x_v=x_v %s y_v) < 0 && y_v > 0 ? x_v + y_v : x_v" % op
        else:
            opnumber = "%s(x_v, y_v)" % opfunc
        if op in ['/', '//', '%']:
            zerodiv = "if (${y}.valueOf() == 0) return @{{raise}}($new(@{{ZeroDivisionError}}, B$str('float divmod()')));\n";
        else:
            zerodiv = ''
        return self.substitute("""\
%(zerodiv)sif (${x} !== null && ${y} !== null) {
    var m = ${i} === true ? '__i%(opname)s__' : '__%(opname)s__';
    switch ((${x}.__number__ << 8) | ${y}.__number__) {
        case 0x0101:
        case 0x0102:
        case 0x0201:
        case 0x0104:
        case 0x0401:
            var x_v = ${x}.valueOf(), y_v = ${y}.valueOf();
            return $new(@{{float}}, %(opnumber)s);
        case 0x0202:
            return @{{int}}['$dict'].__%(opname)s__(${x}, ${y});
        case 0x0204:
            return @{{long}}['$dict'].__%(opname)s($new(@{{long}}, ${x}.__v), ${y});
        case 0x0402:
            return @{{long}}['$dict'].__%(opname)s(${x}, $new(@{{long}}, ${y}.__v));
        case 0x0404:
            return @{{long}}['$dict'].__%(opname)s(${x}, ${y});
    }
    if (${x}['$inst'] === true && ${y}['$inst'] === true) {
        var op, v;
        op = @{{_getattr}}(${x}, m);
        if (typeof op != "undefined") {
            v = @{{fcall}}(this, null, op, ${x}, ${y});
            if (v !== @{{NotImplemented}}) {
                return v;
            }
        }
        if (${i} !== true) {
            op = @{{_getattr}}(${y}, '__r%(opname)s__');
            if (typeof op != "undefined") {
                v = @{{mcall}}(this, null, ${y}, '__r%(opname)s__', ${x});
                if (v !== @{{NotImplemented}}) {
                    return v;
                }
            }
        } else {
            op = @{{_getattr}}(${x}, '__%(opname)s__');
            if (typeof op != "undefined") {
                v = @{{fcall}}(this, null, op, ${x}, ${y});
                if (v !== @{{NotImplemented}}) {
                    return v;
                }
            }
        }
    }
    var x_v = ${x}.valueOf(), y_v = ${y}.valueOf();
    if (typeof x_v == 'number' && typeof y_v == 'number') {
        return $new(@{{float}}, %(opnumber)s);
    }
}
@{{raise}}($new(@{{TypeError}}, B$str("unsupported operand type(s) for %(op)s: '" + @{{repr}}(${x}) + "', '" + @{{repr}}(${y}) + "'")));\
""" % locals(), locals())

    def repl_op_bitexpr2(self, op, opname, x, y):
        return self.substitute("""\
if (${x} !== null && ${y} !== null) {
    switch ((${x}.__number__ << 8) | ${y}.__number__) {
        case 0x0202:
            if (${x}['__class__'] === @{{int}}) {
                return ${x}['__class__']['$dict']['__%(opname)s__'](${x}, ${y});
            }
            break
        case 0x0204:
            if (${y}['__class__'] === @{{long}}) {
                return ${y}['__class__']['$dict']['__r%(opname)s__'](${y}, $new(@{{long}}, ${x}));
            }
            break
        case 0x0402:
            if (${x}['__class__'] === @{{long}}) {
                return ${x}['__class__']['$dict']['__%(opname)s'](${x}, $new(@{{long}}, ${y}.__v));
            }
            break
        case 0x0404:
            if (${x}['__class__'] === @{{long}}) {
                return ${x}['__class__']['$dict']['__%(opname)s'](${x}, ${y});
            }
            break
    }
    var v = @{{_getattr}}(${x}, '__%(opname)s__');
    if (typeof v != "undefined") {
        v = @{{fcall}}(this, null, v, ${x}, ${y});
        if (v !== @{{NotImplemented}}) {
            return v;
        }
    }
    v = @{{_getattr}}(${y}, '__r%(opname)s__');
    if (typeof v != "undefined") {
        v = @{{fcall}}(this, null, v, ${y}, ${x});
        if (v !== @{{NotImplemented}}) {
            return v;
        }
    }
}
@{{raise}}($new(@{{TypeError}}, @{{sprintf}}("unsupported operand type(s) for %(op)s: '%%r', '%%r'", [${x}, ${y}])));\
""" % locals(), locals())

    def repl_op_bitexpr(self, op, opname, args):
        return self.substitute("""\
var a;
if (args[0] !== null && args[1] !== null && args.length > 1) {
    var v, r, arg;
    v = args[0];
    for (var i = 1; i < args.length; i++) {
        arg = args[i]
        r = @{{_getattr}}(v, '__%(opname)s__');
        if (typeof r != "undefined") {
            r = @{{fcall}}(this, null, r, v, arg);
            if (r !== @{{NotImplemented}}) {
                v = r;
                continue;
            }
        }
        r = @{{_getattr}}(arg, '__r%(opname)s__');
        if (typeof r != "undefined") {
            r = @{{fcall}}(this, null, r, arg, v);
            if (r !== @{{NotImplemented}}) {
                v = r;
                continue;
            }
        }
        v = null;
        break;
    }
    if (v !== null) {
        return v;
    }
}
var msg = "unsupported operand type(s) for %(op)s: "
for (var i = 0; i < args.length; i++) {
    msg += @{{repr}}(args[i]);
}
@{{raise}}($new(@{{TypeError}}, B$str(msg)));\
""" % locals(), locals())

    def repl_op_iexpr(self, op, opname, x, y):
        return self.substitute("""\
@{{raise}}($new(@{{TypeError}}, B$str(msg)));\
""" % locals(), locals())



if __name__ == '__main__':
    import sys
    if not sys.argv[1:]:
        src = open("__builtin__.py.in", 'r').read()
        dst = Replacement().substitute(src, {})
        open("__builtin__.py", 'w').write(dst)
    else:
        src = open(sys.argv[1], 'r').read()
        dst = Replacement().substitute(src, {})
        print dst
        #open("pyjslib.py", 'w').write(dst)
