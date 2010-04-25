# Testing datetime module

import sys
import UnitTest
import datetime


class DatetimeModuleTest(UnitTest.UnitTest):

    def testDate(self):
        d = datetime.date(2010, 4, 9)
        self.assertEqual(d.year, 2010)
        self.assertEqual(d.month, 4)
        self.assertEqual(d.day, 9)
        self.assertEqual(d.weekday(), 4)

    def testTime(self):
        t = datetime.time(9, 45, 11, 95000)
        self.assertEqual(t.hour, 9)
        self.assertEqual(t.minute, 45)
        self.assertEqual(t.second, 11)
        self.assertEqual(t.microsecond, 95000)

    def testTimestamp(self):
        d = datetime.date.fromtimestamp(1270804609)
        self.assertEqual(str(d), '2010-04-09')
        dt = datetime.datetime.fromtimestamp(1270804609.95)
        self.assertEqual(str(dt), '2010-04-09 11:16:49.950000')

    def testCtime(self):
        d = datetime.date(2010, 4, 9)
        self.assertEqual(d.ctime(), "Fri Apr  9 00:00:00 2010")
        dt = datetime.datetime(2010, 4, 9, 10, 57, 32)
        self.assertEqual(dt.ctime(), "Fri Apr  9 10:57:32 2010")

    def testIsoCalendar(self):
        d = datetime.date(2010, 4, 9)
        self.assertEqual(d.isocalendar(), (2010, 14, 5))
        d1 = datetime.date(2007, 12, 31)
        self.assertEqual(d1.isocalendar(), (2008, 1, 1))

    def testIsoFormat(self):
        d = datetime.date(2010, 4, 9)
        self.assertEqual(d.isoformat(), '2010-04-09')
        dt = datetime.datetime(2010, 4, 9, 10, 57, 32)
        self.assertEqual(dt.isoformat(), '2010-04-09T10:57:32')
        dt2 = datetime.datetime(2010, 4, 9, 10, 57, 32, 95000)
        self.assertEqual(dt2.isoformat(), '2010-04-09T10:57:32.095000')

    def testOrdinal(self):
        d = datetime.date.fromordinal(1)
        self.assertEqual(str(d), '0001-01-01')
        d1 = datetime.date.fromordinal(733871)
        self.assertEqual(str(d1), '2010-04-09')
        self.assertEqual(d1.toordinal(), 733871)

    def testReplace(self):
        d = datetime.date(2010, 4, 9).replace(month=6, day=13)
        self.assertEqual(str(d), '2010-06-13')
        t = datetime.time(23, 59, 59).replace(minute=45, microsecond=95000)
        self.assertEqual(str(t), '23:45:59.095000')
        dt = datetime.datetime(2010, 4, 9, 10, 57, 32).replace(month=6, day=13, hour=12, minute=0, second=0)
        self.assertEqual(str(dt), '2010-06-13 12:00:00')

    def testTimetuple(self):
        tm = datetime.date(2010, 4, 9).timetuple()
        self.assertEqual(tm.tm_year, 2010)
        self.assertEqual(tm.tm_mon, 4)
        self.assertEqual(tm.tm_mday, 9)
        self.assertEqual(tm.tm_hour, 0)
        self.assertEqual(tm.tm_min, 0)
        self.assertEqual(tm.tm_sec, 0)
        self.assertEqual(tm.tm_wday, 4)
        self.assertEqual(tm.tm_yday, 99)

    def testStrftime(self):
        d = datetime.date(2010, 4, 9)
        self.assertEqual(d.strftime("%d/%m/%y"), "09/04/10")

    def testComparision(self):
        d1 = datetime.date(2010, 6, 8)
        d2 = datetime.date(2010, 6, 8)
        d3 = datetime.date(2010, 4, 9)
        self.assertTrue(d1 == d2, "d1 and d2 differ")
        self.assertTrue(d1 > d3, "d1 is not later than d3")
        self.assertTrue(d3 < d1, "d3 is not earlier than d1")

    def testOperations(self):
        d1 = datetime.date(2010, 4, 9)
        d2 = datetime.date(2010, 6, 13)
        diff = d2 - d1
        self.assertEqual(diff.days, 65)
        self.assertEqual(str(d1 + diff), "2010-06-13")
        self.assertEqual(str(d1 - diff), "2010-02-03")

