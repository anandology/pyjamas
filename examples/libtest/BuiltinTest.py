from UnitTest import UnitTest

class Foo:
    pass

class BuiltinTest(UnitTest):
    def __init__(self):
        UnitTest.__init__(self)

    def getName(self):
        return "Builtin"

    def testMinMax(self):
        self.assertEqual(max(1,2,3,4), 4)
        self.assertEqual(min(1,2,3,4), 1)
        self.assertEqual(max([1,2,3,4]), 4)
        self.assertEqual(min([1,2,3,4]), 1)
        self.assertTrue(max([5,3,4],[6,1,2]) == [6,1,2] , "max([5,3,4],[6,1,2])")
        self.assertTrue(min([5,3,4],[6,1,2]) == [5,3,4] , "min([5,3,4],[6,1,2])")

    def testInt(self):
        self.assertEqual(int("5"), 5)

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
            self.assertEqual(why.message, "hex() argument can't be converted to hex")

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

    def testDivmod(self):
        test_set = [(14, 3, 4, 2),
                    (14.1, 3, 4.0, 2.1),
                    (14.1, 3.1, 4.0, 1.7),
                   ]
        for x, y, p, q in test_set:
            d = divmod(x,y)
            self.assertEqual(d[0], p)
            self.assertEqual(abs(d[1] - q) < 0.00001, True)

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

