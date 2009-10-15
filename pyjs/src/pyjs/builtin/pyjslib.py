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

# must declare import _before_ importing sys

from __pyjamas__ import JS, setCompilerOptions, debugger

setCompilerOptions("noBoundMethods", "noDescriptors", "noAttributeChecking", "noSourceTracking", "noLineTracking", "noStoreSource")

platform = JS("$pyjs.platform")
sys = None
dynamic = None
JS("""
var $max_float_int = 1;
for (var i = 0; i < 1000; i++) {
    $max_float_int *= 2;
    if ($max_float_int + 1 == $max_float_int) {
        break;
    }
}
$max_int = 0x7fffffff;
$min_int = -0x80000000;
""")

class object:
    pass

def op_is(a,b):
    JS("""
    if (a === b) return true;
    if (a !== null && b !== null) {
        switch ((a.__number__ << 8) | b.__number__) {
            case 0x0101:
                return a == b;
            case 0x0202:
                return a.__v == b.__v;
            case 0x0404:
                return a.__cmp__(b) == 0;
        }
    }
    return false;
""")

@compiler.noSourceTracking
def op_eq(a,b):
    # All 'python' classes and types are implemented as objects/functions.
    # So, for speed, do a typeof X / X.__cmp__  on a/b.
    # Checking for the existance of .__cmp__ is expensive when it doesn't exist
    #setCompilerOptions("InlineEq")
    #return a == b
    JS("""
    if (a === null) {
        if (b === null) return true;
        return false;
    }
    if (b === null) {
        return false;
    }
    switch ((a.__number__ << 8) | b.__number__) {
        case 0x0101:
        case 0x0401:
            return a == b;
        case 0x0102:
            return a == b.__v;
        case 0x0201:
            return a.__v == b;
        case 0x0202:
            return a.__v == b.__v;
        case 0x0104:
        case 0x0204:
            a = new pyjslib['long'](a.valueOf());
        case 0x0404:
            return a.__cmp__(b) == 0;
        case 0x0402:
            return a.__cmp__(new pyjslib['long'](b.valueOf())) == 0;
    }
    if ((typeof a == 'object' || typeof a == 'function') && typeof a.__cmp__ == 'function') {
        return a.__cmp__(b) == 0;
    } else if ((typeof b == 'object' || typeof b == 'function') && typeof b.__cmp__ == 'function') {
        return b.__cmp__(a) == 0;
    }
    return a == b;
    """)

def op_uadd(v):
    JS("""
    switch (v.__number__) {
        case 0x01:
        case 0x02:
        case 0x04:
            return v;
    }
    if (v !== null) {
        if (typeof v['__pos__'] == 'function') return v.__pos__();
    }
""")
    raise TypeError("bad operand type for unary +: '%r'" % v)

def op_usub(v):
    JS("""
    switch (v.__number__) {
        case 0x01:
            return -v;
        case 0x02:
            return new pyjslib['int'](-v);
    }
    if (v !== null) {
        if (typeof v['__neg__'] == 'function') return v.__neg__();
    }
""")
    raise TypeError("bad operand type for unary -: '%r'" % v)

def op_add(x, y):
    JS("""
    if (x !== null && y !== null) {
        switch ((x.__number__ << 8) | y.__number__) {
            case 0x0101:
            case 0x0104:
            case 0x0401:
                return x + y;
            case 0x0102:
                return x + y.__v;
            case 0x0201:
                return x.__v + y;
            case 0x0202:
                return new pyjslib['int'](x.__v + y.__v);
            case 0x0204:
                return (new pyjslib['long'](x.__v)).__add(y);
            case 0x0402:
                return x.__add(new pyjslib['long'](y.__v));
            case 0x0404:
                return x.__add(y);
        }
        if (!x.__number__) {
            if (typeof x == 'string' && typeof y == 'string') return x + y;
            if (   !y.__number__
                && x.__mro__.length > y.__mro__.length
                && pyjslib['isinstance'](x, y)
                && typeof x['__add__'] == 'function')
                return y.__add__(x);
            if (typeof x['__add__'] == 'function') return x.__add__(y);
        }
        if (!y.__number__ && typeof y['__radd__'] == 'function') return y.__radd__(x);
    }
    throw pyjslib['TypeError']("unsupported operand type(s) for +: '%r', '%r'" % (x, y))
""")

def op_sub(x, y):
    JS("""
    if (x !== null && y !== null) {
        switch ((x.__number__ << 8) | y.__number__) {
            case 0x0101:
            case 0x0104:
            case 0x0401:
                return x - y;
            case 0x0102:
                return x - y.__v;
            case 0x0201:
                return x.__v - y;
            case 0x0202:
                return new pyjslib['int'](x.__v - y.__v);
            case 0x0204:
                return (new pyjslib['long'](x.__v)).__sub(y);
            case 0x0402:
                return x.__sub(new pyjslib['long'](y.__v));
            case 0x0404:
                return x.__sub(y);
        }
        if (!x.__number__) {
            if (   !y.__number__
                && x.__mro__.length > y.__mro__.length
                && pyjslib['isinstance'](x, y)
                && typeof x['__sub__'] == 'function')
                return y.__sub__(x);
            if (typeof x['__sub__'] == 'function') return x.__sub__(y);
        }
        if (!y.__number__ && typeof y['__rsub__'] == 'function') return y.__rsub__(x);
    }
    throw pyjslib['TypeError']("unsupported operand type(s) for -: '%r', '%r'" % (x, y))
""")

def op_floordiv(x, y):
    JS("""
    if (x !== null && y !== null) {
        switch ((x.__number__ << 8) | y.__number__) {
            case 0x0101:
            case 0x0104:
            case 0x0401:
                if (y == 0) throw pyjslib['ZeroDivisionError']('float divmod()');
                return Math.floor(x / y);
            case 0x0102:
                if (y.__v == 0) throw pyjslib['ZeroDivisionError']('float divmod()');
                return Math.floor(x / y.__v);
            case 0x0201:
                if (y == 0) throw pyjslib['ZeroDivisionError']('float divmod()');
                return Math.floor(x.__v / y);
            case 0x0202:
                if (y.__v == 0) throw pyjslib['ZeroDivisionError']('integer division or modulo by zero');
                return new pyjslib['int'](Math.floor(x.__v / y.__v));
            case 0x0204:
                return (new pyjslib['long'](x.__v)).__floordiv(y);
            case 0x0402:
                return x.__floordiv(new pyjslib['long'](y.__v));
            case 0x0404:
                return x.__floordiv(y);
        }
        if (!x.__number__) {
            if (   !y.__number__
                && x.__mro__.length > y.__mro__.length
                && pyjslib['isinstance'](x, y)
                && typeof x['__floordiv__'] == 'function')
                return y.__floordiv__(x);
            if (typeof x['__floordiv__'] == 'function') return x.__floordiv__(y);
        }
        if (!y.__number__ && typeof y['__rfloordiv__'] == 'function') return y.__rfloordiv__(x);
    }
    throw pyjslib['TypeError']("unsupported operand type(s) for //: '%r', '%r'" % (x, y))
""")

def op_div(x, y):
    JS("""
    if (x !== null && y !== null) {
        switch ((x.__number__ << 8) | y.__number__) {
            case 0x0101:
            case 0x0104:
            case 0x0401:
                if (y == 0) throw pyjslib['ZeroDivisionError']('float divmod()');
                return x / y;
            case 0x0102:
                if (y.__v == 0) throw pyjslib['ZeroDivisionError']('float divmod()');
                return x / y.__v;
            case 0x0201:
                if (y == 0) throw pyjslib['ZeroDivisionError']('float divmod()');
                return x.__v / y;
            case 0x0202:
                if (y.__v == 0) throw pyjslib['ZeroDivisionError']('float divmod()');
                return new pyjslib['int'](x.__v / y.__v);
            case 0x0204:
                return (new pyjslib['long'](x.__v)).__div(y);
            case 0x0402:
                return x.__div(new pyjslib['long'](y.__v));
            case 0x0404:
                return x.__div(y);
        }
        if (!x.__number__) {
            if (   !y.__number__
                && x.__mro__.length > y.__mro__.length
                && pyjslib['isinstance'](x, y)
                && typeof x['__div__'] == 'function')
                return y.__div__(x);
            if (typeof x['__div__'] == 'function') return x.__div__(y);
        }
        if (!y.__number__ && typeof y['__rdiv__'] == 'function') return y.__rdiv__(x);
    }
    throw pyjslib['TypeError']("unsupported operand type(s) for /: '%r', '%r'" % (x, y))
""")

def op_mul(x, y):
    JS("""
    if (x !== null && y !== null) {
        switch ((x.__number__ << 8) | y.__number__) {
            case 0x0101:
            case 0x0104:
            case 0x0401:
                return x * y;
            case 0x0102:
                return x * y.__v;
            case 0x0201:
                return x.__v * y;
            case 0x0202:
                return new pyjslib['int'](x.__v * y.__v);
            case 0x0204:
                return (new pyjslib['long'](x.__v)).__mul(y);
            case 0x0402:
                return x.__mul(new pyjslib['long'](y.__v));
            case 0x0404:
                return x.__mul(y);
        }
        if (!x.__number__) {
            if (   !y.__number__
                && x.__mro__.length > y.__mro__.length
                && pyjslib['isinstance'](x, y)
                && typeof x['__mul__'] == 'function')
                return y.__mul__(x);
            if (typeof x['__mul__'] == 'function') return x.__mul__(y);
        }
        if (!y.__number__ && typeof y['__rmul__'] == 'function') return y.__rmul__(x);
    }
    throw pyjslib['TypeError']("unsupported operand type(s) for *: '%r', '%r'" % (x, y))
""")

def op_mod(x, y):
    JS("""
    if (x !== null && y !== null) {
        switch ((x.__number__ << 8) | y.__number__) {
            case 0x0101:
            case 0x0104:
            case 0x0401:
                if (y == 0) throw pyjslib['ZeroDivisionError']('float divmod()');
                return x % y;
            case 0x0102:
                if (y.__v == 0) throw pyjslib['ZeroDivisionError']('float divmod()');
                return x % y.__v;
            case 0x0201:
                if (y == 0) throw pyjslib['ZeroDivisionError']('float divmod()');
                return x.__v % y;
            case 0x0202:
                if (y.__v == 0) throw pyjslib['ZeroDivisionError']('integer division or modulo by zero');
                return new pyjslib['int'](x.__v % y.__v);
            case 0x0204:
                return (new pyjslib['long'](x.__v)).__mod(y);
            case 0x0402:
                return x.__mod(new pyjslib['long'](y.__v));
            case 0x0404:
                return x.__mod(y);
        }
        if (typeof x == 'string') {
            return pyjslib.sprintf(x, y);
        }
        if (!x.__number__) {
            if (   !y.__number__
                && x.__mro__.length > y.__mro__.length
                && pyjslib['isinstance'](x, y)
                && typeof x['__mod__'] == 'function')
                return y.__mod__(x);
            if (typeof x['__mod__'] == 'function') return x.__mod__(y);
        }
        if (!y.__number__ && typeof y['__rmod__'] == 'function') return y.__rmod__(x);
    }
    throw pyjslib['TypeError']("unsupported operand type(s) for %: '%r', '%r'" % (x, y))
""")

def op_pow(x, y):
    JS("""
    if (x !== null && y !== null) {
        switch ((x.__number__ << 8) | y.__number__) {
            case 0x0101:
            case 0x0104:
            case 0x0401:
                if (y == 0) throw pyjslib['ZeroDivisionError']('float divmod()');
                return Math.pow(x, y);
            case 0x0102:
                if (y.__v == 0) throw pyjslib['ZeroDivisionError']('float divmod()');
                return Math.pow(x,y.__v);
            case 0x0201:
                if (y == 0) throw pyjslib['ZeroDivisionError']('float divmod()');
                return Math.pow(x.__v,y);
            case 0x0202:
                return x.__pow__(y);
            case 0x0204:
                return (new pyjslib['long'](x.__v)).__pow(y);
            case 0x0402:
                return x.__pow(new pyjslib['long'](y.__v))
            case 0x0404:
                return x.__pow(y);
        }
        if (!x.__number__) {
            if (   !y.__number__
                && x.__mro__.length > y.__mro__.length
                && pyjslib['isinstance'](x, y)
                && typeof x['__pow__'] == 'function')
                return y.__pow__(x);
            if (typeof x['__pow__'] == 'function') return x.__pow__(y);
        }
        if (!y.__number__ && typeof y['__rpow__'] == 'function') return y.__rpow__(x);
    }
    throw pyjslib['TypeError']("unsupported operand type(s) for %: '%r', '%r'" % (x, y))
""")

def op_invert(v):
    JS("""
    if (v !== null) {
        if (typeof v['__invert__'] == 'function') return v.__invert__();
    }
""")
    raise TypeError("bad operand type for unary -: '%r'" % v)

def op_bitshiftleft(x, y):
    JS("""
    if (x !== null && y !== null) {
        switch ((x.__number__ << 8) | y.__number__) {
            case 0x0202:
                return x.__lshift__(y);
            case 0x0204:
                return y.__rlshift__(x);
            case 0x0402:
                return x.__lshift(y.__v);
            case 0x0404:
                return x.__lshift(y.valueOf());
        }
        if (typeof x['__lshift__'] == 'function') {
            var v = x.__lshift__(y);
            if (v !== pyjslib['NotImplemented']) return v;
        }
        if (typeof y['__rlshift__'] != 'undefined') return y.__rlshift__(x);
    }
    throw pyjslib['TypeError']("unsupported operand type(s) for <<: '%r', '%r'" % (x, y))
""")

def op_bitshiftright(x, y):
    JS("""
    if (x !== null && y !== null) {
        switch ((x.__number__ << 8) | y.__number__) {
            case 0x0202:
                return x.__rshift__(y);
            case 0x0204:
                return y.__rrshift__(x);
            case 0x0402:
                return x.__rshift(y.__v);
            case 0x0404:
                return x.__rshift(y.valueOf());
        }
        if (typeof x['__rshift__'] == 'function') {
            var v = x.__rshift__(y);
            if (v !== pyjslib['NotImplemented']) return v;
        }
        if (typeof y['__rrshift__'] != 'undefined') return y.__rrshift__(x);
    }
    throw pyjslib['TypeError']("unsupported operand type(s) for >>: '%r', '%r'" % (x, y))
""")

def op_bitand2(x, y):
    JS("""
    if (x !== null && y !== null) {
        switch ((x.__number__ << 8) | y.__number__) {
            case 0x0202:
                return x.__and__(y);
            case 0x0204:
                return y.__and(new pyjslib['long'](x));
            case 0x0402:
                return x.__and(new pyjslib['long'](y.__v));
            case 0x0404:
                return x.__and(y);
        }
        if (typeof x['__rshift__'] == 'function') {
            var v = x.__rshift__(y);
            if (v !== pyjslib['NotImplemented']) return v;
        }
        if (typeof y['__rrshift__'] != 'undefined') return y.__rrshift__(x);
    }
    throw pyjslib['TypeError']("unsupported operand type(s) for &: '%r', '%r'" % (x, y))
""")

op_bitand = JS("""function (args) {
    if (args[0] !== null && args[1] !== null && args.length > 1) {
        var res, r;
        res = args[0];
        for (i = 1; i < args.length; i++) {
            if (typeof res['__and__'] == 'function') {
                r = res;
                res = res.__and__(args[i]);
                if (res === pyjslib['NotImplemented'] && typeof args[i]['__rand__'] == 'function') {
                    res = args[i].__rand__(r);
                }
            } else if (typeof args[i]['__rand__'] == 'function') {
                res = args[i].__rand__(res);
            } else {
                res = null;
                break;
            }
            if (res === pyjslib['NotImplemented']) {
                res = null;
                break;
            }
        }
        if (res !== null) {
            return res;
        }
    }
""")
raise TypeError("unsupported operand type(s) for &: " + ', '.join([repr(a) for a in list(args)]))
JS("""
}
""")

def op_bitxor2(x, y):
    JS("""
    if (x !== null && y !== null) {
        switch ((x.__number__ << 8) | y.__number__) {
            case 0x0202:
                return x.__xor__(y);
            case 0x0204:
                return y.__xor(new pyjslib['long'](x));
            case 0x0402:
                return x.__xor(new pyjslib['long'](y.__v));
            case 0x0404:
                return x.__xor(y);
        }
        if (typeof x['__rshift__'] == 'function') {
            var v = x.__rshift__(y);
            if (v !== pyjslib['NotImplemented']) return v;
        }
        if (typeof y['__rrshift__'] != 'undefined') return y.__rrshift__(x);
    }
    throw pyjslib['TypeError']("unsupported operand type(s) for &: '%r', '%r'" % (x, y))
""")

op_bitxor = JS("""function (args) {
    if (args[0] !== null && args[1] !== null && args.length > 1) {
        var res, r;
        res = args[0];
        for (i = 1; i < args.length; i++) {
            if (typeof res['__xor__'] == 'function') {
                r = res;
                res = res.__xor__(args[i]);
                if (res === pyjslib['NotImplemented'] && typeof args[i]['__rxor__'] == 'function') {
                    res = args[i].__rxor__(r);
                }
            } else if (typeof args[i]['__rxor__'] == 'function') {
                res = args[i].__rxor__(res);
            } else {
                res = null;
                break;
            }
            if (res === pyjslib['NotImplemented']) {
                res = null;
                break;
            }
        }
        if (res !== null) {
            return res;
        }
    }
""")
raise TypeError("unsupported operand type(s) for ^: " + ', '.join([repr(a) for a in args]))
JS("""
}
""")

