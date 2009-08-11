"""
The ``ui.Hyperlink`` class acts as an "internal" hyperlink to a particular
state of the application.  These states are stored in the application's
history, allowing for the use of the Back and Next buttons in the browser to
move between application states.

The ``ui.Hyperlink`` class only makes sense in an application which keeps track
of state using the ``History`` module.  When the user clicks on a hyperlink,
the application changes state by calling ``History.newItem(newState)``.  The
application then uses a history listener function to respond to the change in
state in whatever way makes sense.
"""
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.Hyperlink import Hyperlink
from pyjamas.ui.Label import Label
from pyjamas import History


class HyperlinkDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        History.addHistoryListener(self)

        vPanel = VerticalPanel()

        self.stateDisplay = Label()
        vPanel.add(self.stateDisplay)

        hPanel = HorizontalPanel(Spacing=5)
        hPanel.add(Hyperlink("State 1", False, "state number 1"))
        hPanel.add(Hyperlink("State 2", False, "state number 2"))

        vPanel.add(hPanel)
        self.add(vPanel)

    def onHistoryChanged(self, state):
        self.stateDisplay.setText(state)

