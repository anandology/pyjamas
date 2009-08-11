
# vim: set ts=4 sw=4 expandtab:

import puremvc.interfaces
import puremvc.patterns.mediator

from ApplicationConstants import Notification

from pyjamas.Window import alert

class DatePickerMediator(puremvc.patterns.mediator.Mediator, puremvc.interfaces.IMediator):

    NAME = 'DatePickerMediator'

    def __init__(self, viewComponent):
        super(DatePickerMediator, self).__init__(DatePickerMediator.NAME, viewComponent)
        self.viewComponent.mediator = self
        self.viewComponent.displayDay()

    def listNotificationInterests(self):
        return [
            Notification.PREV_DAY,
            Notification.NEXT_DAY,
            Notification.PREV_WEEK,
            Notification.NEXT_WEEK,
            Notification.DISPLAY_DAY,
        ]

    def handleNotification(self, note):
        try:
            noteName = note.getName()
            if noteName == Notification.PREV_DAY:
                self.viewComponent.prevDay()
            elif noteName == Notification.NEXT_DAY:
                self.viewComponent.nextDay()
            elif noteName == Notification.PREV_WEEK:
                self.viewComponent.prevWeek()
            elif noteName == Notification.NEXT_WEEK:
                self.viewComponent.nextWeek()
            elif noteName == Notification.DISPLAY_DAY:
                self.viewComponent.displayDay()
        except:
            raise

