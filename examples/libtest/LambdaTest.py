from UnitTest import UnitTest

class Handler:

    def __init__(self, x):
        self._x = x

    def handle(self, y):
        return self._x == y

class LambdaTest(UnitTest):

    def __init__(self):
        UnitTest.__init__(self)

    def getName(self):
        return "Lambda"

    def testLambda(self):
        # NOTE: kwargs and varargs are currently not supported an
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
        h = Handler(5, self)
        f = lambda x: h.handle(x)
        self.assertTrue(f(5))
        self.assertFalse(f(4))

