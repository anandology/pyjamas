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

from pyjamas.ui.FocusWidget import FocusWidget
from pyjamas.ui import Event

class ListBox(FocusWidget):
    def __init__(self):
        self.changeListeners = []
        self.INSERT_AT_END = -1
        FocusWidget.__init__(self, DOM.createSelect())
        self.sinkEvents(Event.ONCHANGE)
        self.setStyleName("gwt-ListBox")

    def addChangeListener(self, listener):
        self.changeListeners.append(listener)

    def addItem(self, item, value = None):
        self.insertItem(item, value, self.INSERT_AT_END)

    def clear(self):
        h = self.getElement()
        while DOM.getChildCount(h) > 0:
            DOM.removeChild(h, DOM.getChild(h, 0))

    def getItemCount(self):
        return DOM.getChildCount(self.getElement())

    def getItemText(self, index):
        child = DOM.getChild(self.getElement(), index)
        return DOM.getInnerText(child)

    def getName(self):
        return DOM.getAttribute(self.getElement(), "name")

    def getSelectedIndex(self):
        return DOM.getIntAttribute(self.getElement(), "selectedIndex")

    def getValue(self, index):
        self.checkIndex(index)

        option = DOM.getChild(self.getElement(), index)
        return DOM.getAttribute(option, "value")

    def getVisibleItemCount(self):
        return DOM.getIntAttribute(self.getElement(), "size")

    # also callable as insertItem(item, index)
    def insertItem(self, item, value, index=None):
        if index == None:
            index = value
            value = None
        DOM.insertListItem(self.getElement(), item, value, index)

    def isItemSelected(self, index):
        self.checkIndex(index)
        option = DOM.getChild(self.getElement(), index)
        return DOM.getBooleanAttribute(option, "selected")

    def isMultipleSelect(self):
        return DOM.getBooleanAttribute(self.getElement(), "multiple")

    def onBrowserEvent(self, event):
        if DOM.eventGetType(event) == "change":
            for listener in self.changeListeners:
                if listener.onChange:
                    listener.onChange(self)
                else:
                    listener(self)
        else:
            FocusWidget.onBrowserEvent(self, event)

    def removeChangeListener(self, listener):
        self.changeListeners.remove(listener)

    def removeItem(self, idx):
        child = DOM.getChild(self.getElement(), idx)
        DOM.removeChild(self.getElement(), child)

    def setItemSelected(self, index, selected):
        self.checkIndex(index)
        option = DOM.getChild(self.getElement(), index)
        DOM.setBooleanAttribute(option, "selected", selected)

    def setMultipleSelect(self, multiple):
        DOM.setBooleanAttribute(self.getElement(), "multiple", multiple)

    def setName(self, name):
        DOM.setAttribute(self.getElement(), "name", name)

    def setSelectedIndex(self, index):
        DOM.setIntAttribute(self.getElement(), "selectedIndex", index)

    def selectValue(self, value):
        for n in range(self.getItemCount()):
            # http://code.google.com/p/pyjamas/issues/detail?id=63
            if self.getItemText(n) == value:
                self.setSelectedIndex(n)
                return n
        return None

    def setItemText(self, index, text):
        self.checkIndex(index)
        if text == None:
            console.error("Cannot set an option to have null text")
            return
        DOM.setOptionText(self.getElement(), text, index)

    def setValue(self, index, value):
        self.checkIndex(index)

        option = DOM.getChild(self.getElement(), index)
        DOM.setAttribute(option, "value", value)

    def setVisibleItemCount(self, visibleItems):
        DOM.setIntAttribute(self.getElement(), "size", visibleItems)

    def checkIndex(self, index):
        elem = self.getElement()
        if (index < 0) or (index >= DOM.getChildCount(elem)):
            #throw new IndexOutOfBoundsException();
            pass


