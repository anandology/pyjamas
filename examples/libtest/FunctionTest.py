from UnitTest import UnitTest

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
    global x
    return x

def aFunctionReturningGlobalX2():
    global x
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

class FunctionTest(UnitTest):

    def __init__(self):
        UnitTest.__init__(self)

    def getName(self):
        return "Function"

    def testLambda(self):
        # NOTE: kwargs and varargs are currently not supported and
        # raise a TranslationError
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

