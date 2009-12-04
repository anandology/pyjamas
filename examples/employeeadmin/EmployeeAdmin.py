"""
PureMVC Python Demo - wxPython Employee Admin
By Toby de Havilland <toby.de.havilland@puremvc.org>
Copyright(c) 2007-08 Toby de Havilland, Some rights reserved.
Addapted for pyjamas: Kees Bos
Suggestions and code enhancements: Jim Washington
"""

import pyjd # dummy

try:
    import puremvc.patterns.facade
except:
    from pyjamas.Window import alert
    alert("""\
This application depends on puremvc for python,\n\
which doesn't seem to be available.\n\
See README.
""")

from puremvc.patterns.facade import Facade
from ApplicationConstants import Command
import controller, components

class AppFacade(Facade):
    
    def __init__(self):
        self.initializeFacade()
        self.initializeController()
        self.registerCommand(Command.STARTUP, controller.StartupCommand)
        self.registerCommand(Command.DELETE_USER, controller.DeleteUserCommand)
        self.registerCommand(Command.ADD_ROLE_RESULT, controller.AddRoleResultCommand)
        
    @staticmethod
    def getInstance():
        return AppFacade()


if __name__ == '__main__':
    
    pyjd.setup("./public/EmployeeAdmin.html")
    app = AppFacade.getInstance()
    pyjsApp = components.PyJsApp()
    app.sendNotification(Command.STARTUP, pyjsApp.appFrame)
    pyjd.run()
