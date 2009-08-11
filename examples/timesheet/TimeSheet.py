try:
    import puremvc.patterns.facade
except:
    from pyjamas.Window import alert
    alert("""\
This application depends on puremvc for python,\n\
which doesn't seem to be available.\n\
See README.
""")

from ApplicationConstants import Notification
from controller.StartupCommand import StartupCommand
from components.AppFrame import AppFrame

class AppFacade(puremvc.patterns.facade.Facade):

    def __init__(self):
        self.initializeFacade()

    @staticmethod
    def getInstance():
        return AppFacade()

    def initializeFacade(self):
        super(AppFacade, self).initializeFacade()
        self.initializeController()

    def initializeController(self):
        super(AppFacade, self).initializeController()
        super(AppFacade, self).registerCommand(Notification.STARTUP, StartupCommand)

def main():
    app = AppFacade.getInstance()
    appFrame = AppFrame()
    app.sendNotification(Notification.STARTUP, appFrame)

if __name__ == '__main__':
    main()

