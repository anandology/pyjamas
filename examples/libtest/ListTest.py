from UnitTest import UnitTest

class ListTest(UnitTest):
    def __init__(self):
        UnitTest.__init__(self)

    def getName(self):
        return "List"

    def testSliceGet(self):
        value = [0, 1, 2, 3, 4]

        self.assertTrue(value[-1]==4)
        self.assertTrue(value[1]==1)
        self.assertTrue(value[4]==4)
        self.assertTrue(value[-3]==2)

    def testSliceRange(self):
        value = [0, 1, 2, 3, 4]

        self.assertTrue(value[1:3][0]==1)
        self.assertTrue(value[1:3][1]==2)
        self.assertTrue(len(value[1:2])==1)
        self.assertTrue(len(value[1:3])==2)

        self.assertTrue(value[:2][0]==0)
        self.assertTrue(value[:2][1]==1)
        self.assertTrue(len(value[:2])==2)
        self.assertTrue(len(value[:1])==1)

        self.assertTrue(value[:-1][0]==0)
        self.assertTrue(value[:-1][3]==3)
        self.assertTrue(len(value[:-1])==4)

        self.assertTrue(value[:][3]==3)
        self.assertTrue(len(value[:])==5)

        self.assertTrue(value[0:][3]==3)
        self.assertTrue(value[1:][0]==1)
        self.assertTrue(len(value[1:])==4)

        self.assertTrue(value[-1:][0]==4)
        self.assertTrue(len(value[-1:3])==0)

    def testDelete(self):
        value = [0, 1, 2, 3, 4]
        del value[4]
        self.assertTrue(len(value)==4)
        self.assertTrue(value[3]==3)

        del value[-1]
        self.assertTrue(len(value)==3)
        self.assertTrue(value[2]==2)

    def testPop(self):
        a = ['a']
        b = ['b']
        c = ['c']
        d = ['d']
        e = ['e']

        value = [a, b, c, d, e]

        x = value.pop(4)
        self.assertTrue(x==e)
        self.assertTrue(len(value)==4)

        x = value.pop(-1)
        self.assertTrue(x==d)
        self.assertTrue(len(value)==3)

        x = value.pop()
        self.assertTrue(x==c)
        self.assertTrue(len(value)==2)

        x = value.pop(0)
        self.assertTrue(x==a)
        self.assertTrue(len(value)==1)

    def testSort(self):
        l1 = ['c', 'd', 'a', 'b']
        l1.sort()
        self.assertTrue(l1[0] == 'a')
        self.assertTrue(l1[1] == 'b')
        self.assertTrue(l1[2] == 'c')
        self.assertTrue(l1[3] == 'd')

        l2 = ['C', 'd', 'A', 'b']
        def toLower(x):
            return x.lower()
        l2.sort(None, toLower)
        self.assertTrue(l2[0] == 'A')
        self.assertTrue(l2[1] == 'b')
        self.assertTrue(l2[2] == 'C')
        self.assertTrue(l2[3] == 'd')

        l3 = ['C', 'd', 'A', 'b']
        l3.sort(None, toLower, True)
        self.assertTrue(l3[0] == 'd')
        self.assertTrue(l3[1] == 'C')
        self.assertTrue(l3[2] == 'b')
        self.assertTrue(l3[3] == 'A')

        l4 = ['c', 'd', 'a', 'b']
        l4.sort(None, None, True)
        self.assertTrue(l4[0] == 'd')
        self.assertTrue(l4[1] == 'c')
        self.assertTrue(l4[2] == 'b')
        self.assertTrue(l4[3] == 'a')

    def testSortCmp(self):
        a = A()
        l1 = [a, 1]
        l1.sort()
        l2 = [1, a]
        l2.sort()
        self.assertTrue(l1[0] is a) # don't use == it will call A.__cmp__!
        self.assertTrue(l2[0] is a) # don't use == it will call A.__cmp__!
        self.assertFalse(l1[0] == a) # use == A.__cmp__ always fails

    def testReverse(self):
        l = [1,2,3]
        l.reverse()
        self.assertEqual(l[0], 3)
        self.assertEqual(l[2], 1)

    def testConstructor(self):
        l1 = list()
        self.assertEqual(len(l1),0)

        # only accept list or iterator
        l2 = list()
        self.assertEqual(len(l2),0)

        l3 = list([])
        self.assertEqual(len(l3),0)

        l4 = list([10,])
        self.assertEqual(len(l4),1)
        self.assertEqual(l4[0],10)

        l5 = list(range(10,40,10))
        self.assertEqual(len(l5),3)
        self.assertEqual(l5[0],10)
        self.assertEqual(l5[1],20)
        self.assertEqual(l5[2],30)

        l6 = list(l4)
        self.assertEqual(len(l6),1)
        self.assertEqual(l6[0],10)

    def testExtend(self):
        l = [10,20]
        l.extend([30,40])
        self.assertEqual(len(l),4)
        self.assertEqual(l[0], 10)
        self.assertEqual(l[1], 20)
        self.assertEqual(l[2], 30)
        self.assertEqual(l[3], 40)

        l2 = [10,20]
        l2.extend([])
        self.assertEqual(len(l2),2)

        l3 = []
        l3.extend([10,20])
        self.assertEqual(len(l3),2)
        self.assertEqual(l3[0],10)
        self.assertEqual(l3[1],20)

        l4 = []
        l4.extend([])
        self.assertEqual(len(l4),0)

class A:

    def __cmp__(self, other):
        return -1



