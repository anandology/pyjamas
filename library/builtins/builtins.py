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
#
# Contributions:
#   - iteration from Bob Ippolito's Iteration in JavaScript
#   - python object orientation emulation by Lluis Pamies-Juarez


#
# Pyjamas internal functions
# Used to keep python objects.
#

def ___tojs___(code):
    pass

___tojs___('''
if(!__window) {
    __window = window;
    __navigator = navigator;
    __screen = screen;
    __history = history;
    __location = location;
    __document = document;
}

function __default_value(func, var_name, value) {
    if(!func.__pyjamasdefaults__) {
        func.__pyjamasdefaults__ = {};
    }
    if(!func.__pyjamasdefaults__[var_name]){
        func.__pyjamasdefaults__[var_name] = value;
    }
    return func.__pyjamasdefaults__[var_name];
}

function __class_inheritance(klass) {
    for(var i=0; i<klass.__bases__.length; i++) {
        var base = klass.__bases__[i];
        for(var attr in base) {
            if(!klass[attr]) {
                klass[attr] = base[attr];
            }
        }
    }
}

function __args_check(args,kargs,pos,name,_default,func) {
    if(typeof(args[pos])!='undefined') {
        return args[pos];
    }else if(typeof(kargs[name])!='undefined') {
        return kargs[name];
    }else if(typeof(_default)!='undefined') {
        if(func) {
            return __default_value(func,name,_default);
        }else{
            return _default;
        }
    }else{
        throw "Incorrect arguments ("+name+")";
    }
}

function __class_method(klass, name, method) {
    method.__pyjamasclass__ = klass
    method.__name__ = name
    klass[name] = method
    if(typeof(klass.__jsclass__)!='undefined') {
        klass.__jsclass__.prototype[name] = function(args,kargs) {
            args.unshift(this);
            return method(args, kargs);
        };
    }
}

function __create_class(name, bases, wrap) {
    function method_wrap(method, obj) {
        return function(iargs, ikargs) {
            iargs.unshift(obj);
            return method(iargs,ikargs);
        };
    }
    var klass = function(){};

    var constructor = function(args,kargs) {
        var k = klass.__pyjamasclass__;
        if(name=='str') {
            var o = args[0];
        }else{
            var o = function(){};
        }
        for(var method_name in k) {
            var method = k[method_name];
            if(typeof(method)=='function') {
                if(method.classmethod) {
                    o[method_name] = method
                } else if (name != 'str') {
                    o[method_name] = method_wrap(method, o);
                }
            }
        }
        if (name == 'str') {
            return o;
        };
        o.__class__ = k;
        o.__dict__ = o;
        if(k.__init__) {
            args.unshift(o);
            k.__init__(args,kargs);
        }
        return o;
    };

    constructor['__init__'] = function(args,kargs) {
        if(bases[0]) bases[0].__init__(args,kargs);
    };

    klass.__pyjamasclass__ = constructor;
    constructor.__jsclass__ = wrap;
    constructor.__name__ = name;
    constructor.__bases__ = bases;
    constructor.__dict__ = constructor;
    return constructor;
}

function __sprintf(str, args) {
    if(typeof(args)=='string') var args = [args]
    var re = /([^%]*)%('.|0|\x20)?(-)?(\d+)?(\.\d+)?(%|b|c|d|u|f|o|s|x|X)(.*)/;
    var a = b = [], numSubstitutions = 0, numMatches = 0;
    while (a = re.exec(str)) {
        var leftpart = a[1], pPad = a[2], pJustify = a[3], pMinLength = a[4];
        var pPrecision = a[5], pType = a[6], rightPart = a[7];
        
        numMatches++;
        if (pType == '%') {
            subst = '%';
        } else {
            numSubstitutions++;
            if (numSubstitutions >= args.length+1) {
                __print(['Error! Not enough function arguments !'],{});
            }
            var param = args[numSubstitutions-1];
            var pad = '';
            if (pPad && pPad.substr(0,1) == "'") pad = leftpart.substr(1,1);
            else if (pPad) pad = pPad;
            var justifyRight = 1;
            if (pJustify && pJustify === "-") justifyRight = 0;
            var minLength = -1;
            if (pMinLength) minLength = parseInt(pMinLength);
            var precision = -1;
            if (pPrecision && pType == 'f') precision = parseInt(pPrecision.substring(1));
            var subst = param;
            if (pType == 'b') subst = parseInt(param).toString(2);
            else if (pType == 'c') subst = String.fromCharCode(parseInt(param));
            else if (pType == 'd') subst = parseInt(param) ? parseInt(param) : 0;
            else if (pType == 'u') subst = Math.abs(param);
            else if (pType == 'f') subst = (precision > -1) ? Math.round(parseFloat(param) * Math.pow(10, precision)) / Math.pow(10, precision): parseFloat(param);
            else if (pType == 'o') subst = parseInt(param).toString(8);
            else if (pType == 's') subst = param;
            else if (pType == 'x') subst = ('' + parseInt(param).toString(16)).toLowerCase();
            else if (pType == 'X') subst = ('' + parseInt(param).toString(16)).toUpperCase();
        }
        str = leftpart + subst + rightPart;
    }
    return str;
}
''')

