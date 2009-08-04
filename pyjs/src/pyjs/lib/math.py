JS("""
math.ceil = Math.ceil;
math.fabs = Math.abs;
math.floor = Math.floor;
math.exp = Math.exp;
math.log = Math.log;
math.pow = Math.pow;
math.sqrt = Math.sqrt;
math.cos = Math.cos;
math.sin = Math.sin;
math.tan = Math.tan;
math.acos = Math.acos;
math.asin = Math.asin;
math.atan = Math.atan;
math.atan2 = Math.atan2;
math.pi = Math.PI;
math.e = Math.E;
""")

def ldexp(x, i):
    return x * (2**i)

__log2__ = log(2)
def frexp(x):
    global __log2__
    if x == 0:
        return (0.0, 0)
    # x = m * 2**e
    e = int(log(abs(x))/__log2__) + 1
    m = x / (2.**e)
    return (m,e)
