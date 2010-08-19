""" This example shows how to check in onBrowserEvent whether the
    event targets a child, and if so refuse to handle it, so that
    the child widget will be the only widget dealing with it.

    see _event_targets_title() for details.
"""

import pyjd # dummy in pyjs

from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.HTML import HTML
from pyjamas.ui.ClickListener import ClickHandler
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui import Event
from pyjamas import log
from pyjamas import DOM

class Board(VerticalPanel, ClickHandler):
    def __init__(self):
        """ Standard initialiser.
        """
        VerticalPanel.__init__(self)
        ClickHandler.__init__(self)
        self.addClickListener(self)
        self.title=Text('Board')
        self.title.setzIndex(100)
        self.add(self.title)
        self.setSize("100%", "50%")        
        self.setBorderWidth(1)

    def onClick(self, sender):
        log.writebr('Text'+str(sender))

    def _event_targets_title(self, event):
        target = DOM.eventGetTarget(event)
        return target and DOM.isOrHasChild(self.title.getElement(), target)

    def onBrowserEvent(self, event):
        etype = DOM.eventGetType(event)
        if etype == "click":
            if self._event_targets_title(event):
                return
        ClickHandler.onBrowserEvent(self, event)


class Text(HTML, ClickHandler):
    def __init__(self, text):
        HTML.__init__(self, text)
        ClickHandler.__init__(self, preventDefault=True)
        self.addClickListener(self)        

    def onClick(self, sender):
        log.writebr('Text'+str(sender))


if __name__ == "__main__":
    pyjd.setup("./Override.html")
    board = Board()
    RootPanel().add(board)
    pyjd.run()