def op_bitor2(x, y):
    JS("""
    if (x !== null && y !== null) {
        switch ((x.__number__ << 8) | y.__number__) {
            case 0x0202:
                return x.__or__(y);
            case 0x0204:
                return y.__or(new pyjslib['long'](x));
            case 0x0402:
                return x.__or(new pyjslib['long'](y.__v));
            case 0x0404:
                return x.__or(y);
        }
        if (typeof x['__rshift__'] == 'function') {
            var v = x.__rshift__(y);
            if (v !== pyjslib['NotImplemented']) return v;
        }
        if (typeof y['__rrshift__'] != 'undefined') return y.__rrshift__(x);
    }
    throw pyjslib['TypeError']("unsupported operand type(s) for &: '%r', '%r'" % (x, y))
""")

op_bitor = JS("""function (args) {
    if (args[0] !== null && args[1] !== null && args.length > 1) {
        var res, r;
        res = args[0];
        for (i = 1; i < args.length; i++) {
            if (typeof res['__or__'] == 'function') {
                r = res;
                res = res.__or__(args[i]);
                if (res === pyjslib['NotImplemented'] && typeof args[i]['__ror__'] == 'function') {
                    res = args[i].__ror__(r);
                }
            } else if (typeof args[i]['__ror__'] == 'function') {
                res = args[i].__ror__(res);
            } else {
                res = null;
                break;
            }
            if (res === pyjslib['NotImplemented']) {
                res = null;
                break;
            }
        }
        if (res !== null) {
            return res;
        }
    }
""")
raise TypeError("unsupported operand type(s) for |: " + ', '.join([repr(a) for a in args]))
JS("""
}
""")


@compiler.noSourceTracking
def ___import___(path, context, module_name=None, get_base=True):
    save_track_module = JS("$pyjs.track.module")
    module = JS("$pyjs.loaded_modules[path]")
    in_context = (not context is None)
    parts = path.split('.')
    parent_module = None
    if in_context:
        importName = context + '.'
    else:
        importName = ''
    l = len(parts)
    for i, name in enumerate(parts):
        importName += name
        if in_context:
            module = JS("$pyjs.loaded_modules[importName]")
            if i == 0:
                if JS("typeof module != 'undefined'"):
                    if JS("typeof $pyjs.loaded_modules[context + '.' + path] != 'undefined'"):
                        # module is already loaded
                        if JS("typeof $pyjs.loaded_modules[context + '.' + path].__was_initialized__ != 'undefined'"):
                            break
                else:
                    if JS("$pyjs.options.dynamic_loading"):
                        module = __dynamic_load__(importName)
                    if JS("typeof module == 'undefined'"):
                        in_context = False
                        if JS("typeof $pyjs.loaded_modules[path] != 'undefined'"):
                            # module is already loaded
                            if JS("typeof $pyjs.loaded_modules[path].__was_initialized__ != 'undefined'"):
                                break
                        importName = name
                        module = JS("$pyjs.loaded_modules[importName]")
        else:
            module = JS("$pyjs.loaded_modules[importName]")
        if JS("typeof module == 'undefined'"):
            if JS("$pyjs.options.dynamic_loading"):
                module = __dynamic_load__(importName)
            if JS("typeof module == 'undefined'"):
                if not parent_module is None and hasattr(parent_module, name):
                    break
                JS("$pyjs.track.module = save_track_module;")
                raise ImportError(
                    "No module named %s, %s in context %s" % (importName, path, context))
        if i == 0 and not in_context:
            JS("$pyjs.__modules__[importName] = module;")
        if l==i+1:
            # This is the last module, we set the module name here
            module(module_name)
        else:
            module(None)
        importName += '.'
        parent_module = module
    JS("$pyjs.track.module = save_track_module;")
    if in_context:
        importName = context + '.' + parts[0]
    else:
        if get_base == True:
            importName = parts[0]
        else:
            importName = path
    return JS("$pyjs.loaded_modules[importName]")

def __dynamic_load__(importName):
    setCompilerOptions("noDebug")
    module = JS("""$pyjs.loaded_modules[importName]""")
    if sys is None or dynamic is None:
        return module
    if JS("""typeof module == 'undefined'"""):
        try:
            dynamic.ajax_import("lib/" + importName + ".__" + platform + "__.js")
            module = JS("""$pyjs.loaded_modules[importName]""")
        except:
            pass
    if JS("""typeof module == 'undefined'"""):
        try:
            dynamic.ajax_import("lib/" + importName + ".js")
            module = JS("""$pyjs.loaded_modules[importName]""")
        except:
            pass
    return module

class BaseException:

    message = ''

    def __init__(self, *args):
        self.args = args
        if len(args) == 1:
            self.message = args[0]

    def __getitem__(self, index):
        return self.args.__getitem__(index)

    @compiler.noDescriptors
    def __str__(self):
        if len(self.args) is 0:
            return ''
        elif len(self.args) is 1:
            return str(self.message)
        return repr(self.args)

    @compiler.noDescriptors
    def __repr__(self):
        return self.__name__ + repr(self.args)

class Exception(BaseException):
    pass

class StandardError(Exception):
    pass

class AssertionError(Exception):
    pass

class GeneratorExit(Exception):
    pass

class TypeError(StandardError):
    pass

class AttributeError(StandardError):
    pass

class NameError(StandardError):
    pass

class ValueError(StandardError):
    pass

class ImportError(StandardError):
    pass

class LookupError(StandardError):
    pass

class RuntimeError(StandardError):
    pass

class ArithmeticError(StandardError):
    pass

class KeyError(LookupError):

    def __str__(self):
        if len(self.args) is 0:
            return ''
        elif len(self.args) is 1:
            return repr(self.message)
        return repr(self.args)

class IndexError(LookupError):
    pass

class NotImplementedError(RuntimeError):
    pass

class ZeroDivisionError(ArithmeticError):
    pass

class OverflowError(ArithmeticError):
    pass

def init():

    # There seems to be an bug in Chrome with accessing the message
    # property, on which an error is thrown
    # Hence the declaration of 'var message' and the wrapping in try..catch
    JS("""
pyjslib._errorMapping = function(err) {
    if (err instanceof(ReferenceError) || err instanceof(TypeError)) {
        var message = '';
        try {
            message = err.message;
        } catch ( e) {
        }
        return pyjslib.AttributeError(message);
    }
    return err;
};
""")
    # The TryElse 'error' is used to implement the else in try-except-else
    # (to raise an exception when there wasn't any)
    JS("""
pyjslib.TryElse = function () { };
pyjslib.TryElse.prototype = new Error();
pyjslib.TryElse.__name__ = 'TryElse';
pyjslib.TryElse.message = 'TryElse';
""")
    # StopIteration is used to get out of an iteration loop
    JS("""
pyjslib.StopIteration = function () { };
pyjslib.StopIteration.prototype = new Error();
pyjslib.StopIteration.__name__ = 'StopIteration';
//pyjslib.StopIteration.message = 'StopIteration';
""")

    # Patching of the standard javascript String object
    JS("""
String.prototype.rfind = function(sub, start, end) {
    var pos;
    if (!pyjslib.isUndefined(start)) {
        /* *sigh* - python rfind goes *RIGHT*, NOT left */
        pos = this.substring(start).lastIndexOf(sub);
        if (pos == -1) {
            return -1;
        }
        pos += start;
    }
    else {
        pos=this.lastIndexOf(sub, start);
    }
    if (pyjslib.isUndefined(end)) return pos;

    if (pos + sub.length>end) return -1;
    return pos;
};

String.prototype.find = function(sub, start, end) {
    var pos=this.indexOf(sub, start);
    if (pyjslib.isUndefined(end)) return pos;

    if (pos + sub.length>end) return -1;
    return pos;
};

String.prototype.join = function(data) {
    var text="";

    if (data.constructor == Array) {
        return data.join(this);
    }
    else if (data.prototype.__md5__ == pyjslib.List.prototype.__md5__) {
        return data.l.join(this);
    }
    else if (pyjslib.isIteratable(data)) {
        var iter=data.__iter__();
        try {
            text+=iter.next();
            while (true) {
                var item=iter.next();
                text+=this + item;
            }
        }
        catch (e) {
            if (e.__name__ != 'StopIteration') throw e;
        }
    }

    return text;
};

String.prototype.isdigit = function() {
    return (this.match(/^\d+$/g) != null);
};

String.prototype.__replace=String.prototype.replace;
String.prototype.replace = function(old, replace, count) {
    var do_max=false;
    var start=0;
    var new_str="";
    var pos=0;

    if (!pyjslib.isString(old)) return this.__replace(old, replace);
    if (!pyjslib.isUndefined(count)) do_max=true;

    while (start<this.length) {
        if (do_max && !count--) break;

        pos=this.indexOf(old, start);
        if (pos<0) break;

        new_str+=this.substring(start, pos) + replace;
        start=pos+old.length;
    }
    if (start<this.length) new_str+=this.substring(start);

    return new_str;
};

String.prototype.__contains__ = function(s){
    return this.indexOf(s)>=0;
};

String.prototype.__split = String.prototype.split;

String.prototype.split = function(sep, maxsplit) {
    var items=new pyjslib.List();
    var do_max=false;
    var subject=this;
    var start=0;
    var pos=0;

    if (pyjslib.isUndefined(sep) || pyjslib.isNull(sep)) {
        sep=" ";
        subject=subject.strip();
        subject=subject.replace(/\s+/g, sep);
    }
    else if (!pyjslib.isUndefined(maxsplit)) do_max=true;

    if (subject.length == 0) {
        return items;
    }

    while (start<subject.length) {
        if (do_max && !maxsplit--) break;

        pos=subject.indexOf(sep, start);
        if (pos<0) break;

        items.append(subject.substring(start, pos));
        start=pos+sep.length;
    }
    if (start<=subject.length) items.append(subject.substring(start));

    return items;
};

String.prototype.__iter__ = function() {
    var i = 0;
    var s = this;
    return {
        'next': function() {
            if (i >= s.length) {
                throw pyjslib.StopIteration;
            }
            return s.substring(i++, i, 1);
        },
        '__iter__': function() {
            return this;
        }
    };
};

String.prototype.strip = function(chars) {
    return this.lstrip(chars).rstrip(chars);
};

String.prototype.lstrip = function(chars) {
    if (pyjslib.isUndefined(chars)) return this.replace(/^\s+/, "");
    if (chars.length == 0) return this;
    return this.replace(new RegExp("^[" + chars + "]+"), "");
};

String.prototype.rstrip = function(chars) {
    if (pyjslib.isUndefined(chars)) return this.replace(/\s+$/, "");
    if (chars.length == 0) return this;
    return this.replace(new RegExp("[" + chars + "]+$"), "");
};

String.prototype.startswith = function(prefix, start, end) {
    // FIXME: accept tuples as suffix (since 2.5)
    if (pyjslib.isUndefined(start)) start = 0;
    if (pyjslib.isUndefined(end)) end = this.length;

    if ((end - start) < prefix.length) return false;
    if (this.substr(start, prefix.length) == prefix) return true;
    return false;
};

String.prototype.endswith = function(suffix, start, end) {
    // FIXME: accept tuples as suffix (since 2.5)
    if (pyjslib.isUndefined(start)) start = 0;
    if (pyjslib.isUndefined(end)) end = this.length;

    if ((end - start) < suffix.length) return false;
    if (this.substr(end - suffix.length, suffix.length) == suffix) return true;
    return false;
};

String.prototype.ljust = function(width, fillchar) {
    switch (width.__number__) {
        case 0x02:
        case 0x04:
            width = width.valueOf();
            break;
        case 0x01:
            if (Math.floor(width) == width) break;
        default:
            throw (pyjslib.TypeError("an integer is required"));
    }
    if (pyjslib.isUndefined(fillchar)) fillchar = ' ';
    if (typeof(fillchar) != 'string' ||
        fillchar.length != 1) {
        throw (pyjslib.TypeError("ljust() argument 2 must be char, not " + typeof(fillchar)));
    }
    if (this.length >= width) return this;
    return this + new Array(width+1 - this.length).join(fillchar);
};

String.prototype.rjust = function(width, fillchar) {
    switch (width.__number__) {
        case 0x02:
        case 0x04:
            width = width.valueOf();
            break;
        case 0x01:
            if (Math.floor(width) == width) break;
        default:
            throw (pyjslib.TypeError("an integer is required"));
    }
    if (pyjslib.isUndefined(fillchar)) fillchar = ' ';
    if (typeof(fillchar) != 'string' ||
        fillchar.length != 1) {
        throw (pyjslib.TypeError("rjust() argument 2 must be char, not " + typeof(fillchar)));
    }
    if (this.length >= width) return this;
    return new Array(width + 1 - this.length).join(fillchar) + this;
};

String.prototype.center = function(width, fillchar) {
    switch (width.__number__) {
        case 0x02:
        case 0x04:
            width = width.valueOf();
            break;
        case 0x01:
            if (Math.floor(width) == width) break;
        default:
            throw (pyjslib.TypeError("an integer is required"));
    }
    if (pyjslib.isUndefined(fillchar)) fillchar = ' ';
    if (typeof(fillchar) != 'string' ||
        fillchar.length != 1) {
        throw (pyjslib.TypeError("center() argument 2 must be char, not " + typeof(fillchar)));
    }
    if (this.length >= width) return this;
    padlen = width - this.length;
    right = Math.ceil(padlen / 2);
    left = padlen - right;
    return new Array(left+1).join(fillchar) + this + new Array(right+1).join(fillchar);
};

String.prototype.__getslice__ = function(lower, upper) {
    if (lower < 0) {
       lower = this.length + lower;
    }
    if (upper < 0) {
       upper = this.length + upper;
    }
    if (pyjslib.isNull(upper)) upper=this.length;
    return this.substring(lower, upper);
}

String.prototype.__getitem__ = function(idx) {
    if (idx < 0) idx += this.length;
    if (idx < 0 || idx > this.length) {
        throw(pyjslib.IndexError("string index out of range"));
    }
    return this.charAt(idx);
};

String.prototype.__setitem__ = function(idx, val) {
    throw(pyjslib.TypeError("'str' object does not support item assignment"));
}

String.prototype.upper = String.prototype.toUpperCase;
String.prototype.lower = String.prototype.toLowerCase;

String.prototype.__add__ = function(y) {
    if (typeof y != "string") {
        throw pyjslib.TypeError("cannot concatenate 'str' and non-str objects");
    }
    return this + y;
}

String.prototype.__mul__ = function(y) {
    switch (y.__number__) {
        case 0x02:
        case 0x04:
            y = y.valueOf();
            break;
        case 0x01:
            if (Math.floor(y) == y) break;
        default:
            throw pyjslib.TypeError("can't multiply sequence by non-int of type 'str'");
    }
    var s = '';
    while (y-- > 0) {
        s += this;
    }
    return s;
}
String.prototype.__rmul__ = String.prototype.__mul__;
String.prototype.__number__ = null;
String.prototype.__name__ = 'str';
String.prototype.__class__ = String.prototype;
String.prototype.__is_instance__ = null;
String.prototype.__str__ = function () {
    if (typeof this == 'string') return this.toString();
    return "<type 'str'>";
}
String.prototype.__repr__ = function () {
    if (typeof this == 'string') return "'" + this.toString() + "'";
    return "<type 'str'>";
}

""")

    # Patching of the standard javascript Boolean object
    JS("""
Boolean.prototype.__number__ = 0x01;
Boolean.prototype.__name__ = 'bool';
Boolean.prototype.__class__ = Boolean.prototype;
Boolean.prototype.__is_instance__ = null;
Boolean.prototype.__str__= function () {
    if (typeof this == 'string') {
     	if (this === true) return "True";
    	return "False";
    }
    return "<type 'bool'>";
}
Boolean.prototype.__repr__ = Boolean.prototype.__str__;

""")

    # Patching of the standard javascript Array object
    # This makes it imposible to use for (k in Array())
    JS("""
if (!Array.prototype.indexOf) {
    Array.prototype.indexOf = function(elt /*, from*/) {
        var len = this.length >>> 0;

        var from = Number(arguments[1]) || 0;
        from = (from < 0)
                ? Math.ceil(from)
                : Math.floor(from);
        if (from < 0)
            from += len;

        for (; from < len; from++) {
            if (from in this &&
                this[from] === elt)
                return from;
        }
        return -1;
    };
}
""")

    # Patching of the standard javascript RegExp
    JS("""
RegExp.prototype.Exec = RegExp.prototype.exec;
""")
    JS("""
pyjslib.abs = Math.abs;
""")

class Class:
    def __init__(self, name):
        self.name = name

    def __str___(self):
        return self.name

@compiler.noSourceTracking
def open(fname, mode='r'):
    raise NotImplementedError("open is not implemented in browsers")

@compiler.noSourceTracking
def cmp(a,b):
    JS("""
    if (typeof a == typeof b) {
        switch (typeof a) {
            case 'number':
            case 'string':
            case 'boolean':
                return a == b ? 0 : (a < b ? -1 : 1);
        }
        if (a === b) return 0;
    }
    if (a === null) {
        if (b === null) return 0;
        return -1;
    }
    if (b === null) {
        return 1;
    }

    switch ((a.__number__ << 8)|b.__number__) {
        case 0x0202:
            a = a.__v;
            b = b.__v;
        case 0x0101:
            return a == b ? 0 : (a < b ? -1 : 1);
        case 0x0100:
        case 0x0200:
        case 0x0400:
            if (typeof b.__cmp__ == 'function') {
                return -b.__cmp__(a);
            }
            return -1;
        case 0x0001:
        case 0x0002:
        case 0x0004:
            if (typeof a.__cmp__ == 'function') {
                return a.__cmp__(b);
            }
            return 1;
        case 0x0102:
            return -b.__cmp__(new pyjslib['int'](a));
        case 0x0104:
            return -b.__cmp__(new pyjslib['long'](a));
        case 0x0201:
            return a.__cmp__(new pyjslib['int'](b));
        case 0x0401:
            return a.__cmp__(new pyjslib['long'](b));
        case 0x0204:
            return -b.__cmp__(new pyjslib['long'](a));
        case 0x0402:
            return a.__cmp__(new pyjslib['long'](b));
        case 0x0404:
            return a.__cmp__(b);
    }

    if (typeof a.__class__ == typeof b.__class__ && typeof a.__class__ == 'function') {
        if (a.__class__.__name__ < b.__class__.__name__) {
            return -1;
        }
        if (a.__class__.__name__ > b.__class__.__name__) {
            return 1;
        }
    }

    if ((typeof a == 'object' || typeof a == 'function') && typeof a.__cmp__ == 'function') {
        return a.__cmp__(b);
    } else if ((typeof b == 'object' || typeof b == 'function') && typeof b.__cmp__ == 'function') {
        return -b.__cmp__(a);
    }
    if (a == b) return 0;
    if (a > b) return 1;
    return -1;
    """)

