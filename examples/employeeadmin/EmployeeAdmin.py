"""
PureMVC Python Demo - wxPython Employee Admin
By Toby de Havilland <toby.de.havilland@puremvc.org>
Copyright(c) 2007-08 Toby de Havilland, Some rights reserved.
Addapted for pyjamas: Kees Bos
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

import controller, components

class AppFacade(puremvc.patterns.facade.Facade):
    
    STARTUP           = "startup"
    NEW_USER          = "newUser"
    DELETE_USER       = "deleteUser"
    CANCEL_SELECTED   = "cancelSelected"

    USER_SELECTED     = "userSelected"
    USER_ADDED        = "userAdded"
    USER_UPDATED      = "userUpdated"
    USER_DELETED      = "userDeleted"

    ADD_ROLE_RESULT   = "addRoleResult"
    
    SHOW_DIALOG       = "showDialog"
    
    
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
        
        super(AppFacade, self).registerCommand(AppFacade.STARTUP, controller.StartupCommand)
        super(AppFacade, self).registerCommand(AppFacade.DELETE_USER, controller.DeleteUserCommand)
        super(AppFacade, self).registerCommand(AppFacade.ADD_ROLE_RESULT, controller.AddRoleResultCommand)


if __name__ == '__main__':
    
    pyjd.setup("./public/EmployeeAdmin.html")
    app = AppFacade.getInstance()
    pyjsApp = components.PyJsApp()
    app.sendNotification(AppFacade.STARTUP, pyjsApp.appFrame)
    pyjd.run()
