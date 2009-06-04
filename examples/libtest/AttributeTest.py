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
            self.assertEqual(e.__class__.__name__, 'AttributeError')
            return
        self.fail("No AttributeError raised")

    def testSetAttr(self):

        f1 = Foo(1)
        self.assertEqual(f1.getV(), 1)

        f2 = Foo(2)
        self.assertEqual(f2.getV(), 2)

        f3 = Foo(3)
        self.assertEqual(f3.getV(), 3)

        # bound method
        setattr(f1, "getV", getattr(f2, "getV"))
        self.assertEqual(f1.getV(), 2)

        # unbound method
        setattr(f1, "getV", f3.getV) # reeallly need to have __getattr__
        self.assertEqual(f1.getV(), 3)

    def testDelAttr(self):

        foo = Foo(1)
        self.assertEqual(hasattr(foo, "v"), True)
        delattr(foo, "v")
        self.assertEqual(hasattr(foo, "v"), False)
        
        self.assertEqual(hasattr(foo, "getV"), True)
        try:
            delattr(foo, "getV")
            self.fail("No AttributeError raised")
        except AttributeError, e:
            self.assertEqual(str(e), "Foo instance has no attribute 'getV'")

    def testAttrErr(self):
        foo = Foo(1)
        try:
            v = foo.bar
            self.fail("No Error raised on foo.bar")
        except:
            self.assertTrue(True, "Exception raised")
