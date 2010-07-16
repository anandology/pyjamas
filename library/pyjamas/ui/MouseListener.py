# Copyright 2006 James Tauber and contributors
# Copyright (C) 2009 Luke Kenneth Casson Leighton <lkcl@lkcl.net>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from pyjamas import DOM
from pyjamas.ui import Event
from pyjamas.EventController import Handler

def fireMouseEvent(listeners, sender, event):
    x = DOM.eventGetClientX(event) - DOM.getAbsoluteLeft(sender.getElement())
    y = DOM.eventGetClientY(event) - DOM.getAbsoluteTop(sender.getElement())

    etype = DOM.eventGetType(event)
    if etype == "mousedown":
        for listener in listeners:
            listener.onMouseDown(sender, x, y)
        return True
    elif etype == "mouseup":
        for listener in listeners:
            listener.onMouseUp(sender, x, y)
        return True
    elif etype == "mousemove":
        for listener in listeners:
            listener.onMouseMove(sender, x, y)
        return True
    elif etype == "mouseover":
        from_element = DOM.eventGetFromElement(event)
        if not DOM.isOrHasChild(sender.getElement(), from_element):
            for listener in listeners:
                listener.onMouseEnter(sender)
        return True
    elif etype == "mouseout":
        to_element = DOM.eventGetToElement(event)
        if not DOM.isOrHasChild(sender.getElement(), to_element):
            for listener in listeners:
                listener.onMouseLeave(sender)
        return True
    return False

MOUSE_EVENTS = [ "mousedown", "mouseup", "mousemove", "mouseover", "mouseout"]

class MouseHandler(object):

    def __init__(self, preventDefault=False):

        self._mouseListeners = 1
        self._md = Handler(self, "MouseDown")
        self._mu = Handler(self, "MouseUp")
        self._mm = Handler(self, "MouseMove")
        self._me = Handler(self, "MouseEnter")
        self._ml = Handler(self, "MouseLeave")
        self._mousePreventDefault = preventDefault
        self.sinkEvents( Event.MOUSEEVENTS )

    def onBrowserEvent(self, event):
        etype = DOM.eventGetType(event)
        if etype in MOUSE_EVENTS:
            if self._mousePreventDefault:
                DOM.eventPreventDefault(event)
            x = DOM.eventGetClientX(event) - \
                DOM.getAbsoluteLeft(self.getElement())
            y = DOM.eventGetClientY(event) - \
                DOM.getAbsoluteTop(self.getElement())

            if etype == "mousedown":
                self.onMouseDownEvent(self, x, y)
            elif etype == "mouseup":
                self.onMouseUpEvent(self, x, y)
            elif etype == "mousemove":
                self.onMouseMoveEvent(self, x, y)
            elif etype == "mouseover":
                from_element = DOM.eventGetFromElement(event)
                if not DOM.isOrHasChild(self.getElement(), from_element):
                    self.onMouseEnterEvent(self)
            elif etype == "mouseout":
                to_element = DOM.eventGetToElement(event)
                if not DOM.isOrHasChild(self.getElement(), to_element):
                    self.onMouseLeaveEvent(self)
            return True

        return False

    def onMouseMove(self, sender, x, y):
        pass
        
    def onMouseDown(self, sender, x, y):
        pass

    def onMouseUp(self, sender, x, y):
        pass

    def onMouseEnter(self, sender):
        pass

    def onMouseLeave(self, sender):
        pass

