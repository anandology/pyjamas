
# vim: set ts=4 sw=4 expandtab:

from puremvc.patterns.mediator import Mediator

from ApplicationConstants import Notification

import model
from model.TimeProxy import TimeProxy
from model.vo.TimeVO import TimeVO

from pyjamas.Cookies import setCookie
from pyjamas.Window import alert

class TimeGridMediator(Mediator):

    NAME = 'TimeGridMediator'

    def __init__(self, viewComponent):
        super(TimeGridMediator, self).__init__(TimeGridMediator.NAME, viewComponent)
        self.viewComponent.mediator = self
        self.timeProxy = self.facade.retrieveProxy(TimeProxy.NAME)

    def listNotificationInterests(self):
        return [
            Notification.CELL_SELECTED,
            Notification.CELL_UPDATED,
            Notification.DATE_SELECTED,
            Notification.EDIT_SELECTED,
            Notification.SUM_SELECTED,
            Notification.FILE_LOADED,
        ]

    def handleNotification(self, note):
        try:
            noteName = note.getName()
            nodeBody = note.getBody()
            if noteName == Notification.CELL_SELECTED:
                alert("Select cell is not implemented yet")
            elif noteName == Notification.CELL_UPDATED:
                alert("Cell changed is not implemented yet")
            elif noteName == Notification.DATE_SELECTED:
                self.onDateSelected(nodeBody)
            elif noteName == Notification.EDIT_SELECTED:
                self.onEditSelected()
            elif noteName == Notification.SUM_SELECTED:
                self.onSumSelected()
            elif noteName == Notification.FILE_LOADED:
                self.onFileLoaded(*nodeBody)
        except:
            raise

    def onDateSelected(self, date):
        if not self.viewComponent.date is None and self.viewComponent.dirty:
            self.timeProxy.setDateEntries(self.viewComponent.date, 
                                          self.viewComponent.getEntries())
        self.viewComponent.date = date
        self.viewComponent.setEntries(self.timeProxy.getDateEntries(self.viewComponent.date))

    def onEditSelected(self):
        self.viewComponent.setVisible(True)

    def onSumSelected(self):
        self.viewComponent.setVisible(False)
        self.onDateSelected(self.viewComponent.date)
        self.sendNotification(Notification.DATE_SELECTED, self.viewComponent.date)

    def onFileLoaded(self, filename, data):
        def invalid(lineno, line):
            alert("Invalid line at %s:\n%s" % (lineno, line))
            return False
        date = self.timeProxy.importData(data, invalid)
        if date:
            try:
                setCookie("fileLocation", filename, 1000000000)
            except:
                pass
            self.sendNotification(Notification.DATE_SELECTED, date)
