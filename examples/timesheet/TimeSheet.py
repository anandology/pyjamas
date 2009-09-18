import pyjd

try:
    import puremvc.patterns.facade
except:
    from pyjamas.Window import alert
    alert("""\
This application depends on puremvc for python,\n\
which doesn't seem to be available.\n\
See README.
""")

from pyjamas.Timer import Timer

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

# workaround for pyjd xulrunner issue: timesheet uses XMLHttpRequest.
class TimerCls:
    def __init__(self):
        self.app = AppFacade.getInstance()
        Timer(1, self)
    def onTimer(self, tid):
        appFrame = AppFrame()
        self.app.sendNotification(Notification.STARTUP, appFrame)

if __name__ == '__main__':
    pyjd.setup("http://127.0.0.1/examples/timesheet/public/TimeSheet.html")
    t = TimerCls()
    pyjd.run()

