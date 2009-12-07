
# vim: set ts=4 sw=4 expandtab:

from ApplicationConstants import Notification

from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.FlexTable import FlexTable
from pyjamas.ui.Label import Label

from Grid import Grid

import time

class Summary(FlexTable):

    columns = [("Time", 5, 5), 
               ("Description", None, 60),
              ]
    rows = 0
    cols = 0
    date = None

    def __init__(self):
        try:
            FlexTable.__init__(self)
            self.cols = len(self.columns)
            self.setVisible(False)
        except:
            raise

    def setEntries(self, entries):
      try:
        #tt = time.localtime(time.time())
        tt = [0] * 9
        if self.date:
            tt[0] = int(self.date[:4])
            tt[1] = int(self.date[4:6])
            tt[2] = int(self.date[6:8])
        tt[3] = 0
        tt[4] = 0
        tt[5] = 0
        tt[6] = -1
        tt[7] = -1
        tt[8] = -1
        timelines = {}
        for timeVO in entries:
            t1 = tt[0:]
            t2 = tt[0:]
            if not timeVO.start or not timeVO.end:
                continue
            t1[3] = int(timeVO.start[:2])
            t1[4] = int(timeVO.start[3:])
            t2[3] = int(timeVO.end[:2])
            t2[4] = int(timeVO.end[3:])
            t1 = time.mktime(t1)
            t2 = time.mktime(t2)
            dt = t2 - t1
            project = timelines.get(timeVO.project.lower(), [0, timeVO.project, {}])
            project[0] = project[0] + dt
            descr = project[2].get(timeVO.description.lower(), [0, timeVO.description])
            descr[0] = descr[0] + dt
            project[2][timeVO.description.lower()] = descr
            timelines[timeVO.project.lower()] = project
        for row in range(self.getRowCount()):
            self.removeRow(0)
        self.rows = 0
        self.addHeader()
        projects = timelines.keys()
        projects.sort()
        for project in projects:
            self.addRow([self.HHMM(timelines[project][0]), timelines[project][1]])
            descriptions = timelines[project][2]
            descriptions = descriptions.keys()
            descriptions.sort()
            for desc in descriptions:
                if timelines[project][2][desc][1]:
                    self.addRow(['', self.HHMM(timelines[project][2][desc][0]) + " " + timelines[project][2][desc][1]])
      except:
        raise

    def HHMM(self, t):
        t = t / 60  # From seconds to minutes
        hh = t / 60
        mm = t % 60
        return "%02d:%02d" % (hh, mm)

    def addHeader(self):
        # HH:MM|Description
        col = 0
        for label, maxLength, visibleLength in self.columns:
            self.setWidget(0, col, Label(label, wordWrap=False))
            col += 1

    def addRow(self, values):
        self.rows += 1
        col = -1
        for name, maxLength, visibleLength in self.columns:
            col += 1
            label = Label()
            label.setText(values[col])
            self.setWidget(self.rows, col, label)



