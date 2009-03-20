from UnitTest import UnitTest

class Handler:

    def __init__(self, x):
        self._x = x

    def handle(self, y):
        return self._x == y

def aProcedure():
    x = 1
    if x == 2:
        # a return statement which is not reached
        return "something"
    #this is a comment

def aArgs(*args):
    return args

def aFunctionReturningNone():
    return None

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

    def testArgs(self):

        args = (1,2)
        res = aArgs(*args)
        self.assertEqual(args, res)

        args = 1
        try:
            res = aArgs(*args)
            called = True
        except TypeError:
            called = False

        self.assertFalse(called,
                    "exception expected but not raised - TypeError: aArgs() argument after * must be a sequence")


        args = (1,)
        res = aArgs(*args)
        self.assertEqual(args, res)

        args = (1,)
        res = aArgs(args)
        self.assertEqual(args, (res,))

