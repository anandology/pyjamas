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


# iteration from Bob Ippolito's Iteration in JavaScript
# pyjs_extend from Kevin Lindsey's Inteheritance Tutorial (http://www.kevlindev.com/tutorials/javascript/inheritance/)
from __pyjamas__ import JS

JS("""
StopIteration = function () {};
StopIteration.prototype = new Error();
StopIteration.name = 'StopIteration';
StopIteration.message = 'StopIteration';

KeyError = function () {};
KeyError.prototype = new Error();
KeyError.name = 'KeyError';
KeyError.message = 'KeyError';

AttributeError = function () {};
AttributeError.name = 'KeyError';
AttributeError.message = 'KeyError';
AttributeError.prototype.toString = function () {
   return "AttributeError";
}

TypeError = function () {};
TypeError.prototype = new Error();
TypeError.name = "TypeError";
TypeError.message = "TypeError";

function pyjslib_String_find(sub, start, end) {
    var pos=this.indexOf(sub, start);
    if (pyjslib_isUndefined(end)) return pos;

    if (pos + sub.length>end) return -1;
    return pos;
}

function pyjslib_String_join(data) {
    var text="";

    if (pyjslib_isArray(data)) {
        return data.join(this);
    }
    else if (pyjslib_isIteratable(data)) {
        var iter=data.__iter__();
        try {
            text+=iter.next();
            while (true) {
                var item=iter.next();
                text+=this + item;
            }
        }
        catch (e) {
            if (e != StopIteration) throw e;
        }
    }

    return text;
}

function pyjslib_String_replace(old, replace, count) {
    var do_max=false;
    var start=0;
    var new_str="";
    var pos=0;

    if (!pyjslib_isString(old)) return this.__replace(old, replace);
    if (!pyjslib_isUndefined(count)) do_max=true;

    while (start<this.length) {
        if (do_max && !count--) break;

        pos=this.indexOf(old, start);
        if (pos<0) break;

        new_str+=this.substring(start, pos) + replace;
        start=pos+old.length;
    }
    if (start<this.length) new_str+=this.substring(start);

    return new_str;
}

function pyjslib_String_split(sep, maxsplit) {
    var items=new pyjslib_List();
    var do_max=false;
    var subject=this;
    var start=0;
    var pos=0;

    if (pyjslib_isUndefined(sep) || pyjslib_isNull(sep)) {
        sep=" ";
        subject=subject.strip();
        subject=subject.replace(/\s+/g, sep);
    }
    else if (!pyjslib_isUndefined(maxsplit)) do_max=true;

    while (start<subject.length) {
        if (do_max && !maxsplit--) break;

        pos=subject.indexOf(sep, start);
        if (pos<0) break;

        items.append(subject.substring(start, pos));
        start=pos+sep.length;
    }
    if (start<subject.length) items.append(subject.substring(start));

    return items;
}

function pyjslib_String_strip(chars) {
    return this.lstrip(chars).rstrip(chars);
}

function pyjslib_String_lstrip(chars) {
    if (pyjslib_isUndefined(chars)) return this.replace(/^\s+/, "");

    return this.replace(new RegExp("^[" + chars + "]+"), "");
}

function pyjslib_String_rstrip(chars) {
    if (pyjslib_isUndefined(chars)) return this.replace(/\s+$/, "");

    return this.replace(new RegExp("[" + chars + "]+$"), "");
}

function pyjslib_String_startswith(prefix, start) {
    if (pyjslib_isUndefined(start)) start = 0;

    if (this.substring(start, prefix.length) == prefix) return true;
    return false;
}

String.prototype.__getitem__ = String.prototype.charAt;
String.prototype.upper = String.prototype.toUpperCase;
String.prototype.lower = String.prototype.toLowerCase;
String.prototype.find=pyjslib_String_find;
String.prototype.join=pyjslib_String_join;

String.prototype.__replace=String.prototype.replace;
String.prototype.replace=pyjslib_String_replace;

String.prototype.split=pyjslib_String_split;
String.prototype.strip=pyjslib_String_strip;
String.prototype.lstrip=pyjslib_String_lstrip;
String.prototype.rstrip=pyjslib_String_rstrip;
String.prototype.startswith=pyjslib_String_startswith;

var str = String;

var pyjslib_abs = Math.abs;

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

""")

class Object:
    pass

class Class:
    def __init__(self, name):
        self.name = name

    def __str___(self):
        return self.name

def cmp(a,b):
    if hasattr(a, "__cmp__"):
        return a.__cmp__(b)
    elif hasattr(b, "__cmp__"):
        return -b.__cmp__(a)
    if a > b:
        return 1
    elif b > a:
        return -1
    else:
        return 0

