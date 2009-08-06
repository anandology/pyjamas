"""
PureMVC Python Demo - wxPython Employee Admin
By Toby de Havilland <toby.de.havilland@puremvc.org>
Copyright(c) 2007-08 Toby de Havilland, Some rights reserved.
Addapted for pyjamas: Kees Bos
"""

from pyjamas.ui.DockPanel import DockPanel
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.AbsolutePanel import AbsolutePanel
from pyjamas.ui.FlexTable import FlexTable
from pyjamas.ui.Button import Button
from pyjamas.ui.Label import Label
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.TextBox import TextBox
from pyjamas.ui.PasswordTextBox import PasswordTextBox
from pyjamas.ui.ListBox import ListBox

from Grid import Grid

import EmployeeAdmin

class PyJsApp(object):
    
    appFrame = None
    
    def __init__(self):
        self.appFrame = AppFrame()

class AppFrame(object):
    
    userForm = None
    userList = None
    rolePanel = None
    
    def __init__(self):
        self.panel = DockPanel()
        self.userList = UserList(self)
        self.userForm = UserForm(self)
        self.rolePanel = RolePanel(self)
        self.panel.add(self.userList, DockPanel.NORTH)
        self.panel.add(self.userForm, DockPanel.WEST)
        self.panel.add(self.rolePanel, DockPanel.EAST)
        RootPanel().add(self.panel)
        self.Show()

    def Show(self):
        pass

class RolePanel(AbsolutePanel):
    
    user = None
    selectedRole = None
    
    roleList = None
    roleCombo = None
    addBtn = None
    removeBtn = None
    
    def __init__(self,parent):
        AbsolutePanel.__init__(self)

        self.roleList = ListBox()
        self.roleList.setWidth('300px')
        self.roleList.setVisibleItemCount(6)
        self.roleList.addClickListener(self.onListClick)
        self.roleList.addKeyboardListener(self)
        self.roleCombo = ListBox()
        self.roleCombo.addClickListener(self.onComboClick)
        self.roleCombo.addKeyboardListener(self)
        self.addBtn = Button("Add", self)
        self.addBtn.addClickListener(self.onAdd)
        self.addBtn.setEnabled(False)
        self.removeBtn = Button("Remove", self)
        self.removeBtn.addClickListener(self.onRemove)
        self.removeBtn.setEnabled(False)

        vpanel = VerticalPanel()
        vpanel.add(self.roleList)
        hpanel = HorizontalPanel()
        hpanel.add(self.roleCombo)
        hpanel.add(self.addBtn)
        hpanel.add(self.removeBtn)
        vpanel.add(hpanel)

        self.add(vpanel)

        return
    
    def updateRoleList(self,items):
        self.roleList.clear()
        for item in items:
            self.roleList.addItem(item)
        #self.roleList.addItem('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;')
        #self.roleList.addItem('- - - - - - - -')
    
    def updateRoleCombo(self,choices, default_):
        self.roleCombo.clear()
        for choice in choices:
            self.roleCombo.addItem(choice)
        self.roleCombo.selectValue(default_)
    
    def onComboClick(self, sender, keyCode=None, modifiers=None):
        selected = self.roleCombo.getSelectedItemText()
        if not selected or not self.user:
            self.addBtn.setEnabled(False)
            self.selectedRole=None
        else:
            self.addBtn.setEnabled(True)
            self.selectedRole=selected[0]
        self.removeBtn.setEnabled(False)
        self.roleList.setItemTextSelection(None)
    
    def onListClick(self, sender):
        selected = self.roleList.getSelectedItemText()
        if selected:
            self.removeBtn.setEnabled(True)
            self.selectedRole=selected[0]
        else:
            self.removeBtn.setEnabled(False)
            self.selectedRole=None
        self.addBtn.setEnabled(False)
        self.roleCombo.setItemTextSelection(None)
    
    def onAdd(self, evt):
        self.mediator.sendNotification(EmployeeAdmin.AppFacade.ADD_ROLE,self.selectedRole)
    
    def onRemove(self,evt):
        self.mediator.sendNotification(EmployeeAdmin.AppFacade.REMOVE_ROLE,self.selectedRole)

    def onClick(self, sender):
        pass

    def onKeyUp(self, sender, keyCode, modifiers):
        if sender == self.roleCombo:
            self.onComboClick(sender)
        elif sender == self.roleList:
            self.onListClick(sender)

    def onKeyDown(self, sender, keyCode, modifiers):
        pass

    def onKeyPress(self, sender, keyCode, modifiers):
        pass

