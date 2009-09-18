
# vim: set ts=4 sw=4 expandtab:

from ApplicationConstants import Notification

from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.Label import Label
from pyjamas.ui.Button import Button
from pyjamas.ui.DialogBox import DialogBox
from pyjamas.ui.FormPanel import FormPanel
from pyjamas.ui.FileUpload import FileUpload
from pyjamas.ui.HTML import HTML
from pyjamas.ui.DockPanel import DockPanel
from pyjamas.ui.Frame import Frame
import pyjamas.DOM as DOM

from __pyjamas__ import doc
from pyjamas.Window import alert
from pyjamas import Window
import sys

has_getAsText = True

class FileOpenDlg(DialogBox):

    files = None

    def __init__(self, left = 50, top = 50, fileLocation = None):
        global has_getAsText
        try:
            DialogBox.__init__(self, modal = False)

            self.setPopupPosition(left, top)
            self.dockPanel = DockPanel()
            self.dockPanel.setSpacing(4)
            self.setText("File Open")

            if not fileLocation is None:
                msg = HTML("Loading file...", True)
                self.dockPanel.add(msg, DockPanel.NORTH)
                location =  fileLocation
                if fileLocation.find("://") < 0:
                    base = Window.getLocation().getHref()
                    print base
                    if base.find('/') >= 0:
                        sep = '/'
                    else:
                        sep = '\\'
                    base = sep.join(base.split(sep)[:-1]) + sep
                    location = base + fileLocation
                self.iframe = Frame(location)
                self.dockPanel.add(self.iframe, DockPanel.CENTER)
            else:
                msg = HTML("Choose a file", True)

                self.browseFile = FileUpload()
                elem = self.browseFile.getElement()
                if False and has_getAsText and hasattr(elem, 'files'):
                    self.iframe = None
                    self.files = elem.files
                    self.dockPanel.add(self.browseFile, DockPanel.CENTER)
                else:
                    self.browseFile = None
                    self.files = None
                    base = '' + doc().location
                    if base.find('/') >= 0:
                        sep = '/'
                    else:
                        sep = '\\'
                    if not base.lower()[:5] == "file:":
                        base = "file:///C:/"
                        msg = HTML("You'll have to place the application on a local file system, otherwise the browser forbids access.", True)
                    else:
                        base = sep.join(base.split(sep)[:-1]) + sep
                    self.iframe = Frame(base)
                    self.dockPanel.add(self.iframe, DockPanel.CENTER)
                self.dockPanel.add(msg, DockPanel.NORTH)

            if self.iframe:
                self.iframe.setWidth("36em")
            hpanel = HorizontalPanel()
            self.openBtn = Button("Open", self)
            hpanel.add(self.openBtn)
            self.cancelBtn = Button("Cancel", self)
            hpanel.add(self.cancelBtn)
            self.dockPanel.add(hpanel, DockPanel.SOUTH)

            self.setWidget(self.dockPanel)
        except:
            raise

    def onClick(self, sender):
        global has_getAsText
        if sender == self.cancelBtn:
            self.hide()
        elif sender == self.openBtn:
            data = None
            filename = None
            if self.files:
                if self.files.length == 0:
                    return
                if self.files.length > 1:
                    alert("Cannot open more than one file")
                    return
                file = self.files.item(0)
                filename = file.fileName
                try:
                    data = file.getAsText("")
                except AttributeError, e:
                    has_getAsText = False
                    alert("Sorry. cannot retrieve file in this browser.\nTry again.")
            else:
                elem = self.iframe.getElement()
                # On firefox, this runs into:
                #   Permission denied to get property Window.document
                # when the file is not in the current domain
                body = elem.contentWindow.document.body
                try:
                    filename = '' + elem.contentWindow.location
                except:
                    filename = None
                if body.childNodes.length == 1:
                    data = '' + body.childNodes.item(0).innerHTML
                else:
                    data = '' + body.innerHTML
            self.hide()
            if data:
                self.mediator.sendNotification(Notification.FILE_LOADED, (filename, data))
