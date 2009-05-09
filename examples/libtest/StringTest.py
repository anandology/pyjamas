# -*- coding: utf-8 -*-
from UnitTest import UnitTest
import write

class StringTest(UnitTest):
    def __init__(self):
        UnitTest.__init__(self)

    def getName(self):
        return "String"

    def testReplace(self):
        text="this is a rather long string"
        expected_result1="th--- --- a rather long string"
        expected_result2="thi-- is a rather long string"
        expected_result3="this_is_a_rather_long_string"

        result=text.replace("is", "---")
        self.assertEquals(result, expected_result1)

        result=text.replace("s", "--", 1)
        self.assertEquals(result, expected_result2)

        result=text.replace(" ", "_")
        self.assertEquals(result, expected_result3)

    def testFind(self):
        text="this is a rather long string"

        result=text.find("not found")
        self.assertEquals(result, -1)

        result=text.find("is")
        self.assertEquals(result, 2)

        result=text.find("is", 3)
        self.assertEquals(result, 5)

        result=text.find("is", 2, 3)
        self.assertEquals(result, -1)

    def testJoin(self):
        data="this is a rather long string"
        data=data.split(" ")
        sep1=", "
        sep2=""
        expected_result1="this, is, a, rather, long, string"
        expected_result2="thisisaratherlongstring"

        result=sep1.join(data)
        self.assertEquals(result, expected_result1)

        result=sep2.join(data)
        self.assertEquals(result, expected_result2)

    def testSplit(self):
        text=" this is  a rather long string  "
        space=" "
        empty=""
        expected_result1=" this is  a rather long string  "
        expected_result2="thisis  a rather long string  "
        expected_result3="this is a rather long string"

        t = text.split(space)
        self.assertEquals(t[0], '')
        self.assertEquals(t[1], 'this')
        self.assertEquals(t[2], 'is')
        self.assertEquals(t[3], '')
        self.assertEquals(t[4], 'a')

        result=space.join(t)
        self.assertEquals(result, expected_result1)

        result=empty.join(text.split(space, 2))
        self.assertEquals(result, expected_result2)

        result=space.join(text.split())
        self.assertEquals(result, expected_result3)

        result=empty.split()
        self.assertEquals(len(result), 0)

    def testStrip(self):
        text=" this is  a rather long string  "
        expected_result1="this is  a rather long string"
        expected_result2="a rather long string"

        result=text.strip()
        self.assertEquals(result, expected_result1)

        result=text.strip(" sthi")
        self.assertEquals(result, expected_result2)

    def testUnicode(self):
        text=u"""Liebe 'hallo' "grüsse" Grüsse"""
        self.assertEqual(text, text[:])

    def testIsDigit(self):
        self.assertEqual("123".isdigit(), True)

        self.assertEqual("-123".isdigit(), False)

        self.assertEqual("123.45".isdigit(), False)

        self.assertEqual("1a".isdigit(), False)

        self.assertEqual("   ".isdigit(), False)

    def testStringIterate(self):
        text=" this is  a rather long string  "
        t = ''
        for x in text:
            t += x
        self.assertEqual(text, t)

    def testStrTuple(self):
        self.assertEqual(str((5,6)), "(5, 6)")

    def testStrList(self):
        self.assertEqual(str([5,6]), "[5, 6]")

    def testStartsWith(self):
        s = 'abcd'
        self.assertEqual(s.startswith('ab'), True)
        self.assertEqual(s.startswith('ab', 0), True)
        self.assertEqual(s.startswith('ab', 1), False)
        self.assertEqual(s.startswith('bc', 1), True)
        self.assertEqual(s.startswith('ab', 0, 8), True)
        self.assertEqual(s.startswith('ab', 0, 3), True)
        self.assertEqual(s.startswith('ab', 0, 2), True)
        self.assertEqual(s.startswith('ab', 0, 1), False)

    def testEndsWith(self):
        s = 'abcd'
        self.assertEqual(s.endswith('cd'), True)
        self.assertEqual(s.endswith('cd', 0), True)
        self.assertEqual(s.endswith('cd', 2), True)
        self.assertEqual(s.endswith('cd', 3), False)
        self.assertEqual(s.endswith('cd', 0, 3), False)
        self.assertEqual(s.endswith('bc', 0, 3), True)

    def testLjust(self):
        self.assertEqual('a'.ljust(0), 'a')
        self.assertEqual('a'.ljust(4), 'a   ')
        self.assertEqual('a'.ljust(4, 'b'), 'abbb')

    def testRjust(self):
        self.assertEqual('a'.rjust(4, 'b'), 'bbba')

    def testCenter(self):
        self.assertEqual('a'.center(4, '1'), '1a11')

    def testSprintfList(self):
        self.assertEqual("%s" % 'foo', "foo")
        self.assertEqual("%% %s" % '', "% ")
        self.assertEqual("[%% %s]" % '', "[% ]")
        self.assertEqual("[%c]" % 0x20, '[ ]')
        self.assertEqual("[%r]" % 11, "[11]")
        self.assertEqual("[%s]" % 11, "[11]")
        self.assertEqual("[%d]" % 11, "[11]")
        self.assertEqual("[%i]" % 11, "[11]")
        self.assertEqual("[%u]" % 11, "[11]")
        self.assertEqual("[%e]" % 11, "[1.100000e+01]")
        self.assertEqual("[%E]" % 11, "[1.100000E+01]")
        self.assertEqual("[%f]" % 11, "[11.000000]")
        self.assertEqual("[%F]" % 11, "[11.000000]")
        self.assertEqual("[%g]" % 11, "[11]")
        self.assertEqual("[%G]" % 11, "[11]")
        self.assertEqual("[%o]" % 11, "[13]")
        self.assertEqual("[%x]" % 11, "[b]")
        self.assertEqual("[%X]" % 11, "[B]")
        self.assertEqual("%*g,%10f" % (6, 1.234, 1.234), " 1.234,  1.234000")
        self.assertEqual("%0*g,%010f" % (6, 1.234, 1.234), "01.234,001.234000")
        self.assertEqual("[%04x]" % 1234, "[04d2]")
        # FIXME: Next line fails. Slightly different output.
        #self.assertEqual("[%g,%g,%g,%g,%g]" % (1.234567, 123456.7, 1234567, 0.0001234, 0.00001234), "[1.23457,123457,1.23457e+06,0.0001234,1.234e-05]")
        self.assertEqual("[%3% %s]" % 'a', "[  % a]")

        try:
            s = "%*g,%10f" % (1, 2)
            self.fail('Failed to raise error for "%*g,%10f" % (1, 2)')
        except TypeError, e:
            self.assertEqual(str(e), "not enough arguments for format string")
        try:
            s = "%*g,%10f" % (1, 2, 3, 4)
            self.fail('Failed to raise error for "%*g,%10f" % (1, 2, 3, 4)')
        except TypeError, e:
            self.assertEqual(str(e), "not all arguments converted during string formatting")

    def testSprintfDict(self):
        testdict = {'s1': 'string',
                    's2': 'another string',
                    'v0': 0,
                    'v1': 1,
                    'v2': 1.234,
                   }
        self.assertEqual("[%(v1)12s|%(v1)-12s]" % testdict, '[           1|1           ]')
        self.assertEqual("[%(v1)012o|%(v1)-012o]" % testdict, '[000000000001|1           ]')
        self.assertEqual("[%(v1)#012o|%(v1)#-012o]" % testdict, '[000000000001|01          ]')
        self.assertEqual("[%(v0)#012o|%(v0)#-012o]" % testdict, '[000000000000|0           ]')
        self.assertEqual("[%(v1)#012x|%(v1)#-012x]" % testdict, '[0x0000000001|0x1         ]')
        self.assertEqual("%(s1)3% %(s1)s" % testdict, '  % string')
        #FIXME: next line failes, since it's a mixture of Dict/Tuple format
        #self.assertEqual("%3% %(s1)s" % testdict, '  % string')
        self.assertEqual("%(v1)#g" % testdict, '1.00000')

        try:
            s = "%(not-there)s" % testdict
            self.fail('Failed to raise error for "%(not-there)s" % testdict')
        except KeyError, e:
            self.assertEqual(str(e), "'not-there'")
