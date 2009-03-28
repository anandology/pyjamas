# Copyright 2006 James Tauber and contributors
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

from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.Focus import Focus
from pyjamas.ui.Event import Event
from pyjamas.ui.FocusListener import FocusListener
from pyjamas.ui.MouseListener import MouseListener
from pyjamas.ui import KeyboardListener

class FocusPanel(SimplePanel):
    def __init__(self, child=None):
        self.clickListeners = []
        self.focusListeners = []
        self.keyboardListeners = []
        self.mouseListeners = []

        SimplePanel.__init__(self, Focus.createFocusable(self))
        self.sinkEvents(Event.FOCUSEVENTS | Event.KEYEVENTS | Event.ONCLICK | Event.MOUSEEVENTS)

        if child:
            self.setWidget(child)

    def addClickListener(self, listener):
        self.clickListeners.append(listener)

    def addFocusListener(self, listener):
        self.focusListeners.append(listener)

    def addKeyboardListener(self, listener):
        self.keyboardListeners.append(listener)

    def addMouseListener(self, listener):
        self.mouseListeners.append(listener)

    def getTabIndex(self):
        return Focus.getTabIndex(self, self.getElement())

    def onBrowserEvent(self, event):
        type = DOM.eventGetType(event)

        if type == "click":
            for listener in self.clickListeners:
                if listener.onClick: listener.onClick(self, event)
                else: listener(self, event)
        elif type == "mousedown" or type == "mouseup" or type == "mousemove" or type == "mouseover" or type == "mouseout":
            MouseListener.fireMouseEvent(self, self.mouseListeners, self, event)
        elif type == "blur" or type == "focus":
            FocusListener.fireFocusEvent(self, self.focusListeners, self, event)
        elif type == "keydown" or type == "keypress" or type == "keyup":
            KeyboardListener.fireKeyboardEvent(self.keyboardListeners, self, event)

    def removeClickListener(self, listener):
        self.clickListeners.remove(listener)

    def removeFocusListener(self, listener):
        self.focusListeners.remove(listener)

    def removeKeyboardListener(self, listener):
        self.keyboardListeners.remove(listener)

    def removeMouseListener(self, listener):
        self.mouseListeners.remove(listener)

    def setAccessKey(self, key):
        Focus.setAccessKey(self, self.getElement(), key)

    def setFocus(self, focused):
        if (focused):
            Focus.focus(self, self.getElement())
        else:
            Focus.blur(self, self.getElement())

    def setTabIndex(self, index):
        Focus.setTabIndex(self, self.getElement(), index)


