
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

            prevDayBtn = Button(" < ", self.onPrevDay)
            nextDayBtn = Button(" > ", self.onNextDay)
            prevWeekBtn = Button(" << ", self.onPrevWeek)
            nextWeekBtn = Button(" >> ", self.onNextWeek)
            self.dateBox = TextBox()
            self.dateBox.setMaxLength(10)
            self.dateBox.setVisibleLength(10)

            self.add(prevWeekBtn)
            self.add(prevDayBtn)
            self.add(self.dateBox)
            self.add(nextDayBtn)
            self.add(nextWeekBtn)
        except:
            raise

    def onPrevDay(self, sender):
        self.mediator.sendNotification(Notification.PREV_DAY)

    def onNextDay(self, sender):
        self.mediator.sendNotification(Notification.NEXT_DAY)

    def onPrevWeek(self, sender):
        self.mediator.sendNotification(Notification.PREV_WEEK)

    def onNextWeek(self, sender):
        self.mediator.sendNotification(Notification.NEXT_WEEK)

    def displayDay(self):
        self.dateBox.setText(time.strftime("%d/%m/%Y", time.localtime(self.time)))
        date = time.strftime("%Y%m%d", time.localtime(self.time))
        self.mediator.sendNotification(Notification.DATE_SELECTED, date)

    def prevDay(self):
        self.time -= 86400
        self.displayDay()

    def nextDay(self):
        self.time += 86400
        self.displayDay()

    def prevWeek(self):
        self.time -= 7*86400
        self.displayDay()

    def nextWeek(self):
        self.time += 7*86400
        self.displayDay()

