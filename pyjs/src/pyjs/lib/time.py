# Check http://docs.python.org/library/time.html

from __pyjamas__ import JS
import math

timezone = JS("60 * (new Date(new Date().getFullYear(), 0, 1)).getTimezoneOffset()")
altzone = JS("60 * (new Date(new Date().getFullYear(), 6, 1)).getTimezoneOffset()")
if altzone > timezone:
    # Probably on southern parth of the earth...
    d = timezone
    timezone = altzone
    altzone = d
d = JS("(new Date(new Date().getFullYear(), 0, 1))")
d = d.toLocaleString().split()[-1]
if d[0] == '(':
    d = d[1:-1]
tzname = (d, None)
del d

__c__days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
__c__months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


def time():
    JS("return new Date().getTime() / 1000.0;")

class struct_time(object):
    n_fields = 9
    n_sequence_fields = 9
    n_unnamed_fields = 0
    tm_year = None
    tm_mon = None
    tm_mday = None
    tm_hour = None
    tm_min = None
    tm_sec = None
    tm_wday = None
    tm_yday = None
    tm_isdst = None

    def __init__(self, ttuple = None):
        if not ttuple is None:
            self.tm_year = ttuple[0]
            self.tm_mon = ttuple[1]
            self.tm_mday = ttuple[2]
            self.tm_hour = ttuple[3]
            self.tm_min = ttuple[4]
            self.tm_sec = ttuple[5]
            self.tm_wday = ttuple[6]
            self.tm_yday = ttuple[7]
            self.tm_isdst = ttuple[8]

    def __str__(self):
        t = (
            self.tm_year,
            self.tm_mon,
            self.tm_mday,
            self.tm_hour,
            self.tm_min,
            self.tm_sec,
            self.tm_wday,
            self.tm_yday,
            self.tm_isdst,
        )
        return t.__str__()

    def __getitem__(self, idx):
        return [self.tm_year, self.tm_mon, self.tm_mday, 
                self.tm_hour, self.tm_min, self.tm_sec, 
                self.tm_wday, self.tm_yday, self.tm_isdst][idx]

    def __getslice__(self, lower, upper):
        return [self.tm_year, self.tm_mon, self.tm_mday, 
                self.tm_hour, self.tm_min, self.tm_sec, 
                self.tm_wday, self.tm_yday, self.tm_isdst][lower:upper]

def gmtime(t = None):
    if t == None:
        t = time()
    date = JS("new Date(@{{t}}*1000)")
    tm = struct_time()
    tm.tm_year = date.getUTCFullYear()
    tm.tm_mon = date.getUTCMonth() + 1
    tm.tm_mday = date.getUTCDate()
    tm.tm_hour = date.getUTCHours()
    tm.tm_min = date.getUTCMinutes()
    tm.tm_sec = date.getUTCSeconds()
    tm.tm_wday = (date.getUTCDay() + 6) % 7
    tm.tm_isdst = 0
    startOfYear = JS("new Date('Jan 1 '+ @{{tm}}.tm_year +' GMT+0000')")
    tm.tm_yday = 1 + int((t - startOfYear.getTime()/1000)/86400)
    return tm

def localtime(t = None):
    if t == None:
        t = time()
    date = JS("new Date(@{{t}}*1000)")
    dateOffset = date.getTimezoneOffset()
    tm = struct_time()
    tm.tm_year = date.getFullYear()
    tm.tm_mon = date.getMonth() + 1
    tm.tm_mday = date.getDate()
    tm.tm_hour = date.getHours()
    tm.tm_min = date.getMinutes()
    tm.tm_sec = date.getSeconds()
    tm.tm_wday = (date.getDay() + 6) % 7
    tm.tm_isdst = 0 if timezone == 60*date.getTimezoneOffset() else 1
    startOfYear = JS("new Date(@{{tm}}.tm_year,0,1)") # local time
    startOfYearOffset = startOfYear.getTimezoneOffset()
    startOfDay = JS("new Date(@{{tm}}.tm_year,@{{tm}}.tm_mon-1,@{{tm}}.tm_mday)")
    dt = (startOfDay.getTime() - startOfYear.getTime())/1000
    dt = dt + 60 * (startOfYearOffset - dateOffset)
    tm.tm_yday = 1 + int(dt/86400.0)
    return tm
    if startOfYearOffset != dateOffset:
        # Changed from std to dst or the opposite
        #if startOfYearOffset > dateOffset:
        # Changed from std to dst
        tm.tm_yday += 1
        dt2 = dt + 60 * (startOfYearOffset - dateOffset)
        print dt, dt/86400.0, (startOfYearOffset, dateOffset), dt2, dt2/86400.0
        tm.tm_yday = 1 + int(dt2/86400.0)
    #if tm.tm_isdst and 60*startOfYearOffset == timezone:
    #    tm.tm_yday += 1
    return tm

