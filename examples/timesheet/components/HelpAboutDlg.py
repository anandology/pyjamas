
# vim: set ts=4 sw=4 expandtab:

from ApplicationConstants import Notification

from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.Label import Label
from pyjamas.ui.Button import Button
from pyjamas.ui.DialogBox import DialogBox
from pyjamas.ui.HTML import HTML
from pyjamas.ui.DockPanel import DockPanel
from pyjamas.ui.Frame import Frame
import pyjamas.DOM as DOM


from pyjamas.Window import alert

class HelpAboutDlg(DialogBox):

    def __init__(self, left = 50, top = 50):
        try:
            DialogBox.__init__(self, modal = False)

            self.setPopupPosition(left, top)
            self.dockPanel = DockPanel()
            self.dockPanel.setSpacing(4)
            self.setText("About")

            msg = HTML("""\
This is an example application, which uses PureMVC<br/>
<br/>
""", True)
            self.dockPanel.add(msg, DockPanel.CENTER)
            self.closeBtn = Button("Close", self)
            self.dockPanel.add(self.closeBtn, DockPanel.SOUTH)

            self.setWidget(self.dockPanel)
        except:
            raise

    def onClick(self, sender):
        self.hide()
