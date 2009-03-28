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
from __pyjamas__ import JS, console
from pyjamas import DOM

from pyjamas.ui.Widget import Widget
from pyjamas.ui.Focus import Focus
from pyjamas.ui import Event
from pyjamas.ui.FocusListener import FocusListener
from pyjamas.ui import KeyboardListener

class FocusWidget(Widget):

    def __init__(self, element, **kwargs):
        Widget.__init__(self, **kwargs)
        self.clickListeners = []
        self.focusListeners = []
        self.keyboardListeners = []

        self.setElement(element)
        self.sinkEvents(Event.ONCLICK | Event.FOCUSEVENTS | Event.KEYEVENTS)

    def addClickListener(self, listener):
        self.clickListeners.append(listener)

    def addFocusListener(self, listener):
        self.focusListeners.append(listener)

    def addKeyboardListener(self, listener):
        self.keyboardListeners.append(listener)

    def getTabIndex(self):
        return Focus.getTabIndex(self, self.getElement())

    def isEnabled(self):
        return not DOM.getBooleanAttribute(self.getElement(), "disabled")

    def onBrowserEvent(self, event):
        type = DOM.eventGetType(event)
        if type == "click":
            for listener in self.clickListeners:
                if hasattr(listener, "onClick"): listener.onClick(self, event)
                else: listener(self, event)
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

    def setAccessKey(self, key):
        DOM.setAttribute(self.getElement(), "accessKey", "" + key)

    def setEnabled(self, enabled):
        DOM.setBooleanAttribute(self.getElement(), "disabled", not enabled)

    def setFocus(self, focused):
        if (focused):
            Focus.focus(self, self.getElement())
        else:
            Focus.blur(self, self.getElement())

    def setTabIndex(self, index):
        Focus.setTabIndex(self, self.getElement(), index)


