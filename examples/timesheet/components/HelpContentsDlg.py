
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

class HelpContentsDlg(DialogBox):

    def __init__(self, left = 50, top = 50):
        try:
            DialogBox.__init__(self, modal = False)

            self.setPopupPosition(left, top)
            self.dockPanel = DockPanel()
            self.dockPanel.setSpacing(4)
            self.setText("Help Contents")
            self.setWidth('80%')

            msg = HTML("""\
<h2>Introduction</h2>

This application can be used to maintain a timesheet.

<p/>
On startup, it tries to open the last opened timesheet.

<p/>
There are two modes: Edit and Summary (see menu). In edit mode the user can enter/modify his timescheet. There's some inteligence built in. The 'From' is filled in automatically when the previous line has a 'To'. The 'To' can be filled in as time span, or as end-time. The 'Project' is mandatory (as the 'From' and 'To' are). The user can walk around with the cursor keys.


<h2>Opening and saving sheets</h2>
The sheet can be loaded and saved from a local file. There might be some issues with Firefox, which might refuse access to the document in an iframe.

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
