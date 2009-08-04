from UnitTest import UnitTest

try:
    builtin_value = builtin.value
except:
    builtin_value = None
if False:
    import builtin
import builtin

class Foo:
    pass

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
            self.fail("No int() argument error raised")
        except ValueError, e:
            self.assertEqual(e[0], "invalid literal for int() with base 10: 'not int'")

        try:
            int(1, 10)
            self.fail("No int() argument error raised")
        except TypeError, e:
            self.assertEqual(e[0], "int() can't convert non-string with explicit base")

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