# for List.sort()
__cmp = cmp

@compiler.noSourceTracking
def bool(v):
    # this needs to stay in native code without any dependencies here,
    # because this is used by if and while, we need to prevent
    # recursion
    #setCompilerOptions("InlineBool")
    #if v:
    #    return True
    #return False
    JS("""
    if (!v) return false;
    switch(typeof v){
    case 'boolean':
        return v;
    case 'object':
        if (v.__nonzero__){
            return v.__nonzero__();
        }else if (v.__len__){
            return v.__len__()>0;
        }
        return true;
    }
    return Boolean(v);
    """)

class float:
    __number__ = JS("0x01")
    def __new__(self, args):
        JS("""
        var v = Number(args[0]);
        if (isNaN(v)) {
            throw pyjslib.ValueError("invalid literal for float(): " + args[0]);
        }
        return v;
""")
# Patching of the standard javascript Number
# which is in principle the python 'float'
JS("""
Number.prototype.__number__ = 0x01;
Number.prototype.__name__ = 'float';
Number.prototype.__init__ = function (value, radix) {
    return null;
}

Number.prototype.__str__ = function () {
    if (typeof this == 'number') return this.toString();
    return "<type 'float'>";
}

Number.prototype.__repr__ = function () {
    if (typeof this == 'number') return this.toString();
    return "<type 'float'>";
}

Number.prototype.__nonzero__ = function () {
    return this != 0;
}

Number.prototype.__cmp__ = function (y) {
    return this < y? -1 : (this == y ? 0 : 1);
}

Number.prototype.__hash__ = function () {
    return this;
}

Number.prototype.__oct__ = function () {
    return '0'+this.toString(8);
}

Number.prototype.__hex__ = function () {
    return '0x'+this.toString(16);
}

Number.prototype.__pos__ = function () {
    return this;
}

Number.prototype.__neg__ = function () {
    return -this;
}

Number.prototype.__abs__ = function () {
    if (this >= 0) return this;
    return -this;
}

Number.prototype.__add__ = function (y) {
    if (!y.__number__ || isNaN(y = y.valueOf())) return pyjslib['NotImplemented'];
    return this + y;
}

Number.prototype.__radd__ = function (y) {
    if (!y.__number__ || isNaN(y = y.valueOf())) return pyjslib['NotImplemented'];
    return y + this;
}

Number.prototype.__sub__ = function (y) {
    if (!y.__number__ || isNaN(y = y.valueOf())) return pyjslib['NotImplemented'];
    return this - y;
}

Number.prototype.__rsub__ = function (y) {
    if (!y.__number__ || isNaN(y = y.valueOf())) return pyjslib['NotImplemented'];
    return y - this;
}

Number.prototype.__floordiv__ = function (y) {
    if (!y.__number__ || isNaN(y = y.valueOf())) return pyjslib['NotImplemented'];
    if (y == 0) throw pyjslib['ZeroDivisionError']('float divmod()');
    return Math.floor(this / y);
}

Number.prototype.__rfloordiv__ = function (y) {
    if (!y.__number__ || isNaN(y = y.valueOf())) return pyjslib['NotImplemented'];
    if (this == 0) throw pyjslib['ZeroDivisionError']('float divmod');
    return Math.floor(y / this);
}

Number.prototype.__div__ = function (y) {
    if (!y.__number__ || isNaN(y = y.valueOf())) return pyjslib['NotImplemented'];
    if (y == 0) throw pyjslib['ZeroDivisionError']('float division');
    return this / y;
}

Number.prototype.__rdiv__ = function (y) {
    if (!y.__number__ || isNaN(y = y.valueOf())) return pyjslib['NotImplemented'];
    if (this == 0) throw pyjslib['ZeroDivisionError']('float division');
    return y / this;
}

Number.prototype.__mul__ = function (y) {
    if (!y.__number__ || isNaN(y = y.valueOf())) return pyjslib['NotImplemented'];
    return this * y;
}

Number.prototype.__rmul__ = function (y) {
    if (!y.__number__ || isNaN(y = y.valueOf())) return pyjslib['NotImplemented'];
    return y * this;
}

Number.prototype.__mod__ = function (y) {
    if (!y.__number__ || isNaN(y = y.valueOf())) return pyjslib['NotImplemented'];
    if (y == 0) throw pyjslib['ZeroDivisionError']('float modulo');
    return this % y;
}

Number.prototype.__rmod__ = function (y) {
    if (!y.__number__ || isNaN(y = y.valueOf())) return pyjslib['NotImplemented'];
    if (this == 0) throw pyjslib['ZeroDivisionError']('float modulo');
    return y % this;
}

Number.prototype.__pow__ = function (y, z) {
    if (!y.__number__ || isNaN(y = y.valueOf())) return pyjslib['NotImplemented'];
    if (typeof z == 'undefined' || z == null) {
        return Math.pow(this, y);
    }
    if (!z.__number__ || isNaN(z = z.valueOf())) return pyjslib['NotImplemented'];
    return Math.pow(this, y) % z;
}

""")

def float_int(value, radix=None):
    JS("""
    var v;
    if (value.__number__) {
        if (radix !== null) {
            throw pyjslib.TypeError("int() can't convert non-string with explicit base");
        }
        v = value.valueOf()
        if (v > 0) {
            v = Math.floor(v);
        } else {
            v = Math.ceil(v);
        }
    } else if (typeof value == 'string') {
        if (radix === null) {
            radix = 10;
        }
        switch (value[value.length-1]) {
            case 'l':
            case 'L':
                v = value.slice(0, value.length-2)
                break;
            default:
                v = value;
        }
        v = parseInt(v, radix);
    } else {
        throw pyjslib.TypeError("TypeError: int() argument must be a string or a number");
    }
    if (isNaN(v) || !isFinite(v)) {
        throw pyjslib.ValueError("invalid literal for int() with base " + radix + ": '" + value + "'")
    }
    return v;
""")

JS("""
(function(){
    var $int = pyjslib['int'] = function (value, radix) {
        var v, i;
        if (typeof radix == 'undefined' || radix === null) {
            if (typeof value == 'undefined') {
                throw pyjslib.TypeError("int() takes at least 1 argument");
            }
            switch (value.__number__) {
                case 0x01:
                    value = value > 0 ? Math.floor(value) : Math.ceil(value);
                    break;
                case 0x02:
                    return value;
                case 0x04:
                    v = value.valueOf();
                    if (!($min_int <= v && v <= $max_int))
                        return value;
            }
            radix = null;
        }
        if (typeof this != 'object' || this.__number__ != 0x02) return new $int(value, radix);
        if (value.__number__) {
            if (radix !== null) throw pyjslib.TypeError("int() can't convert non-string with explicit base");
            v = value.valueOf();
        } else if (typeof value == 'string') {
            if (radix === null) {
                radix = 10;
            }
            v = parseInt(value, radix);
        } else {
            throw pyjslib.TypeError("TypeError: int() argument must be a string or a number");
        }
        if (isNaN(v) || !isFinite(v)) {
            throw pyjslib.ValueError("invalid literal for int() with base " + radix + ": '" + value + "'")
        }
        if ($min_int <= v && v <= $max_int) {
            this.__v = v;
            return this;
        }
        return new pyjslib['long'](v);
    }
    $int.__init__ = function () {};
    $int.__number__ = 0x02;
    $int.__v = 0;
    $int.__name__ = 'int';
    $int.prototype = $int;
    $int.__class__ = $int;

    $int.toExponential = function (fractionDigits) {
        return (typeof fractionDigits == 'undefined' || fractionDigits === null) ? this.__v.toExponential() : this.__v.toExponential(fractionDigits);
    }

    $int.toFixed = function (digits) {
        return (typeof digits == 'undefined' || digits === null) ? this.__v.toFixed() : this.__v.toFixed(digits);
    }

    $int.toLocaleString = function () {
        return this.__v.toLocaleString();
    }

    $int.toPrecision = function (precision) {
        return (typeof precision == 'undefined' || precision === null) ? this.__v.toPrecision() : this.__v.toPrecision(precision);
    }

    $int.toString = function (radix) {
        return (typeof radix == 'undefined' || radix === null) ? this.__v.toString() : this.__v.toString(radix);
    }

    $int.valueOf = function () {
        return this.__v.valueOf();
    }

    $int.__str__ = function () {
        if (typeof this == 'object' && this.__number__ == 0x02) return this.__v.toString();
        return "<type 'int'>";
    }

    $int.__repr__ = function () {
        if (typeof this == 'object' && this.__number__ == 0x02) return this.__v.toString();
        return "<type 'int'>";
    }

    $int.__nonzero__ = function () {
        return this.__v != 0;
    }

    $int.__cmp__ = function (y) {
        return this.__v < y? -1 : (this.__v == y ? 0 : 1);
    }

    $int.__hash__ = function () {
        return this.__v;
    }

    $int.__invert__ = function () {
        return new $int(~this.__v);
    }

    $int.__lshift__ = function (y) {
        if (y.__number__ != 0x02) return pyjslib['NotImplemented'];
        y = y.__v;
        if (y < 32) {
            var v = this.__v << y;
            if (v > this.__v) {
                return new $int(v);
            }
        }
        return new pyjslib['long'](this.__v).__lshift__(y);
    }

    $int.__rlshift__ = function (y) {
        if (y.__number__ != 0x02) return pyjslib['NotImplemented'];
        y = y.__v;
        if (this.__v < 32) {
            var v = y << this.__v;
            if (v > this.__v) {
                return new $int(v);
            }
        }
        return new pyjslib['long'](y).__lshift__(this.__v);
    }

    $int.__rshift__ = function (y) {
        if (y.__number__ != 0x02) return pyjslib['NotImplemented'];
        y = y.__v;
        return new $int(this.__v >>> y);
    }

    $int.__rrshift__ = function (y) {
        if (y.__number__ != 0x02) return pyjslib['NotImplemented'];
        y = y.__v;
        return new $int(y >>> this.__v);
    }

    $int.__and__ = function (y) {
        if (y.__number__ != 0x02) return pyjslib['NotImplemented'];
        y = y.__v;
        return new $int(this.__v & y);
    }

    $int.__rand__ = function (y) {
        if (y.__number__ != 0x02) return pyjslib['NotImplemented'];
        y = y.__v;
        return new $int(y & this.__v);
    }

    $int.__xor__ = function (y) {
        if (y.__number__ != 0x02) return pyjslib['NotImplemented'];
        y = y.__v;
        return new $int(this.__v ^ y);
    }

    $int.__rxor__ = function (y) {
        if (y.__number__ != 0x02) return pyjslib['NotImplemented'];
        y = y.__v;
        return new $int(y ^ this.__v);
    }

    $int.__or__ = function (y) {
        if (y.__number__ != 0x02) return pyjslib['NotImplemented'];
        y = y.__v;
        return new $int(this.__v | y);
    }

    $int.__ror__ = function (y) {
        if (y.__number__ != 0x02) return pyjslib['NotImplemented'];
        y = y.__v;
        return new $int(y | this.__v);
    }

    $int.__oct__ = function () {
        return '0x'+this.__v.toString(8);
    }

    $int.__hex__ = function () {
        return '0x'+this.__v.toString(16);
    }

    $int.__pos__ = function () {
        return this;
    }

    $int.__neg__ = function () {
        return new $int(-this.__v);
    }

    $int.__abs__ = function () {
        if (this.__v >= 0) return this;
        return new $int(-this.__v);
    }

    $int.__add__ = function (y) {
        if (y.__number__ != 0x02) return pyjslib['NotImplemented'];
        y = y.__v;
        var v = this.__v + y;
        if ($min_int <= v && v <= $max_int) {
            return new $int(v);
        }
        if (-$max_float_int < v && v < $max_float_int) {
            return new pyjslib['long'](v);
        }
        return new pyjslib['long'](this.__v).__add__(new pyjslib['long'](y));
    }

    $int.__radd__ = $int.__add__;

    $int.__sub__ = function (y) {
        if (y.__number__ != 0x02) return pyjslib['NotImplemented'];
        y = y.__v;
        var v = this.__v - y;
        if ($min_int <= v && v <= $max_int) {
            return new $int(v);
        }
        if (-$max_float_int < v && v < $max_float_int) {
            return new pyjslib['long'](v);
        }
        return new pyjslib['long'](this.__v).__sub__(new pyjslib['long'](y));
    }

    $int.__rsub__ = function (y) {
        if (y.__number__ != 0x02) return pyjslib['NotImplemented'];
        y = y.__v;
        var v = y -this.__v;
        if ($min_int <= v && v <= $max_int) {
            return new $int(v);
        }
        if (-$max_float_int < v && v < $max_float_int) {
            return new pyjslib['long'](v);
        }
        return new pyjslib['long'](y).__sub__(new pyjslib['long'](this.__v));
    }

    $int.__floordiv__ = function (y) {
        if (y.__number__ != 0x02) return pyjslib['NotImplemented'];
        y = y.__v;
        if (y == 0) throw pyjslib['ZeroDivisionError']('integer division or modulo by zero');
        return new $int(Math.floor(this.__v / y));
    }

    $int.__rfloordiv__ = function (y) {
        if (y.__number__ != 0x02) return pyjslib['NotImplemented'];
        y = y.__v;
        if (this.__v == 0) throw pyjslib['ZeroDivisionError']('integer division or modulo by zero');
        return new $int(Math.floor(y / this.__v));
    }

    $int.__div__ = function (y) {
        if (y.__number__ != 0x02) return pyjslib['NotImplemented'];
        y = y.__v;
        if (y == 0) throw pyjslib['ZeroDivisionError']('integer division or modulo by zero');
        return new $int(this.__v / y);
    }

    $int.__rdiv__ = function (y) {
        if (y.__number__ != 0x02) return pyjslib['NotImplemented'];
        y = y.__v;
        if (this.__v == 0) throw pyjslib['ZeroDivisionError']('integer division or modulo by zero');
        return new $int(y / this.__v);
    }

    $int.__mul__ = function (y) {
        if (y.__number__ != 0x02) return pyjslib['NotImplemented'];
        y = y.__v;
        var v = this.__v * y;
        if ($min_int <= v && v <= $max_int) {
            return new $int(v);
        }
        if (-$max_float_int < v && v < $max_float_int) {
            return new pyjslib['long'](v);
        }
        return new pyjslib['long'](this.__v).__mul__(new pyjslib['long'](y));
    }

    $int.__rmul__ = $int.__mul__;

    $int.__mod__ = function (y) {
        if (y.__number__ != 0x02) return pyjslib['NotImplemented'];
        y = y.__v;
        if (y == 0) throw pyjslib['ZeroDivisionError']('integer division or modulo by zero');
        return new $int(this.__v % y);
    }

    $int.__rmod__ = function (y) {
        if (y.__number__ != 0x02) return pyjslib['NotImplemented'];
        y = y.__v;
        if (this.__v == 0) throw pyjslib['ZeroDivisionError']('integer division or modulo by zero');
        return new $int(y % this.__v);
    }

    $int.__pow__ = function (y) {
        if (y.__number__ != 0x02) return pyjslib['NotImplemented'];
        y = y.__v;
        var v = Math.pow(this.__v, y);
        if ($min_int <= v && v <= $max_int) {
            return new $int(v);
        }
        if (-$max_float_int < v && v < $max_float_int) {
            return new pyjslib['long'](v);
        }
        return new pyjslib['long'](this.__v).__pow__(new pyjslib['long'](y));
    }
})();
""")

