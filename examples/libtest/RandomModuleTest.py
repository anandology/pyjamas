from UnitTest import UnitTest

import random
from math import log, exp, sqrt, pi
try:
    from math import fsum as msum
except:
    # fsum is new in 2.6
    from math import fabs
    def msum(x):
        xx = [(fabs(v), i) for i, v in enumerate(x)]
        xx.sort()
        sum = 0
        for i in xx:
            sum += x[i[1]]
        return sum


_gammacoeff = (0.9999999999995183, 676.5203681218835, -1259.139216722289,
              771.3234287757674,  -176.6150291498386, 12.50734324009056,
              -0.1385710331296526, 0.9934937113930748e-05, 0.1659470187408462e-06)

def gamma(z, cof=_gammacoeff, g=7):
    z -= 1.0
    # Next line fails when not compiled with --operator-funcs
    #s = msum([cof[0]] + [cof[i] / (z+i) for i in range(1,len(cof))])
    v1 = [cof[0]]
    v2 = [cof[i] / (z+i) for i in range(1,len(cof))]
    v1 = v1.__add__(v2)
    s = msum(v1)
    z += 0.5
    return (z+g)**z / exp(z+g) * sqrt(2.0*pi) * s

class RandomModuleTest(UnitTest):

    def test_zeroinputs(self):
        # Verify that distributions can handle a series of zero inputs'
        g = random.Random()
        xx = [g.random() for i in xrange(50)]
        x = [0.0]
        xx = xx.__add__(x.__mul__(5))
        x = xx[:]
        g.random = getattr(x, 'pop')
        g.uniform(1,10)
        x = xx[:]
        g.random = getattr(x, 'pop')
        g.paretovariate(1.0)
        x = xx[:]
        g.random = getattr(x, 'pop')
        g.expovariate(1.0)
        x = xx[:]
        g.random = getattr(x, 'pop')
        g.weibullvariate(1.0, 1.0)
        x = xx[:]
        g.random = getattr(x, 'pop')
        g.normalvariate(0.0, 1.0)
        x = xx[:]
        g.random = getattr(x, 'pop')
        g.gauss(0.0, 1.0)
        x = xx[:]
        g.random = getattr(x, 'pop')
        g.lognormvariate(0.0, 1.0)
        x = xx[:]
        g.random = getattr(x, 'pop')
        g.vonmisesvariate(0.0, 1.0)
        x = xx[:]
        g.random = getattr(x, 'pop')
        g.gammavariate(0.01, 1.0)
        x = xx[:]
        g.random = getattr(x, 'pop')
        g.gammavariate(1.0, 1.0)
        x = xx[:]
        g.random = getattr(x, 'pop')
        g.gammavariate(200.0, 1.0)
        x = xx[:]
        g.random = getattr(x, 'pop')
        g.betavariate(3.0, 3.0)
        if hasattr(g, 'triangular'):
            x = xx[:]
            g.random = getattr(x, 'pop')
            g.triangular(0.0, 1.0, 1.0/3.0)

    def test_avg_std(self):
        # Use integration to test distribution average and standard deviation.
        # Only works for distributions which do not consume variates in pairs
        g = random.Random()
        N = 5000
        xx = [i/float(N) for i in xrange(1,N)]
        dists = [
                (g.uniform, (1.0,10.0), (10.0+1.0)/2, (10.0-1.0)**2/12),
                (g.expovariate, (1.5,), 1/1.5, 1/1.5**2),
                (g.paretovariate, (5.0,), 5.0/(5.0-1),
                                  5.0/((5.0-1)**2*(5.0-2))),
                (g.weibullvariate, (1.0, 3.0), gamma(1+1/3.0),
                                  gamma(1+2/3.0)-gamma(1+1/3.0)**2) ]
        if hasattr(g, 'triangular'):
            dists.append((g.triangular, (0.0, 1.0, 1.0/3.0), 4.0/9.0, 7.0/9.0/18.0))
        for variate, args, mu, sigmasqrd in dists:
            x = xx[:]
            g.random = getattr(x, 'pop')
            y = []
            for i in xrange(len(x)):
                try:
                    y.append(variate(*args))
                except IndexError:
                    pass
            s1 = s2 = 0
            for e in y:
                s1 += e
                s2 += (e - mu) ** 2
            N = len(y)
            self.assertAlmostEqual(s1/N, mu, 2)
            self.assertAlmostEqual(s2/(N-1), sigmasqrd, 2)



