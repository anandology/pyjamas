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
from pyjamas.ui import Event
from pyjamas.ui import MouseListener

class Label(Widget):

    def __init__(self, text=None, wordWrap=True):
        Widget.__init__(self)
        self.horzAlign = ""
        self.clickListeners = []
        self.mouseListeners = []

        self.setElement(DOM.createDiv())
        self.sinkEvents(Event.ONCLICK | Event.MOUSEEVENTS)
        self.setStyleName("gwt-Label")
        if text:
            self.setText(text)

        self.setWordWrap(wordWrap)

    def addClickListener(self, listener):
        self.clickListeners.append(listener)

    def addMouseListener(self, listener):
        self.mouseListeners.append(listener)

    def getHorizontalAlignment(self):
        return self.horzAlign

    def getText(self):
        return DOM.getInnerText(self.getElement())

    def getWordWrap(self):
        return not (DOM.getStyleAttribute(self.getElement(), "whiteSpace") == "nowrap")

    def onBrowserEvent(self, event):
        type = DOM.eventGetType(event)
        #print "Label onBrowserEvent", type, self.clickListeners
        if type == "click":
            for listener in self.clickListeners:
                if listener.onClick: listener.onClick(self, event)
                else: listener(self, event)
        elif type == "mousedown" or type == "mouseup" or type == "mousemove" or type == "mouseover" or type == "mouseout":
            MouseListener.fireMouseEvent(self.mouseListeners, self, event)
        else:
            Widget.onBrowserEvent(self, event)

    def removeClickListener(self, listener):
        self.clickListeners.remove(listener)

    def removeMouseListener(self, listener):
        self.mouseListeners.remove(listener)

    def setHorizontalAlignment(self, align):
        self.horzAlign = align
        DOM.setStyleAttribute(self.getElement(), "textAlign", align)

    def setText(self, text):
        DOM.setInnerText(self.getElement(), text)

    def setWordWrap(self, wrap):
        if wrap:
            style = "normal"
        else:
            style = "nowrap"
        DOM.setStyleAttribute(self.getElement(), "whiteSpace", style)


