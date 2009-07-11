"""
PureMVC Python Demo - wxPython Employee Admin 
By Toby de Havilland <toby.de.havilland@puremvc.org>
Copyright(c) 2007-08 Toby de Havilland, Some rights reserved.
Addapted for pyjamas: Kees Bos
"""

import puremvc.patterns.command
import puremvc.interfaces
import model, view, EmployeeAdmin


class StartupCommand(puremvc.patterns.command.SimpleCommand, puremvc.interfaces.ICommand):
    def execute(self,note):
        self.facade.registerProxy(model.UserProxy())
        self.facade.registerProxy(model.RoleProxy())
    
        mainPanel = note.getBody()
        self.facade.registerMediator(view.DialogMediator(mainPanel))
        self.facade.registerMediator(view.UserFormMediator(mainPanel.userForm))
        self.facade.registerMediator(view.UserListMediator(mainPanel.userList))
        self.facade.registerMediator(view.RolePanelMediator(mainPanel.rolePanel))

class AddRoleResultCommand(puremvc.patterns.command.SimpleCommand, puremvc.interfaces.ICommand):
    def execute(self,note):
        result = note.getBody()
        if not result:
            self.facade.sendNotification(EmployeeAdmin.AppFacade.SHOW_DIALOG, "Role already exists for this user.")

class DeleteUserCommand(puremvc.patterns.command.SimpleCommand, puremvc.interfaces.ICommand):
    def execute(self,note):
           user = note.getBody()
           userProxy = self.facade.retrieveProxy(model.UserProxy.NAME)
           roleProxy = self.facade.retrieveProxy(model.RoleProxy.NAME)
           userProxy.deleteItem(user)       
           roleProxy.deleteItem(user)
           self.facade.sendNotification(EmployeeAdmin.AppFacade.USER_DELETED)
