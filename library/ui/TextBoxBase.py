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
from __pyjamas__ import JS
from pyjamas import DOM

from pyjamas.ui.FocusWidget import FocusWidget
from pyjamas.ui.Event import Event

class TextBoxBase(FocusWidget):
    ALIGN_CENTER = "center"
    ALIGN_JUSTIFY = "justify"
    ALIGN_LEFT = "left"
    ALIGN_RIGHT = "right"

    def __init__(self, element):
        self.changeListeners = []
        self.clickListeners = []
        self.currentEvent = None
        self.keyboardListeners = []

        FocusWidget.__init__(self, element)
        self.sinkEvents(Event.ONCHANGE)

    def addChangeListener(self, listener):
        self.changeListeners.append(listener)

    def addClickListener(self, listener):
        self.clickListeners.append(listener)

    def addKeyboardListener(self, listener):
        self.keyboardListeners.append(listener)

    def cancelKey(self):
        if self.currentEvent != None:
            DOM.eventPreventDefault(self.currentEvent)

    def getCursorPos(self):
        JS("""
        try {
            var element = this.getElement()
            return element.selectionStart;
        } catch (e) {
            return 0;
        }
        """)

    def getName(self):
        return DOM.getAttribute(self.getElement(), "name")

    def getSelectedText(self):
        start = self.getCursorPos()
        length = self.getSelectionLength()
        text = self.getText()
        return text[start:start + length]

    def getSelectionLength(self):
        JS("""
        try{
            var element = this.getElement()
            return element.selectionEnd - element.selectionStart;
        } catch (e) {
            return 0;
        }
        """)

    def getText(self):
        return DOM.getAttribute(self.getElement(), "value")

    # BUG: keyboard & click events already fired in FocusWidget.onBrowserEvent
    def onBrowserEvent(self, event):
        FocusWidget.onBrowserEvent(self, event)

        type = DOM.eventGetType(event)
        #if DOM.eventGetTypeInt(event) & Event.KEYEVENTS:
            #self.currentEvent = event
            #KeyboardListener.fireKeyboardEvent(self.keyboardListeners, self, event)
            #self.currentEvent = None
        #elif type == "click":
            #for listener in self.clickListeners:
                #if listener.onClick: listener.onClick(self, event)
                #else: listener(self)
        #elif type == "change":
            #for listener in self.changeListeners:
                #if listener.onChange: listener.onChange(self, event)
                #else: listener(self)
        if type == "change":
            for listener in self.changeListeners:
                if listener.onChange: listener.onChange(self)
                else: listener(self)

    def removeChangeListener(self, listener):
        self.changeListeners.remove(listener)

    def removeClickListener(self, listener):
        self.clickListeners.remove(listener)

    def removeKeyboardListener(self, listener):
        self.keyboardListeners.remove(listener)

    def selectAll(self):
        length = len(self.getText())
        if length > 0:
            self.setSelectionRange(0, length)

    def setCursorPos(self, pos):
        self.setSelectionRange(pos, 0)

    def setKey(self, key):
        if self.currentEvent != None:
            DOM.eventSetKeyCode(self.currentEvent, key)

    def setName(self, name):
        DOM.setAttribute(self.getElement(), "name", name)

    def setSelectionRange(self, pos, length):
        if length < 0:
            # throw new IndexOutOfBoundsException("Length must be a positive integer. Length: " + length);
            console.error("Length must be a positive integer. Length: " + length)

        if (pos < 0) or (length + pos > len(self.getText())):
            #throw new IndexOutOfBoundsException("From Index: " + pos + "  To Index: " + (pos + length) + "  Text Length: " + getText().length());
            console.error("From Index: " + pos + "  To Index: " + (pos + length) + "  Text Length: " + len(self.getText()))

        element = self.getElement()
        element.setSelectionRange(pos, pos + length)

    def setText(self, text):
        DOM.setAttribute(self.getElement(), "value", text)

    def setTextAlignment(self, align):
        DOM.setStyleAttribute(self.getElement(), "textAlign", align)


