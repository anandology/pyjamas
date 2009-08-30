""" 
    Copyright (C) 2008, 2009 - Luke Kenneth Casson Leighton <lkcl@lkcl.net>

"""
from pyjamas import DOM
from pyjamas.ui import Event

class ClickHandler:

    def __init__(self):
        self._clickListeners = []
        
        self.sinkEvents( Event.ONCLICK )

    def onBrowserEvent(self, event):
        type = DOM.eventGetType(event)

    def onLostFocus(self, sender):
        pass

    def onClick(self, sender=None):
        pass

    def addClickListener(self, listener):
        self._clickListeners.append(listener)

    def onBrowserEvent(self, event):
        type = DOM.eventGetType(event)
        if type == "click":
            for listener in self._clickListeners:
                if hasattr(listener, "onClick"):
                    listener.onClick(self)
                else:
                    listener(self)

    def removeClickListener(self, listener):
        self._clickListeners.remove(listener)

