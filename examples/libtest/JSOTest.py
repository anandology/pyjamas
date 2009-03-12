from UnitTest import UnitTest
import pyjslib

class Foo:pass

class JSOTest(UnitTest):

    """tests for javascript object conversion"""

    def __init__(self):
        UnitTest.__init__(self)

    def getName(self):
        return "JSO"


    def testJSObject(self):
        f1 = Foo()
        d = {'f1key': f1}
        self.assertEqual(pyjslib.toJSObjects(d).f1key, f1)

        f2 = Foo()
        d = {'x':1, 'y':[1,2,3], 'z':{'a':3}, 'f': f1}
        dd = {'d':d}
        self.assertEqual(pyjslib.toJSObjects(dd).d.z.a, 3)




