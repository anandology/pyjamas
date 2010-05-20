# Testing time module

import sys
import UnitTest
import time


class TimeModuleTest(UnitTest.UnitTest):

    def time_tuple(self, tm):
        return (
            tm.tm_year,
            tm.tm_mon,
            tm.tm_mday,
            tm.tm_hour,
            tm.tm_min,
            tm.tm_sec,
            tm.tm_wday,
            tm.tm_yday,
            tm.tm_isdst,
        )

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
        self.assertEqual(ttuple[4], 2,    "Minute mismatch")
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

    def testAsctime(self):
        t = (2010, 5, 19, 9, 22, 44, 2, 139, 1)
        self.assertEqual(
            time.asctime(t),
            'Wed May 19 09:22:44 2010',
        )

    def testLocaltime(self):
        start2010utc = 1262304000
        self.assertEqual(
            self.time_tuple(time.gmtime(start2010utc)),
            (2010, 1, 1, 0, 0, 0, 4, 1, 0),
        )
        t1 = time.gmtime(start2010utc - time.timezone)
        t2 = time.localtime(start2010utc)
        self.assertEqual(self.time_tuple(t1), self.time_tuple(t2))

    def testGmtime(self):
        start2010utc = 1262304000
        day = 86400
        for i in [0,1,2,3,29,30]:
            self.assertEqual(
                self.time_tuple(time.gmtime(start2010utc + i*day)),
                (2010, 1, i+1, 0, 0, 0, (4+i)%7, i+1, 0),
            )




if __name__ == '__main__':
    from write import writebr

    class RunTests:
        def __init__(self):
            self.testlist = {}
            self.test_idx = 0

        def add(self, test):
            self.testlist[len(self.testlist)] = test

        def start_test(self):
            if self.test_idx >= len(self.testlist):
                return

            idx = self.test_idx
            self.test_idx += 1

            test_kls = self.testlist[idx]
            t = test_kls()
            t.start_next_test = getattr(self, "start_test")
            t.run()

    t = RunTests()
    t.add(TimeModuleTest)
    t.start_test()
