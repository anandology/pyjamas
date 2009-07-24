from UnitTest import UnitTest

from write import write, writebr


def add(arg1, arg2):
    return arg1 + arg2


class TypeCompatibilityTest(UnitTest):

    def test_string_plus_number(self):
        try:
            add("string", 1)
        except TypeError:
            pass
        else:
            self.fail('adding "string" and 1 should fail')

        try:
            add(1, "string")
        except TypeError:
            pass
        else:
            self.fail('adding 1 and "string" should fail')

#         self.assertRaises(TypeError, add, "string", 1)
#         self.assertRaises(TypeError, add, 1, "string")
