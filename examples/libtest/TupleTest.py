from UnitTest import UnitTest

class TupleTest(UnitTest):

    def testContains(self):
        value = (0, 1, 2, 3, 4)
        self.assertTrue(1 in value)
        self.assertFalse(10 in value)

    def testTupleAdd(self):
        t1 = (1,2)
        t2 = (3,4)
        added = t1 + t2
        self.assertTrue(added == (1,2,3,4), "t1 + t2")
        t1 += t2
        self.assertTrue(t1 == (1,2,3,4), "t1 += t2")

