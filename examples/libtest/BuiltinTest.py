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

    def testInt(self):
        self.assertEqual(int("5"), 5)

    def testOrdChr(self):
        for i in range(256):
            self.assertEqual(ord(chr(i)), i)


