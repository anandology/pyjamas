import UnitTest
import foo
import foo as myfoo
from foo import foo_value as myfoo_value, get_foo_value as myget_foo_value

module_global_x = 1

data = []
data.append(5)
data.append(6)

data_test = cmp(data, [1,2,3])

def changeme(lst):
    lst[0] = 5

def import_sys():
    global sys
    import sys

# setting the bases as a GetAttr expression here is by intent to test
# GetAttr nodes in Class bases
class VarsTest(UnitTest.UnitTest):

    def testGlobalListData(self):
        self.assertTrue(cmp(data, [1,2,3]), "global list should be [1,2,3]")
        self.assertTrue(data_test, "global test of list should be True")

    def testChangeUsingTopLevelFunction(self):
        l = [1,2,3]
        changeme(l)
        self.assertEqual(l[0], 5)

    def testChangeVarInInnerScope(self):
        x = 5
        if x == 1:
            x = 2
        elif x == 5:
            x = 3
        self.assertEqual(x, 3, "the value of x should be 3")

    def testGlobalVars(self):
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
        b = foo.Bar()
        self.assertEqual(b.X, 1) # declared instance works
        self.assertEqual(foo.Bar.X, 1) # XXX due to __Bar, this fails.  hmmm...
        self.assertEqual(foo.bar.X, 1)

    def testImport(self):
        global sys
        a0 = foo.foo_value
        a1 = 2
        self.assertEqual(myfoo_value, a0)
        self.assertEqual(myget_foo_value(), a0)
        myfoo.foo_value = a1
        self.assertEqual(myfoo_value, a0)
        self.assertEqual(myget_foo_value(), a1)
        import_sys()
        try:
            self.assertEqual(sys.__name__, 'sys')
        except:
            self.fail("Global module sys not available (bug #216)")

