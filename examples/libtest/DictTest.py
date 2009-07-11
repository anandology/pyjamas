from UnitTest import UnitTest

class Foo:
    pass

class DictTest(UnitTest):
    def __init__(self):
        UnitTest.__init__(self)

    def getName(self):
        return "Dict"

    def testStringKeys(self):
        d = {'a':1, 'b':2, '3':3, 3:4}
        self.assertEqual(d['a'], 1)
        self.assertEqual(d['b'], 2)

        # XXX: the length here is 3 because we have the same keys for "3"
        # and 3

        #self.assertEqual(len(d), 4)
        # XXX: we have to have constant handling in the translator in
        # order to distinguish ints and strings, so the lines below do
        # not work
        #self.assertEqual(d['3'], 3)
        #self.assertEqual(d[3], 4)

        try:
            x = d['notthere']
        except KeyError, e:
            self.assertEqual(e.__class__.__name__, 'KeyError')
            self.assertEqual(str(e), "'notthere'")
            return
        self.fail('__getitem__ must raise KeyError')

    def testObjectKeys(self):
        f1 = Foo()
        f2 = Foo()
        f3 = Foo()
        d = {f1:1, f2:2}
        self.assertEqual(d[f1], 1)
        self.assertEqual(d[f2], 2)

        # keys's result has no implied order, so sort explicitly
        keys = d.keys()
        keys.sort()
        expected = [f1, f2]
        expected.sort()
        self.assertEqual(keys, expected)

        # values's result has no implied order, so sort explicitly
        values = d.values()
        values.sort()
        # already sorted
        expected = [1, 2]
        self.assertEqual(values, expected)

        self.failUnless(f1 in d)
        self.failUnless(f2 in d)
        self.failIf(f3 in d)

        self.assertEqual(None, d.get(f3))
        self.assertEqual(1, d.get(f3, 1))

        d.update({f3:3})
        self.failUnless(f3 in d)
        self.assertEqual(d[f3], 3)

        self.assertEqual(3, len(d))

        dd = d.copy()
        self.assertEqual(dd[f3], 3)
        self.failIf(dd is d)

    def testConstructor(self):
        d = dict(([1, 1], [2,2]))
        self.assertEqual(d[1], 1)
        self.assertEqual(d[2], 2)
        # XXX: the other constructors handle javascript objets only,
        # we need the other constructors too, like:
        # d = dict({1:1, 2:2})

    def testIter(self):
        d = {1: [1,2,3], 2: {'a': 1, 'b': 2, 'c': 3}}
        a = 0
        for k in d:
            a += k
        self.assertEqual(a, 3)

        a = 0
        for k in d[1]:
            a += k
        self.assertEqual(a, 6)

        a = 0
        for k in d[1][1:]:
            a += k
        self.assertEqual(a, 5)

        a = 0
        for k in d[2]:
            a += d[2][k]
        self.assertEqual(a, 6)

