# Tests for the implementatuion of --no-inline-code

import sys
import UnitTest
import urllib

def test(a):
   return None

class NoInlineCodeTest(UnitTest.UnitTest):

    def test_bool(self):
        i1 = bool(1)
        def fn():
            i2 = True
            bool = test
            i3 = bool(1)
            i4 = True
            self.assertEqual(i1, True)
            self.assertEqual(i1, i2)
            self.assertNotEqual(i1, i3)
            self.assertEqual(i1, i4)
        fn()

    def test_int(self):
        i1 = int(1)
        def fn():
            i2 = 1
            int = test
            i3 = int(1)
            i4 = 1
            self.assertEqual(i1, 1)
            self.assertEqual(i1, i2)
            self.assertNotEqual(i1, i3)
            self.assertEqual(i1, i4)
        fn()

    def test_hexint(self):
        i1 = int(1)
        def fn():
            i2 = 0x1
            int = hex = test
            i3 = int(0x1)
            i4 = 0x1
            self.assertEqual(i1, 1)
            self.assertEqual(i1, i2)
            self.assertNotEqual(i1, i3)
            self.assertEqual(i1, i4)
        fn()

    def test_long(self):
        i1 = long(1)
        def fn():
            i2 = 1L
            long = test
            i3 = long(1)
            i4 = 1L
            self.assertEqual(i1, 1L)
            self.assertEqual(i1, i2)
            self.assertNotEqual(i1, i3)
            self.assertEqual(i1, i4)
        fn()

    def test_float(self):
        i1 = float(1.0)
        def fn():
            i2 = 1.0
            float = test
            i3 = float(1.0)
            i4 = 1.0
            self.assertEqual(i1, 1.0)
            self.assertEqual(i1, i2)
            self.assertNotEqual(i1, i3)
            self.assertEqual(i1, i4)
        fn()

    def test_tuple(self):
        i1 = tuple((1,))
        def fn():
            i2 = (1,)
            tuple = test
            i3 = tuple((1,))
            i4 = (1,)
            self.assertEqual(i1, (1,))
            self.assertEqual(i1, i2)
            self.assertNotEqual(i1, i3)
            self.assertEqual(i1, i4)
        fn()

    def test_list(self):
        i1 = list([1])
        def fn():
            i2 = [1]
            list = test
            i3 = list([1])
            i4 = [1]
            self.assertEqual(i1, [1])
            self.assertEqual(i1, i2)
            self.assertNotEqual(i1, i3)
            self.assertEqual(i1, i4)
        fn()

    def test_dict(self):
        i1 = dict(a=1)
        def fn():
            i2 = {'a':1}
            dict = test
            i3 = dict(a=1)
            i4 = {'a':1}
            self.assertEqual(i1, {'a':1})
            self.assertEqual(i1, i2)
            self.assertNotEqual(i1, i3)
            self.assertEqual(i1, i4)
        fn()

    def test_set(self):
        i1 = set([1])
        _set = set
        def fn():
            set = test
            i3 = set([1])
            i4 = _set([1])
            self.assertNotEqual(i1, i3)
            self.assertEqual(i1, i4)
        fn()

    def test_ArithmeticError(self):
        e1 = ArithmeticError
        def fn():
            ArithmeticError = bool
            try:
                a = 1/0
            except e1, e:
                self.assertTrue(isinstance(e, e1))
                self.assertFalse(isinstance(e, ArithmeticError))
            else:
                self.fail("Failed to raise ArithmeticError")
        fn()