#
# Builtin Javascript Functions and types
# Depecrated !!!
#   Since all javascript code comes from python,
#   this functions are never used directly.
#

def decodeURI(s):
    ___tojs___('''
    return decodeURI(s);
    ''')
    
def decodeURIComponent(s):
    ___tojs___('''
    return decodeURIComponent(s);
    ''')

def encodeURI(s):
    ___tojs___('''
    return encodeURI(s);
    ''')

def encodeURIComponent(s):
    ___tojs___('''
    return encodeURIComponent(s);
    ''')

def escape(s):
    ___tojs___('''
    return escape(s);
    ''')

def unescape(s):
    ___tojs___('''
    return unescape(s);
    ''')

def parseInt(num, radix):
    ___tojs___('''
    return parseInt(num, radix);
    ''')

#
# Python builtin types
#

class object:
    def __getattr__(self, item):
        return self.__dict__[item]
    
    def __settattr__(self, item, value):
        self.__dict__[item] = value

str = None
def _str_upper(self):
    ___tojs___('''
    return self.toUpperCase();
    ''')

def _str_lower(self):
    ___tojs___('''
    return self.toLowerCase();
    ''')

def _str_find(self, sub, start, end):
    ___tojs___('''
    var pos=self.indexOf(sub, start);
    if (__isUndefined([end],{})) return pos;

    if (pos + sub.length>end) return -1;
    return pos;
    ''')

def _str_join(self, data):
    ___tojs___('''
    var text="";
    
    if (__isArray([data],{})) {
        return data.join(self);
    }
    else if (__isIteratable([data],{})) {
        var iter=data.__iter__([],{});
        try {
            text+=iter.next([],{});
            while (1) {
                var item=iter.next();
                text+=self + item;
            }
        }
        catch (e) {
            if (e != '__stop_iteration') throw e;
        }
    }

    return text;
    ''')

def _str_replace(self, old, replace, count=None):
    ___tojs___('''
    var do_max=0;
    var start=0;
    var new_str="";
    var pos=0;
    
    if (!__isString([old],{})) return self.__replace(old, replace);
    if (!__isNull([count],{})) do_max=1;
    
    while (start<self.length) {
        if (do_max && !count--) break;
        
        pos=self.indexOf(old, start);
        if (pos<0) break;
        
        new_str+=self.substring(start, pos) + replace;
        start=pos+old.length;
    }
    if (start<self.length) new_str+=self.substring(start);

    return new_str;
    ''')

