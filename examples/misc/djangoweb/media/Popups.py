from pyjamas.ui.Button import Button
from pyjamas.ui.PopupPanel import PopupPanel
from pyjamas.ui.HTML import HTML
from pyjamas.ui.DockPanel import DockPanel
from pyjamas.ui.DialogBox import DialogBox
from pyjamas.ui.Frame import Frame
from pyjamas.ui import HasAlignment

class FileDialog(DialogBox):
    def __init__(self, url):
        DialogBox.__init__(self)
        self.setText("Upload Files")
        
        iframe = Frame(url)
        closeButton = Button("Close", self)
        msg = HTML("<center>Upload files, here.  Please avoid spaces in file names.<br />(rename the file before uploading)</center>", True)

        dock = DockPanel()
        dock.setSpacing(4)
        
        dock.add(closeButton, DockPanel.SOUTH)
        dock.add(msg, DockPanel.NORTH)
        dock.add(iframe, DockPanel.CENTER)
        
        dock.setCellHorizontalAlignment(closeButton, HasAlignment.ALIGN_RIGHT)
        dock.setCellWidth(iframe, "100%")
        dock.setWidth("100%")
        iframe.setWidth("800px")
        iframe.setHeight("600px")
        self.setWidget(dock)

    def onClick(self, sender):
        self.hide()

