import UnitTest
import foo

module_global_x = 1

data = []
data.append(5)
data.append(6)

data_test = cmp(data, [1,2,3])

def changeme(lst):
    lst[0] = 5

# setting the bases as a GetAttr expression here is by intent to test
# GetAttr nodes in Class bases
class VarsTest(UnitTest.UnitTest):
    def __init__(self):
        UnitTest.UnitTest.__init__(self)

    def getName(self):
        return "Vars"

    def testGlobalListData(self):
        global data
        global data_test

        self.assertTrue(cmp(data, [1,2,3]), "global list should be [1,2,3]")
        self.assertTrue(data_test, "global test of list should be True")

    def testChangeUsingTopLevelFunction(self):
        l = [1,2,3]
        changeme(l)
        self.assertEqual(l[0], 5)

    def testChangeVarInInnerScope(self):
        x = 5
        if x is 1:
            x = 2
        elif x is 5:
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

    def testUnpack(self):
        l = [1, 2]
        x, y = l
        self.assertEqual(x, 1)
        self.assertEqual(y, 2)

    def testUnpackInLoop(self):
        l = [[1, 2],[1, 2]]
        for xxx, yyy in l:
            self.assertEqual(xxx, 1)
            self.assertEqual(yyy, 2)

    def testImportedNamespace(self):
        self.assertEqual(foo.Bar.X, 1)
        # XXX: the next line does not work because we assume that we
        # import classes, which is wrong.
        #self.assertEqual(foo.bar.X, 1)
