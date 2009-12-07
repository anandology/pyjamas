
# vim: set ts=4 sw=4 expandtab:

from ApplicationConstants import Notification

from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.Label import Label
from pyjamas.ui.Button import Button
from pyjamas.ui.DialogBox import DialogBox
from pyjamas.ui.FlexTable import FlexTable
from pyjamas.ui.HTML import HTML
from pyjamas.ui.TextBox import TextBox
from pyjamas.Cookies import setCookie, getCookie

from pyjamas.Window import alert

class PreferencesDlg(DialogBox):

    fileLocation = None

    def __init__(self, left = 50, top = 50):
        DialogBox.__init__(self, modal = False)

        self.setPopupPosition(left, top)
        self.setText("Preferences")
        ftable = FlexTable()
        ftableFormatter = ftable.getFlexCellFormatter()
        row = 0

        try:
            self.fileLocation = getCookie("fileLocation")
        except:
            self.fileLocation = None

        row += 1
        ftable.setWidget(row, 0, Label("Sheet loaded on startup", wordWrap=False))
        self.fileLocationInput = TextBox()
        self.fileLocationInput.addChangeListener(self.checkValid)
        self.fileLocationInput.addKeyboardListener(self)
        self.fileLocationInput.setVisibleLength(30)
        self.fileLocationInput.setText(self.fileLocation)
        ftable.setWidget(row, 1, self.fileLocationInput)

        row += 1
        hpanel = HorizontalPanel()
        self.saveBtn = Button("Save", self.onSave)
        self.saveBtn.setEnabled(False)
        hpanel.add(self.saveBtn)
        self.cancelBtn = Button("Cancel", self.onCancel)
        hpanel.add(self.cancelBtn)
        ftable.setWidget(row, 0, hpanel)
        ftableFormatter.setColSpan(row, 0, 2)

        self.setWidget(ftable)

    def onCancel(self, sender):
        self.hide()

    def onSave(self, sender):
        try:
            setCookie("fileLocation", self.fileLocationInput.getText(), 1000000000)
        except:
            pass
        self.hide()

    def checkValid(self, evt=None):
        if self.fileLocation != self.fileLocationInput.getText():
            self.saveBtn.setEnabled(True)
        else:
            self.saveBtn.setEnabled(False)

    def onClick(self, sender):
        pass

    def onKeyUp(self, sender, keyCode, modifiers):
        self.checkValid()

    def onKeyDown(self, sender, keyCode, modifiers):
        pass

    def onKeyPress(self, sender, keyCode, modifiers):
        pass