class List:
    def __init__(self, data=None):
        JS("""
        this.l = [];

        if (pyjslib_isArray(data)) {
            for (var i=0; i < data.length; i++) {
                this.l[i]=data[i];
                }
            }
        else if (pyjslib_isIteratable(data)) {
            var iter=data.__iter__();
            var i=0;
            try {
                while (true) {
                    var item=iter.next();
                    this.l[i++]=item;
                    }
                }
            catch (e) {
                if (e != StopIteration) throw e;
                }
            }
        """)

    def append(self, item):
        JS("""    this.l[this.l.length] = item;""")

    def remove(self, value):
        JS("""
        var index=this.index(value);
        if (index<0) return false;
        this.l.splice(index, 1);
        return true;
        """)

    def index(self, value, start=0):
        JS("""
        var length=this.l.length;
        for (var i=start; i<length; i++) {
            if (this.l[i]==value) {
                return i;
                }
            }
        return -1;
        """)

    def insert(self, index, value):
        JS("""    var a = this.l; this.l=a.slice(0, index).concat(value, a.slice(index));""")

    def pop(self, index = -1):
        JS("""
        if (index<0) index = this.l.length + index;
        var a = this.l[index];
        this.l.splice(index, 1);
        return a;
        """)

    def slice(self, lower, upper):
        JS("""
        if (upper==null) return pyjslib_List(this.l.slice(lower));
        return pyjslib_List(this.l.slice(lower, upper));
        """)

    def __getitem__(self, index):
        JS("""
        if (index<0) index = this.l.length + index;
        return this.l[index];
        """)

    def __setitem__(self, index, value):
        JS("""    this.l[index]=value;""")

    def __delitem__(self, index):
        JS("""    this.l.splice(index, 1);""")

    def __len__(self):
        JS("""    return this.l.length;""")

    def __contains__(self, value):
        return self.index(value) >= 0

    def __iter__(self):
        JS("""
        var i = 0;
        var l = this.l;
        return {
            'next': function() {
                if (i >= l.length) {
                    throw StopIteration;
                }
                return l[i++];
            },
            '__iter__': function() {
                return this;
            }
        };
        """)

    def sort(self, compareFunc=None, keyFunc=None, reverse=False):
        if not compareFunc:
            global cmp
            compareFunc = cmp
        if keyFunc and reverse:
            def thisSort1(a,b):
                return -compareFunc(keyFunc(a), keyFunc(b))
            self.l.sort(thisSort1)
        elif keyFunc:
            def thisSort2(a,b):
                return compareFunc(keyFunc(a), keyFunc(b))
            self.l.sort(thisSort2)
        elif reverse:
            def thisSort3(a,b):
                return -compareFunc(a, b)
            self.l.sort(thisSort3)
        else:
            self.l.sort(compareFunc)

    def getArray(self):
        """
        Access the javascript Array that is used internally by this list
        """
        return self.l

list = List

class Tuple(List):
    def __init__(self, data):
        List.__init__(self, data)

tuple = Tuple


class Dict:
    def __init__(self, data=None):
        JS("""
        this.d = {};

        if (pyjslib_isArray(data)) {
            for (var i in data) {
                var item=data[i];
                var sKey=this._keyToStr(item[0]);
                this.d[sKey]=item[1];
                }
            }
        else if (pyjslib_isIteratable(data)) {
            var iter=data.__iter__();
            try {
                while (true) {
                    var item=iter.next();
                    var sKey=this._keyToStr(item.__getitem__(0));
                    this.d[sKey]=item.__getitem__(1);
                    }
                }
            catch (e) {
                if (e != StopIteration) throw e;
                }
            }
        else if (pyjslib_isObject(data)) {
            for (var key in data) {
                this.d[key]=data[key];
                }
            }
        """)

    def __setitem__(self, key, value):
        JS("""
        var sKey = this._keyToStr(key);
        this.d[sKey]=value;
        """)

    def __getitem__(self, key):
        JS("""
        var sKey = this._keyToStr(key);
        var value=this.d[sKey];
        // if (pyjslib_isUndefined(value)) throw KeyError;
        return value;
        """)

    def __len__(self):
        JS("""
        var size=0;
        for (var i in this.d) size++;
        return size;
        """)

    def has_key(self, key):
        JS("""
        var sKey = this._keyToStr(key);
        if (pyjslib_isUndefined(this.d[sKey])) return false;
        return true;
        """)

    def __delitem__(self, key):
        JS("""
        var sKey = this._keyToStr(key);
        delete this.d[sKey];
        """)

    def __contains__(self, key):
        JS("""
        var sKey = this._keyToStr(key);
        return (pyjslib_isUndefined(this.d[sKey])) ? false : true;
        """)

    def keys(self):
        JS("""
        var keys=new pyjslib_List();
        for (var key in this.d) keys.append(key);
        return keys;
        """)

    def values(self):
        JS("""
        var keys=new pyjslib_List();
        for (var key in this.d) keys.append(this.d[key]);
        return keys;
        """)

    def items(self):
        JS("""
        var items = new pyjslib_List();
        for (var key in this.d) {
          var value = this.d[key];
          items.append(new pyjslib_List([key, value]))
          }
          return items;
        """)

    def __iter__(self):
        JS("""
        return this.keys().__iter__();
        """)

    def iterkeys(self):
        JS("""
        return this.keys().__iter__();
        """)

    def itervalues(self):
        JS("""
        return this.values().__iter__();
        """)

    def iteritems(self):
        JS("""
        var d = this.d;
        var iter=this.keys().__iter__();

        return {
            '__iter__': function() {
                return this;
            },

            'next': function() {
                var key;
                while (key=iter.next()) {
                    var item=new pyjslib_List();
                    item.append(key);
                    item.append(d[key]);
                    return item;
                }
            }
        };
        """)

    def setdefault(self, key, default_value):
        sKey = self._keyToStr(key)
        if not self.has_key(sKey):
            self[sKey] = default_value

    def get(self, key, default_value=None):
        sKey = self._keyToStr(key)
        value = self[sKey]
        JS("if(pyjslib_isUndefined(value)) { value = default_value; }")
        return value;

    def update(self, d):
        for k,v in d.iteritems():
            self[k] = v

    def getObject(self):
        """
        Return the javascript Object which this class uses to store dictionary keys and values
        """
        return self.d

    def _keyToStr(self, key):
        """ Convert the given object to a string we can safely use as a key.
        """
        if isString(key) or isNumber(key):
            return key
        else:
            return repr(key)