def _str_split(self, sep, maxsplit):
    ___tojs___('''
    var items = [];
    var do_max=0;
    var subject=self;
    var start=0;
    var pos=0;
    
    if (__isUndefined([sep],{}) || __isNull([sep],{})) {
        sep=" ";
        subject=subject.strip();
        subject=subject.replace(/\s+/g, sep);
    }
    else if (!__isUndefined([maxsplit],{})) do_max=1;

    while (start<subject.length) {
        if (do_max && !maxsplit--) break;
    
        pos=subject.indexOf(sep, start);
        if (pos<0) break;
        
        items.append(subject.substring(start, pos));
        start=pos+sep.length;
    }
    if (start<subject.length) items.append(subject.substring(start));
    
    return items;
    ''')

def _str_strip(self, chars):
    ___tojs___('''
    return self.lstrip(chars).rstrip(chars);
    ''')

def _str_lstrip(self, chars):
    ___tojs___('''
    if (__isUndefined([chars],{})) return self.replace(/^\s+/, "");

    return self.replace(new RegExp("^[" + chars + "]+"), "");
    ''')

def _str_rstrip(self, chars):
    ___tojs___('''
    if (__isUndefined([chars],{})) return self.replace(/\s+$/, "");

    return self.replace(new RegExp("[" + chars + "]+$"), "");
    ''')

def _str_startswith(self, prefix, start):
    ___tojs___('''
    if (__isUndefined([start],{})) start = 0;

    if (self.substring(start, prefix.length) == prefix) return 1;
    return 0;
    ''')

def _str___getitem__(self, key):
    #TODO: Check string length
    ___tojs___('''
    return self.charAt(key)
    ''')

___tojs___('''
var str = __create_class('str',[], String);
__class_method(str, 'upper', _str_upper)
__class_method(str, 'lower', _str_lower)
__class_method(str, 'split', _str_split)
__class_method(str, 'replace', _str_replace)
__class_method(str, 'find', _str_find)
__class_method(str, 'join', _str_join)
__class_method(str, 'strip', _str_strip)
__class_method(str, 'lstrip', _str_lstrip)
__class_method(str, 'rstrip', _str_rstrip)
__class_method(str, 'startswith', _str_startswith)
__class_method(str, '__getitem__', _str___getitem__)
''')


list = None
def _list___init__(self, data=None):
    ___tojs___("""
    if (__isArray([data],{})) {
        for (var i=0; i < data.length; i++) {
            self[i]=data[i];
        }
    } else if (__isIteratable([data],{})) {
        var iter=data.__iter__([],{});
        var i=0;
        try {
            while (1) {
                var item=iter.next();
                self[i++]=item;
            }
        }
        catch (e) {
            if (e != '__stop_iteration') throw e;
        }
    }
    """)

def _list___getitem__(self, index):
    ___tojs___("""
    if (index<0) index = self.length + index;
    if(__isUndefined([self[index]],{})){
        return null;
    }else{
        return self[index];
    }
    """)

def _list___setitem__(self, index, value):
    ___tojs___("""
    if (index<0) index = self.length + index;
    self[index]=value;
    """)

def _list___delitem__(self, index):
    ___tojs___("""
    self.splice(index, 1);
    """)

def _list___len__(self):
    ___tojs___("""
    return self.length;
    """)

def _list___contains__(self, value):
    return self.index(value) >= 0

def _list___iter__(self):
    ___tojs___("""
    var i = 0;
    var l = self;
    
    return {
        'next': function() {
            if (i >= l.length) {
                throw('__stop_iteration');
            }
            return l[i++];
        },
        '__iter__': function() {
            return self;
        }
    };
    """)
   
def _list_append(self, item):
    ___tojs___("""
    self[self.length] = item;
    """)

def _list_index(self, value, start=0):
    ___tojs___("""
    for (var i=start; i<self.length; i++) {
        if (self[i]==value) {
            return i;
        }
    }
    return -1;
    """)

def _list_insert(self, index, value):
    ___tojs___("""
    self.splice(index, 0, value)
    """)

def _list_pop(self, index=-1):
    ___tojs___("""
    if (index<0) index = self.length + index;
    var a = self[index];
    self.splice(index, 1);
    return a;
    """)

