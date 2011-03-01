from __pyjamas__ import JS
JS("""
$m.ceil = Math.ceil;
$m.fabs = Math.abs;
$m.floor = Math.floor;
$m.exp = Math.exp;
$m.log = Math.log;
$m.pow = Math.pow;
$m.sqrt = Math.sqrt;
$m.cos = Math.cos;
$m.sin = Math.sin;
$m.tan = Math.tan;
$m.acos = Math.acos;
$m.asin = Math.asin;
$m.atan = Math.atan;
$m.atan2 = Math.atan2;
$m.pi = Math.PI;
$m.e = Math.E;
$m.__log10__ = Math.LN10;
""")

__log2__ = log(2)

# This is not the real thing, but i helps to start with the small numbers
def fsum(x):
    xx = [(fabs(v), i) for i, v in enumerate(x)]
    xx.sort()
    sum = 0
    for i in xx:
        sum += x[i[1]]
    return sum

def frexp(x):
    global __log2__
    if x == 0:
        return (0.0, 0)
    # x = m * 2**e
    e = int(log(abs(x))/__log2__) + 1
    m = x / (2.**e)
    return (m,e)

def ldexp(x, i):
    return x * (2**i)

def log10 (arg):
    return log(arg) / __log10__

def degrees(x):
    return x * 180 / pi

def radians(x):
    return x * pi / 180
