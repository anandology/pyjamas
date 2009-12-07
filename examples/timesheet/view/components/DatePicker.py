
# vim: set ts=4 sw=4 expandtab:

from ApplicationConstants import Notification

from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.Button import Button
from pyjamas.ui.TextBox import TextBox

import time

class DatePicker(HorizontalPanel):

    time = None
    dateBox = None

    def __init__(self):
        try:
            HorizontalPanel.__init__(self)
            self.time = time.time()
            self.date = None

            self.prevDayBtn = Button(" < ", self.onPrevDay)
            self.nextDayBtn = Button(" > ", self.onNextDay)
            self.prevWeekBtn = Button(" << ", self.onPrevWeek)
            self.nextWeekBtn = Button(" >> ", self.onNextWeek)
            self.dateBox = TextBox()
            self.dateBox.setMaxLength(10)
            self.dateBox.setVisibleLength(10)

            self.add(self.prevWeekBtn)
            self.add(self.prevDayBtn)
            self.add(self.dateBox)
            self.add(self.nextDayBtn)
            self.add(self.nextWeekBtn)
        except:
            raise

    def onPrevDay(self, sender):
        self.time -= 86400

    def onNextDay(self, sender):
        self.time += 86400

    def onPrevWeek(self, sender):
        self.time -= 7*86400

    def onNextWeek(self, sender):
        self.time += 7*86400

    def displayDay(self):
        self.dateBox.setText(time.strftime("%d/%m/%Y", time.localtime(self.time)))
        self.date = time.strftime("%Y%m%d", time.localtime(self.time))
