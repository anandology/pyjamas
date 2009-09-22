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

    def testIter2(self):
        i = 0

        for item in (0,1,2,3):
            self.assertEqual(item, i)
            i += 1

        i = 0
        for item in (0,1,2,3)[1:-1]:
            i += item
        self.assertEqual(i, 3)

    def testIter(self):
        t = (0,1,2,3)
        i = 0

        it = t.__iter__()
        while True:
            try:
                item = it.next()
            except StopIteration:
                break
            self.assertEqual(item, t[i])
            i += 1

