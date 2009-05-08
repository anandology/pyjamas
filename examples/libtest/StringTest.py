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
