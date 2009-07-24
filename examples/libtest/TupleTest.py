from UnitTest import UnitTest

class TupleTest(UnitTest):

    def testContains(self):
        value = (0, 1, 2, 3, 4)
        self.assertTrue(1 in value)
        self.assertFalse(10 in value)
