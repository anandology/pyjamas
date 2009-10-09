""" 
    Copyright (C) 2008, 2009 - Luke Kenneth Casson Leighton <lkcl@lkcl.net>
  
"""
from pyjamas import DOM
from pyjamas.ui import Event

class ClickHandler(object):

    def __init__(self):
        self._clickListeners = []
        
        self.sinkEvents( Event.ONCLICK )

    def onClick(self, sender=None):
        pass

    def addClickListener(self, listener):
        self._clickListeners.append(listener)

    def onBrowserEvent(self, event):
        """Listen to events raised by the browser and call the appropriate 
        method of the listener (widget, ..) object. 
        """
        type = DOM.eventGetType(event)
        if type == "click":
            for listener in self._clickListeners:
                if hasattr(listener, "onClick"):
                    listener.onClick(self)
                else:
                    listener(self)

    def removeClickListener(self, listener):
        self._clickListeners.remove(listener)

class DoubleClickHandler(object):

    def __init__(self):
        self._doubleclickListeners = []
        
        self.sinkEvents( Event.ONDBLCLICK )

    def onDoubleClick(self, sender=None):
        pass

    def addDoubleClickListener(self, listener):
        self._doubleclickListeners.append(listener)

    def onBrowserEvent(self, event):
        """Listen to events raised by the browser and call the appropriate 
        method of the listener (widget, ..) object. 
        """
        type = DOM.eventGetType(event)
        if type == "dblclick":
            for listener in self._doubleclickListeners:
                if hasattr(listener, "onDblClick"):
                    listener.onDblClick(self)
                else:
                    listener(self)

    def removeDoubleClickListener(self, listener):
        self._doubleclickListeners.remove(listener)

