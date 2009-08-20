from pyjamas.ui.HTML import HTML
from pyjamas.ui.Button import Button
from pyjamas.ui.HTMLPanel import HTMLPanel
from pyjamas.ui.DockPanel import DockPanel
from pyjamas.ui.ScrollPanel import ScrollPanel
from pyjamas.ui.DialogBox import DialogBox
from pyjamas.ui import HasAlignment

class HTMLDialog(DialogBox):
    def __init__(self, name, html):
        DialogBox.__init__(self)
        self.setText(name)

        closeButton = Button("Close", self)

        htp = HTMLPanel(html)
        self.sp = ScrollPanel(htp)

        dock = DockPanel()
        dock.setSpacing(4)

        dock.add(closeButton, DockPanel.SOUTH)
        dock.add(self.sp, DockPanel.CENTER)

        dock.setCellHorizontalAlignment(closeButton, HasAlignment.ALIGN_RIGHT)
        dock.setCellWidth(self.sp, "100%")
        dock.setWidth("100%")
        self.setWidget(dock)

    def setWidth(self, width):
        DialogBox.setWidth(self, "%dpx" % width)
        self.sp.setWidth("%dpx" % (width-20))

    def setHeight(self, height):
        DialogBox.setHeight(self, "%dpx" % height)
        self.sp.setHeight("%dpx" % (height-65))

    def onClick(self, sender):
        self.hide()