def _list_remove(self, value):
    ___tojs___("""
    var index=self.index(value);
    if (index<0) return 0;
    self.splice(index, 1);
    return 1;
    """)

def _list_sort(self, compareFunc=None, keyFunc=None, reverse=False):
    if not compareFunc:
        global cmp
        compareFunc = cmp
    if keyFunc and reverse:
        def selfSort1(a,b):
            return -compareFunc(keyFunc(a), keyFunc(b))
        self.sort(selfSort1)
    elif keyFunc:
        def selfSort2(a,b):
            return compareFunc(keyFunc(a), keyFunc(b))
        self.sort(selfSort2)
    elif reverse:
        def selfSort3(a,b):
            return -compareFunc(a, b)
        self.sort(selfSort3)
    else:
        self.sort(compareFunc)

___tojs___('''
var list = __create_class('list',[], Array);
__class_method(list, 'sort', _list_sort)
__class_method(list, 'remove', _list_remove)
__class_method(list, 'pop', _list_pop)
__class_method(list, 'insert', _list_insert)
__class_method(list, 'index', _list_index)
__class_method(list, 'append', _list_append)
__class_method(list, '__len__', _list___len__)
__class_method(list, '__init__', _list___init__)
__class_method(list, '__iter__', _list___iter__)
__class_method(list, '__delitem__', _list___delitem__)
__class_method(list, '__getitem__', _list___getitem__)
__class_method(list, '__setitem__', _list___setitem__)
__class_method(list, '__contains__', _list___contains__)
Array.prototype.__class__ = list;
''')

tuple = None
___tojs___('''
var tuple = __create_class('tuple',[]);
''')

set = None
___tojs___('''
var set = __create_class('set',[]);
''')

dict = None
def _dict___init__(self, data=None):
    ___tojs___("""
    if (__isArray([data],{})) {
        for (var i in data) {
            var item=data[i];
            self[item[0]]=item[1];
        }
    } else if (__isIteratable([data],{})) {
        var iter=data.__iter__([],{});
        try {
            while (1) {
                var item=iter.next();
                self[item.__getitem__([0],{})]=item.__getitem__([1],{});
            }
        }
        catch (e) {
            if (e != '__stop_iteration') throw e;
        }
    } else if (__isObject([data],{})) {
        for (var key in data) {
            self[key]=data[key];
        }
    }
    """)

def _dict___setitem__(self, key, value):
    ___tojs___(""" self[key]=value;""")

def _dict___getitem__(self, key):
    ___tojs___("""
    if(typeof self[key] == 'undefined') {
        return null;
    }else{
        return self[key];
    }
    """)

def _dict___len__(self):
    ___tojs___("""
    var size=0;
    for (var i in self) size++;
    return size;
    """)

def _dict_has_key(self, key):
    ___tojs___("""
    if (typeof self[key] == 'undefined') return 0;
    return 1;
    """)

def _dict___delitem__(self, key):
    ___tojs___(""" delete self[key];""")

def _dict___contains__(self, key):
    ___tojs___("""    return (__isUndefined([self.__getitem__([key])],{})) ? 0 : 1;""")

def _dict_keys(self):
    ___tojs___("""
    var keys = [];
    for (var key in self) keys.append([key]);
    return keys;
    """)

def _dict_values(self):
    ___tojs___("""
    var keys = list([],{});
    for (var key in self) keys.append([self[key]]);
    return keys;
    """)
    
def _dict___iter__(self):
    ___tojs___("""
    return self.keys([],{}).__iter__([],{});
    """)

def _dict_iterkeys(self):
    ___tojs___("""
    return self.keys([],{}).__iter__([],{});
    """)

def _dict_itervalues(self):
    ___tojs___("""
    return self.values().__iter__();
    return self.values([],{}).__iter__([],{});
    """)

