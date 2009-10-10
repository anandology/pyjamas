from UnitTest import UnitTest
import sys
import random

do_minimal_checks = True
do_all_checks = False

#from __pyjamas__ import debugger

class test_support:
    have_unicode = False

# Used for lazy formatting of failure messages
class Frm(object):
    def __init__(self, format, *args):
        self.format = format
        if len(args) == 1 and isinstance(args[0], tuple):
            self.args = args[0]
        else:
            self.args = args

    def __str__(self):
        print self.format, self.args
        return self.format % self.args

# SHIFT should match the value in longintrepr.h for best testing.
SHIFT = 15
BASE = 2 ** SHIFT
MASK = BASE - 1
KARATSUBA_CUTOFF = 70   # from longobject.c

# Max number of base BASE digits to use in test cases.  Doubling
# this will more than double the runtime.
MAXDIGITS = 15

# build some special values
special = map(long, [0, 1, 2, BASE, BASE >> 1])
special.append(0x5555555555555555L)
special.append(0xaaaaaaaaaaaaaaaaL)
#  some solid strings of one bits
p2 = 4L  # 0 and 1 already added
for i in range(2*SHIFT):
    special.append(p2 - 1)
    p2 = p2 << 1
del p2
# add complements & negations
special = special + map(lambda x: ~x, special) + \
                    map(lambda x: -x, special)

L = [
        ('0', 0),
        ('1', 1),
        ('9', 9),
        ('10', 10),
        ('99', 99),
        ('100', 100),
        ('314', 314),
        (' 314', 314),
        ('314 ', 314),
        ('  \t\t  314  \t\t  ', 314),
        (repr(sys.maxint), sys.maxint),
        ('  1x', ValueError),
        ('  1  ', 1),
        ('  1\02  ', ValueError),
        ('', ValueError),
        (' ', ValueError),
        ('  \t\t  ', ValueError),
]

