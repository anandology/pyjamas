from UnitTest import UnitTest

from ClassTest import PassMeAClass
from ClassTest import ExampleChildClass
from ClassTest import ExampleMultiSuperclassParent1
import Factory2

import imports.decors # must be in this form

class Handler:

    def __init__(self, x):
        self._x = x

    def handle(self, y):
        return self._x is y

def aProcedure():
    x = 1
    if x is 2:
        # a return statement which is not reached
        return "something"
    #this is a comment

def aFunctionWithOnlyDoc():
    """Only a doc string"""

def aFunctionReturningNone():
    return None

def aFunctionReturningParam(param):
    return param

def aFunctionReturningFunction():
    return aFunctionReturningParam

def aFunctionReturningGlobalX1():
    return x

def aFunctionReturningGlobalX2():
    return x

def aFunctionReturningGlobalX3():
    a = x
    return a

def aFunctionReturningLocalX():
    x = 'local test'
    return x

def aFunctionReturningArgX(x):
    return x

x = 'global test'

name = 'mapping-test'
def call(default, arguments, this, label=None):
    return (name, default, arguments, this, label)

def functionDefaults(s = "", l = []):
    n = len(l)
    s = s + "%d" % n
    l.append(n)
    return s, l

class FunctionTest(UnitTest):

    def testLambda(self):
        f = lambda x: x
        self.assertEqual(f(1), 1)
        f = lambda x=1: x
        self.assertEqual(f(), 1)
        self.assertEqual(f(2), 2)

        f = lambda x, y: x*y
        self.assertEqual(f(2,3), 6)
        f = lambda x, y=4: x*y
        self.assertEqual(f(2), 8)
        h = Handler(5)
        f = lambda x: h.handle(x)
        self.assertTrue(f(5))
        self.assertFalse(f(4))

        f = lambda a, b=1, **kw: (a,b,kw)
        v = f(b = 2, c = 3, a = 1)
        self.assertEqual(v[0], 1)
        self.assertEqual(v[1], 2)
        self.assertEqual(v[2]['c'], 3)

        f = lambda a, b=1, *args: (a, b, args)
        v = f(1,2,3,4)
        self.assertEqual(v[2][0], 3)
        self.assertEqual(v[2][1], 4)
    
        try:
            class ClassWithLambdas1:
                f1 = [lambda *args: args[0]]
        except:
            self.fail("issue #385 - lambda in class definition")
        else:
            c = ClassWithLambdas1()
            self.assertEqual(c.f1[0](1), 1, 'issue #385 - lambda function called as bound method')

        try:
            class ClassWithLambdas2:
                f2 = lambda *args: args[0]
        except:
            self.fail("issue #385 - lambda in class definition")
        else:
            c = ClassWithLambdas2()
            self.assertEqual(c.f2(1), c, 'issue #385 - bound method lambda called as function')

    def testProcedure(self):
        self.assertTrue(aFunctionReturningNone() is None,
                        "Function should return None")
        self.assertTrue(aProcedure() is None,
                        "Procedures should always return None")

    def testVariableFunction(self):
        self.assertEqual((aFunctionReturningParam)("foo"), "foo")
        self.assertEqual(aFunctionReturningFunction()("foo"), "foo")

    def testLookup(self):
        expected_result1 = 'global test'
        expected_result2 = 'local test'
        self.assertEqual(aFunctionReturningGlobalX1(), expected_result1)
        self.assertEqual(aFunctionReturningGlobalX2(), expected_result1)
        self.assertEqual(aFunctionReturningGlobalX3(), expected_result1)
        self.assertEqual(aFunctionReturningLocalX(), expected_result2)
        self.assertEqual(aFunctionReturningArgX('test'), 'test')

    def testNameMapping(self):
        r = call(1, 2, this=3, label=4)
        self.assertEqual(r[0], 'mapping-test')
        self.assertEqual(r[1], 1)
        self.assertEqual(r[2], 2)
        self.assertEqual(r[3], 3)
        self.assertEqual(r[4], 4)

    def testFactory(self):

        Factory2.gregister("passme", PassMeAClass)
        Factory2.gregister("exchild", ExampleChildClass)
        Factory2.gregister("mscp1", ExampleMultiSuperclassParent1)

        pmc = Factory2.ggetObject("passme")
        self.assertEqual(pmc.foo(), "foo in PassMeAClass")

        try:
            pmc = Factory2.ggetObject("mscp1", 5)
        except:
            self.assertEqual(False, True, "Exception indicates bug in compiler: 'Error: uncaught exception: ExampleMultiSuperclassParent1() arguments after ** must be a dictionary 5'")
        else:
            self.assertEqual(pmc.x, 5)
        try:
            pmc = Factory2.ggetObject("exchild", 5, 7) # 5 is ignored
        except:
            self.assertEqual(False, True, "Exception indicates bug in compiler: 'Error: uncaught exception: ExampleChildClass() arguments after ** must be a dictionary 7'")
        else:
            self.assertEqual(pmc.prop_a, 1)
            self.assertEqual(pmc.prop_b, 7)

    def testSliceFunc(self):
        s = "123 "
        s = s[1:].rstrip()
        self.assertEqual(s, "23")

    def testFunctionDefaults(self):
        s, l = functionDefaults()
        self.assertEqual(s, '0')
        self.assertTrue(l == [0], "First mutable default mismatch")

        s, l = functionDefaults()
        #self.assertEqual(s, '1') # can be enabled when the next line is fixed
        self.assertTrue(l == [0, 1], "Second mutable default mismatch bug #214")

        inittest = 1
        def f(inittest = inittest):
            return inittest
        self.assertEqual(f(), inittest)

    def testKwargs(self):
        def f(**kwargs):
            return kwargs

        self.assertEqual(f(), {})
        self.assertEqual(f(a=1), dict(a=1))

    def testFunctionDecorating(self):
        log = []
        def deco1(f):
            def fn(*args, **kwargs):
                log.append("deco1 begin")
                res = f(*args, **kwargs)
                log.append("deco1 end")
                return res
            return fn

        def deco2(f):
            def fn(*args, **kwargs):
                log.append("deco2 begin")
                res = f(*args, **kwargs)
                log.append("deco2 end")
                return res
            return fn

        @deco1
        def fn1(a, b = 0):
            return a, b

        @deco1
        @deco2
        def fn2(a, b = 0):
            return a, b

        res = fn1(1,2)
        self.assertEqual(res[0], 1)
        self.assertEqual(res[1], 2)
        self.assertEqual(len(log), 2)
        self.assertEqual(log[0], "deco1 begin")
        self.assertEqual(log[1], "deco1 end")

        log = []
        res = fn2(a=3)
        self.assertEqual(res[0], 3)
        self.assertEqual(res[1], 0)
        self.assertEqual(len(log), 4)
        self.assertEqual(log[0], "deco1 begin")
        self.assertEqual(log[1], "deco2 begin")
        self.assertEqual(log[2], "deco2 end")
        self.assertEqual(log[3], "deco1 end")

        @imports.decors.othermoduledeco1
        def fn3(x):
            return "b"

        self.assertEqual(fn3("b"), "abc")

    def testTopLevelContionalFunction(self):
        self.assertEqual(imports.conditional_func(), "overridden")