# This is the python long implementation. See:
#  - Include/longintrepr.h
#  - Include/longobject.h
#  - Objects/longobject.c
JS("""
(function(){

    var $log2 = Math.log(2);
    var $DigitValue = [
            37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37,
            37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37,
            37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37,
            0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  37, 37, 37, 37, 37, 37,
            37, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
            25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 37, 37, 37, 37,
            37, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
            25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 37, 37, 37, 37,
            37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37,
            37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37,
            37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37,
            37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37,
            37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37,
            37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37,
            37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37,
            37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37,
    ];
    var $log_base_PyLong_BASE = new Array();
    var $convwidth_base = new Array();
    var $convmultmax_base = new Array();
    for (var i = 0; i < 37; i++) {
        $log_base_PyLong_BASE[i] = $convwidth_base[i] = $convmultmax_base[i] = 0;
    }
    var $cdigit = '0123456789abcdefghijklmnopqrstuvwxyz';


    var PyLong_SHIFT = 15;
    var PyLong_MASK = 0x7fff;
    var PyLong_BASE = 0x8000;

    var KARATSUBA_CUTOFF = 70
    var KARATSUBA_SQUARE_CUTOFF = (2 * KARATSUBA_CUTOFF)

    var FIVEARY_CUTOFF = 8

    function array_eq(a, b, n) {
        for (var i = 0 ; i < n; i++) {
            if (a[i] != b[i])
                return false;
        }
        return true;
    }

    function long_normalize(v) {
        var j = v.ob_size < 0 ? -v.ob_size:v.ob_size;
        var i = j;
        while (i > 0 && v.ob_digit[i-1] == 0) {
            i--;
        }
        if (i != j) {
            v.ob_size = v.ob_size < 0 ? -i:i;
        }
        return v;
    }

    function AsScaledDouble(vv) {
        var multiplier = PyLong_BASE; // 1L << PyLong_SHIFT == 1 << 15
        var neg, i, x, nbitsneeded;

        if (vv.ob_size < 0) {
            i = -vv.ob_size;
            neg = true;
        } else if (vv.ob_size > 0) {
            i = vv.ob_size;
            neg = false;
        } else {
            return [0.0, 0];
        }
        --i;
        x = vv.ob_digit[i];
        nbitsneeded = 56;
        while (i > 0 && nbitsneeded > 0) {
            --i;
            x = x * multiplier + vv.ob_digit[i];
            nbitsneeded -= PyLong_SHIFT;
        }
        if (neg) {
            return [-x, i];
        }
        return [x, i];
    }

    function v_iadd(x, m, y, n) {
        var i, carry = 0;
        for (i = 0; i < n; ++i) {
                carry += x[i] + y[i];
                x[i] = carry & PyLong_MASK;
                carry >>= PyLong_SHIFT;
        }
        for (; carry && i < m; ++i) {
                carry += x[i];
                x[i] = carry & PyLong_MASK;
                carry >>= PyLong_SHIFT;
        }
        return carry;
    }

    function v_isub(x, m, y, n) {
        var i, borrow = 0;
        for (i = 0; i < n; ++i) {
                borrow = x[i] - y[i] - borrow;
                x[i] = borrow & PyLong_MASK;
                borrow >>= PyLong_SHIFT;
                borrow &= 1;
        }
        for (; borrow && i < m; ++i) {
                borrow = x[i] - borrow;
                x[i] = borrow & PyLong_MASK;
                borrow >>= PyLong_SHIFT;
                borrow &= 1;
        }
        return borrow;
    }

    //function mul1(a, n) {
    //    return muladd1(a, n, 0);
    //}

    function muladd1(z, a, n, extra) {
        var size_a = a.ob_size < 0 ? -a.ob_size : a.ob_size;
        var carry = extra, i;

        for (i = 0; i < size_a; ++i) {
                carry += a.ob_digit[i] * n;
                z.ob_digit[i] = carry & PyLong_MASK;
                carry >>= PyLong_SHIFT;
        }
        z.ob_digit[i] = carry;
        z.ob_size = i + 1
        return long_normalize(z);
    }

    function inplace_divrem1(pout, pin, pout_idx, pin_idx, size, n) {
        var rem = 0, hi = 0;
        pin_idx += size;
        pout_idx += size;
        while (pin_idx > pin.length) {
            --size;
            --pin_idx;
            pout[--pout_idx] = 0;
        }
        while (--size >= 0) {
            rem = (rem << PyLong_SHIFT) + pin[--pin_idx];
            pout[--pout_idx] = hi = Math.floor(rem / n);
            rem -= hi * n;
        }
        return [rem, pout_idx, pin_idx];
    }

    function divrem1(a, n, prem) {
        var size = a.ob_size < 0 ? -a.ob_size : a.ob_size;
        var z = new $long(0);

        prem[0] = inplace_divrem1(z.ob_digit, a.ob_digit, 0, 0, size, n)[0];
        z.ob_size = size;
        return long_normalize(z);
    }

    function Format(aa, base, addL, newstyle, noBase) {
        var text, str, p, i, bits, sz, sign = '';
        var c_0 = "0".charCodeAt(0);
        var c_a = "a".charCodeAt(0);
        base = base.valueOf()

        if (aa.ob_size == 0) {
            if (addL) {
                text = "0L";
            } else {
                text = "0";
            }
        } else {
            if (aa.ob_size < 0) {
                sign = '-';
                size_a = -aa.ob_size;
            } else {
                size_a = aa.ob_size;
            }
            i = base;
            bits = 0;
            while (i > 1) {
                ++bits;
                i >>>= 1;
            }
            i = addL ? 6 : 5;
            j = size_a * PyLong_SHIFT + bits - 1;
            sz = Math.floor(i + j / bits);
            if (j / PyLong_SHIFT < size_a || sz < i) {
                throw pyjslib['OverflowError']("long is too large to format");
            }
            str = new Array();
            p = sz;
            if (addL) str[--p] = 'L';
            if ((base & (base - 1)) == 0) {
                var accum = 0, accumbits = 0, basebits = 1;
                i = base;
                while ((i >>>= 1) > 1) ++basebits;
                for (i = 0; i < size_a; ++i) {
                    accum |= aa.ob_digit[i] << accumbits;
                    accumbits += PyLong_SHIFT;
                    for (;;) {
                        var cdigit = accum & (base - 1);
                        str[--p] = $cdigit.charAt(cdigit);
                        accumbits -= basebits;
                        accum >>>= basebits;
                        if (i < size_a-1) {
                            if (accumbits < basebits) break;
                        } else if (accum <= 0) break;
                    }
                }
                text = str.join("");
            } else {
                // Not 0, and base not a power of 2.
                var scratch, pin, scratch_idx, pin_idx;
                var powbase = base, power = 1, size = size_a;
               
                for (;;) {
                    var newpow = powbase * base;
                    if (newpow >>> PyLong_SHIFT)  /* doesn't fit in a digit */
                        break;
                    powbase = newpow;
                    ++power;
                }
                scratch = aa.ob_digit.slice(0);
                pin = aa.ob_digit;
                scratch_idx = pin_idx = 0;
                do {
                        var ntostore = power;
                        rem = inplace_divrem1(scratch, pin, scratch_idx, pin_idx, size, powbase);
                        scratch_idx = rem[1];
                        rem = rem[0];
                        pin = scratch;
                        pin_idx = 0;
                        if (pin[size - 1] == 0) {
                            --size;
                        }
                        do {
                            var nextrem = Math.floor(rem / base);
                            str[--p] = $cdigit.charAt(rem - nextrem * base);
                            rem = nextrem;
                            --ntostore;
                        } while (ntostore && (size || rem));
                } while (size !=0);
                text = str.slice(p).join("");
            }
            text = text.lstrip('0');
            if (text == "" || text == "L") text = "0" + text;
        }
        if (noBase !== false) {
            switch (base) {
                case 10:
                    break;
                case 2:
                    text = '0b' + text;
                    break;
                case 8:
                    text = (newstyle ? '0o':(aa.ob_size ? '0': '')) + text;
                    break;
                case 16:
                    text = '0x' + text;
                    break;
                default:
                    text = base + '#' + text
                    break;
            }
        }
        return sign + text;
    }

    function long_divrem(a, b, pdiv, prem) {
        var size_a = a.ob_size < 0 ? -a.ob_size : a.ob_size;
        var size_b = b.ob_size < 0 ? -b.ob_size : b.ob_size;
        var z = null;

        if (size_b == 0) {
            throw pyjslib['ZeroDivisionError']("long division or modulo by zero");
        }
        if (size_a < size_b ||
            (size_a == size_b &&
             a.ob_digit[size_a-1] < b.ob_digit[size_b-1])) {
                // |a| < |b|
                pdiv.ob_size = 0;
                prem.ob_digit = a.ob_digit.slice(0);
                prem.ob_size = a.ob_size;
                return 0;
        }
        if (size_b == 1) {
                rem = [0];
                prem.ob_digit = [0];
                prem.ob_size = 1;
                z = divrem1(a, b.ob_digit[0], prem.ob_digit);
                prem = long_normalize(prem);
        }
        else {
                z = x_divrem(a, b, prem);
        }
        if (z === null) {
            pdiv.ob_size = 0;
        } else {
            pdiv.ob_digit = z.ob_digit.slice(0);
            pdiv.ob_size = z.ob_size;
        }
        if ((a.ob_size < 0) != (b.ob_size < 0))
                pdiv.ob_size = -(pdiv.ob_size);
        if (a.ob_size < 0 && prem.ob_size != 0)
                prem.ob_size = -prem.ob_size;
        return 0;
    }

    function x_divrem(v1, w1, prem) {
        var size_w = w1.ob_size < 0 ? -w1.ob_size : w1.ob_size;
        var d = Math.floor(PyLong_BASE / (w1.ob_digit[size_w-1] + 1));
        var v = muladd1($x_divrem_v, v1, d, 0);
        var w = muladd1($x_divrem_w, w1, d, 0);
        var a, j, k;
        var size_v = v.ob_size < 0 ? -v.ob_size : v.ob_size;
        k = size_v - size_w;
        a = new $long(0);
        a.ob_size = k + 1;

        for (j = size_v; k >= 0; --j, --k) {
            var vj = (j >= size_v) ? 0 : v.ob_digit[j];
            var carry = 0;
            var q, i;

            if (vj == w.ob_digit[size_w-1])
                q = PyLong_MASK;
            else
                q = Math.floor(((vj << PyLong_SHIFT) + v.ob_digit[j-1]) /
                        w.ob_digit[size_w-1]);

            while (w.ob_digit[size_w-2]*q >
                    ((
                        (vj << PyLong_SHIFT)
                        + v.ob_digit[j-1]
                        - q*w.ob_digit[size_w-1]
                                                ) << PyLong_SHIFT)
                    + v.ob_digit[j-2])
                --q;

            for (i = 0; i < size_w && i+k < size_v; ++i) {
                var z = w.ob_digit[i] * q;
                var zz = z >>> PyLong_SHIFT;
                carry += v.ob_digit[i+k] - z
                        + (zz << PyLong_SHIFT);
                v.ob_digit[i+k] = carry & PyLong_MASK;
                // carry = Py_ARITHMETIC_RIGHT_SHIFT(BASE_TWODIGITS_TYPE, carry, PyLong_SHIFT);
                carry >>= PyLong_SHIFT;
                carry -= zz;
            }

            if (i+k < size_v) {
                carry += v.ob_digit[i+k];
                v.ob_digit[i+k] = 0;
            }

            if (carry == 0)
                a.ob_digit[k] = q;
            else {
                a.ob_digit[k] = q-1;
                carry = 0;
                for (i = 0; i < size_w && i+k < size_v; ++i) {
                    carry += v.ob_digit[i+k] + w.ob_digit[i];
                    v.ob_digit[i+k] = carry & PyLong_MASK;
                    // carry = Py_ARITHMETIC_RIGHT_SHIFT( BASE_TWODIGITS_TYPE, carry, PyLong_SHIFT);
                    carry >>= PyLong_SHIFT;
                }
            }
        } /* for j, k */

        i = divrem1(v, d, prem);
        prem.ob_digit = i.ob_digit.slice(0);
        prem.ob_size = i.ob_size;
        return long_normalize(a);
    }

    function x_add(a, b) {
        var size_a = a.ob_size < 0 ? -a.ob_size : a.ob_size;
        var size_b = b.ob_size < 0 ? -b.ob_size : b.ob_size;
        var z = new $long(0);
        var i;
        var carry = 0;

        if (size_a < size_b) {
            var temp = a;
            a = b;
            b = temp;
            temp = size_a;
            size_a = size_b;
            size_b = temp;
        }
        for (i = 0; i < size_b; ++i) {
                carry += a.ob_digit[i] + b.ob_digit[i];
                z.ob_digit[i] = carry & PyLong_MASK;
                carry >>>= PyLong_SHIFT;
        }
        for (; i < size_a; ++i) {
                carry += a.ob_digit[i];
                z.ob_digit[i] = carry & PyLong_MASK;
                carry >>>= PyLong_SHIFT;
        }
        z.ob_digit[i] = carry;
        z.ob_size = i+1;
        return long_normalize(z);
    }

    function x_sub(a, b) {
        var size_a = a.ob_size < 0 ? -a.ob_size : a.ob_size;
        var size_b = b.ob_size < 0 ? -b.ob_size : b.ob_size;
        var z = new $long(0);
        var i;
        var borrow = 0;
        var sign = 1;

        if (size_a < size_b) {
            var temp = a;
            a = b;
            b = temp;
            temp = size_a;
            size_a = size_b;
            size_b = temp;
            sign = -1;
        } else if (size_a == size_b) {
            i = size_a;
            while (--i >= 0 && a.ob_digit[i] == b.ob_digit[i])
                ;
            if (i < 0)
                return z;
            if (a.ob_digit[i] < b.ob_digit[i]) {
                var temp = a;
                a = b;
                b = temp;
                temp = size_a;
                size_a = size_b;
                size_b = temp;
                sign = -1;
            }
            size_a = size_b = i+1;
        }
        for (i = 0; i < size_b; ++i) {
                borrow = a.ob_digit[i] - b.ob_digit[i] - borrow;
                z.ob_digit[i] = borrow & PyLong_MASK;
                borrow >>>= PyLong_SHIFT;
                borrow &= 1;
        }
        for (; i < size_a; ++i) {
                borrow = a.ob_digit[i] - borrow;
                z.ob_digit[i] = borrow & PyLong_MASK;
                borrow >>>= PyLong_SHIFT;
                borrow &= 1;
        }
        z.ob_size = i;
        if (sign < 0)
            z.ob_size = -(z.ob_size);
        return long_normalize(z);
    }

    function x_mul(a, b) {
        var size_a = a.ob_size < 0 ? -a.ob_size : a.ob_size;
        var size_b = b.ob_size < 0 ? -b.ob_size : b.ob_size;
        var z = new $long(0);
        var i, s;

        z.ob_size = size_a + size_b;
        for (i = 0; i < z.ob_size; i++) {
            z.ob_digit[i] = 0;
        }
        if (size_a == size_b && array_eq(a.ob_digit, b.ob_digit, size_a)) {
            // Efficient squaring per HAC, Algorithm 14.16:
            for (i = 0; i < size_a; ++i) {
                var carry;
                var f = a.ob_digit[i];
                var pz = (i << 1);
                var pa = i + 1;
                var paend = size_a;

                carry = z.ob_digit[pz] + f * f;
                z.ob_digit[pz++] = carry & PyLong_MASK;
                carry >>>= PyLong_SHIFT;

                f <<= 1;
                while (pa < paend) {
                    carry += z.ob_digit[pz] + a.ob_digit[pa++] * f;
                    z.ob_digit[pz++] = carry & PyLong_MASK;
                    carry >>>= PyLong_SHIFT;
                }
                if (carry) {
                    carry += z.ob_digit[pz];
                    z.ob_digit[pz++] = carry & PyLong_MASK;
                    carry >>>= PyLong_SHIFT;
                }
                if (carry) {
                    z.ob_digit[pz] += carry & PyLong_MASK;
                }
            }
        }
        else {  // a is not the same as b -- gradeschool long mult
            for (i = 0; i < size_a; ++i) {
                var carry = 0;
                var f = a.ob_digit[i];
                var pz = i;
                var pb = 0;
                var pbend = size_b;

                while (pb < pbend) {
                    carry += z.ob_digit[pz] + b.ob_digit[pb++] * f;
                    z.ob_digit[pz++] = carry & PyLong_MASK;
                    carry >>>= PyLong_SHIFT;
                }
                if (carry) {
                    z.ob_digit[pz] += carry & PyLong_MASK;
                }
            }
        }
        z.ob_size = z.ob_digit.length;
        return long_normalize(z);
    }

    function l_divmod(v, w, pdiv, pmod) {
        var div = $l_divmod_div, 
            mod = $l_divmod_mod; 

        if (long_divrem(v, w, div, mod) < 0)
                return -1;
        if (pdiv == null && pmod == null) return 0;

        if ((mod.ob_size < 0 && w.ob_size > 0) ||
            (mod.ob_size > 0 && w.ob_size < 0)) {
                mod = mod.__add__(w);
                div = div.__sub__($const_long_1);
        }
        if (pdiv !== null) {
            pdiv.ob_digit = div.ob_digit.slice(0);
            pdiv.ob_size = div.ob_size;
        }
        if (pmod !== null) {
            pmod.ob_digit = mod.ob_digit.slice(0);
            pmod.ob_size = mod.ob_size;
        }
        return 0;
    }




    var $long = pyjslib['long'] = function(value, radix) {
        var v, i;
        if (!radix || radix.valueOf() == 0) {
            if (typeof value == 'undefined') {
                throw pyjslib.TypeError("long() takes at least 1 argument");
            }
            switch (value.__number__) {
                case 0x01:
                    value = value > 0 ? Math.floor(value) : Math.ceil(value);
                    break;
                case 0x02:
                    break;
                case 0x04:
                    return value;
            }
            radix = null;
        }
        if (typeof this != 'object' || this.__number__ != 0x04) return new $long(value, radix);

        v = value;
        this.ob_size = 0;
        this.ob_digit = new Array();
        if (v.__number__) {
            if (radix) {
                throw pyjslib.TypeError("long() can't convert non-string with explicit base");
            }
            if (v.__number__ == 0x04) {
                var size = v.ob_size < 0 ? -v.ob_size:v.ob_size;
                for (var i = 0; i < size; i++) {
                    this.ob_digit[i] = v.ob_digit[i];
                }
                this.ob_size = v.ob_size;
                return this;
            }
            if (v.__number__ == 0x02) {
                var neg = false;
                var ndig = 0;
                v = v.valueOf();

                if (v < 0) {
                    v = -v;
                    neg = true;
                }
                // Count the number of Python digits.
                t = v;
                while (t) {
                    this.ob_digit[ndig] = t & PyLong_MASK;
                    t >>>= PyLong_SHIFT;
                    ++ndig;
                }
                this.ob_size = neg ? -ndig : ndig;
                return this;
            }
            if (v.__number__ == 0x01) {
                var ndig, frac, expo, bits;
                var neg = false;

                if (isNaN(v)) {
                    throw pyjslib['ValueError']('cannot convert float NaN to integer');
                }
                if (!isFinite(v)) {
                    throw pyjslib['OverflowError']('cannot convert float infinity to integer');
                }
                if (v == 0) {
                    this.ob_digit[0] = 0;
                    this.ob_size = 0;
                    return this;
                }
                if (v < 0) {
                    v = -v;
                    neg = true;
                }
                // frac = frexp(dval, &expo); // dval = frac*2**expo; 0.0 <= frac < 1.0
                if (v == 0) {
                    frac = 0;
                    expo = 0;
                } else {
                    expo = Math.log(v)/$log2;
                    expo = (expo < 0 ? Math.ceil(expo):Math.floor(expo)) + 1;
                    frac = v / Math.pow(2.0, expo);
                }
                if (expo <= 0) {
                    return this;
                }
                ndig = Math.floor((expo-1) / PyLong_SHIFT) + 1;
                // ldexp(a,b) == a * (2**b)
                frac = frac * Math.pow(2.0, ((expo-1) % PyLong_SHIFT) + 1);
                for (var i = ndig; --i >= 0;) {
                    bits = Math.floor(frac);
                    this.ob_digit[i] = bits;
                    frac -= bits;
                    frac = frac * Math.pow(2.0, PyLong_SHIFT);
                }
                this.ob_size = neg ? -ndig : ndig;
                return this;
            }
            throw pyjslib['ValueError']('cannot convert ' + pyjslib['repr'](value) + 'to integer');
        } else if (typeof v == 'string') {
            var nchars;
            var text = value.lstrip();
            var i = 0;
            var neg = false;

            switch (text.charAt(0)) {
                case '-':
                    neg = true;
                case '+':
                    text = text.slice(1).lstrip();
            }

            if (!radix) {
                if (text == '0' || text.charAt(0) != '0') {
                    radix = 10;
                } else {
                    switch (text.charAt(1)) {
                        case 'x':
                        case 'X':
                            radix = 16;
                            break;
                        case 'o':
                        case 'O':
                            radix = 8;
                            break;
                        case 'b':
                        case 'B':
                            radix = 2;
                            break;
                        default:
                            radix = 8;
                            break;
                    }
                }
            } else if (radix < 1 || radix > 36) {
                throw pyjslib['ValueError']("long() arg 2 must be >= 2 and <= 36");
            }
            if (text.charAt(0) == '0' && text.length > 1) {
                switch (text.charAt(1)) {
                    case 'x':
                    case 'X':
                        if (radix == 16) text = text.slice(2);
                        break;
                    case 'o':
                    case 'O':
                        if (radix == 8) text = text.slice(2);
                        break;
                    case 'b':
                    case 'B':
                        if (radix == 2) text = text.slice(2);
                        break;

                }
            }
            if ((radix & (radix - 1)) == 0) {
                // binary base: 2, 4, 8, ...
                var n, bits_per_char, accum, bits_in_accum, k, pdigit;
                var p = 0;

                n = radix;
                for (bits_per_char = -1; n; ++bits_per_char) {
                    n >>>= 1;
                }
                n = 0;
                while ($DigitValue[text.charCodeAt(p)] < radix) {
                    p++;
                }
                nchars = p;
                n = p * bits_per_char + PyLong_SHIFT-1; //14 = PyLong_SHIFT - 1
                if (n / bits_per_char < p) {
                    throw pyjslib['ValueError']("long string too large to convert");
                }
                this.ob_size = n = Math.floor(n/PyLong_SHIFT);
                for (var i = 0; i < n; i++) {
                    this.ob_digit[i] = 0;
                }
                // Read string from right, and fill in long from left
                accum = 0;
                bits_in_accum = 0;
                pdigit = 0;
                while (--p >= 0) {
                    k = $DigitValue[text.charCodeAt(p)];
                    accum |= k << bits_in_accum;
                    bits_in_accum += bits_per_char;
                    if (bits_in_accum >= PyLong_SHIFT) {
                        this.ob_digit[pdigit] = accum & PyLong_MASK;
                        pdigit++;
                        accum >>>= PyLong_SHIFT;
                        bits_in_accum -= PyLong_SHIFT;
                    }
                }
                if (bits_in_accum) {
                    this.ob_digit[pdigit++] = accum;
                }
                while (pdigit < n) {
                    this.ob_digit[pdigit++] = 0;
                }
                long_normalize(this);
            } else {
                // Non-binary bases (such as radix == 10)
                var c, i, convwidth, convmultmax, convmult, pz, pzstop, scan, size_z;

                if ($log_base_PyLong_BASE[radix] == 0.0) {
                    var i = 1;
                    convmax = radix;
                    $log_base_PyLong_BASE[radix] = Math.log(radix) / Math.log(PyLong_BASE);
                    for (;;) {
                        var next = convmax * radix;
                        if (next > PyLong_BASE) break;
                        convmax = next;
                        ++i;
                    }
                    $convmultmax_base[radix] = convmax;
                    $convwidth_base[radix] = i;
                }
                scan = 0;
                while ($DigitValue[text.charCodeAt(scan)] < radix)
                    ++scan;
                nchars = scan;
                size_z = scan * $log_base_PyLong_BASE[radix] + 1;
                for (var i = 0; i < size_z; i ++) {
                    this.ob_digit[i] = 0;
                }
                this.ob_size = 0;
                convwidth = $convwidth_base[radix];
                convmultmax = $convmultmax_base[radix];
                for (var str = 0; str < scan;) {
                    c = $DigitValue[text.charCodeAt(str++)];
                    for (i = 1; i < convwidth && str != scan; ++i, ++str) {
                        c = c * radix + $DigitValue[text.charCodeAt(str)];
                    }
                    convmult = convmultmax;
                    if (i != convwidth) {
                        convmult = radix;
                        for ( ; i > 1; --i) convmult *= radix;
                    }
                    pz = 0;
                    pzstop = this.ob_size;
                    for (; pz < pzstop; ++pz) {
                        c += this.ob_digit[pz] * convmult;
                        this.ob_digit[pz] = c & PyLong_MASK;
                        c >>>= PyLong_SHIFT;
                    }
                    if (c) {
                        if (this.ob_size < size_z) {
                            this.ob_digit[pz] = c;
                            this.ob_size++;
                        } else {
                            this.ob_digit[this.ob_size] = c;
                        }
                    }
                }
            }
            text = text.slice(nchars);
            if (neg) this.ob_size = -this.ob_size;
            if (text.charAt(0) == 'l' || text.charAt(0) == 'L') text = text.slice(1);
            text = text.lstrip();
            if (text.length === 0) {
                return this;
            }
            throw pyjslib.ValueError("invalid literal for long() with base " +
                                     radix + ": " + value);
        } else {
            throw pyjslib.TypeError("TypeError: long() argument must be a string or a number");
        }
        if (isNaN(v) || !isFinite(v)) {
            throw pyjslib.ValueError("invalid literal for long() with base " + radix + ": '" + v + "'")
        }
        return this;
    }
    $long.__init__ = function () {};
    $long.__number__ = 0x04;
    $long.__name__ = 'long';
    $long.prototype = $long;
    $long.__class__ = $long;
    $long.ob_size = 0;

    $long.toExponential = function (fractionDigits) {
        return (typeof fractionDigits == 'undefined' || fractionDigits === null) ? this.__v.toExponential() : this.__v.toExponential(fractionDigits);
    }

    $long.toFixed = function (digits) {
        return (typeof digits == 'undefined' || digits === null) ? this.__v.toFixed() : this.__v.toFixed(digits);
    }

    $long.toLocaleString = function () {
        return this.__v.toLocaleString();
    }

    $long.toPrecision = function (precision) {
        return (typeof precision == 'undefined' || precision === null) ? this.__v.toPrecision() : this.__v.toPrecision(precision);
    }

    $long.toString = function (radix) {
        return (typeof radix == 'undefined' || radix === null) ? Format(this, 10, false, false) : Format(this, radix, false, false, false);
    }

    $long.valueOf = function() {
        var x, v;
        x = AsScaledDouble(this);
        // ldexp(a,b) == a * (2**b)
        v = x[0] * Math.pow(2.0, x[1] * PyLong_SHIFT);
        if (!isFinite(v)) {
            throw pyjslib['OverflowError']('long int too large to convert to float');
        }
        return v;
    }

    $long.__str__ = function () {
        return Format(this, 10, false, false);
    }

    $long.__repr__ = function () {
        return Format(this, 10, true, false);
    }

    $long.__nonzero__ = function () {
        return this.ob_size != 0;
    }

    $long.__cmp__ = function (b) {
        var sign;
 
        if (this.ob_size != b.ob_size) {
            if (this.ob_size < b.ob_size) return -1;
            return 1;
        }
        var i = this.ob_size < 0 ? - this.ob_size : this.ob_size;
        while (--i >= 0 && this.ob_digit[i] == b.ob_digit[i])
            ;
        if (i < 0) return 0;
        if (this.ob_digit[i] < b.ob_digit[i]) {
            if (this.ob_size < 0) return 1;
            return -1;
        }
        if (this.ob_size < 0) return -1;
        return 1;
    }

    $long.__hash__ = function () {
        var s = this.__str__();
        var v = this.valueOf();
        if (v.toString() == s) {
            return v;
        }
        return s;
    }

    $long.__invert__ = function () {
        var x = this.__add__($const_long_1);
        x.ob_size = -x.ob_size;
        return x;
    }

    $long.__neg__ = function () {
        var x = new $long(0);
        x.ob_digit = this.ob_digit.slice(0);
        x.ob_size = -this.ob_size;
        return x;
    }

    $long.__abs__ = function () {
        if (this.ob_size >= 0) return this;
        var x = new $long(0);
        x.ob_digit = this.ob_digit.slice(0);
        x.ob_size = -x.ob_size;
        return x;
    }

    $long.__lshift = function (y) {
        var a, z, wordshift, remshift, oldsize, newsize, 
            accum, i, j;
        if (y < 0) {
            throw pyjslib['ValueError']('negative shift count');
        }
        if (y >= $max_float_int) {
            throw pyjslib['ValueError']('outrageous left shift count');
        }
        a = this;

        wordshift = Math.floor(y / PyLong_SHIFT);
        remshift  = y - wordshift * PyLong_SHIFT;

        oldsize = a.ob_size < 0 ? -a.ob_size : a.ob_size;
        newsize = oldsize + wordshift;
        if (remshift) ++newsize;
        z = new $long(0);
        z.ob_size = a.ob_size < 0 ? -newsize : newsize;
        for (i = 0; i < wordshift; i++) {
            z.ob_digit[i] = 0;
        }
        accum = 0;
        for (i = wordshift, j = 0; j < oldsize; i++, j++) {
            accum |= a.ob_digit[j] << remshift;
            z.ob_digit[i] = accum & PyLong_MASK;
            accum >>>= PyLong_SHIFT;
        }
        if (remshift) {
            z.ob_digit[newsize-1] = accum;
        }
        z = long_normalize(z);
        return z;
    }

    $long.__lshift__ = function (y) {
        switch (y.__number__) {
            case 0x01:
                if (y == Math.floor(y)) return this.__lshift(y);
                break;
            case 0x02:
                return this.__lshift(y.__v);
            case 0x04:
                y = y.valueOf();
                return this.__lshift(y);
        }
        return pyjslib['NotImplemented'];
    }

    $long.__rlshift__ = function (y) {
        switch (y.__number__) {
            case 0x02:
                return (new $long(y.__v)).__lshift(this.valueOf());
            case 0x04:
                return y.__lshift(this.valueOf());
        }
        return pyjslib['NotImplemented'];
    }

    $long.__rshift = function (y) {
        var a, z, size, wordshift, newsize, loshift, hishift,
            lomask, himask, i, j;
        if (y.__number__ != 0x01) {
            y = y.valueOf();
        } else {
            if (y != Math.floor(y)) {
                pyjslib['TypeError']("unsupported operand type(s) for >>: 'long' and 'float'");
            }
        }
        if (y < 0) {
            throw pyjslib['ValueError']('negative shift count');
        }
        if (y >= $max_float_int) {
            throw pyjslib['ValueError']('shift count too big');
        }
        a = this;
        size = this.ob_size;
        if (this.ob_size < 0) {
            size = -size;
            a = this.__add__($const_long_1);
            a.ob_size = -a.ob_size;
        }

        wordshift = Math.floor(y / PyLong_SHIFT);
        newsize = size - wordshift;
        if (newsize <= 0) {
            z = $const_long_0;
        } else {
            loshift = y % PyLong_SHIFT;
            hishift = PyLong_SHIFT - loshift;
            lomask = (1 << hishift) - 1;
            himask = PyLong_MASK ^ lomask;
            z = new $long(0);
            z.ob_size = a.ob_size < 0 ? -newsize : newsize;
            for (i = 0, j = wordshift; i < newsize; i++, j++) {
                z.ob_digit[i] = (a.ob_digit[j] >>> loshift) & lomask;
                if (i+1 < newsize) {
                    z.ob_digit[i] |=
                      (a.ob_digit[j+1] << hishift) & himask;
                }
            }
            z = long_normalize(z);
        }

        if (this.ob_size < 0) {
            z = z.__add__($const_long_1);
            z.ob_size = -z.ob_size;
        }
        return z;
    }

    $long.__rshift__ = function (y) {
        switch (y.__number__) {
            case 0x01:
                if (y == Math.floor(y)) return this.__rshift(y);
                break;
            case 0x02:
                return this.__rshift(y.__v);
            case 0x04:
                y = y.valueOf();
                return this.__rshift(y);
        }
        return pyjslib['NotImplemented'];
    }

    $long.__rrshift__ = function (y) {
        switch (y.__number__) {
            case 0x02:
                return (new $long(y.__v)).__rshift(this.valueOf());
            case 0x04:
                return y.__rshift(this.valueOf());
        }
        return pyjslib['NotImplemented'];
    }

    $long.__and = function (b) {
        var a, maska, maskb, negz, size_a, size_b, size_z,
            i, z, diga, digb, v, op;

        a = this;

        if (a.ob_size < 0) {
            a = a.__invert__();
            maska = PyLong_MASK;
        } else {
            maska = 0;
        }
        if (b.ob_size < 0) {
            b = b.__invert__();
            maskb = PyLong_MASK;
        } else {
            maskb = 0;
        }
        negz = 0;


            op = '&'
            if (maska && maskb) {
                op = '|';
                maska ^= PyLong_MASK;
                maskb ^= PyLong_MASK;
                negz = -1;
            }


        size_a = a.ob_size;
        size_b = b.ob_size;
        size_z = op == '&'
                    ? (maska
                        ? size_b
                        : (maskb ? size_a : (size_a < size_b ? size_a : size_b)))
                    : (size_a > size_b ? size_a : size_b);
        z = new $long(0);
        z.ob_size = size_z;

        switch (op) {
            case '&':
                for (i = 0; i < size_z; ++i) {
                    diga = (i < size_a ? a.ob_digit[i] : 0) ^ maska;
                    digb = (i < size_b ? b.ob_digit[i] : 0) ^ maskb;
                    z.ob_digit[i] = diga & digb;
                }
                break;
            case '|':
                for (i = 0; i < size_z; ++i) {
                    diga = (i < size_a ? a.ob_digit[i] : 0) ^ maska;
                    digb = (i < size_b ? b.ob_digit[i] : 0) ^ maskb;
                    z.ob_digit[i] = diga | digb;
                }
                break;
            case '^':
                for (i = 0; i < size_z; ++i) {
                    diga = (i < size_a ? a.ob_digit[i] : 0) ^ maska;
                    digb = (i < size_b ? b.ob_digit[i] : 0) ^ maskb;
                    z.ob_digit[i] = diga ^ digb;
                }
                break;
        }
        z = long_normalize(z);
        if (negz == 0) {
            return z;
        }
        return z.__invert__();
    }

    $long.__and__ = function (y) {
        switch (y.__number__) {
            case 0x01:
                if (y == Math.floor(y)) return this.__and(new $long(y));
                break;
            case 0x02:
                return this.__and(new $long(y.__v));
            case 0x04:
                return this.__and(y);
        }
        return pyjslib['NotImplemented'];
    }

    $long.__rand__ = $long.__and__;

    $long.__xor = function (b) {
        var a,maska, maskb, negz, size_a, size_b, size_z,
            i, z, diga, digb, v, op;

        a = this;

        if (a.ob_size < 0) {
            a = a.__invert__();
            maska = PyLong_MASK;
        } else {
            maska = 0;
        }
        if (b.ob_size < 0) {
            b = b.__invert__();
            maskb = PyLong_MASK;
        } else {
            maskb = 0;
        }
        negz = 0;


            op = '^'
            if (maska != maskb) {
                maska ^= PyLong_MASK;
                negz = -1;
            }


        size_a = a.ob_size;
        size_b = b.ob_size;
        size_z = op == '&'
                    ? (maska
                        ? size_b
                        : (maskb ? size_a : (size_a < size_b ? size_a : size_b)))
                    : (size_a > size_b ? size_a : size_b);
        z = new $long(0);
        z.ob_size = size_z;

        switch (op) {
            case '&':
                for (i = 0; i < size_z; ++i) {
                    diga = (i < size_a ? a.ob_digit[i] : 0) ^ maska;
                    digb = (i < size_b ? b.ob_digit[i] : 0) ^ maskb;
                    z.ob_digit[i] = diga & digb;
                }
                break;
            case '|':
                for (i = 0; i < size_z; ++i) {
                    diga = (i < size_a ? a.ob_digit[i] : 0) ^ maska;
                    digb = (i < size_b ? b.ob_digit[i] : 0) ^ maskb;
                    z.ob_digit[i] = diga | digb;
                }
                break;
            case '^':
                for (i = 0; i < size_z; ++i) {
                    diga = (i < size_a ? a.ob_digit[i] : 0) ^ maska;
                    digb = (i < size_b ? b.ob_digit[i] : 0) ^ maskb;
                    z.ob_digit[i] = diga ^ digb;
                }
                break;
        }
        z = long_normalize(z);
        if (negz == 0) {
            return z;
        }
        return z.__invert__();
    }

    $long.__xor__ = function (y) {
        switch (y.__number__) {
            case 0x01:
                if (y == Math.floor(y)) return this.__xor(new $long(y));
                break;
            case 0x02:
                return this.__xor(new $long(y.__v));
            case 0x04:
                return this.__xor(y);
        }
        return pyjslib['NotImplemented'];
    }

    $long.__rxor__ = $long.__xor__;

    $long.__or = function (b) {
        var a, maska, maskb, negz, size_a, size_b, size_z,
            i, z, diga, digb, v, op;

        a = this;

        if (a.ob_size < 0) {
            a = a.__invert__();
            maska = PyLong_MASK;
        } else {
            maska = 0;
        }
        if (b.ob_size < 0) {
            b = b.__invert__();
            maskb = PyLong_MASK;
        } else {
            maskb = 0;
        }
        negz = 0;


            op = '|';
            if (maska || maskb) {
                op = '&';
                maska ^= PyLong_MASK;
                maskb ^= PyLong_MASK;
                negz = -1;
            }


        size_a = a.ob_size;
        size_b = b.ob_size;
        size_z = op == '&'
                    ? (maska
                        ? size_b
                        : (maskb ? size_a : (size_a < size_b ? size_a : size_b)))
                    : (size_a > size_b ? size_a : size_b);
        z = new $long(0);
        z.ob_size = size_z;

        switch (op) {
            case '&':
                for (i = 0; i < size_z; ++i) {
                    diga = (i < size_a ? a.ob_digit[i] : 0) ^ maska;
                    digb = (i < size_b ? b.ob_digit[i] : 0) ^ maskb;
                    z.ob_digit[i] = diga & digb;
                }
                break;
            case '|':
                for (i = 0; i < size_z; ++i) {
                    diga = (i < size_a ? a.ob_digit[i] : 0) ^ maska;
                    digb = (i < size_b ? b.ob_digit[i] : 0) ^ maskb;
                    z.ob_digit[i] = diga | digb;
                }
                break;
            case '^':
                for (i = 0; i < size_z; ++i) {
                    diga = (i < size_a ? a.ob_digit[i] : 0) ^ maska;
                    digb = (i < size_b ? b.ob_digit[i] : 0) ^ maskb;
                    z.ob_digit[i] = diga ^ digb;
                }
                break;
        }
        z = long_normalize(z);
        if (negz == 0) {
            return z;
        }
        return z.__invert__();
    }

    $long.__or__ = function (y) {
        switch (y.__number__) {
            case 0x01:
                if (y == Math.floor(y)) return this.__or(new $long(y));
                break;
            case 0x02:
                return this.__or(new $long(y.__v));
            case 0x04:
                return this.__or(y);
        }
        return pyjslib['NotImplemented'];
    }

    $long.__ror__ = $long.__or__;

    $long.__oct__ = function () {
        return Format(this, 8, true, false);
    }

    $long.__hex__ = function () {
        return Format(this, 16, true, false);
    }

    $long.__add = function (b) {
        var a = this, z;
        if (a.ob_size < 0) {
            if (b.ob_size < 0) {
                z = x_add(a, b);
                z.ob_size = -(z.ob_size);
            }
            else {
                z = x_sub(b, a);
            }
        }
        else {
            z = b.ob_size < 0 ? x_sub(a, b) : x_add(a, b);
        }
        return z;
    }

    $long.__add__ = function (y) {
        switch (y.__number__) {
            case 0x02:
                return this.__add(new $long(y.__v));
            case 0x04:
                return this.__add(y);
        }
        return pyjslib['NotImplemented'];
    }

    $long.__radd__ = $long.__add__;

    $long.__sub = function (b) {
        var a = this, z;
        if (a.ob_size < 0) {
            z = b.ob_size < 0 ? x_sub(a, b) : x_add(a, b);
            z.ob_size = -(z.ob_size);
        }
        else {
            z = b.ob_size < 0 ?  x_add(a, b) : x_sub(a, b);
        }
        return z;
    }

    $long.__sub__ = function (y) {
        switch (y.__number__) {
            case 0x02:
                return this.__sub(new $long(y.__v));
            case 0x04:
                return this.__sub(y);
        }
        return pyjslib['NotImplemented'];
    }

    $long.__rsub__ = function (y) {
        switch (y.__number__) {
            case 0x02:
                return (new $long(y.__v)).__sub(this);
            case 0x04:
                return y.__sub(this);
        }
        return pyjslib['NotImplemented'];
    }

    $long.__mul = function (b) {
        //var z = k_mul(a, b);
        var z = x_mul(this, b);
        if ((this.ob_size ^ b.ob_size) < 0)
            z.ob_size = -(z.ob_size);
        return z;
    }

    $long.__mul__ = function (y) {
        switch (y.__number__) {
            case 0x02:
                return this.__mul(new $long(y.__v));
            case 0x04:
                return this.__mul(y);
        }
        return pyjslib['NotImplemented'];
    }

    $long.__rmul__ = $long.__mul__;

    $long.__div = function (b) {
        var div = new $long(0);
        l_divmod(this, b, div, null);
        return div;
    }

    $long.__div__ = function (y) {
        switch (y.__number__) {
            case 0x02:
                return this.__sub(new $long(y.__v));
            case 0x04:
                return this.__sub(y);
        }
        return pyjslib['NotImplemented'];
    }

    $long.__rdiv__ = function (y) {
        switch (y.__number__) {
            case 0x02:
                return (new $long(y.__v)).__div(this);
            case 0x04:
                return y.__div(this);
        }
        return pyjslib['NotImplemented'];
    }

    $long.__mod = function (b) {
        var mod = new $long(0);
        l_divmod(this, b, null, mod);
        return mod;
    }

    $long.__mod__ = function (y) {
        switch (y.__number__) {
            case 0x02:
                return this.__mod(new $long(y.__v));
            case 0x04:
                return this.__mod(y);
        }
        return pyjslib['NotImplemented'];
    }

    $long.__rmod__ = function (y) {
        switch (y.__number__) {
            case 0x02:
                return (new $long(y.__v)).__mod(this);
            case 0x04:
                return y.__mod(this);
        }
        return pyjslib['NotImplemented'];
    }

    $long.__divmod = function (b) {
        var div = new $long(0);
        var mod = new $long(0);
        l_divmod(this, b, div, mod);
        return pyjslib['tuple']([div, mod]);
    }

    $long.__divmod__ = function (y) {
        switch (y.__number__) {
            case 0x02:
                return this.__divmod(new $long(y.__v));
            case 0x04:
                return this.__divmod(y);
        }
        return pyjslib['NotImplemented'];
    }

    $long.__rdivmod__ = function (y) {
        switch (y.__number__) {
            case 0x02:
                return (new $long(y.__v)).__divmod(this);
            case 0x04:
                return y.__divmod(this);
        }
        return pyjslib['NotImplemented'];
    }

    $long.__floordiv = function (b) {
        var div = new $long(0);
        l_divmod(this, b, div, null);
        return div;
    }

    $long.__floordiv__ = function (y) {
        switch (y.__number__) {
            case 0x02:
                return this.__floordiv(new $long(y.__v));
            case 0x04:
                return this.__floordiv(y);
        }
        return pyjslib['NotImplemented'];
    }

    $long.__rfloordiv__ = function (y) {
        switch (y.__number__) {
            case 0x02:
                return (new $long(y.__v)).__floordiv(this);
            case 0x04:
                return y.__floordiv(this);
        }
        return pyjslib['NotImplemented'];
    }

    $long.__pow = function (w, x) {
        var v = this;
        var a, b, c, negativeOutput = 0, z, i, j, k, temp, bi;
        var table = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];

        a = this;
        b = w.__number__ == 0x04 ? w : new $long(w);
        if (x === null || typeof x == 'undefined') {
            c = null;
        } else {
            c = x.__number__ == 0x04 ? x : new $long(x);
        }

        if (b.ob_size < 0) {
            if (c != null) {
                throw pyjslib['TypeError']("pow() 2nd argument cannot be negative when 3rd argument specified");
            }
            return Math.pow(v.valueOf(), w.valueOf());
        }

        if (c !== null) {
            if (c.ob_size == 0) {
                throw pyjslib['ValueError']("pow() 3rd argument cannot be 0");
            }
            if (c.ob_size < 0) {
                negativeOutput = 1;
                temp = $pow_temp_c;
                temp.ob_digit = c.ob_digit.slice(0);
                temp.ob_size = -c.ob_size;
                c = temp;
            }
            if (c.ob_size == 1 && c.ob_digit[0] == 1) {
                return $const_long_0;
            }
            if (a.ob_size < 0) {
                temp = $pow_temp_a;
                l_divmod(a, c, null, temp);
                a = temp;
            }
        }
        z = new $long(1);
        temp = $pow_temp_z;
        if (b.ob_size <= FIVEARY_CUTOFF) {
            for (i = b.ob_size - 1; i >= 0; --i) {
                bi = b.ob_digit[i];
                for (j = 1 << (PyLong_SHIFT-1); j != 0; j >>>= 1) {
                    z = z.__mul(z);
                    if (c !== null) {
                        l_divmod(z, c, null, temp)
                        z.ob_digit = temp.ob_digit.slice(0);
                        z.ob_size = temp.ob_size;
                    }
                    if (bi & j) {
                        z = z.__mul(a);
                        if (c !== null) {
                            l_divmod(z, c, null, temp)
                            z.ob_digit = temp.ob_digit.slice(0);
                            z.ob_size = temp.ob_size;
                        }
                    }
                }
            }
        } else {
            table[0] = z;
            for (i = 1; i < 32; ++i) {
                table[i] = table[i-1].__mul(a);
                if (c !== null) {
                    l_divmod(table[i], c, null, temp)
                    table[i].ob_digit = temp.ob_digit.slice(0);
                    table[i].ob_size = temp.ob_size;
                }
            }
            for (i = b.ob_size - 1; i >= 0; --i) {
                bi = b.ob_digit[i];
                for (j = PyLong_SHIFT - 5; j >= 0; j -= 5) {
                    var index = (bi >>> j) & 0x1f;
                    for (k = 0; k < 5; ++k) {
                        z = z.__mul(z);
                        if (c !== null) {
                            l_divmod(z, c, null, temp)
                            z.ob_digit = temp.ob_digit.slice(0);
                            z.ob_size = temp.ob_size;
                        }
                    }
                    if (index) {
                        z = z.__mul(table[index]);
                        if (c !== null) {
                            l_divmod(z, c, null, temp)
                            z.ob_digit = temp.ob_digit.slice(0);
                            z.ob_size = temp.ob_size;
                        }
                    }
                }
            }
        }

        if ((c !== null) && negativeOutput && 
            (z.ob_size != 0) && (c.ob_size != 0)) {
            z = z.__sub__(c);
        }
        return z;
    }

    $long.__pow__ = function (y, z) {
        switch (y.__number__) {
            case 0x02:
                if (typeof z == 'undefined')
                    return this.__pow(new $long(y.__v), null);
                switch (z.__number) {
                    case 0x02:
                        return this.__pow(new $long(y.__v), new $long(z));
                    case 0x04:
                        return this.__pow(new $long(y.__v), z);
                }
                break;
            case 0x04:
                if (typeof z == 'undefined')
                    return this.__pow(y, null);
                switch (z.__number) {
                    case 0x02:
                        return this.__pow(y, new $long(z));
                    case 0x04:
                        return this.__pow(y, z);
                }
                break;
        }
        return pyjslib['NotImplemented'];
    }


    var $const_long_0 = new $long(0),
        $const_long_1 = new $long(1);
    // Since javascript is single threaded:
    var $l_divmod_div = new $long(0),
        $l_divmod_mod = new $long(0),
        $x_divrem_v = new $long(0),
        $x_divrem_w = new $long(0),
        $pow_temp_a = new $long(0),
        $pow_temp_c = new $long(0),
        $pow_temp_z = new $long(0);
})();

""")


