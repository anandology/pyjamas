"""
PureMVC Python Demo - wxPython Employee Admin 
By Toby de Havilland <toby.de.havilland@puremvc.org>
Copyright(c) 2007-08 Toby de Havilland, Some rights reserved.
Addapted for pyjamas: Kees Bos
"""

from puremvc.patterns.command import SimpleCommand
import model, view
from ApplicationConstants import Command, Notification

class StartupCommand(SimpleCommand):
    def execute(self,note):
        facade = self.facade
        facade.registerProxy(model.UserProxy())
        facade.registerProxy(model.RoleProxy())
    
        mainPanel = note.getBody()
        facade.registerMediator(view.DialogMediator(mainPanel))
        facade.registerMediator(view.UserFormMediator(mainPanel.userForm))
        facade.registerMediator(view.UserListMediator(mainPanel.userList))
        facade.registerMediator(view.RolePanelMediator(mainPanel.rolePanel))

class AddRoleResultCommand(SimpleCommand):
    def execute(self,note):
        result = note.getBody()
        if not result:
            self.facade.sendNotification(Notification.SHOW_DIALOG, "Role already exists for this user.")

class DeleteUserCommand(SimpleCommand):
    def execute(self,note):
           user = note.getBody()
           facade = self.facade
           userProxy = facade.retrieveProxy(model.UserProxy.NAME)
           roleProxy = facade.retrieveProxy(model.RoleProxy.NAME)
           userProxy.deleteItem(user)       
           roleProxy.deleteItem(user)
           facade.sendNotification(Notification.USER_DELETED)
