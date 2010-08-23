# -*- coding: utf-8 -*-
from UnitTest import UnitTest
import write

class StringTest(UnitTest):

    def testBasestring(self):
        s = 'A string'
        self.assertTrue(isinstance(s, str), "isinstance(s, str)")
        self.assertTrue(isinstance(s, basestring), "isinstance(s, basestring)")

    def testToString(self):
        # TODO: this fails on IE, because we can not override toString
        # in the normal way
        # we need to do something like this
        # http://webreflection.blogspot.com/2007/07/quick-fix-internet-explorer-and.html
        o = ClassWithOwnToString()
        self.assertEquals(o.toString(), 'ClassWithOwnToString as a String')
        o = ClassWithOwnToString2()
        try:
            self.assertEquals(o.toString(), 'ClassWithOwnToString2 as a String')
        except AttributeError, e:
            #AttributeError: 'ClassWithOwnToString2' object has no attribute 'toString
            # mapping of toString to __str__ is not available in normal python
            pass

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

    def testRFind(self):
        text="this is a yes it is a rather long string"

        result=text.rfind("not found")
        self.assertEquals(result, -1)

        result=text.rfind("is")
        self.assertEquals(result, 17)

        result=text.rfind("is", 18)
        self.assertEquals(result, -1)

        result=text.rfind("is", 17)
        self.assertEquals(result, 17)

        result=text.rfind("is", 16)
        self.assertEquals(result, 17)

        result=text.rfind("is", 2, 3)
        self.assertEquals(result, -1)

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
        self.assertEquals(result, [])

        result=empty.split(None)
        self.assertEquals(result, [])

        result=empty.split(' ')
        self.assertEquals(result, [''])

    def testStrip(self):
        text=" this is  a rather long string  "
        expected_result1="this is  a rather long string"
        expected_result2="a rather long string"

        result=text.strip()
        self.assertEquals(result, expected_result1)

        result=text.strip(" sthi")
        self.assertEquals(result, expected_result2)

        result=text.strip("")
        self.assertEquals(result, text)

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
        
    def testStrFloat(self):
        f1 = 1.5
        self.assertEqual(str(f1), "1.5")
        self.assertEqual(f1.__str__(), "1.5", "float.__str__() returns type instead of value, bug #487")

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

    def testZfill(self):
        self.assertEqual('a'.zfill(4), '000a')

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
        self.assertEqual("[%.2f]" % 11, "[11.00]")
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

        # Check for handling of newlines in format string
        self.assertEqual("\n%s\n%s\n" % ('s1', 's2'), '\ns1\ns2\n')

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

        # Check for handling of newlines in format string
        self.assertEqual("\n%(s1)s\n%(s1)s\n" % testdict, '\nstring\nstring\n')

    def testSprintfVar(self):
        f = "%s"
        self.assertEqual(f % 'test', 'test')

    def testIndex(self):
        s = "12345"
        self.assertEqual(s[0], '1')
        self.assertEqual(s[-1], '5')
        self.assertEqual(s[1:-1], '234')
        try:
            a = s[200]
            self.fail("Failed to raise an IndexError")
        except IndexError, e:
            self.assertEqual(e[0], 'string index out of range')
        try:
            a = s[-200]
            self.fail("Failed to raise an IndexError")
        except IndexError, e:
            self.assertEqual(e[0], 'string index out of range')

    def testOperator(self):
        self.assertEqual("1".__add__("2"), "12")
        self.assertEqual("1".__mul__(2), "11")
        self.assertEqual("1".__rmul__(3), "111")
        self.assertEqual("2" * 3, "222")
        self.assertEqual(3 * "3", "333")

    def testIsAlnum(self):
        self.assertTrue("abc".isalnum())
        self.assertTrue("0bc".isalnum())
        self.assertFalse(".?abc".isalnum())
        self.assertFalse(" 0bc".isalnum())

    def testIsAlpha(self):
        self.assertTrue("abc".isalpha())
        self.assertFalse("0bc".isalpha())

    def testIsUpper(self):
        self.assertTrue("ABC".isupper(), "ABC")
        self.assertFalse("AbC".isupper(), "AbC")
        self.assertTrue("A0C".isupper(), "A0C")
        self.assertFalse("A0c".isupper(), "A0c")
        self.assertTrue("A C".isupper(), "A C")
        self.assertFalse("A c".isupper(), "A c")


class ClassWithOwnToString(object):

    def toString(self):
        return 'ClassWithOwnToString as a String'

class ClassWithOwnToString2(object):

    def __str__(self):
        return 'ClassWithOwnToString2 as a String'