"""@CONSTANT_DECLARATION@"""

class NotImplementedType(object):
    def __repr__(self):
        return "<type 'NotImplementedType'>"
    def __str__(self):
        self.__repr__()
    def toString(self):
        self.__repr__()
NotImplemented = NotImplementedType()

class List:
    @compiler.noSourceTracking
    def __init__(self, data=None):
        JS("""
        self.l = [];
        self.extend(data);
        """)

    @compiler.noSourceTracking
    def append(self, item):
        JS("""self.l[self.l.length] = item;""")

    @compiler.noSourceTracking
    def extend(self, data):
        JS("""
        if (pyjslib.isArray(data)) {
            n = self.l.length;
            for (var i=0; i < data.length; i++) {
                self.l[n+i]=data[i];
            }
        } else if (pyjslib.isIteratable(data)) {
            var iter=data.__iter__();
            var i=self.l.length;
            try {
                while (true) {
                    var item=iter.next();
                    self.l[i++]=item;
                    }
                }
            catch (e) {
                if (e.__name__ != 'StopIteration') {
                    throw e;
                }
            }
        }
        """)

    @compiler.noSourceTracking
    def remove(self, value):
        JS("""
        var index=self.index(value);
        if (index<0) {
            throw(pyjslib.ValueError("list.remove(x): x not in list"));
        }
        self.l.splice(index, 1);
        return true;
        """)

    @compiler.noSourceTracking
    def index(self, value, start=0):
        JS("""
        start = start.valueOf();
        if (typeof value == 'number' || typeof value == 'string') {
            start = self.l.indexOf(value, start);
            if (start >= 0)
                return start;
        } else {
            var len = self.l.length >>> 0;

            start = (start < 0)
                    ? Math.ceil(start)
                    : Math.floor(start);
            if (start < 0)
                start += len;

            for (; start < len; start++) {
                if (start in self.l &&
                    pyjslib.cmp(self.l[start], value) == 0)
                    return start;
            }
        }
        """)
        raise ValueError("list.index(x): x not in list")

    @compiler.noSourceTracking
    def insert(self, index, value):
        JS("""    var a = self.l; self.l=a.slice(0, index).concat(value, a.slice(index));""")

    @compiler.noSourceTracking
    def pop(self, index = -1):
        JS("""
        index = index.valueOf();
        if (index<0) index += self.l.length;
        if (index < 0 || index >= self.l.length) {
            if (self.l.length == 0) {
                throw(pyjslib.IndexError("pop from empty list"));
            }
            throw(pyjslib.IndexError("pop index out of range"));
        }
        var a = self.l[index];
        self.l.splice(index, 1);
        return a;
        """)

    @compiler.noSourceTracking
    def __cmp__(self, l):
        if not isinstance(l, List):
            return -1
        ll = len(self) - len(l)
        if ll != 0:
            return ll
        for x in range(len(l)):
            ll = cmp(self.__getitem__(x), l[x])
            if ll != 0:
                return ll
        return 0

    @compiler.noSourceTracking
    def __getslice__(self, lower, upper):
        JS("""
        if (upper==null) return pyjslib.List(self.l.slice(lower));
        return pyjslib.List(self.l.slice(lower, upper));
        """)

    def __delslice__(self, lower, upper):
        JS("""
        var n = upper - lower;
        if (upper==null) {
            n =  self.l.length;
        }
        if (!lower) lower = 0;
        if (n > 0) self.l.splice(lower, n);
        """)
        return None

    def __setslice__(self, lower, upper, data):
        self.__delslice__(lower, upper)
        tail = self.__getslice__(lower, None)
        self.__delslice__(lower, None)
        self.extend(data)
        self.extend(tail)
        return None

    @compiler.noSourceTracking
    def __getitem__(self, index):
        JS("""
        index = index.valueOf();
        if (index < 0) index += self.l.length;
        if (index < 0 || index >= self.l.length) {
            throw(pyjslib.IndexError("list index out of range"));
        }
        return self.l[index];
        """)

    @compiler.noSourceTracking
    def __setitem__(self, index, value):
        JS("""
        index = index.valueOf();
        if (index < 0) index += self.l.length;
        if (index < 0 || index >= self.l.length) {
            throw(pyjslib.IndexError("list assignment index out of range"));
        }
        self.l[index]=value;
        """)

    @compiler.noSourceTracking
    def __delitem__(self, index):
        JS("""
        index = index.valueOf();
        if (index < 0) index += self.l.length;
        if (index < 0 || index >= self.l.length) {
            throw(pyjslib.IndexError("list assignment index out of range"));
        }
        self.l.splice(index, 1);
        """)

    @compiler.noSourceTracking
    def __len__(self):
        return int(JS("""self.l.length"""))

    @compiler.noSourceTracking
    @compiler.noDebug
    def __contains__(self, value):
        try:
            self.index(value)
        except ValueError:
            return False
        return True

    @compiler.noSourceTracking
    def __iter__(self):
        JS("""
        var i = 0;
        var l = self.l;
        return {
            'next': function() {
                if (i >= l.length) {
                    throw pyjslib.StopIteration;
                }
                return l[i++];
            },
            '__iter__': function() {
                return this;
            }
        };
        """)

    @compiler.noSourceTracking
    def reverse(self):
        JS("""    self.l.reverse();""")

    def sort(self, cmp=None, key=None, reverse=False):
        if cmp is None:
            cmp = __cmp
        if key and reverse:
            def thisSort1(a,b):
                return -cmp(key(a), key(b))
            self.l.sort(thisSort1)
        elif key:
            def thisSort2(a,b):
                return cmp(key(a), key(b))
            self.l.sort(thisSort2)
        elif reverse:
            def thisSort3(a,b):
                return -cmp(a, b)
            self.l.sort(thisSort3)
        else:
            self.l.sort(cmp)

    @compiler.noSourceTracking
    def getArray(self):
        """
        Access the javascript Array that is used internally by this list
        """
        return self.l

    @compiler.noSourceTracking
    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        #r = []
        #for item in self:
        #    r.append(repr(item))
        #return '[' + ', '.join(r) + ']'
        JS("""
        var s = "[";
        for (var i=0; i < self.l.length; i++) {
            s += pyjslib.repr(self.l[i]);
            if (i < self.l.length - 1)
                s += ", ";
        }
        s += "]";
        return s;
        """)

    def __add__(self, y):
        if not isinstance(y, self):
            raise TypeError("can only concatenate list to list")
        return list(self.l.concat(y.l))

    def __mul__(self, n):
        if not isNumber(n):
            raise TypeError("can't multiply sequence by non-int")
        a = []
        while n:
            n -= 1
            a.extend(self.l)
        return a

    def __rmul__(self, n):
        return self.__mul__(n)

