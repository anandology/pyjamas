""" 
    Copyright (C) 2008, 2009 - Luke Kenneth Casson Leighton <lkcl@lkcl.net>
  
"""
from pyjamas import DOM
from pyjamas.ui import Event
from pyjamas.EventController import Handler

class ClickHandler(object):

    def __init__(self, preventDefault=False):
        self._clickListeners = Handler(self, "Click")
        self._doubleclickListeners = Handler(self, "DoubleClick")
        self._clickPreventDefault = preventDefault
        
        self.sinkEvents(Event.ONCLICK)
        self.sinkEvents(Event.ONDBLCLICK)

    def onClick(self, sender=None):
        pass

    def onDoubleClick(self, sender=None):
        pass

    def onBrowserEvent(self, event):
        """Listen to events raised by the browser and call the appropriate 
        method of the listener (widget, ..) object. 
        """
        etype = DOM.eventGetType(event)
        if etype == "click":
            if self._clickPreventDefault:
                DOM.eventPreventDefault(event)
            self.onClickEvent(self)
        elif etype == "dblclick":
            if self._clickPreventDefault:
                DOM.eventPreventDefault(event)
            self.onDoubleClickEvent(self)

