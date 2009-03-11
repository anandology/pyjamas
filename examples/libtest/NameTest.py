from UnitTest import UnitTest

class Handler:

    def __init__(self, x):
        self._x = x

    def get_name(self):
        return self.__class__.__name__

def aProcedure():
    return aProcedure.__name__

class NameTest(UnitTest):

    def __init__(self):
        UnitTest.__init__(self)

    def getName(self):
        return "Name"

    def testClassName(self):
        self.assertEqual(Handler.__name__, "Handler")
        self.assertEqual(Handler.get_name.__name__, "get_name")
        x = Handler(5)
        self.assertEqual(x.__class__.__name__, "Handler")
        self.assertEqual(x.get_name.__name__, "get_name")

    def testProcedureName(self):
        self.assertEqual(aProcedure.__name__, "aProcedure")
        self.assertEqual(aProcedure(), "aProcedure")

    def testModuleName(self):
        self.assertEqual(__name__, "NameTest")

