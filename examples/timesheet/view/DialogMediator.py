import puremvc.interfaces
import puremvc.patterns.mediator

from ApplicationConstants import Notification

from pyjamas.Window import alert

class DialogMediator(puremvc.patterns.mediator.Mediator, puremvc.interfaces.IMediator):

    NAME = 'DialogMediator'

    def __init__(self, viewComponent):
        super(DialogMediator, self).__init__(DialogMediator.NAME, viewComponent)
        self.viewComponent.mediator = self

    def listNotificationInterests(self):
        return [
        Notification.SHOW_DIALOG,
        Notification.HELLO,
        ]

    def handleNotification(self, note):
        try:
            noteName = note.getName()
            if noteName == Notification.SHOW_DIALOG:
                alert(note.getBody())
            elif noteName == Notification.HELLO:
                alert("Hello there")
        except:
            raise