class LongTypeTest(UnitTest):

    """tests for long object"""

    def assert_(self, condition, msg=None):
        if not condition:
            if not msg:
                msg = "assert condition is false"
            raise Exception(msg)

    def getran(self, ndigits):
        self.assertTrue(ndigits > 0)
        nbits_hi = ndigits * SHIFT
        nbits_lo = nbits_hi - SHIFT + 1
        answer = 0L
        nbits = 0
        r = int(random.random() * (SHIFT * 2)) | 1  # force 1 bits to start
        while nbits < nbits_lo:
            bits = (r >> 1) + 1
            bits = min(bits, nbits_hi - nbits)
            self.assertTrue(1 <= bits <= SHIFT)
            nbits = nbits + bits
            answer = answer << bits
            if r & 1:
                answer = answer | ((1 << bits) - 1)
            r = int(random.random() * (SHIFT * 2))
        self.assert_(nbits_lo <= nbits <= nbits_hi)
        if random.random() < 0.5:
            answer = -answer
        return answer

    # Get random long consisting of ndigits random digits (relative to base
    # BASE).  The sign bit is also random.

    def getran2(ndigits):
        answer = 0L
        for i in xrange(ndigits):
            answer = (answer << SHIFT) | random.randint(0, MASK)
        if random.random() < 0.5:
            answer = -answer
        return answer

    def check_division(self, x, y):
        eq = self.assertEqual
        q, r = divmod(x, y)
        q2, r2 = x//y, x%y
        pab, pba = x*y, y*x
        eq(pab, pba, Frm("multiplication does not commute for %r and %r", x, y))
        eq(q, q2, Frm("divmod returns different quotient than / for %r and %r", x, y))
        eq(r, r2, Frm("divmod returns different mod than %% for %r and %r", x, y))
        eq(x, q*y + r, Frm("x != q*y + r after divmod on x=%r, y=%r", x, y))
        if y > 0:
            self.assert_(0 <= r < y, Frm("bad mod from divmod on %r and %r", x, y))
        else:
            self.assert_(y < r <= 0, Frm("bad mod from divmod on %r and %r", x, y))


    def test_division(self):
        if do_minimal_checks: return
        if do_all_checks:
            digits = range(1, MAXDIGITS+1) + \
                     range(KARATSUBA_CUTOFF, KARATSUBA_CUTOFF + 14)
        else:
            digits = [1, 2, int(MAXDIGITS/3), 2 * int(MAXDIGITS/3),
                      MAXDIGITS-1, MAXDIGITS, MAXDIGITS+2,
                      KARATSUBA_CUTOFF, KARATSUBA_CUTOFF + 14]
        digits.append(KARATSUBA_CUTOFF * 3)
        for lenx in digits:
            x = self.getran(lenx)
            for leny in digits:
                #y = self.getran(leny) or 1L
                y = self.getran(leny)
                if y == 0L: y = 1L
                self.check_division(x, y)

    def test_karatsuba(self):
        if do_minimal_checks: return
        if do_all_checks:
            digits = range(1, 5) + range(KARATSUBA_CUTOFF, KARATSUBA_CUTOFF + 10)
        else:
            digits = [1, 5, KARATSUBA_CUTOFF, KARATSUBA_CUTOFF + 10]
        digits.extend([KARATSUBA_CUTOFF * 10, KARATSUBA_CUTOFF * 100])

        bits = [digit * SHIFT for digit in digits]

        # Test products of long strings of 1 bits -- (2**x-1)*(2**y-1) ==
        # 2**(x+y) - 2**x - 2**y + 1, so the proper result is easy to check.
        try:
            for abits in bits:
                a = (1L << abits) - 1
                for bbits in bits:
                    if bbits < abits:
                        continue
                    b = (1L << bbits) - 1
                    x = a * b
                    y = ((1L << (abits + bbits)) -
                         (1L << abits) -
                         (1L << bbits) +
                         1)
                    self.assertEqual(x, y,
                        Frm("bad result for a*b: a=%r, b=%r, x=%r, y=%r", a, b, x, y))
        except:
            print abits, bbits
            print sys.tracebackstr()
            raise

    def check_bitop_identities_1(self, x):
        eq = self.assertEqual
        eq(x & 0, 0, Frm("x & 0 != 0 for x=%r", x))
        eq(x | 0, x, Frm("x | 0 != x for x=%r", x))
        eq(x ^ 0, x, Frm("x ^ 0 != x for x=%r", x))
        eq(x & -1, x, Frm("x & -1 != x for x=%r", x))
        eq(x | -1, -1, Frm("x | -1 != -1 for x=%r", x))
        eq(x ^ -1, ~x, Frm("x ^ -1 != ~x for x=%r", x))
        eq(x, ~~x, Frm("x != ~~x for x=%r", x))
        eq(x & x, x, Frm("x & x != x for x=%r", x))
        eq(x | x, x, Frm("x | x != x for x=%r", x))
        eq(x ^ x, 0, Frm("x ^ x != 0 for x=%r", x))
        eq(x & ~x, 0, Frm("x & ~x != 0 for x=%r", x))
        eq(x | ~x, -1, Frm("x | ~x != -1 for x=%r", x))
        eq(x ^ ~x, -1, Frm("x ^ ~x != -1 for x=%r", x))
        eq(-x, 1 + ~x, Frm("not -x == 1 + ~x for x=%r", x))
        eq(-x, ~(x-1), Frm("not -x == ~(x-1) for x=%r", x))
        if not do_all_checks:
            return
        for n in xrange(2*SHIFT):
            p2 = 2L ** n
            eq(x << n >> n, x,
                Frm("x << n >> n != x for x=%r, n=%r", (x, n)))
            eq(x // p2, x >> n,
                Frm("x // p2 != x >> n for x=%r n=%r p2=%r", (x, n, p2)))
            eq(x * p2, x << n,
                Frm("x * p2 != x << n for x=%r n=%r p2=%r", (x, n, p2)))
            eq(x & -p2, x >> n << n,
                Frm("not x & -p2 == x >> n << n for x=%r n=%r p2=%r", (x, n, p2)))
            eq(x & -p2, x & ~(p2 - 1),
                Frm("not x & -p2 == x & ~(p2 - 1) for x=%r n=%r p2=%r", (x, n, p2)))

    def check_bitop_identities_2(self, x, y):
        eq = self.assertEqual
        eq(x & y, y & x, Frm("x & y != y & x for x=%r, y=%r", (x, y)))
        eq(x | y, y | x, Frm("x | y != y | x for x=%r, y=%r", (x, y)))
        eq(x ^ y, y ^ x, Frm("x ^ y != y ^ x for x=%r, y=%r", (x, y)))
        eq(x ^ y ^ x, y, Frm("x ^ y ^ x != y for x=%r, y=%r", (x, y)))
        eq(x & y, ~(~x | ~y), Frm("x & y != ~(~x | ~y) for x=%r, y=%r", (x, y)))
        eq(x | y, ~(~x & ~y), Frm("x | y != ~(~x & ~y) for x=%r, y=%r", (x, y)))
        eq(x ^ y, (x | y) & ~(x & y),
             Frm("x ^ y != (x | y) & ~(x & y) for x=%r, y=%r", (x, y)))
        eq(x ^ y, (x & ~y) | (~x & y),
             Frm("x ^ y == (x & ~y) | (~x & y) for x=%r, y=%r", (x, y)))
        eq(x ^ y, (x | y) & (~x | ~y),
             Frm("x ^ y == (x | y) & (~x | ~y) for x=%r, y=%r", (x, y)))

    def check_bitop_identities_3(self, x, y, z):
        eq = self.assertEqual
        eq((x & y) & z, x & (y & z),
             Frm("(x & y) & z != x & (y & z) for x=%r, y=%r, z=%r", (x, y, z)))
        eq((x | y) | z, x | (y | z),
             Frm("(x | y) | z != x | (y | z) for x=%r, y=%r, z=%r", (x, y, z)))
        eq((x ^ y) ^ z, x ^ (y ^ z),
             Frm("(x ^ y) ^ z != x ^ (y ^ z) for x=%r, y=%r, z=%r", (x, y, z)))
        eq(x & (y | z), (x & y) | (x & z),
             Frm("x & (y | z) != (x & y) | (x & z) for x=%r, y=%r, z=%r", (x, y, z)))
        eq(x | (y & z), (x | y) & (x | z),
             Frm("x | (y & z) != (x | y) & (x | z) for x=%r, y=%r, z=%r", (x, y, z)))

    def test_bitop_identities(self):
        if do_minimal_checks: return
        for x in special:
            self.check_bitop_identities_1(x)
        if not do_all_checks:
            return
        digits = xrange(1, MAXDIGITS+1)
        for lenx in digits:
            x = self.getran(lenx)
            self.check_bitop_identities_1(x)
            for leny in digits:
                y = self.getran(leny)
                self.check_bitop_identities_2(x, y)
                self.check_bitop_identities_3(x, y, self.getran((lenx + leny)//2))

    def slow_format(self, x, base):
        if (x, base) == (0, 8):
            # this is an oddball!
            return "0L"
        digits = []
        sign = 0
        if x < 0:
            sign, x = 1, -x
        while x:
            x, r = divmod(x, base)
            digits.append(int(r))
        digits.reverse()
        #digits = digits or [0]
        if not digits: digits = [0]
        return '-'[:sign] + \
               {8: '0', 10: '', 16: '0x'}[base] + \
               "".join(map(lambda i: "0123456789abcdef"[i], digits)) + "L"

    def check_format_1(self, x):
        for base, mapper in (8, oct), (10, repr), (16, hex):
            got = mapper(x)
            expected = self.slow_format(x, base)
            msg = Frm("%s returned %r but expected %r for %r",
                mapper.__name__, got, expected, x)
            self.assertEqual(got, expected, msg)
            self.assertEqual(long(got, 0), x, Frm('long("%s", 0) != %r', got, x))
        # str() has to be checked a little differently since there's no
        # trailing "L"
        got = str(x)
        expected = self.slow_format(x, 10)[:-1]
        msg = Frm("%s returned %r but expected %r for %r",
            mapper.__name__, got, expected, x)
        self.assertEqual(got, expected, msg)

    def test_format(self):
        for x in special:
            self.check_format_1(x)
        if not do_all_checks:
            return
        for i in xrange(10):
            for lenx in xrange(1, MAXDIGITS+1):
                x = self.getran(lenx)
                self.check_format_1(x)

    def test_long(self):
        self.assertEqual(long(314), 314L)
        self.assertEqual(long(3.14), 3L)
        self.assertEqual(long(314L), 314L)
        # Check that long() of basic types actually returns a long
        #self.assertEqual(type(long(314)), long)
        #self.assertEqual(type(long(3.14)), long)
        #self.assertEqual(type(long(314L)), long)
        self.assertTrue(isinstance(long(314), long))
        self.assertTrue(isinstance(long(3.14), long))
        self.assertTrue(isinstance(long(314L), long))
        # Check that conversion from float truncates towards zero
        self.assertEqual(long(-3.14), -3L)
        self.assertEqual(long(3.9), 3L)
        self.assertEqual(long(-3.9), -3L)
        self.assertEqual(long(3.5), 3L)
        self.assertEqual(long(-3.5), -3L)
        self.assertEqual(long("-3"), -3L)
        if test_support.have_unicode:
            self.assertEqual(long(unicode("-3")), -3L)
        # Different base:
        self.assertEqual(long("10",16), 16L)
        if test_support.have_unicode:
            self.assertEqual(long(unicode("10"),16), 16L)
        # Check conversions from string (same test set as for int(), and then some)
        LL = [
                ('1' + '0'*20, 10L**20),
                ('1' + '0'*100, 10L**100)
        ]
        L2 = L[:]
        if test_support.have_unicode:
            L2 += [
                (unicode('1') + unicode('0')*20, 10L**20),
                (unicode('1') + unicode('0')*100, 10L**100),
        ]
        L2 += LL
        for s, v in L2:
            for sign in "", "+", "-":
                for prefix in "", " ", "\t", "  \t\t  ":
                    ss = prefix + sign + s
                    vv = v
                    if sign == "-" and v is not ValueError:
                        vv = -v
                    try:
                        self.assertEqual(long(ss), long(vv))
                    except v:
                        pass
                    except TypeError:
                        pass

        #self.assertRaises(ValueError, long, '123\0')
        try:
            v = long('123\0')
            self.fail(r"long('123\0')")
        except ValueError:
            self.assertTrue(True)
        #self.assertRaises(ValueError, long, '53', 40)
        try:
            v = long('53', 40)
            self.fail(r"long('53', 40)")
        except ValueError:
            self.assertTrue(True)
        #self.assertRaises(TypeError, long, 1, 12)
        try:
            v = long(1, 12)
            self.fail("long(1, 12)")
        except TypeError:
            self.assertTrue(True)

        # SF patch #1638879: embedded NULs were not detected with
        # explicit base
        #self.assertRaises(ValueError, long, '123\0', 10)
        try:
            v = long('123\0', 10)
            self.fail(r"long('123\0', 10)")
        except ValueError:
            self.assertTrue(True)
        #self.assertRaises(ValueError, long, '123\x00 245', 20)
        try:
            v = long('123\x00 245', 20)
            self.fail(r"(long('123\x00 245', 20)")
        except ValueError:
            self.assertTrue(True)

        self.assertEqual(long('100000000000000000000000000000000', 2),
                         4294967296)
        self.assertEqual(long('102002022201221111211', 3), 4294967296)
        self.assertEqual(long('10000000000000000', 4), 4294967296)
        self.assertEqual(long('32244002423141', 5), 4294967296)
        self.assertEqual(long('1550104015504', 6), 4294967296)
        self.assertEqual(long('211301422354', 7), 4294967296)
        self.assertEqual(long('40000000000', 8), 4294967296)
        self.assertEqual(long('12068657454', 9), 4294967296)
        self.assertEqual(long('4294967296', 10), 4294967296)
        self.assertEqual(long('1904440554', 11), 4294967296)
        self.assertEqual(long('9ba461594', 12), 4294967296)
        self.assertEqual(long('535a79889', 13), 4294967296)
        self.assertEqual(long('2ca5b7464', 14), 4294967296)
        self.assertEqual(long('1a20dcd81', 15), 4294967296)
        self.assertEqual(long('100000000', 16), 4294967296)
        self.assertEqual(long('a7ffda91', 17), 4294967296)
        self.assertEqual(long('704he7g4', 18), 4294967296)
        self.assertEqual(long('4f5aff66', 19), 4294967296)
        self.assertEqual(long('3723ai4g', 20), 4294967296)
        self.assertEqual(long('281d55i4', 21), 4294967296)
        self.assertEqual(long('1fj8b184', 22), 4294967296)
        self.assertEqual(long('1606k7ic', 23), 4294967296)
        self.assertEqual(long('mb994ag', 24), 4294967296)
        self.assertEqual(long('hek2mgl', 25), 4294967296)
        self.assertEqual(long('dnchbnm', 26), 4294967296)
        self.assertEqual(long('b28jpdm', 27), 4294967296)
        self.assertEqual(long('8pfgih4', 28), 4294967296)
        self.assertEqual(long('76beigg', 29), 4294967296)
        self.assertEqual(long('5qmcpqg', 30), 4294967296)
        self.assertEqual(long('4q0jto4', 31), 4294967296)
        self.assertEqual(long('4000000', 32), 4294967296)
        self.assertEqual(long('3aokq94', 33), 4294967296)
        self.assertEqual(long('2qhxjli', 34), 4294967296)
        self.assertEqual(long('2br45qb', 35), 4294967296)
        self.assertEqual(long('1z141z4', 36), 4294967296)

        self.assertEqual(long('100000000000000000000000000000001', 2),
                         4294967297)
        self.assertEqual(long('102002022201221111212', 3), 4294967297)
        self.assertEqual(long('10000000000000001', 4), 4294967297)
        self.assertEqual(long('32244002423142', 5), 4294967297)
        self.assertEqual(long('1550104015505', 6), 4294967297)
        self.assertEqual(long('211301422355', 7), 4294967297)
        self.assertEqual(long('40000000001', 8), 4294967297)
        self.assertEqual(long('12068657455', 9), 4294967297)
        self.assertEqual(long('4294967297', 10), 4294967297)
        self.assertEqual(long('1904440555', 11), 4294967297)
        self.assertEqual(long('9ba461595', 12), 4294967297)
        self.assertEqual(long('535a7988a', 13), 4294967297)
        self.assertEqual(long('2ca5b7465', 14), 4294967297)
        self.assertEqual(long('1a20dcd82', 15), 4294967297)
        self.assertEqual(long('100000001', 16), 4294967297)
        self.assertEqual(long('a7ffda92', 17), 4294967297)
        self.assertEqual(long('704he7g5', 18), 4294967297)
        self.assertEqual(long('4f5aff67', 19), 4294967297)
        self.assertEqual(long('3723ai4h', 20), 4294967297)
        self.assertEqual(long('281d55i5', 21), 4294967297)
        self.assertEqual(long('1fj8b185', 22), 4294967297)
        self.assertEqual(long('1606k7id', 23), 4294967297)
        self.assertEqual(long('mb994ah', 24), 4294967297)
        self.assertEqual(long('hek2mgm', 25), 4294967297)
        self.assertEqual(long('dnchbnn', 26), 4294967297)
        self.assertEqual(long('b28jpdn', 27), 4294967297)
        self.assertEqual(long('8pfgih5', 28), 4294967297)
        self.assertEqual(long('76beigh', 29), 4294967297)
        self.assertEqual(long('5qmcpqh', 30), 4294967297)
        self.assertEqual(long('4q0jto5', 31), 4294967297)
        self.assertEqual(long('4000001', 32), 4294967297)
        self.assertEqual(long('3aokq95', 33), 4294967297)
        self.assertEqual(long('2qhxjlj', 34), 4294967297)
        self.assertEqual(long('2br45qc', 35), 4294967297)
        self.assertEqual(long('1z141z5', 36), 4294967297)


