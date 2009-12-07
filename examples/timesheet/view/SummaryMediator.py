
# vim: set ts=4 sw=4 expandtab:

from puremvc.patterns.mediator import Mediator

from ApplicationConstants import Notification

import model
from model.TimeProxy import TimeProxy

from pyjamas.Window import alert

class SummaryMediator(Mediator):

    NAME = 'SummaryMediator'

    def __init__(self, viewComponent):
        super(SummaryMediator, self).__init__(SummaryMediator.NAME, viewComponent)
        self.viewComponent.mediator = self
        self.timeProxy = self.facade.retrieveProxy(TimeProxy.NAME)

    def listNotificationInterests(self):
        return [
            Notification.DATE_SELECTED,
            Notification.EDIT_SELECTED,
            Notification.SUM_SELECTED,
        ]

    def handleNotification(self, note):
        try:
            noteName = note.getName()
            nodeBody = note.getBody()
            if noteName == Notification.DATE_SELECTED:
                self.onDateSelected(nodeBody)
            elif noteName == Notification.EDIT_SELECTED:
                self.onEditSelected()
            elif noteName == Notification.SUM_SELECTED:
                self.onSumSelected()
        except:
            raise

    def onDateSelected(self, date):
        self.viewComponent.date = date
        self.viewComponent.setEntries(self.timeProxy.getDateEntries(self.viewComponent.date))

    def onEditSelected(self):
        self.viewComponent.setVisible(False)

    def onSumSelected(self):
        self.viewComponent.setVisible(True)
