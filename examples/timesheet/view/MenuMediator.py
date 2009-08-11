
# vim: set ts=4 sw=4 expandtab:

import puremvc.interfaces
import puremvc.patterns.mediator

from ApplicationConstants import Notification

from pyjamas.Window import alert
from model.TimeProxy import TimeProxy
from components.FileOpenDlg import FileOpenDlg
from components.PreferencesDlg import PreferencesDlg
from components.HelpContentsDlg import HelpContentsDlg
from components.HelpAboutDlg import HelpAboutDlg
from pyjamas.Cookies import getCookie

import sys
from pyjamas.Window import alert

import base64

class MenuMediator(puremvc.patterns.mediator.Mediator, puremvc.interfaces.IMediator):

    NAME = 'MenuMediator'
    fileLocation = None

    def __init__(self, viewComponent):
        super(MenuMediator, self).__init__(MenuMediator.NAME, viewComponent)
        self.viewComponent.mediator = self
        self.timeProxy = self.facade.retrieveProxy(TimeProxy.NAME)
        self.fileLocation = getCookie("fileLocation")
        if not self.fileLocation:
            self.fileLocation = "timesheet.txt"
        self.onFileOpen(self.fileLocation)

    def listNotificationInterests(self):
        return [
            Notification.MENU_FILE_OPEN,
            Notification.MENU_FILE_SAVEAS,
            Notification.MENU_FILE_PREFS,
            Notification.MENU_VIEW_EDIT,
            Notification.MENU_VIEW_SUM,
            Notification.MENU_VIEW_EDIT,
            Notification.MENU_VIEW_SUM,
            Notification.MENU_HELP_CONTENTS,
            Notification.MENU_HELP_ABOUT,
        ]

    def handleNotification(self, note):
        try:
            noteName = note.getName()
            if noteName == Notification.MENU_FILE_OPEN:
                self.onFileOpen()
            elif noteName == Notification.MENU_FILE_SAVEAS:
                self.onFileSaveAs()
            elif noteName == Notification.MENU_FILE_PREFS:
                self.onPreferences()
            elif noteName == Notification.MENU_VIEW_EDIT:
                self.onViewEdit()
            elif noteName == Notification.MENU_VIEW_SUM:
                self.onViewSummary()
            elif noteName == Notification.MENU_HELP_CONTENTS:
                self.onHelpContents()
            elif noteName == Notification.MENU_HELP_ABOUT:
                self.onHelpAbout()
        except:
            raise

    def onFileOpen(self, fileLocation = None):
        try:
            dlg = FileOpenDlg(fileLocation = fileLocation)
            dlg.mediator = self
            dlg.show()
        except:
            raise

    def onFileSaveAs(self):
        data = self.timeProxy.exportData()
        data_uri = 'data:text/plain;base64,%s' % base64.encodestring(data)
        wnd = wnd().open('','_blank','scrollbars=yes,width=300,height=300')
        wnd.document.open("text/html")
        wnd.document.write("""<a href="%s">Right click here</a> if your browser supports data uri<br />Otherwise, you'll have to copy and paste this output to a text file<br />\n""" % data_uri)
        wnd.document.write("<pre>")
        wnd.document.write(data)
        wnd.document.write("</pre>")
        wnd.document.close()

    def onPreferences(self):
        dlg = PreferencesDlg()
        dlg.mediator = self
        dlg.show()

    def onViewEdit(self):
        self.sendNotification(Notification.EDIT_SELECTED)

    def onViewSummary(self):
        self.sendNotification(Notification.SUM_SELECTED)

    def onHelpContents(self):
        dlg = HelpContentsDlg()
        dlg.mediator = self
        dlg.show()

    def onHelpAbout(self):
        dlg = HelpAboutDlg()
        dlg.mediator = self
        dlg.show()

