from UnitTest import UnitTest
import pyjslib

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

    def testObjectKeys(self):
        f1 = Foo()
        f2 = Foo()
        f3 = Foo()
        d = {f1:1, f2:2}
        self.assertEqual(d[f1], 1)
        self.assertEqual(d[f2], 2)

        k1, k2 = d.keys()
        self.assertEqual(f1, k1)
        self.assertEqual(f2, k2)

        v1, v2 = d.values()
        self.assertEqual(1, v1)
        self.assertEqual(2, v2)

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
        d = pyjslib.Dict(([1, 1], [2,2]))
        self.assertEqual(d[1], 1)
        self.assertEqual(d[2], 2)
        # XXX: the other constructors handle javascript objets only,
        # we need the other constructors too, like:
        # d = pyjslib.Dict({1:1, 2:2})

