from UnitTest import UnitTest

try:
    builtin_value = builtin.value
except:
    builtin_value = None
if False:
    import builtin
import builtin

from imports.cls import CLS
from imports.cls1 import CLS as CLS1


def other(**kwargs):
    return kwargs

def foo(_some, _long, _list, _of, _arguments):
     _additional = 5
     return other(**locals())

class ColourThing(object):
     def rgb():
         def fset(self, rgb):
             self.r, self.g, self.b = rgb
         def fget(self):
             return (self.r, self.g, self.b)
         return property(**locals()) 

class Foo:
    pass

class LocalsTest:
    def __init__(self):
        pass

    def testargs(self, test1, test2):
        return locals()

    def testkwargs(self, test1=None, test2=None):
        return locals()

class BuiltinTest(UnitTest):

    def testMinMax(self):
        self.assertEqual(max(1,2,3,4), 4)
        self.assertEqual(min(1,2,3,4), 1)
        self.assertEqual(max([1,2,3,4]), 4)
        self.assertEqual(min([1,2,3,4]), 1)
        self.assertTrue(max([5,3,4],[6,1,2]) == [6,1,2] , "max([5,3,4],[6,1,2])")
        self.assertTrue(min([5,3,4],[6,1,2]) == [5,3,4] , "min([5,3,4],[6,1,2])")

    def testInt(self):
        self.assertEqual(int("5"), 5)
        self.assertEqual(int("09"), 9)
        self.assertEqual(6, 6)

        try:
            int('not int')
            self.fail("No int() argument error raised: int('not-int')")
        except ValueError, e:
            self.assertEqual(e[0], "invalid literal for int() with base 10: 'not int'")

        try:
            int(1, 10)
            self.fail("No int() argument error raised: int(1, 10)")
        except TypeError, e:
            self.assertEqual(e[0], "int() can't convert non-string with explicit base")

    def testFloat(self):
        self.assertEqual(float("5.1"), 5.1)
        self.assertEqual(float("09"), 9)
        self.assertEqual(6.1, 6.1)

        try:
            float('not float')
            self.fail("No float() argument error raised")
        except ValueError, e:
            self.assertEqual(e[0], "invalid literal for float(): not float")

    def testOrdChr(self):
        for i in range(256):
            self.assertEqual(ord(chr(i)), i)

    def testMod(self):
        self.assertEqual(12 % 5, 2)

    def testPower(self):
        self.assertEqual(3 ** 4, 81)

    def testPowerfunc(self):
        self.assertEqual(pow(10, 3), 1000)
        self.assertEqual(pow(10, 3, 7), 6)

    def testHex(self):
        self.assertEqual(hex(23), '0x17')
        try:
            h = hex(23.2)
            self.fail("No hex() argument error raised")
        except TypeError, why:
            self.assertEqual(why.args[0], "hex() argument can't be converted to hex")

    def testOct(self):
        self.assertEqual(oct(23), '027')
        try:
            o = oct(23.2)
            self.fail("No oct() argument error raised")
        except TypeError, why:
            self.assertEqual(str(why), "oct() argument can't be converted to oct")

    def testRound(self):
        self.assertEqual(round(13.12345), 13.0)
        self.assertEqual(round(13.12345, 3), 13.123)
        self.assertEqual(round(-13.12345), -13.0)
        self.assertEqual(round(-13.12345, 3), -13.123)
        self.assertEqual(round(13.62345), 14.0)
        self.assertEqual(round(13.62345, 3), 13.623)
        self.assertEqual(round(-13.62345), -14.0)
        self.assertEqual(round(-13.62345, 3), -13.623)

    def testDivmod(self):
        test_set = [(14, 3, 4, 2),
                    (14.1, 3, 4.0, 2.1),
                    (14.1, 3.1, 4.0, 1.7),
                   ]
        for x, y, p, q in test_set:
            d = divmod(x,y)
            self.assertEqual(d[0], p)
            self.assertEqual(abs(d[1] - q) < 0.00001, True)

    def testFloorDiv(self):
        self.assertEqual(1, 4//3)
        self.assertEqual(1, 5//3)
        self.assertEqual(2, 6//3)

    def testAll(self):
        self.assertEqual(all([True, 1, 'a']), True)
        self.assertEqual(all([True, 1, None, 'a']), False)
        self.assertEqual(all([True, 1, '', 'a']), False)
        self.assertEqual(all([True, 1, False, 'a']), False)

    def testAny(self):
        self.assertEqual(any([True, 1, 'a']), True)
        self.assertEqual(any([True, 1, None, 'a']), True)
        self.assertEqual(any([True, 1, '', 'a']), True)
        self.assertEqual(any([True, 1, False, 'a']), True)
        self.assertEqual(any([False, '', None]), False)

    def testRepr(self):
        l1 = [1,2,3]
        l2 = ["a", "b", "c"]
        t1 = (4,5,6,7)
        t2 = ("aa", "bb")
        d1 = {'a': 1, "b": "B"}
        d2 = {1: l1, 2: l2, 3: t1, 4: t2, 5:d1}
        self.assertEqual(repr(l1), '[1, 2, 3]')
        self.assertEqual(repr(l2), "['a', 'b', 'c']")
        self.assertEqual(repr(t1), '(4, 5, 6, 7)')
        self.assertEqual(repr(t2), "('aa', 'bb')")
        self.assertEqual(repr(d1), "{'a': 1, 'b': 'B'}")
        self.assertEqual(repr(d2), "{1: [1, 2, 3], 2: ['a', 'b', 'c'], 3: (4, 5, 6, 7), 4: ('aa', 'bb'), 5: {'a': 1, 'b': 'B'}}")
        self.assertEqual(`l1`, '[1, 2, 3]')

    def testIsInstance(self):

        s = 'hello'
        self.assertTrue(isinstance(s, str), "s is a string")
        self.assertFalse(isinstance(s, int), "s is a string not an integer")

        s = 1
        self.assertFalse(isinstance(s, str), "s is an integer not a string")
        self.assertTrue(isinstance(s, int), "s is an integer")

    def testImport(self):
        self.assertEqual(builtin_value, None, "The builtin is loaded before import!")
        try:
            self.assertEqual(builtin.value, builtin.get_value())
        except:
            self.fail("Import failed for builtin")

        from imports import overrideme
        cls1 = CLS1()
        self.assertTrue(CLS is CLS1, "CLS is CLS1")
        self.assertTrue(isinstance(cls1, CLS), "isinstance(cls1, CLS)")
        self.assertEqual(overrideme, "not overridden")
        import imports.override
        self.assertEqual(overrideme, "not overridden")
        from imports import overrideme
        try:
            self.assertTrue(overrideme.overridden is True, "overrideme.overridden is True")
        except:
            self.fail("Exception on 'overrideme.overridden is True'")

        import imports
        self.assertTrue(CLS is imports.loccls.CLS, "CLS is imports.loccls.CLS")
        self.assertTrue(CLS is imports.upcls.CLS, "CLS is imports.upcls.CLS")
	
    def testBitOperations(self):
        self.assertEqual(1 << 2 - 1, 2, "shift error 1")
        self.assertEqual((1 << 2) - 1, 3, "shift error 2")
        self.assertEqual(1 & 3 + 1, 0, "and error 1")
        self.assertEqual((1 & 3) + 1, 2, "and error 2")
        self.assertEqual(4 >> 2, 1, "right shift error 1")
        self.assertEqual(-4 >> 2, -1, "right shift error 2 - bug #341")

    def testLocals(self):
        v1 = 1
        v2 = 2

        local_vars = locals()
        self.assertEqual(len(local_vars), 3)
        self.assertEqual(local_vars['v1'], 1)

        def fn1():
            a = 1
            def fn2():
                b = 1
                c = locals()
                return c
            return fn2()

        local_vars = fn1()
        self.assertEqual(local_vars, {'b': 1})

        args = {'test1': 5, 'test2': 'hello'}
        la = LocalsTest()
        argsreturn = la.testkwargs(**args)
        args['self'] = la
        self.assertEqual(args, argsreturn)

        del args['self']
        argsreturn = la.testargs(**args)
        args['self'] = la
        self.assertEqual(args, argsreturn)

        t = ColourThing()
        t.rgb = 1
        self.assertEqual(t.rgb, 1)

        args = foo(0, 1, 2, 3, 4)
        self.assertEqual(args, {'_some': 0, '_additional': 5,
                                '_of': 3, '_list': 2,
                                '_long': 1, '_arguments': 4})

    def testIfExp(self):
        var = 1 if True else 0
        self.assertEqual(var, 1)
        var = 1 if False else 0
        self.assertEqual(var, 0)
        var = 1 if [] else 0
        self.assertEqual(var, 0)
        var = 1 if not [] else 0
        self.assertEqual(var, 1)

    def testRange(self):
        r = range(3)
        self.assertEqual(r, [0, 1, 2])
        r = range(2, 5)
        self.assertEqual(r, [2, 3, 4])
        r = range(2, 15, 3)
        self.assertEqual(r, [2, 5, 8, 11, 14])
        r = range(15, 2, -3)
        self.assertEqual(r, [15, 12, 9, 6, 3])
        r = range(15, 2, 3)
        self.assertEqual(r, [])
        r = range(-6, -2, -1)
        self.assertEqual(r, [])

    def testXRange(self):
        r = [i for i in xrange(3)]
        self.assertEqual(r, [0, 1, 2])
        r = [i for i in xrange(2, 5)]
        self.assertEqual(r, [2, 3, 4])
        r = [i for i in xrange(2, 15, 3)]
        self.assertEqual(r, [2, 5, 8, 11, 14])
        r = [i for i in xrange(15, 2, -3)]
        self.assertEqual(r, [15, 12, 9, 6, 3])
        r = [i for i in xrange(15, 2, 3)]
        self.assertEqual(r, [])
        r = [i for i in xrange(-6, -2, -1)]
        self.assertEqual(r, [])
        self.assertEqual(str(xrange(3)), "xrange(3)")
        self.assertEqual(str(xrange(3,4)), "xrange(3, 4)")
        self.assertEqual(str(xrange(3,4,5)), "xrange(3, 8, 5)")
        self.assertEqual(str(xrange(14,3,-5)), "xrange(14, -1, -5)")

    def testForLoop(self):
        n1 = 0
        n2 = 0
        for i in range(10):
            n1 += i
            for i in xrange(4):
                n2 += i
        self.assertEqual(n1, 45)
        self.assertEqual(n2, 60)
        self.assertEqual(i, 3)

        try:
            for i in xrange(4):
                raise StopIteration
            self.fail("Failed to raise StopIteration")
        except StopIteration:
            self.assertTrue(True)
        self.assertEqual(i, 0)

        e = 0
        i = -1
        for i in range(1):
            pass
        else:
            e = 1
        self.assertEqual(i, 0)
        self.assertEqual(e, 1)

        e = 0
        i = -1
        for i in range(0):
            pass
        else:
            e = 1
        self.assertEqual(i, -1)
        self.assertEqual(e, 1, "bug #316 for X in Y:... else ...")

        e = 0
        i = -1
        for i in range(1):
            e = 1
            break
        else:
            e = 2
        self.assertEqual(i, 0)
        self.assertEqual(e, 1)


    def testIter(self):

        class i:
            def __init__(self):
                self.idx = 0

            def __iter__(self):
                return self

            def next(self):
                self.idx += 1
                if self.idx == 5:
                    raise StopIteration
                return self.idx


        res = []
        try:
            for j in i():
                res.append(j)
                if len(res) > 5:
                    self.fail("too many items in user-defined iterator")
                    break
        except:
            self.fail("error in user-defined iterator (caught here so tests can proceed)")
            
        self.assertEqual(res, range(1,5))

    def testSorted(self):
        lst1 = range(10)
        lst2 = range(10)
        lst2.reverse()
        self.assertTrue(lst1 == sorted(lst2), "lst1 == sorted(lst2)")

        self.assertTrue(lst1 == sorted(xrange(10)), "lst1 == sorted(xrange(1))")
        self.assertTrue(lst2 == sorted(xrange(10), reverse=True), "lst2 == sorted(xrange(10), reverse=True)")

    def testReversed(self):
        lst1 = range(10)
        lst2 = range(10)
        lst2.reverse()
        tpl1 = tuple(lst1)
        self.assertTrue(lst1 == list(reversed(lst2)), "lst1 == reversed(lst2)")
        self.assertTrue(lst2 == list(reversed(xrange(10))), "lst2 == reversed(xrange(10), reverse=True)")
        self.assertTrue(lst2 == list(reversed(tpl1)), "lst1 == reversed(lst2)")
        dict1 = {'a': 'A', 'b': 'B'}
        self.assertRaises(TypeError, reversed, dict1)


    def testType(self):
        try:
            self.assertTrue(type(object) is type)
        except NotImplementedError, why:
            self.fail("Bug #229" + str(why))

    def testIter(self):
        class G(object):
            def __getitem__(self, i):
                if 0 <= i <= 4:
                    return i
                raise IndexError("index out of range")
        def fn():
            for i in [0,1,2,3,4]:
                yield i

        lst = [0,1,2,3,4]
        self.assertEqual(lst, list(iter(lst)), "iter(lst)")
        g = G()
        self.assertEqual(lst, list(iter(g)), "iter(g)")
        self.assertEqual(lst, list(iter(fn().next, 5)), "iter(fn().next, 5)")
        self.assertEqual([0,1], list(iter(fn().next, 2)), "iter(fn().next, 2)")

    def testReduce(self):
        v = reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
        self.assertEqual(v, 15)

    def testZip(self):
        lst1 = [0,1,2,3]
        lst2 = [10,11,12]
        dict1 = {'a': 'A', 'b': 'B'}
        v = zip(lst1)
        self.assertEqual(v, [(0,), (1,), (2,), (3,)])
        v = zip(lst1, lst2)
        self.assertEqual(v, [(0, 10), (1, 11), (2, 12)])
        v = zip(dict1)
        self.assertEqual(v, [('a',), ('b',)])
        v = zip(lst1, dict1, lst2)
        self.assertEqual(v, [(0, 'a', 10), (1, 'b', 11)])

    def testSum(self):
        self.assertEqual(6, sum([0,1,2,3]))
        self.assertEqual(5, sum([0,1,2,3], -1))
        self.assertRaises(TypeError, sum, [0,1,2,3], "a")
