from UnitTest import UnitTest

class Foo:

    def __init__(self, v):
        self.v = v

    def getV(self):
        return self.v


class AttributeTest(UnitTest):
    def __init__(self):
        UnitTest.__init__(self)

    def getName(self):
        return "Attribute"

    def testHasattr(self):
        self.assertEqual(hasattr(self, "getName"), True, "AttrTest should have method 'getName'")
        self.assertEqual(hasattr(self, "blah"), False, "AttrTest has no method 'getName'")

    def testGetattr(self):
        func = getattr(self, "getName")
        self.assertEqual(func(), "Attribute", "getattr does not return correct value'")

        self.assertEqual(1, getattr(Foo, "notthere", 1))
        foo = Foo(1)
        self.assertEqual(foo.v, getattr(foo, "v"))

        # test on none object type
        self.assertEqual(getattr(1, 'x', 2), 2)
        self.assertEqual(getattr(None, 'x', 2), 2)

        try:
            self.assertEqual(1, getattr(foo, "vv"))
        except AttributeError, e:
            self.assertEqual(e.name, 'AttributeError')
            return
        self.fail("No AttributeError raised")

    def testSetAttr(self):

        f1 = Foo(1)
        self.assertEqual(f1.getV(), 1)

        f2 = Foo(2)
        self.assertEqual(f2.getV(), 2)

        # bound method
        setattr(f1, "getV", getattr(f2, "getV"))
        self.assertEqual(f1.getV(), 2)

        # unbound method
        setattr(f1, "getV", f2.getV)
        self.assertEqual(f1.getV(), 1)