class UserList(AbsolutePanel):
    
    userGrid = None
    newBtn = None
    deleteBtn = None
    
    users = None
    selectedUser = None
    
    def __init__(self,parent):
        AbsolutePanel.__init__(self)
        self.userGrid = Grid()
        self.userGrid.createGrid(6, 6)
        self.userGrid.addTableListener(self)

        self.userGrid.setBorderWidth(2)
        self.userGrid.setCellPadding(4)
        self.userGrid.setCellSpacing(1)
        self.userGrid.setColLabelValue(0,"Username")
        self.userGrid.setColLabelValue(1,"First Name")
        self.userGrid.setColLabelValue(2,"Last Name")
        self.userGrid.setColLabelValue(3,"Email")
        self.userGrid.setColLabelValue(4,"Department")
        self.userGrid.setColLabelValue(5,"Password")

        self.newBtn = Button("New", self.onNew)
        self.deleteBtn = Button("Delete", self.onDelete)
        self.deleteBtn.setEnabled(False)

        self.add(self.userGrid)
        self.add(self.newBtn)
        self.add(self.deleteBtn)
        
        return
    
    def updateUserGrid(self, users):
        self.userGrid.clearGrid()
        self.users = users
        for i in range(len(users)):
            self.userGrid.setCellValue(i, 0, users[i].username)
            self.userGrid.setCellValue(i, 1, users[i].fname)
            self.userGrid.setCellValue(i, 2, users[i].lname)
            self.userGrid.setCellValue(i, 3, users[i].email)
            self.userGrid.setCellValue(i, 4, users[i].department)
            self.userGrid.setCellValue(i, 5, users[i].password)
    
    def onCellClicked(self, sender, row, col):
        try:
            if row > 0 and row <= len(self.users):
                self.selectedUser = self.users[row-1]
                self.userGrid.selectRow(row)
                self.deleteBtn.setEnabled(True)
            else:
                self.userGrid.selectRow(-1)
                self.selectedUser = None
                self.deleteBtn.setEnabled(False)
            self.mediator.sendNotification(EmployeeAdmin.AppFacade.USER_SELECTED,self.selectedUser)
        except IndexError:
            pass
    
    def deSelect(self):
        self.userGrid.selectRow(-1)
    
    def onNew(self, sender):
        self.mediator.sendNotification(EmployeeAdmin.AppFacade.NEW_USER)
        self.deSelect()

    def onDelete(self, sender):
        if self.selectedUser:
            self.mediator.sendNotification(EmployeeAdmin.AppFacade.DELETE_USER, self.selectedUser)
            self.deSelect()

