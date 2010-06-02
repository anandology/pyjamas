"""
The ``ui.PopupPanel`` class implements a panel that pops up in the browser
window to display some contents.  When the user clicks outside the popup, it
disappears again.

The PopupPanel requires stylesheet definitions in order to work properly.  The
following stylesheet definitions were used in the example below:

    .showcase-popup {
        background-color: white;
        border: 1px solid #87B3FF;
        padding: 4px;
    }

Also, PopupPanel implements an optional &ldquo;glass&rdquo; &mdash; a shadowed
background that overlays everything under popup. See DialogBox demo to look at
the glass usage example.

Note that the popup panel is supposed to close when the user clicks outside of
it.  However, this doesn't work under Firefox 3, so the code below adds a click
handler so the user can click on the popup itself to close it.
"""
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.HTML import HTML
from pyjamas.ui.Button import Button
from pyjamas.ui.PopupPanel import PopupPanel

class PopupPanelDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        vPanel = VerticalPanel()
        vPanel.setSpacing(4)

        self._btn = Button("Click Me", getattr(self, "showPopup"))

        vPanel.add(HTML("Click on the button below to display the popup."))
        vPanel.add(self._btn)

        self.add(vPanel)


    def showPopup(self, event):
        contents = HTML("Hello, World!")
        contents.addClickListener(getattr(self, "onClick"))

        self._popup = PopupPanel(autoHide=True)
        self._popup.add(contents)
        self._popup.setStyleName("showcase-popup")

        left = self._btn.getAbsoluteLeft() + 10
        top  = self._btn.getAbsoluteTop() + 10
        self._popup.setPopupPosition(left, top)
        self._popup.show()


    def onClick(self, sender=None):
        self._popup.hide()

