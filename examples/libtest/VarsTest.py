import UnitTest

module_global_x = 1

# setting the bases as a GetAttr expression here is by intent to test
# GetAttr nodes in Class bases
class VarsTest(UnitTest.UnitTest):
    def __init__(self):
        UnitTest.UnitTest.__init__(self)

    def getName(self):
        return "Vars"

    def testChangeVarInInnerScope(self):
        x = 5
        if x == 1:
            x = 2
        elif x == 5:
            x = 3
        self.assertEqual(x, 3, "the value of x should be 3")

    def testGlobalVars(self):
        global module_global_x
        self.assertEqual(module_global_x, 1)

    def testImports(self):
        self.failUnless(UnitTest.UnitTest())

    def testLocalVar(self):
        VarsTest = 1
        self.assertEqual(VarsTest, 1)