list = List

class Tuple:
    @compiler.noSourceTracking
    def __init__(self, data=None):
        JS("""
        self.l = [];
        if (pyjslib.isArray(data)) {
            n = self.l.length;
            for (var i=0; i < data.length; i++) {
                self.l[n+i]=data[i];
            }
        } else if (pyjslib.isIteratable(data)) {
            var iter=data.__iter__();
            var i=self.l.length;
            try {
                while (true) {
                    var item=iter.next();
                    self.l[i++]=item;
                }
            } catch (e) {
                if (e.__name__ != 'StopIteration') {
                    throw e;
                }
            }
        }
        """)

    def __hash__(self):
        return '$tuple$' + str(self.l)

    @compiler.noSourceTracking
    def __cmp__(self, l):
        if not isinstance(l, Tuple):
            return 1
        ll = len(self) - len(l)
        if ll != 0:
            return ll
        for x in range(len(l)):
            ll = cmp(self.__getitem__(x), l[x])
            if ll != 0:
                return ll
        return 0

    @compiler.noSourceTracking
    def __getslice__(self, lower, upper):
        JS("""
        if (upper==null) return pyjslib.Tuple(self.l.slice(lower));
        return pyjslib.Tuple(self.l.slice(lower, upper));
        """)

    @compiler.noSourceTracking
    def __getitem__(self, index):
        JS("""
        index = index.valueOf();
        if (index < 0) index += self.l.length;
        if (index < 0 || index >= self.l.length) {
            throw(pyjslib.IndexError("tuple index out of range"));
        }
        return self.l[index];
        """)

    @compiler.noSourceTracking
    def __len__(self):
        return int(JS("""self.l.length"""))

    @compiler.noSourceTracking
    def __contains__(self, value):
        return JS('self.l.indexOf(value)>=0')

    @compiler.noSourceTracking
    def __iter__(self):
        JS("""
        var i = 0;
        var l = self.l;
        return {
            'next': function() {
                if (i >= l.length) {
                    throw pyjslib.StopIteration;
                }
                return l[i++];
            },
            '__iter__': function() {
                return this;
            }
        };
        """)

    @compiler.noSourceTracking
    def getArray(self):
        """
        Access the javascript Array that is used internally by this list
        """
        return self.l

    @compiler.noSourceTracking
    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        #r = []
        #for item in self:
        #    r.append(repr(item))
        #if len(r) == 1:
        #    return '(' + ', '.join(r) + ',)'
        #return '(' + ', '.join(r) + ')'
        JS("""
        var s = "(";
        for (var i=0; i < self.l.length; i++) {
            s += pyjslib.repr(self.l[i]);
            if (i < self.l.length - 1)
                s += ", ";
        }
        if (self.l.length == 1)
            s += ",";
        s += ")";
        return s;
        """)

    def __add__(self, y):
        if not isinstance(y, self):
            raise TypeError("can only concatenate tuple to tuple")
        return tuple(self.l.concat(y.l))

    def __mul__(self, n):
        if not isNumber(n):
            raise TypeError("can't multiply sequence by non-int")
        a = []
        while n:
            n -= 1
            a.extend(self.l)
        return a

    def __rmul__(self, n):
        return self.__mul__(n)

