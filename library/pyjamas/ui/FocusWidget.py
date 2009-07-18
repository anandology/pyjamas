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

from pyjamas.ui.Widget import Widget
from pyjamas.ui import Focus
from pyjamas.ui import Event
from pyjamas.ui import FocusListener
from pyjamas.ui import KeyboardListener

class FocusWidget(Widget):

    def __init__(self, element, **kwargs):
        self.setElement(element)
        self.clickListeners = []
        self.focusListeners = []
        self.keyboardListeners = []

        Widget.__init__(self, **kwargs)
        self.sinkEvents(Event.ONCLICK | Event.FOCUSEVENTS | Event.KEYEVENTS)

    def addClickListener(self, listener):
        self.clickListeners.append(listener)

    def addFocusListener(self, listener):
        self.focusListeners.append(listener)

    def addKeyboardListener(self, listener):
        self.keyboardListeners.append(listener)

    def getTabIndex(self):
        return Focus.getTabIndex(self.getElement())

    def isEnabled(self):
        try:
            return not DOM.getBooleanAttribute(self.getElement(), "disabled")
        except TypeError:
            return True
        except AttributeError:
            return True

    def onBrowserEvent(self, event):
        type = DOM.eventGetType(event)
        if type == "click":
            for listener in self.clickListeners:
                if hasattr(listener, "onClick"): listener.onClick(self)
                else: listener(self)
        elif type == "blur" or type == "focus":
            FocusListener.fireFocusEvent(self.focusListeners, self, event)
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
            Focus.focus(self.getElement())
        else:
            Focus.blur(self.getElement())

    def setTabIndex(self, index):
        Focus.setTabIndex(self.getElement(), index)


