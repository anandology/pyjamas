
# vim: set ts=4 sw=4 expandtab:

import puremvc.patterns.proxy

from vo.TimeVO import TimeVO

import time

class TimeProxy(puremvc.patterns.proxy.Proxy):
    
    NAME = "TimeProxy"
    def __init__(self):
        super(TimeProxy, self).__init__(TimeProxy.NAME, [])
        self.clear()

    def clear(self):
        self.data = {}

    def getDateEntries(self, date):
        if self.data.has_key(date):
            return self.data[date]
        return []

    def setDateEntries(self, date, entries):
        self.data[date] = entries
   
    def addItem(self, date, item):
        if not self.data.has_key(date):
            self.data[date] = []
        self.data[date].append(item)

    def removeDate(self, date):
        if self.data.has_key(date):
            self.data[date] = []

    def exportData(self):
        lines = []
        dates = self.data.keys()
        dates.sort()
        for date in dates:
            for timeVO in self.data[date]:
                lines.append('''"%s","%s","%s","%s","%s"''' % (date, timeVO.start, timeVO.end, timeVO.project, timeVO.description))
        lines.sort()
        return "\n".join(lines)

    def importData(self, data, onError):
        today = time.strftime("%Y%m%d", time.localtime())
        dateEntries = {}
        lines = data.split("\n")
        if len(lines) == 1:
            lines = data.split("\r")
        lineno = 0
        for line in lines:
            lineno += 1
            line = line.strip()
            if line == "" or line[0] == '#':
                # Ignore empty lines, or lines starting with a #
                continue
            if len(line) < 3 or line[0] != '"' or line[-1] != '"':
                return onError(lineno, line)
            s = line[1:-1]
            cols = s.split('","')
            if len(cols) != 5:
                return onError(lineno, line)
            date = cols[0]
            if date == 'TODAY':
                date = today
            if not dateEntries.has_key(date):
                dateEntries[date] = []
            dateEntries[date].append(cols[1:])

        # We got this far, so we have no errors yet
        self.clear()
        dates = dateEntries.keys()
        dates.sort()
        for date in dates:
            thisDate = []
            for cols in dateEntries[date]:
                timeVO = TimeVO(*cols)
                thisDate.append(timeVO)
            self.setDateEntries(date, thisDate)
        return date