class UserForm(AbsolutePanel):
    
    MODE_ADD    = "modeAdd";
    MODE_EDIT   = "modeEdit";
    
    user = None
    mode = None
    
    usernameInput = None
    firstInput = None
    lastInput = None
    emailInput = None
    passwordInput = None
    confirmInput = None
    departmentCombo = None
    addBtn = None
    cancelBtn = None
    
    def __init__(self,parent):
        AbsolutePanel.__init__(self)
        ftable = FlexTable()

        ftable.setWidget(0, 0, Label("First Name", wordWrap=False))
        ftableFormatter = ftable.getFlexCellFormatter()
        self.firstInput = TextBox()
        self.firstInput.addChangeListener(self.checkValid)
        self.firstInput.addKeyboardListener(self)
        ftable.setWidget(0, 1, self.firstInput)

        ftable.setWidget(1, 0, Label("Last Name", wordWrap=False))
        self.lastInput = TextBox()
        self.lastInput.addChangeListener(self.checkValid)
        self.lastInput.addKeyboardListener(self)
        ftable.setWidget(1, 1, self.lastInput)

        ftable.setWidget(2, 0, Label("Email", wordWrap=False))
        self.emailInput = TextBox()
        self.emailInput.addChangeListener(self.checkValid)
        self.emailInput.addKeyboardListener(self)
        ftable.setWidget(2, 1, self.emailInput)

        ftable.setWidget(3, 0, Label("Username", wordWrap=False))
        self.usernameInput = TextBox()
        self.usernameInput.addChangeListener(self.checkValid)
        self.usernameInput.addKeyboardListener(self)
        ftable.setWidget(3, 1, self.usernameInput)

        ftable.setWidget(4, 0, Label("Password", wordWrap=False))
        self.passwordInput = PasswordTextBox()
        self.passwordInput.addChangeListener(self.checkValid)
        self.passwordInput.addKeyboardListener(self)
        ftable.setWidget(4, 1, self.passwordInput)

        ftable.setWidget(5, 0, Label("Confirm", wordWrap=False))
        self.confirmInput = PasswordTextBox()
        self.confirmInput.addChangeListener(self.checkValid)
        self.confirmInput.addKeyboardListener(self)
        ftable.setWidget(5, 1, self.confirmInput)

        ftable.setWidget(6, 0, Label("Department", wordWrap=False))
        self.departmentCombo = ListBox()
        self.departmentCombo.addChangeListener(self.checkValid)
        self.departmentCombo.addKeyboardListener(self)
        ftable.setWidget(6, 1, self.departmentCombo)

        hpanel = HorizontalPanel()
        self.addBtn = Button("Add User", self.onAdd)
        self.addBtn.setEnabled(False)
        hpanel.add(self.addBtn)
        self.cancelBtn = Button("Cancel", self.onCancel)
        hpanel.add(self.cancelBtn)
        ftable.setWidget(7, 0, hpanel)
        ftableFormatter.setColSpan(7, 0, 2)

        self.add(ftable)
        return

    def updateUser(self, user):
        self.user = user
        self.usernameInput.setText(self.user.username)
        self.firstInput.setText(self.user.fname)
        self.lastInput.setText(self.user.lname)
        self.emailInput.setText(self.user.email)
        self.passwordInput.setText(self.user.password)
        self.confirmInput.setText(self.user.password)
        self.departmentCombo.setItemTextSelection([self.user.department])
        self.checkValid()

    def updateDepartmentCombo(self,choices, default_):
        self.departmentCombo.clear()
        for choice in choices:
            self.departmentCombo.addItem(choice)
        self.departmentCombo.selectValue(default_)
    
    def updateMode(self, mode):
        self.mode = mode
        if self.mode == self.MODE_ADD:
            self.addBtn.setText("Add User")
        else:
            self.addBtn.setText("Update User")
        
    def onAdd(self, evt):       
        if self.mode == self.MODE_ADD:
            self.mediator.sendNotification(EmployeeAdmin.AppFacade.ADD_USER)
        else:
            self.mediator.sendNotification(EmployeeAdmin.AppFacade.UPDATE_USER)
        self.checkValid()

    def onCancel(self, evt):
        self.mediator.sendNotification(EmployeeAdmin.AppFacade.CANCEL_USER)

    def checkValid(self, evt=None):
        if self.enableSubmit(self.usernameInput.getText(),self.passwordInput.getText(),self.confirmInput.getText(), self.departmentCombo.getSelectedItemText(True)):
            self.addBtn.setEnabled(True)
        else:
            self.addBtn.setEnabled(False)
    
    def enableSubmit(self, u, p, c, d):
        return (len(u) > 0 and len(p) >0 and p == c and len(d) > 0)

    def onClick(self, sender):
        pass

    def onKeyUp(self, sender, keyCode, modifiers):
        self.checkValid()

    def onKeyDown(self, sender, keyCode, modifiers):
        pass

    def onKeyPress(self, sender, keyCode, modifiers):
        pass


