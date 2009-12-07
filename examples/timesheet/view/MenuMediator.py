
# vim: set ts=4 sw=4 expandtab:

from puremvc.patterns.mediator import Mediator

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
from __pyjamas__ import wnd

import base64

class MenuMediator(Mediator):

    NAME = 'MenuMediator'
    fileLocation = None

    def __init__(self, viewComponent):
        Mediator.__init__(self, MenuMediator.NAME, viewComponent)
        viewComponent.mFileOpen.setHandler(self.onFileOpen)
        viewComponent.mFileSaveAs.setHandler(self.onFileSaveAs)
        viewComponent.mFilePreferences.setHandler(self.onFilePreferences)
        viewComponent.mViewEdit.setHandler(self.onViewEdit)
        viewComponent.mViewSummary.setHandler(self.onViewSummary)
        viewComponent.mHelpContents.setHandler(self.onHelpContents)
        viewComponent.mHelpAbout.setHandler(self.onHelpAbout)
        self.timeProxy = self.facade.retrieveProxy(TimeProxy.NAME)
        try:
            fileLocation = getCookie("fileLocation")
        except:
            fileLocation = None
        self.fileLocation = self.checkFileLocation(fileLocation)
        self.onFileOpen(self.fileLocation)

    def listNotificationInterests(self):
        return []

    def handleNotification(self, note):
        pass

    def checkFileLocation(self, fileLocation):
        if fileLocation is None \
           or fileLocation is "null":
            fileLocation = "timesheet.txt"
        return fileLocation

    def onFileOpen(self, fileLocation = None):
        try:
            dlg = None

            def onOpen(sender):
                self.sendNotification(Notification.FILE_LOADED, 
                                      (dlg.filename, dlg.data))

            fileLocation = self.checkFileLocation(fileLocation)
            dlg = FileOpenDlg(fileLocation = fileLocation)
            dlg.openBtn.addClickListener(onOpen)
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

    def onFilePreferences(self):
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
