# Testing time module

import sys
import UnitTest
import time


class TimeModuleTest(UnitTest.UnitTest):
    def __init__(self):
        UnitTest.UnitTest.__init__(self)

    def getName(self):
        return "TimeModule"

    def testBasics(self):
        t = time.time()
        self.assertTrue(t > 1246924800, "time.time() result invalid")
        ttuple1 = time.gmtime(t)
        t1 = time.mktime(ttuple1)
        ttuple2 = time.localtime(t + time.timezone)
        t2 = time.mktime(ttuple2)
        self.assertTrue(t1 == t2, "t1 and t2 differ")
        self.assertEqual(ttuple1[0], ttuple2[0])
        self.assertEqual(ttuple1[1], ttuple2[1])
        self.assertEqual(ttuple1[2], ttuple2[2])

        t = 1246446123
        ttuple = time.gmtime(t)
        self.assertEqual(ttuple[0], 2009, "Year mismatch")
        self.assertEqual(ttuple[1], 7,    "Month mismatch")
        self.assertEqual(ttuple[2], 1,    "Month day mismatch")
        self.assertEqual(ttuple[3], 11,   "Hour mismatch")
        self.assertEqual(ttuple[4], 2,   "Minute mismatch")
        self.assertEqual(ttuple[5], 3,    "Second mismatch")
        self.assertEqual(ttuple[6], 2,    "Week day mismatch")
        self.assertEqual(ttuple[7], 182,  "Year day mismatch")
        self.assertEqual(ttuple[8], 0,    "DST mismatch")

    def testStrftime(self):
        t = 1246446000
        ttuple = time.gmtime(t)
        s = time.strftime("-%%-%d-%H-%I-%j-%m-%M-%p-%S-%w-%W-%y-%Y-", ttuple)
        self.assertEqual(s, "-%-01-11-11-182-07-00-AM-00-3-26-09-2009-")
        s = time.strftime("%c")
        s = time.strftime("%x")
        s = time.strftime("%X")