tuple = Tuple

class Dict:
    @compiler.noSourceTracking
    def __init__(self, data=None):
        JS("""
        self.d = {};

        if (pyjslib.isArray(data)) {
            for (var i = 0; i < data.length; i++) {
                var item=data[i];
                self.__setitem__(item[0], item[1]);
                //var sKey=pyjslib.hash(item[0]);
                //self.d[sKey]=item[1];
            }
        } else if (pyjslib.isIteratable(data)) {
            var iter=data.__iter__();
            try {
                while (true) {
                    var item=iter.next();
                    self.__setitem__(item.__getitem__(0), item.__getitem__(1));
                }
            } catch (e) {
                if (e.__name__ != 'StopIteration') {
                    throw e;
                }
            }
        } else if (pyjslib.isObject(data)) {
            for (var key in data) {
                self.__setitem__(key, data[key]);
            }
        }
        """)

    @compiler.noSourceTracking
    def __setitem__(self, key, value):
        JS("""
        if (typeof value != 'undefined') {
            var sKey = pyjslib.hash(key);
            self.d[sKey]=[key, value];
        }
        """)

    @compiler.noSourceTracking
    def __getitem__(self, key):
        JS("""
        var sKey = pyjslib.hash(key);
        var value=self.d[sKey];
        if (pyjslib.isUndefined(value)){
            throw pyjslib.KeyError(key);
        }
        return value[1];
        """)

    @compiler.noSourceTracking
    def __nonzero__(self):
        JS("""
        for (var i in self.d){
            return true;
        }
        return false;
        """)

    @compiler.noSourceTracking
    def __cmp__(self, d):
        if not isinstance(d, Dict):
            raise TypeError("dict.__cmp__(x,y) requires y to be a 'dict'")
        self_keys = self.keys()
        d_keys = d.keys()
        JS("""
        if (self_keys.l.length < d_keys.l.length) {
            return -1;
        }
        if (self_keys.l.length > d_keys.l.length) {
            return 1;
        }
        self_keys.sort();
        d_keys.sort();
        var c, sKey;
        for (var idx = 0; idx < self_keys.l.length; idx++) {
            c = pyjslib.cmp(self_keys.l[idx], d_keys.l[idx]);
            if (c != 0) {
                return c;
            }
            sKey = pyjslib.hash(self_keys.l[idx]);
            c = pyjslib.cmp(self.d[sKey][1], d.d[sKey][1]);
            if (c != 0) {
                return c;
            }
        }
        return 0;""")

    @compiler.noSourceTracking
    def __len__(self):
        size = 0
        JS("""
        for (var i in self.d) size++;
        """)
        return int(size);

    @compiler.noSourceTracking
    def has_key(self, key):
        return self.__contains__(key)

    @compiler.noSourceTracking
    def __delitem__(self, key):
        JS("""
        var sKey = pyjslib.hash(key);
        delete self.d[sKey];
        """)

    @compiler.noSourceTracking
    def __contains__(self, key):
        JS("""
        var sKey = pyjslib.hash(key);
        return (pyjslib.isUndefined(self.d[sKey])) ? false : true;
        """)

    @compiler.noSourceTracking
    def keys(self):
        JS("""
        var keys=new pyjslib.List();
        for (var key in self.d) {
            keys.append(self.d[key][0]);
        }
        return keys;
        """)

    @compiler.noSourceTracking
    def values(self):
        JS("""
        var values=new pyjslib.List();
        for (var key in self.d) values.append(self.d[key][1]);
        return values;
        """)

    @compiler.noSourceTracking
    def items(self):
        JS("""
        var items = new pyjslib.List();
        for (var key in self.d) {
          var kv = self.d[key];
          items.append(new pyjslib.List(kv));
          }
          return items;
        """)

    @compiler.noSourceTracking
    def __iter__(self):
        return self.keys().__iter__()

    @compiler.noSourceTracking
    def iterkeys(self):
        return self.__iter__()

    @compiler.noSourceTracking
    def itervalues(self):
        return self.values().__iter__();

    @compiler.noSourceTracking
    def iteritems(self):
        return self.items().__iter__();

    @compiler.noSourceTracking
    def setdefault(self, key, default_value):
        if not self.has_key(key):
            self[key] = default_value
        return self[key]

    @compiler.noSourceTracking
    def get(self, key, default_value=None):
        if not self.has_key(key):
            return default_value
        return self[key]

    @compiler.noSourceTracking
    def update(self, d):
        for k,v in d.iteritems():
            self[k] = v

    @compiler.noSourceTracking
    def pop(self, k, *d):
        if len(d) > 1:
            raise TypeError("pop expected at most 2 arguments, got %s" %
                            (1 + len(d)))
        try:
            res = self[k]
            del self[k]
            return res
        except KeyError:
            if d:
                return d[0]
            else:
                raise

    @compiler.noSourceTracking
    def popitem(self):
        for (k, v) in self.iteritems():
            break
        else:
            raise KeyError('popitem(): dictionary is empty')
        del self[k]
        return (k, v)

    @compiler.noSourceTracking
    def getObject(self):
        """
        Return the javascript Object which this class uses to store
        dictionary keys and values
        """
        return self.d

    @compiler.noSourceTracking
    def copy(self):
        return Dict(self.items())

    @compiler.noSourceTracking
    def clear(self):
        self.d = JS("{}")

    @compiler.noSourceTracking
    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        #r = []
        #for item in self:
        #    r.append(repr(item) + ': ' + repr(self[item]))
        #return '{' + ', '.join(r) + '}'
        JS("""
        var keys = new Array();
        for (var key in self.d)
            keys.push(key);

        var s = "{";
        for (var i=0; i<keys.length; i++) {
            var v = self.d[keys[i]];
            s += pyjslib.repr(v[0]) + ": " + pyjslib.repr(v[1]);
            if (i < keys.length-1)
                s += ", ";
        }
        s += "}";
        return s;
        """)

dict = Dict

class property(object):
    # From: http://users.rcn.com/python/download/Descriptor.htm
    # Extended with setter(), deleter() and fget.__doc_ copy
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if not doc is None or not hasattr(fget, '__doc__') :
            self.__doc__ = doc
        else:
            self.__doc__ = fget.__doc__

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError, "unreadable attribute"
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError, "can't set attribute"
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError, "can't delete attribute"
        self.fdel(obj)

    def setter(self, fset):
        self.fset = fset
        return self

    def deleter(self, fdel):
        self.fdel = fdel
        return self


def staticmethod(func):
    JS("""
    var fnwrap = function() {
        var args = [];
        for (var i = 0; i < arguments.length; i++) {
          args.push(arguments[i]);
        }
        return func.apply(null,args);
    };
    fnwrap.__name__ = func.__name__;
    fnwrap.__args__ = func.__args__;
    fnwrap.__bind_type__ = 0;
    return fnwrap;
    """)

@compiler.noSourceTracking
def super(type_, object_or_type = None):
    # This is a partially implementation: only super(type, object)
    if not _issubtype(object_or_type, type_):
        raise TypeError("super(type, obj): obj must be an instance or subtype of type")
    JS("""
    var fn = $pyjs_type('super', type_.__mro__.slice(1), {});
    fn.__new__ = fn.__mro__[1].__new__;
    fn.__init__ = fn.__mro__[1].__init__;
    if (object_or_type.__is_instance__ === false) {
        return fn;
    }
    var obj = new Object();
    function wrapper(obj, name) {
        var fnwrap = function() {
            var args = [];
            for (var i = 0; i < arguments.length; i++) {
              args.push(arguments[i]);
            }
            return obj[name].apply(object_or_type,args);
        };
        fnwrap.__name__ = name;
        fnwrap.__args__ = obj[name].__args__;
        fnwrap.__bind_type__ = obj[name].__bind_type__;
        return fnwrap;
    }
    for (var m in fn) {
        if (typeof fn[m] == 'function') {
            obj[m] = wrapper(fn, m);
        }
    }
    obj.__is_instance__ = object_or_type.__is_instance__;
    return obj;
    """)

# taken from mochikit: range( [start,] stop[, step] )
@compiler.noSourceTracking
def xrange(start, stop = None, step = 1):
    if stop is None:
        stop = start
        start = 0
    if not isNumber(start):
        raise TypeError("xrange() integer start argument expected, got %s" % stop.__class__.__name__)
    if not isNumber(stop):
        raise TypeError("xrange() integer end argument expected, got %s" % stop.__class__.__name__)
    if not isNumber(step):
        raise TypeError("xrange() integer step argument expected, got %s" % stop.__class__.__name__)
    rval = nval = start
    JS("""
    var nstep = (stop-start)/step;
    nstep = nstep < 0 ? Math.ceil(nstep) : Math.floor(nstep);
    if ((stop-start) % step) {
        nstep++;
    }
    stop = start + nstep * step;
    if (nstep <= 0) nval = stop;
    var x = {
        'next': function() {
            if (nval == stop) {
                throw pyjslib.StopIteration;
            }
            rval = nval;
            nval += step;
""")
    return int(rval);
    JS("""
        },
        '__iter__': function() {
            return this;
        },
        'toString': function() {
            var s = "xrange("
            if (start != 0) {
                s += start + ", ";
            }
            s += stop;
            if (step != 1) {
                s += ", " + step;
            }
            return s + ")"
        },
        '__repr__': function() {
            return "'" + this.toString() + "'";
        }
    };
    x['__str__'] = x.toString;
    return x;
    """)

def range(start, stop = None, step = 1):
    if stop is None:
        stop = start
        start = 0
    i = start
    if not isNumber(start):
        raise TypeError("range() integer start argument expected, got %s" % stop.__class__.__name__)
    if not isNumber(stop):
        raise TypeError("range() integer end argument expected, got %s" % stop.__class__.__name__)
    if not isNumber(step):
        raise TypeError("range() integer step argument expected, got %s" % stop.__class__.__name__)
    items = JS("new Array()")
    JS("""
    var nstep = (stop-start)/step;
    nstep = nstep < 0 ? Math.ceil(nstep) : Math.floor(nstep);
    if ((stop-start) % step) {
        nstep++;
    }
    stop = start + nstep * step;
    if (nstep <= 0) i = stop;
    for (; i != stop; i += step)
""")
    items.push(int(i))
    return list(items)

@compiler.noSourceTracking
def slice(object, lower, upper):
    JS("""
    if (typeof object.__getslice__ == 'function') {
        return object.__getslice__(lower, upper);
    }
    if (pyjslib.isObject(object) && object.slice)
        return object.slice(lower, upper);

    return null;
    """)

def __delslice(object, lower, upper):
    JS("""
    if (typeof object.__delslice__ == 'function') {
        return object.__delslice__(lower, upper);
    }
    if (object.__getslice__ == 'function' && object.__delitem__ == 'function') {
        if (upper == null) {
            upper = pyjslib.len(object);
        }
        for (var i = lower; i < upper; i++) {
            object.__delitem__(i);
        }
        return null;
    }
    throw pyjslib.TypeError('object does not support item deletion');
    return null;
    """)

def __setslice(object, lower, upper, value):
    JS("""
    if (typeof object.__setslice__ == 'function') {
        return object.__setslice__(lower, upper, value);
    }
    throw pyjslib.TypeError('object does not support __setslice__');
    return null;
    """)

@compiler.noSourceTracking
def str(text):
    JS("""
    if (pyjslib.hasattr(text,"__str__")) {
        return text.__str__();
    }
    return String(text);
    """)

@compiler.noSourceTracking
def ord(x):
    if(isString(x) and len(x) is 1):
        return int(x.charCodeAt(0));
    else:
        JS("""throw pyjslib.TypeError("ord() expected string of length 1")""")
    return None

@compiler.noSourceTracking
def chr(x):
    JS("""
        return String.fromCharCode(x);
    """)

@compiler.noSourceTracking
def is_basetype(x):
    JS("""
       var t = typeof(x);
       return t == 'boolean' ||
       t == 'function' ||
       t == 'number' ||
       t == 'string' ||
       t == 'undefined';
    """)

@compiler.noSourceTracking
def get_pyjs_classtype(x):
    JS("""
        if (pyjslib.hasattr(x, "__is_instance__")) {
            var src = x.__name__;
            return src;
        }
        return null;
    """)

@compiler.noSourceTracking
def repr(x):
    """ Return the string representation of 'x'.
    """
    if hasattr(x, '__repr__'):
        return x.__repr__()
    JS("""
       if (x === null)
           return "null";

       if (x === undefined)
           return "undefined";

       var t = typeof(x);

        //alert("repr typeof " + t + " : " + x);

       if (t == "boolean")
           return x.toString();

       if (t == "function")
           return "<function " + x.toString() + ">";

       if (t == "number")
           return x.toString();

       if (t == "string") {
           if (x.indexOf("'") == -1)
               return "'" + x + "'";
           if (x.indexOf('"') == -1)
               return '"' + x + '"';
           var s = x.replace(new RegExp('"', "g"), '\\\\"');
           return '"' + s + '"';
       }

       if (t == "undefined")
           return "undefined";

       // If we get here, x is an object.  See if it's a Pyjamas class.

       if (!pyjslib.hasattr(x, "__init__"))
           return "<" + x.toString() + ">";

       // Handle the common Pyjamas data types.

       var constructor = "UNKNOWN";

       constructor = pyjslib.get_pyjs_classtype(x);

        //alert("repr constructor: " + constructor);

       // If we get here, the class isn't one we know -> return the class name.
       // Note that we replace underscores with dots so that the name will
       // (hopefully!) look like the original Python name.

       //var s = constructor.replace(new RegExp('_', "g"), '.');
       return "<" + constructor + " object>";
    """)

@compiler.noSourceTracking
def len(object):
    v = 0
    JS("""
    if (object === null) return v;
    else if (typeof object.__len__ == 'function') v = object.__len__();
    else if (typeof object.length != 'undefined') v = object.length;
    else throw pyjslib.TypeError("object has no len()")
    if (v.__number__ == 0x02) return v;
    """)
    return int(v)

@compiler.noSourceTracking
def isinstance(object_, classinfo):
    if isUndefined(object_):
        return False
    JS("""
    if (object_ == null) {
        if (classinfo == null) {
            return true;
        }
        return false;
    }
    switch (classinfo.__name__) {
        case 'int':
        case 'float_int':
            return pyjslib.isNumber(object_); /* XXX TODO: check rounded? */
        case 'str':
            return pyjslib.isString(object_);
        case 'bool':
            return pyjslib.isBool(object_);
        case 'long':
            return object_.__number__ == 0x04;
    }
""")
    if not isObject(object_):
        return False
    if _isinstance(classinfo, Tuple):
        if _isinstance(object_, Tuple):
            return True
        for ci in classinfo:
            if isinstance(object_, ci):
                return True
        return False
    else:
        return _isinstance(object_, classinfo)

