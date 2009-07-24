import pyjslib
from UnitTest import UnitTest

class Foo:pass

class JSOTest(UnitTest):

    """tests for javascript object conversion"""

    def testJSObject(self):
        f1 = Foo()
        d = {'f1key': f1}
        self.assertEqual(pyjslib.toJSObjects(d).f1key, f1)

        f2 = Foo()
        d = {'x':1, 'y':[1,2,3], 'z':{'a':3}, 'f': f1}
        dd = {'d':d}
        self.assertEqual(pyjslib.toJSObjects(dd).d.z.a, 3)