def _dict_iteritems(self):
    ___tojs___("""
    var d = self;
    var iter=self.keys([],{}).__iter__([],{});
    
    return {
        '__iter__': function() {
            return self;
        },

        'next': function() {
            var key;
            while (key=iter.next()) {
                var item = list([],{});
                item.append([key]);
                item.append([d[key]]);
                return item;
            }
        }
    };
    """)
    
def _dict_setdefault(self, key, default_value): 
    if not self.has_key(key):
        self[key] = default_value
    return self[key]

def _dict_get(self, key, default_value=None):    
    value = self[key]
    ___tojs___("if(__isUndefined([value],{})) { value = default_value; }")
    return value;

def _dict_update(self, d):
    for k,v in d.iteritems():
        self[k] = v

___tojs___('''
var dict = __create_class('dict',[], Object);
__class_method(dict, 'update', _dict_update);
__class_method(dict, 'get', _dict_get);
__class_method(dict, 'setdefault', _dict_setdefault);
__class_method(dict, 'iteritems', _dict_iteritems);
__class_method(dict, 'itervalues', _dict_itervalues);
__class_method(dict, 'iterkeys', _dict_iterkeys);
__class_method(dict, '__iter__', _dict___iter__);
__class_method(dict, 'values', _dict_values);
__class_method(dict, 'keys', _dict_keys);
__class_method(dict, '__contains__', _dict___contains__);
__class_method(dict, '__delitem__', _dict___delitem__);
__class_method(dict, 'has_key', _dict_has_key);
__class_method(dict, '__len__', _dict___len__);
__class_method(dict, '__getitem__', _dict___getitem__);
__class_method(dict, '__setitem__', _dict___setitem__);
__class_method(dict, '__init__', _dict___init__);
Object.prototype.__class__ = dict;
''')

class BaseException:
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

    def __repr__(self):
        return self.msg

class Exception(BaseException):
    pass

def float(str):
    ___tojs___('''
    return parseFloat(str);
    ''')

def int(str):
    ___tojs___('''
    return parseInt(str);
    ''')

def classmethod(func):
    ___tojs___('''
    var func = __args_check(args,kargs,0,'func');
    function inner(args, kargs) {
        args.unshift(func.__pyjamasclass__)
        return func(args,kargs);
    }
    inner.classmethod = 1;
    return inner;
    ''')

def staticmethod(func):
    return func

def isinstance(obj, klass):
    ___tojs___('''
    if(obj.__class__ == klass) return 1;

    var bases = obj.__class__.__bases__.splice(0,obj.__class__.__bases__.length);
    while(bases.length > 0) {
        var base = bases.shift();
        if(klass == base) return 1;
        bases = bases.concat(base.__bases__);
    }
    return 0;
    ''')
         
def cmp(a,b):
    if hasattr(a, "__cmp__"):
        return a.__cmp__(b)
    elif hasattr(a, "__cmp__"):
        return -b.__cmp__(a)
    if a > b:
        return 1
    elif b > a:
        return -1
    else:
        return 0

# taken from mochikit: range( [start,] stop[, step] )
def range(*args):
    ___tojs___("""
    var start = 0;
    var stop = 0;
    var step = 1;

    if (args.length == 2) {
        start = args[0];
        stop = args[1];
        }
    else if (args.length == 3) {
        start = args[0];
        stop = args[1];
        step = args[2];
        }
    else if (args.length>0) stop = args[0];

    return {
        'next': function() {
            if ((step > 0 && start >= stop) || (step < 0 && start <= stop)) throw('__stop_iteration');
            var rval = start;
            start += step;
            return rval;
            },
        '__iter__': function() {
            return this;
            }
        }
    """)

def slice(object, lower, upper):
    ___tojs___("""
    if (__isString([object],{})) {
        if (__isNull([upper],{})) upper=object.length;
        return object.substring([lower, upper],{});
        }
    if (__isObject([object],{}) && object.slice) return object.slice([lower, upper],{});
    
    return null;
    """)

def abs(num):
    ___tojs___("""
    return Math.abs(num);
    """)

def int(text, radix=0):
    ___tojs___("""
    return parseInt(text, radix);
    """)