dict = Dict

# taken from mochikit: range( [start,] stop[, step] )
def range():
    JS("""
    var start = 0;
    var stop = 0;
    var step = 1;

    if (arguments.length == 2) {
        start = arguments[0];
        stop = arguments[1];
        }
    else if (arguments.length == 3) {
        start = arguments[0];
        stop = arguments[1];
        step = arguments[2];
        }
    else if (arguments.length>0) stop = arguments[0];

    return {
        'next': function() {
            if ((step > 0 && start >= stop) || (step < 0 && start <= stop)) throw StopIteration;
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
    JS("""
    if (pyjslib_isString(object)) {
        if (lower < 0) {
           lower = object.length + lower;
        }
        if (upper < 0) {
           upper = object.length + upper;
        }
        if (pyjslib_isNull(upper)) upper=object.length;
        return object.substring(lower, upper);
    }
    if (pyjslib_isObject(object) && object.slice)
        return object.slice(lower, upper);

    return null;
    """)

def str(text):
    JS("""
    return String(text);
    """)

def ord(x):
    if(isString(x) and len(x) == 1):
        JS("""
            return x.charCodeAt(0);
        """)
    else:
        JS("""
            throw TypeError;
        """)
    return None

def chr(x):
    JS("""
        return String.fromCharCode(x)
    """)

def is_basetype(x):
    JS("""
       var t = typeof(x);
       return t == 'boolean' ||
       t == 'function' ||
       t == 'number' ||
       t == 'string' ||
       t == 'undefined'
       ;
    """)

def get_pyjs_classtype(x):
    JS("""
       if (pyjslib_hasattr(x, "__class__"))
           if (pyjslib_hasattr(x.__class__, "__new__"))
               var src = x.__class__.__new__.toString();
               return src.match(/function (\w*)/)[1];
       return null;
    """)

def repr(x):
    """ Return the string representation of 'x'.
    """
    JS("""
       if (x === null)
           return "null";

       if (x === undefined)
           return "undefined";

       var t = typeof(x);

       if (t == "boolean")
           return x.toString();

       if (t == "function")
           return "<function " + x.toString() + ">";

       if (t == "number")
           return x.toString();

       if (t == "string") {
           if (x.indexOf('"') == -1)
               return '"' + x + '"';
           if (x.indexOf("'") == -1)
               return "'" + x + "'";
           var s = x.replace(new RegExp('"', "g"), '\\\\"');
           return '"' + s + '"';
       };

       if (t == "undefined")
           return "undefined";

       // If we get here, x is an object.  See if it's a Pyjamas class.

       if (!pyjslib_hasattr(x, "__init__"))
           return "<" + x.toString() + ">";

       // Handle the common Pyjamas data types.

       var constructor = "UNKNOWN";

       constructor = pyjslib_get_pyjs_classtype(x);

       if (constructor == "pyjslib_Tuple") {
           var contents = x.getArray();
           var s = "(";
           for (var i=0; i < contents.length; i++) {
               s += pyjslib_repr(contents[i]);
               if (i < contents.length - 1)
                   s += ", ";
           };
           s += ")"
           return s;
       };

       if (constructor == "pyjslib_List") {
           var contents = x.getArray();
           var s = "[";
           for (var i=0; i < contents.length; i++) {
               s += pyjslib_repr(contents[i]);
               if (i < contents.length - 1)
                   s += ", ";
           };
           s += "]"
           return s;
       };

       if (constructor == "pyjslib_Dict") {
           var keys = new Array();
           for (var key in x.d)
               keys.push(key);

           var s = "{";
           for (var i=0; i<keys.length; i++) {
               var key = keys[i]
               s += pyjslib_repr(key) + ": " + pyjslib_repr(x.d[key]);
               if (i < keys.length-1)
                   s += ", "
           };
           s += "}";
           return s;
       };

       // If we get here, the class isn't one we know -> return the class name.
       // Note that we replace underscores with dots so that the name will
       // (hopefully!) look like the original Python name.

       var s = constructor.replace(new RegExp('_', "g"), '.');
       return "<" + s + " object>";
    """)

def int(text, radix=0):
    JS("""
    return parseInt(text, radix);
    """)

def len(object):
    JS("""
    if (object==null) return 0;
    if (pyjslib_isObject(object) && object.__len__) return object.__len__();
    return object.length;
    """)

def getattr(obj, name, default_):
    JS("""
    if (pyjslib_isUndefined(obj[name])){
        if (pyjslib_isUndefined(default_)){
            throw new AttributeError();
        }else{
        return default_;
        }
    }
    if (!pyjslib_isFunction(obj[name])) return obj[name];
    return function() {
        var args = [];
        for (var i = 0; i < arguments.length; i++) {
          args.push(arguments[i]);
        }
        return obj[name].apply(obj,args);
        }
    """)

def setattr(obj, name, value):
    JS("""
    if (!pyjslib_isObject(obj)) return null;

    obj[name] = value;

    """)

def hasattr(obj, name):
    JS("""
    if (!pyjslib_isObject(obj)) return false;
    if (pyjslib_isUndefined(obj[name])) return false;

    return true;
    """)

def dir(obj):
    JS("""
    var properties=new pyjslib_List();
    for (property in obj) properties.append(property);
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


def enumerate(sequence):
    enumeration = []
    nextIndex = 0
    for item in sequence:
        enumeration.append([nextIndex, item])
        nextIndex = nextIndex + 1
    return enumeration


def min(sequence):
    minValue = None
    for item in sequence:
        if minValue == None:
            minValue = item
        elif item < minValue:
            minValue = item
    return minValue


def max(sequence):
    maxValue = None
    for item in sequence:
        if maxValue == None:
            maxValue = item
        elif item > maxValue:
            maxValue = item
    return maxValue


next_hash_id = 0

def hash(obj):
    JS("""
    if (obj == null) return null;

    if (obj.$H) return obj.$H;
    if (obj.__hash__) return obj.__hash__();
    if (obj.constructor == String || obj.constructor == Number || obj.constructor == Date) return obj;

    obj.$H = ++pyjslib_next_hash_id;
    return obj.$H;
    """)


# type functions from Douglas Crockford's Remedial Javascript: http://www.crockford.com/javascript/remedial.html
def isObject(a):
    JS("""
    return (a && typeof a == 'object') || pyjslib_isFunction(a);
    """)

def isFunction(a):
    JS("""
    return typeof a == 'function';
    """)

def isString(a):
    JS("""
    return typeof a == 'string';
    """)

def isNull(a):
    JS("""
    return typeof a == 'object' && !a;
    """)

def isArray(a):
    JS("""
    return pyjslib_isObject(a) && a.constructor == Array;
    """)

def isUndefined(a):
    JS("""
    return typeof a == 'undefined';
    """)

def isIteratable(a):
    JS("""
    return pyjslib_isObject(a) && a.__iter__;
    """)

def isNumber(a):
    JS("""
    return typeof a == 'number' && isFinite(a);
    """)

def toJSObjects(x):
    """
       Convert the pyjs pythonic List and Dict objects into javascript Object and Array
       objects, recursively.
    """
    result = x

    if isObject(x) and x.__class__:
        if x.__class__ == 'pyjslib_Dict':
            return toJSObjects(x.d)
        elif x.__class__ == 'pyjslib_List':
            return toJSObjects(x.l)

    if isObject(x):
        JS("""
        result = {};
        for(var k in x) {
           var v = x[k];
           var tv = pyjslib_toJSObjects(v)
           result[k] = tv;
        }
        """)
    if isArray(x):
        JS("""
        result = [];
        for(var k=0; k < x.length; k++) {
           var v = x[k];
           var tv = pyjslib_toJSObjects(v);
           result.push(tv);
        }
        """)

    return result

def printFunc(objs):
    JS("""
    var s = "";
    for(var i=0; i < objs.length; i++) {
        if(s != "") s += " ";
        s += objs[i];
    }
    console.debug(s)
    """)

