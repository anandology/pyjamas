from UnitTest import UnitTest

class FloatTest(UnitTest):

    """tests for javascript float conversion"""

    def testZero(self):
        """ test for correct conversion of zero"""
        f1 = float(0)
        self.assertEqual(0.0, f1)

    def testEmptyString(self):
        """ test for ValueError exception on empty string"""
        try:
            f1 = float("")
        except ValueError:
            self.assertTrue(True)
        else:
            self.assertTrue(False)