def mktime(t):
    tm_year = t[0]
    tm_mon = t[1] - 1
    tm_mday = t[2]
    tm_hour = t[3]
    tm_min = t[4]
    tm_sec = t[5]
    date = JS("new Date(@{{tm_year}}, @{{tm_mon}}, @{{tm_mday}}, @{{tm_hour}}, @{{tm_min}}, @{{tm_sec}})") # local time
    if t[8] == 0:
        return date.getTime()/1000 - 60 * date.getTimezoneOffset()
    #return date.getTime()/1000 - 60 * date.getTimezoneOffset() + (60 * date.getTimezoneOffset() - timezone)
    return date.getTime()/1000 - timezone

def strftime(fmt, t = None):
    if t is None:
        t = localtime()
    else:
        if not isinstance(t, struct_time) and len(t) != 9:
            raise TypeError('argument must be 9-item sequence, not float')
    tm_year = t[0]
    tm_mon = t[1]
    tm_mday = t[2]
    tm_hour = t[3]
    tm_min = t[4]
    tm_sec = t[5]
    tm_wday = t[6]
    tm_yday = t[7]
    date = JS("new Date(@{{tm_year}}, @{{tm_mon}} - 1, @{{tm_mday}}, @{{tm_hour}}, @{{tm_min}}, @{{tm_sec}})")
    startOfYear = JS("new Date(@{{tm_year}},0,1)")
    firstMonday = 1 - ((startOfYear.getDay() + 6) % 7) + 7
    firstWeek = JS("new Date(@{{tm_year}},0,@{{firstMonday}})")
    weekNo = date.getTime() - firstWeek.getTime()
    if weekNo < 0:
        weekNo = 0
    else:
        weekNo = 1 + int(weekNo/604800000)

    def format(c):
        if c == '%':
            return '%'
        elif c == 'a':
            raise NotImplementedError("strftime format character '%s'" % c)
        elif c == 'A':
            raise NotImplementedError("strftime format character '%s'" % c)
        elif c == 'b':
            raise NotImplementedError("strftime format character '%s'" % c)
        elif c == 'B':
            raise NotImplementedError("strftime format character '%s'" % c)
        elif c == 'c':
            return date.toLocaleString()
        elif c == 'd':
            return "%02d" % tm_mday
        elif c == 'H':
            return "%02d" % tm_hour
        elif c == 'I':
            return "%02d" % (tm_hour % 12)
        elif c == 'j':
            return "%03d" % tm_yday
        elif c == 'm':
            return "%02d" % tm_mon
        elif c == 'M':
            return "%02d" % tm_min
        elif c == 'p': # FIXME: should be locale dependent
            if tm_hour < 12:
                return "AM"
            return "PM"
        elif c == 'S':
            return "%02d" % tm_sec
        elif c == 'U':
            raise NotImplementedError("strftime format character '%s'" % c)
        elif c == 'w':
            return "%d" % ((tm_wday+1) % 7)
        elif c == 'W':
            return "%d" % weekNo
        elif c == 'x':
            return "%s" % date.toLocaleDateString()
        elif c == 'X':
            return "%s" % date.toLocaleTimeString()
        elif c == 'y':
            return "%02d" % (tm_year % 100)
        elif c == 'Y':
            return "%04d" % tm_year
        elif c == 'Z':
            raise NotImplementedError("strftime format character '%s'" % c)
        return "%" + c
    result = ''
    remainder = fmt
    re_pct = JS("/([^%]*)%(.)(.*)/")
    JS("var a, fmtChar;")
    while remainder:
        JS("""
        @{{a}} = @{{re_pct}}.exec(@{{remainder}});
        if (!@{{a}}) {
            @{{result}} += @{{remainder}};
            @{{remainder}} = null;
        } else {
            @{{result}} += @{{a}}[1];
            @{{fmtChar}} = @{{a}}[2];
            @{{remainder}} = @{{a}}[3];
            if (typeof @{{fmtChar}} != 'undefined') {
                @{{result}} += @{{format}}(@{{fmtChar}});
            }
        }
        """)
    return result

def asctime(t = None):
    if t == None:
        t = localtime()
    return "%s %s %02d %02d:%02d:%02d %04d" % (__c__days[(t[6]+1)%7][:3], __c__months[t[1]-1], t[2], t[3], t[4], t[5], t[0])

def ctime(t = None):
    t = localtime()
    return asctime(t)