@compiler.noSourceTracking
def _isinstance(object_, classinfo):
    JS("""
    if (object_.__is_instance__ !== true) {
        return false;
    }
    for (var c in object_.__mro__) {
        if (object_.__mro__[c].__md5__ == classinfo.prototype.__md5__) return true;
    }
    return false;
    """)

@compiler.noSourceTracking
def _issubtype(object_, classinfo):
    JS("""
    if (object_.__is_instance__ == null || classinfo.__is_instance__ == null) {
        return false;
    }
    for (var c in object_.__mro__) {
        if (object_.__mro__[c] == classinfo.prototype) return true;
    }
    return false;
    """)

@compiler.noSourceTracking
def getattr(obj, name, default_value=None):
    JS("""
    if ((!pyjslib.isObject(obj))||(pyjslib.isUndefined(obj[name]))){
        if (arguments.length != 3){
            throw pyjslib.AttributeError(obj, name);
        }else{
        return default_value;
        }
    }
    var method = obj[name];
    if (method !== null && typeof method.__get__ == 'function') {
        if (obj.__is_instance__) {
            return method.__get__(obj, obj.__class__);
        } else {
            return method.__get__(null, obj.__class__);
        }
    }
    if (    (!pyjslib.isFunction(obj[name]))
        || (typeof obj.__is_instance__ == 'undefined'
            && typeof obj[name].__is_instance__ == 'undefined')) {
        return obj[name];
    }
    var fnwrap = function() {
        var args = [];
        for (var i = 0; i < arguments.length; i++) {
          args.push(arguments[i]);
        }
        return method.apply(obj,args);
    };
    fnwrap.__name__ = name;
    fnwrap.__args__ = obj[name].__args__;
    fnwrap.__bind_type__ = obj[name].__bind_type__;
    return fnwrap;
    """)

@compiler.noSourceTracking
def _del(obj):
    JS("""
    if (typeof obj.__delete__ == 'function') {
        obj.__delete__(obj);
    } else {
        delete obj;
    }
    """)

@compiler.noSourceTracking
def delattr(obj, name):
    JS("""
    if (!pyjslib.isObject(obj)) {
       throw pyjslib.AttributeError("'"+typeof(obj)+"' object has no attribute '"+name+"'")
    }
    if ((pyjslib.isUndefined(obj[name])) ||(typeof(obj[name]) == "function") ){
        throw pyjslib.AttributeError(obj.__name__+" instance has no attribute '"+ name+"'");
    }
    if (typeof obj[name].__delete__ == 'function') {
        obj[name].__delete__(obj);
    } else {
        delete obj[name];
    }
    """)

@compiler.noSourceTracking
def setattr(obj, name, value):
    JS("""
    if (!pyjslib.isObject(obj)) return null;

    if (   typeof obj[name] != 'undefined'
        && obj[name] !== null
        && typeof obj[name].__set__ == 'function') {
        obj[name].__set__(obj, value);
    } else {
        obj[name] = value;
    }
    """)

@compiler.noSourceTracking
def hasattr(obj, name):
    JS("""
    if (!pyjslib.isObject(obj)) return false;
    if (pyjslib.isUndefined(obj[name])) return false;

    return true;
    """)

@compiler.noSourceTracking
def dir(obj):
    JS("""
    var properties=new pyjslib.List();
    for (property in obj) properties.append(property);
    return properties;
    """)

@compiler.noSourceTracking
def filter(obj, method, sequence=None):
    # object context is LOST when a method is passed, hence object must be passed separately
    # to emulate python behaviour, should generate this code inline rather than as a function call
    items = []
    if sequence is None:
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


@compiler.noSourceTracking
def map(obj, method, sequence=None):
    items = []

    if sequence is None:
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


def min(*sequence):
    if len(sequence) == 1:
        sequence = sequence[0]
    minValue = None
    for item in sequence:
        if minValue is None:
            minValue = item
        elif cmp(item, minValue) == -1:
            minValue = item
    return minValue


def max(*sequence):
    if len(sequence) == 1:
        sequence = sequence[0]
    maxValue = None
    for item in sequence:
        if maxValue is None:
            maxValue = item
        elif cmp(item, maxValue) == 1:
            maxValue = item
    return maxValue

next_hash_id = 0

@compiler.noSourceTracking
def hash(obj):
    JS("""
    if (obj == null) return null;

    if (obj.$H) return obj.$H;
    if (obj.__hash__) return obj.__hash__();
    if (obj.constructor == String || obj.constructor == Number || obj.constructor == Date) return '$'+obj;

    try {
        obj.$H = ++pyjslib.next_hash_id;
        return obj.$H;
    } catch (e) {
        return obj;
    }
    """)


# type functions from Douglas Crockford's Remedial Javascript: http://www.crockford.com/javascript/remedial.html
@compiler.noSourceTracking
def isObject(a):
    JS("""
    return (a != null && (typeof a == 'object')) || pyjslib.isFunction(a);
    """)

@compiler.noSourceTracking
def isFunction(a):
    JS("""
    return typeof a == 'function';
    """)

callable = isFunction

@compiler.noSourceTracking
def isString(a):
    JS("""
    return typeof a == 'string';
    """)

@compiler.noSourceTracking
def isNull(a):
    JS("""
    return typeof a == 'object' && !a;
    """)

@compiler.noSourceTracking
def isArray(a):
    JS("""
    return pyjslib.isObject(a) && a.constructor == Array;
    """)

@compiler.noSourceTracking
def isUndefined(a):
    JS("""
    return typeof a == 'undefined';
    """)

@compiler.noSourceTracking
def isIteratable(a):
    JS("""
    return pyjslib.isString(a) || (pyjslib.isObject(a) && a.__iter__);
    """)

@compiler.noSourceTracking
def isNumber(a):
    JS("""
    return a.__number__ && (a.__number__ != 0x01 || isFinite(a));
    """)

def isInteger(a):
    JS("""
    switch (a.__number__) {
        case 0x01:
            if (a != Math.floor(a)) break;
        case 0x02:
        case 0x04:
            return true;
    }
    return false;
""")

@compiler.noSourceTracking
def toJSObjects(x):
    """
       Convert the pyjs pythonic List and Dict objects into javascript Object and Array
       objects, recursively.
    """
    if isArray(x):
        JS("""
        var result = [];
        for(var k=0; k < x.length; k++) {
           var v = x[k];
           var tv = pyjslib.toJSObjects(v);
           result.push(tv);
        }
        return result;
        """)
    if isObject(x):
        if x.__number__:
            return x.valueOf()
        elif isinstance(x, Dict):
            JS("""
            var o = x.getObject();
            var result = {};
            for (var i in o) {
               result[o[i][0].toString()] = o[i][1];
            }
            return pyjslib.toJSObjects(result)
            """)
        elif isinstance(x, List):
            return toJSObjects(x.l)
        elif hasattr(x, '__class__'):
            # we do not have a special implementation for custom
            # classes, just pass it on
            return x
    if isObject(x):
        JS("""
        var result = {};
        for(var k in x) {
            var v = x[k];
            var tv = pyjslib.toJSObjects(v);
            result[k] = tv;
            }
            return result;
         """)
    return x

@compiler.noSourceTracking
def sprintf(strng, args):
    # See http://docs.python.org/library/stdtypes.html
    constructor = get_pyjs_classtype(args)
    JS(r"""
    var re_dict = /([^%]*)%[(]([^)]+)[)]([#0\x20\x2B-]*)(\d+)?(\.\d+)?[hlL]?(.)((.|\n)*)/;
    var re_list = /([^%]*)%([#0\x20\x2B-]*)(\*|(\d+))?(\.\d+)?[hlL]?(.)((.|\n)*)/;
    var re_exp = /(.*)([+-])(.*)/;
""")
    strlen = len(strng)
    argidx = 0
    nargs = 0
    result = []
    remainder = strng

    def next_arg():
        if argidx == nargs:
            raise TypeError("not enough arguments for format string")
        arg = args[argidx]
        argidx += 1
        return arg

    def formatarg(flags, minlen, precision, conversion, param):
        subst = ''
        numeric = True
        if not minlen:
            minlen=0
        else:
            minlen = int(minlen)
        if not precision:
            precision = None
        else:
            precision = int(precision[1:])
        left_padding = 1
        if flags.find('-') >= 0:
            left_padding = 0
        if conversion == '%':
            numeric = False
            subst = '%'
        elif conversion == 'c':
            numeric = False
            subst = chr(int(param))
        elif conversion == 'd' or conversion == 'i' or conversion == 'u':
            subst = str(int(param))
        elif conversion == 'e':
            if precision is None:
                precision = 6
            JS("""
            subst = re_exp.exec(String(param.toExponential(precision)));
            if (subst[3].length == 1) {
                subst = subst[1] + subst[2] + '0' + subst[3];
            } else {
                subst = subst[1] + subst[2] + subst[3];
            }""")
        elif conversion == 'E':
            if precision is None:
                precision = 6
            JS("""
            subst = re_exp.exec(String(param.toExponential(precision)).toUpperCase());
            if (subst[3].length == 1) {
                subst = subst[1] + subst[2] + '0' + subst[3];
            } else {
                subst = subst[1] + subst[2] + subst[3];
            }""")
        elif conversion == 'f':
            if precision is None:
                precision = 6
            JS("""
            subst = String(parseFloat(param).toFixed(precision));""")
        elif conversion == 'F':
            if precision is None:
                precision = 6
            JS("""
            subst = String(parseFloat(param).toFixed(precision)).toUpperCase();""")
        elif conversion == 'g':
            if flags.find('#') >= 0:
                if precision is None:
                    precision = 6
            if param >= 1E6 or param < 1E-5:
                JS("""
                subst = String(precision == null ? param.toExponential() : param.toExponential().toPrecision(precision));""")
            else:
                JS("""
                subst = String(precision == null ? parseFloat(param) : parseFloat(param).toPrecision(precision));""")
        elif conversion == 'G':
            if flags.find('#') >= 0:
                if precision is None:
                    precision = 6
            if param >= 1E6 or param < 1E-5:
                JS("""
                subst = String(precision == null ? param.toExponential() : param.toExponential().toPrecision(precision)).toUpperCase();""")
            else:
                JS("""
                subst = String(precision == null ? parseFloat(param) : parseFloat(param).toPrecision(precision)).toUpperCase().toUpperCase();""")
        elif conversion == 'r':
            numeric = False
            subst = repr(param)
        elif conversion == 's':
            numeric = False
            subst = str(param)
        elif conversion == 'o':
            param = int(param)
            JS("""
            subst = param.toString(8);""")
            if flags.find('#') >= 0 and subst != '0':
                subst = '0' + subst
        elif conversion == 'x':
            param = int(param)
            JS("""
            subst = param.toString(16);""")
            if flags.find('#') >= 0:
                if left_padding:
                    subst = subst.rjust(minlen - 2, '0')
                subst = '0x' + subst
        elif conversion == 'X':
            param = int(param)
            JS("""
            subst = param.toString(16).toUpperCase();""")
            if flags.find('#') >= 0:
                if left_padding:
                    subst = subst.rjust(minlen - 2, '0')
                subst = '0X' + subst
        else:
            raise ValueError("unsupported format character '" + conversion + "' ("+hex(ord(conversion))+") at index " + (strlen - len(remainder) - 1))
        if minlen and len(subst) < minlen:
            padchar = ' '
            if numeric and left_padding and flags.find('0') >= 0:
                padchar = '0'
            if left_padding:
                subst = subst.rjust(minlen, padchar)
            else:
                subst = subst.ljust(minlen, padchar)
        return subst

    def sprintf_list(strng, args):
        a = None
        left = None
        flags = None
        precision = None
        conversion = None
        minlen = None
        minlen_type = None
        while remainder:
            JS("""
            a = re_list.exec(remainder);""")
            if a is None:
                result.append(remainder)
                break;
            JS("""
            left = a[1], flags = a[2];
            minlen = a[3], precision = a[5], conversion = a[6];
            remainder = a[7];
            if (typeof minlen == 'undefined') minlen = null;
            if (typeof precision == 'undefined') precision = null;
            if (typeof conversion == 'undefined') conversion = null;
""")
            result.append(left)
            if minlen == '*':
                minlen = next_arg()
                JS("minlen_type = typeof(minlen);")
                if not isInteger(minlen):
                    raise TypeError('* wants int')
            if conversion != '%':
                param = next_arg()
            result.append(formatarg(flags, minlen, precision, conversion, param))

    def sprintf_dict(strng, args):
        arg = args
        argidx += 1
        a = None
        key = None
        left = None
        flags = None
        precision = None
        conversion = None
        minlen = None
        while remainder:
            JS("""
            a = re_dict.exec(remainder);""")
            if a is None:
                result.append(remainder)
                break;
            JS("""
            left = a[1], key = a[2], flags = a[3];
            minlen = a[4], precision = a[5], conversion = a[6];
            remainder = a[7];
            if (typeof minlen == 'undefined') minlen = null;
            if (typeof precision == 'undefined') precision = null;
            if (typeof conversion == 'undefined') conversion = null;
""")
            result.append(left)
            if not arg.has_key(key):
                raise KeyError(key)
            else:
                param = arg[key]
            result.append(formatarg(flags, minlen, precision, conversion, param))

    a = None
    JS("""
    a = re_dict.exec(strng);
""")
    if a is None:
        if constructor != "Tuple":
            args = (args,)
        nargs = len(args)
        sprintf_list(strng, args)
        if argidx != nargs:
            raise TypeError('not all arguments converted during string formatting')
    else:
        if constructor != "Dict":
            raise TypeError("format requires a mapping")
        sprintf_dict(strng, args)
    return ''.join(result)

@compiler.noSourceTracking
def debugReport(msg):
    JS("""
    alert(msg);
    """)

@compiler.noSourceTracking
def printFunc(objs, newline):
    JS("""
    if ($wnd.console==undefined)  return;
    var s = "";
    for(var i=0; i < objs.length; i++) {
        if(s != "") s += " ";
        s += objs[i];
    }
    console.debug(s)
    """)

@compiler.noSourceTracking
def type(clsname, bases=None, methods=None):
    """ creates a class, derived from bases, with methods and variables
    """
    JS(" var mths = {}; ")
    if methods:
        for k in methods.keys():
            mth = methods[k]
            JS(" mths[k] = mth; ")

    JS(" var bss = null; ")
    if bases:
        JS("bss = bases.l;")
    JS(" return $pyjs_type(clsname, bss, mths); ")

def pow(x, y, z = None):
    p = None
    JS("p = Math.pow(x, y);")
    if z is None:
        return float(p)
    return float(p % z)

def hex(x):
    JS("""
    if (typeof x == 'number') {
        if (Math.floor(x) == x) {
            return '0x' + x.toString(16);
        }
    } else {
        switch (x.__number__) {
            case 0x02:
                return '0x' + x.__v.toString(16);
            case 0x04:
                return x.__hex__();
        }
    }
""")
    raise TypeError("hex() argument can't be converted to hex")

def oct(x):
    JS("""
    if (typeof x == 'number') {
        if (Math.floor(x) == x) {
            return x == 0 ? '0': '0' + x.toString(8);
        }
    } else {
        switch (x.__number__) {
            case 0x02:
                return x.__v == 0 ? '0': '0' + x.__v.toString(8);
            case 0x04:
                return x.__oct__();
        }
    }
""")
    raise TypeError("oct() argument can't be converted to oct")

def round(x, n = 0):
    n = pow(10, n)
    r = None
    JS("r = Math.round(n*x)/n;")
    return float(r)

def divmod(x, y):
    JS("""
    if (x !== null && y !== null) {
        switch ((x.__number__ << 8) | y.__number__) {
            case 0x0101:
            case 0x0104:
            case 0x0401:
                if (y == 0) throw pyjslib['ZeroDivisionError']('float divmod()');
                var f = Math.floor(x / y);
                return pyjslib['tuple']([f, x - f * y]);
            case 0x0102:
                if (y.__v == 0) throw pyjslib['ZeroDivisionError']('float divmod()');
                var f = Math.floor(x / y.__v);
                return pyjslib['tuple']([f, x - f * y.__v]);
            case 0x0201:
                if (y == 0) throw pyjslib['ZeroDivisionError']('float divmod()');
                var f = Math.floor(x.__v / y);
                return pyjslib['tuple']([f, x.__v - f * y]);
            case 0x0202:
                if (y.__v == 0) throw pyjslib['ZeroDivisionError']('integer division or modulo by zero');
                var f = Math.floor(x.__v / y.__v);
                return pyjslib['tuple']([new pyjslib['int'](f), new pyjslib['int'](x.__v - f * y.__v)]);
            case 0x0204:
                return y.__rdivmod__(new pyjslib['long'](x.__v))
            case 0x0402:
                return x.__divmod__(new pyjslib['long'](y.__v))
            case 0x0404:
                return x.__divmod__(y);
        }
        if (!x.__number__) {
            if (   !y.__number__
                && x.__mro__.length > y.__mro__.length
                && pyjslib['isinstance'](x, y)
                && typeof x['__divmod__'] == 'function')
                return y.__divmod__(x);
            if (typeof x['__divmod__'] == 'function') return x.__divmod__(y);
        }
        if (!y.__number__ && typeof y['__rdivmod__'] == 'function') return y.__rdivmod__(x);
    }
    throw pyjslib['TypeError']("unsupported operand type(s) for divmod(): '%r', '%r'" % (x, y))
""")

def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

def any(iterable):
    for element in iterable:
        if element:
            return True
    return False

init()

def __import__(name, globals={}, locals={}, fromlist=[], level=-1):
    module = ___import___(name, None)
    if not module is None and hasattr(module, '__was_initialized__'):
        return module
    raise ImportError("No module named " + name)

import sys # needed for debug option
import dynamic # needed for ___import___
