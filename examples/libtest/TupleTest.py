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

    # XXX: This does not even compile
    def test_tuple_unpacking(self):
        self.fail('Tuple unpacking not supported for more than one level')
    #    (a, b), c, (d, e) = x
    #    self.assertEqual((a, b, c, d, e), (1, 2, 3, 4, 5))

    # XXX: This does not even compile
    def test_tuple_unpacking_in_loop(self):
        self.fail('Tuple unpacking in for-loops not supported for more than one level')
    #    x = ((1, 2), 3, (4, 5))
    #    for (a, b), c, (d, e) in [x, x, x]:
    #        self.assertEqual((a, b, c, d, e), (1, 2, 3, 4, 5))

    def test_tuple_unpacking_args(self):
        def func(a, (b, c), d):
            return a + b + c + d
        self.assertEqual(func(1, (2, 3), 4), 10, 'Tuple unpacking for args not supported')

    # XXX: This does not even compile
    def test_deep_tuple_unpacking_args(self):
        self.fail('Tuple unpacking in function args not supported for more than one level')
    #    def func(a, (b, (c, d)), e):
    #        return a + b + c + d + e
    #    self.assertEqual(func(1, (2, (3, 4)), 5), 15, 'Tuple unpacking for args not supported')