def round(number, ndigits=0):
    ___tojs___("""
    return parseFloat(number.toFixed(ndigits));
    """)

def len(obj):
    ___tojs___("""
    if (obj==null) return 0;
    if (__isObject([obj],{}) && obj.__len__) return obj.__len__([],{});
    return obj.length;
    """)

def getattr(obj, method):
    ___tojs___("""
    if (!__isObject([obj],{})) return null;
    if (!__isFunction([obj[method]],{})) return obj[method];

    return function() {
        obj[method].call(obj);
    };
    """)

def hasattr(obj, method):
    ___tojs___("""
    if (!__isObject([obj],{})) return 0;
    if (__isUndefined([obj.__getitem__([method])],{})) return 0;

    return 1;
    """)

def dir(obj):
    ___tojs___("""
    var properties = list([],{})
    for (property in obj) properties.append([property]);
    return properties;
    """)

def filter(obj, method, sequence=None):
    # object context is LOST when a method is passed, hence object must be passed separately
    # to emulate python behaviour, should generate this code inline rather than as a function call
    items = []
    if sequence == None:
        sequence = method
        method = obj

        for item in sequence:
            if method(item):
                items.append(item)
    else:
        for item in sequence:
            if method.call(obj, item):
                items.append(item)

    return items


def map(obj, method, sequence=None):
    items = []
    
    if sequence == None:
        sequence = method
        method = obj
        
        for item in sequence:
            items.append(method(item))
    else:
        for item in sequence:
            items.append(method.call(obj, item))
    
    return items


__next_hash_id = 0

def hash(obj):
    ___tojs___("""
    if (obj == null) return null;
    
    if (obj.$H) return obj.$H;
    if (obj.__hash__) return obj.__hash__();
    if (obj.constructor == String || obj.constructor == Number || obj.constructor == Date) return obj;
    
    obj.$H = ++__next_hash_id;
    return obj.$H;
    """)


# type functions from Douglas Crockford's Remedial Javascript: http://www.crockford.com/javascript/remedial.html
def __isObject(a):
    ___tojs___("""
    return (a && typeof a == 'object') || __isFunction([a],{});
    """)

def __isFunction(a):
    ___tojs___("""
    return typeof a == 'function';
    """)

def __isString(a):
    ___tojs___("""
    return typeof a == 'string';
    """)

def __isNull(a):
    ___tojs___("""
    return typeof a == 'object' && !a;
    """)

def __isArray(a):
    ___tojs___("""
    return __isObject([a],{}) && a.constructor == Array;
    """)

def __isUndefined(a):
    ___tojs___("""
    return typeof a == 'undefined';
    """)

def __isIteratable(a):
    ___tojs___("""
    return __isObject([a],{}) && a.__iter__;
    """)

def __isNumber(a):
    ___tojs___("""
    return typeof a == 'number' && isFinite([a]);
    """)

def __toJSObjects(x):
    """
       Convert the pyjs pythonic List and Dict objects into javascript Object and Array
       objects, recursively.
    """
    result = x
   
    if __isObject(x) and x.__class__:
        if x.__class__ == dict:
            return __toJSObjects(x)
        elif x.__class__ == list:
            return __toJSObjects(x)
   
    if __isObject(x):
        ___tojs___("""
        result = {};
        for(var k in x) {
           var v = x[k];
           var tv = __toJSObjects([v])
           result[k] = tv;
        }
        """)
    if __isArray(x):
        ___tojs___("""
        result = [];
        for(var k=0; k < x.length; k++) {
           var v = x[k];
           var tv = __toJSObjects([v]);
           result.push(tv);
        }
        """)
        
    return result


def __print(*objs):
    ___tojs___("""
    var s = "";
    for(var i=0; i < objs.length; i++) {
        if(s != "") s += " ";
        if(objs[i].__str__) s+= objs[i].__str__([],{});
        else s+= objs[i];

    }
    alert(s);
    //console.debug(s)
    //print(s);
    """)
