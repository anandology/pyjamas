
# vim: set ts=4 sw=4 expandtab:

from puremvc.patterns.mediator import Mediator

from ApplicationConstants import Notification

from pyjamas.Window import alert

class DatePickerMediator(Mediator):

    NAME = 'DatePickerMediator'

    def __init__(self, viewComponent):
        Mediator.__init__(self, DatePickerMediator.NAME, viewComponent)
        viewComponent.prevDayBtn.addClickListener(self.displayDay)
        viewComponent.nextDayBtn.addClickListener(self.displayDay)
        viewComponent.prevWeekBtn.addClickListener(self.displayDay)
        viewComponent.nextWeekBtn.addClickListener(self.displayDay)
        self.displayDay()

    def listNotificationInterests(self):
        return []

    def handleNotification(self, note):
        pass

    def displayDay(self, sender=None):
        self.viewComponent.displayDay()
        self.sendNotification(Notification.DATE_SELECTED, 
                              self.viewComponent.date)
