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
from pyjamas.ui.Tooltip import TooltipListener

from Grid import Grid
import ApplicationConstants

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
        self.roleList.addChangeListener(self.onListChange)
        #self.roleList.addKeyboardListener(self)
        self.roleCombo = ListBox()
        self.roleCombo.addKeyboardListener(self)
        self.roleCombo.addChangeListener(self.onComboChange)
        self.addBtn = Button("Add")
        self.addBtn.setEnabled(False)
        self.removeBtn = Button("Remove")
        self.removeBtn.setEnabled(False)

        vpanel = VerticalPanel()
        vpanel.add(self.roleList)
        hpanel = HorizontalPanel()
        hpanel.add(self.roleCombo)
        hpanel.add(self.addBtn)
        hpanel.add(self.removeBtn)
        vpanel.add(hpanel)

        self.add(vpanel)
        self.clearForm()
        return

    def clearForm(self):
        self.user = None
        self.updateRoleList([])
        self.roleCombo.setItemTextSelection(None)

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
    
    def onComboChange(self, sender, keyCode=None, modifiers=None):
        selected = self.roleCombo.getSelectedItemText()
        if  not selected \
            or selected[0] == ApplicationConstants.ROLE_NONE_SELECTED \
            or not self.user:
            self.addBtn.setEnabled(False)
            self.selectedRole=None
        else:
            self.addBtn.setEnabled(True)
            self.selectedRole=selected[0]
        self.removeBtn.setEnabled(False)
        self.roleList.setItemTextSelection(None)
    
    def onListChange(self, sender):
        selected = self.roleList.getSelectedItemText()
        if selected:
            self.removeBtn.setEnabled(True)
            self.selectedRole=selected[0]
        else:
            self.removeBtn.setEnabled(False)
            self.selectedRole=None
        self.addBtn.setEnabled(False)
        self.roleCombo.setItemTextSelection(None)
    
    def onClick(self, sender):
        pass

    def onKeyUp(self, sender, keyCode, modifiers):
        if sender == self.roleCombo:
            self.onComboChange(sender)
        elif sender == self.roleList:
            self.onListChange(sender)

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

        self.newBtn = Button("New")
        self.deleteBtn = Button("Delete")
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
        except IndexError:
            pass
    
    def deSelect(self):
        self.userGrid.selectRow(-1)
    

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

        w = Label("* Username", wordWrap=False)
        w.addMouseListener(TooltipListener("Required, not changable"))
        ftable.setWidget(3, 0, w)
        self.usernameInput = TextBox()
        self.usernameInput.addChangeListener(self.checkValid)
        self.usernameInput.addKeyboardListener(self)
        ftable.setWidget(3, 1, self.usernameInput)

        w = Label("* Password", wordWrap=False)
        w.addMouseListener(TooltipListener("Required"))
        ftable.setWidget(4, 0, w)
        self.passwordInput = PasswordTextBox()
        self.passwordInput.addChangeListener(self.checkValid)
        self.passwordInput.addKeyboardListener(self)
        ftable.setWidget(4, 1, self.passwordInput)

        w = Label("* Confirm", wordWrap=False)
        w.addMouseListener(TooltipListener("Required"))
        ftable.setWidget(5, 0, w)
        self.confirmInput = PasswordTextBox()
        self.confirmInput.addChangeListener(self.checkValid)
        self.confirmInput.addKeyboardListener(self)
        ftable.setWidget(5, 1, self.confirmInput)

        w = Label("* Department", wordWrap=False)
        w.addMouseListener(TooltipListener("Required"))
        ftable.setWidget(6, 0, w)
        self.departmentCombo = ListBox()
        self.departmentCombo.addChangeListener(self.checkValid)
        self.departmentCombo.addKeyboardListener(self)
        ftable.setWidget(6, 1, self.departmentCombo)

        hpanel = HorizontalPanel()
        self.addBtn = Button("Add User")
        self.addBtn.setEnabled(False)
        hpanel.add(self.addBtn)
        self.cancelBtn = Button("Cancel")
        hpanel.add(self.cancelBtn)
        ftable.setWidget(7, 0, hpanel)
        ftableFormatter.setColSpan(7, 0, 2)

        self.add(ftable)
        self.clearForm()
        return

    def clearForm(self):
        self.user = None
        self.usernameInput.setText('')
        self.firstInput.setText('')
        self.lastInput.setText('')
        self.emailInput.setText('')
        self.passwordInput.setText('')
        self.confirmInput.setText('')
        self.departmentCombo.setItemTextSelection(None)
        self.updateMode(self.MODE_ADD)
        self.checkValid()

    def updateUser(self, user):
        def setText(elem, value):
            if value:
                elem.setText(value)
            else:
                elem.setText("")
        self.user = user
        setText(self.usernameInput, self.user.username)
        setText(self.firstInput, self.user.fname)
        setText(self.lastInput, self.user.lname)
        setText(self.emailInput, self.user.email)
        setText(self.passwordInput, self.user.password)
        setText(self.confirmInput, self.user.password)
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


