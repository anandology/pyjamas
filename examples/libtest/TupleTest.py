from UnitTest import UnitTest

class TupleTest(UnitTest):
    def __init__(self):
        UnitTest.__init__(self)

    def getName(self):
        return "Tuple"

    def testContains(self):
        value = (0, 1, 2, 3, 4)
        self.assertTrue(1 in value)
        self.assertFalse(10 in value)
