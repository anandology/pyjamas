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

from pyjamas.ui.ButtonBase import ButtonBase
from pyjamas.ui.Event import Event

class CheckBox(ButtonBase):

    def __init__(self, label=None, asHTML=False):
        self.initElement(DOM.createInputCheck())

        self.setStyleName("gwt-CheckBox")
        if label:
            if asHTML:
                self.setHTML(label)
            else:
                self.setText(label)

    def initElement(self, element):
        ButtonBase.__init__(self, DOM.createSpan())
        self.inputElem = element
        self.labelElem = DOM.createLabel()

        self.unsinkEvents(Event.FOCUSEVENTS| Event.ONCLICK)
        DOM.sinkEvents(self.inputElem, Event.FOCUSEVENTS | Event.ONCLICK | DOM.getEventsSunk(self.inputElem))

        DOM.appendChild(self.getElement(), self.inputElem)
        DOM.appendChild(self.getElement(), self.labelElem)

        uid = "check" + self.getUniqueID()
        DOM.setAttribute(self.inputElem, "id", uid)
        DOM.setAttribute(self.labelElem, "htmlFor", uid)

    # emulate static
    def getUniqueID(self):
        JS("""
        _CheckBox_unique_id++;
        return _CheckBox_unique_id;
        };
        var _CheckBox_unique_id=0;
        {
        """)

    def getHTML(self):
        return DOM.getInnerHTML(self.labelElem)

    def getName(self):
        return DOM.getAttribute(self.inputElem, "name")

    def getText(self):
        return DOM.getInnerText(self.labelElem)

    def setChecked(self, checked):
        DOM.setBooleanAttribute(self.inputElem, "checked", checked)
        DOM.setBooleanAttribute(self.inputElem, "defaultChecked", checked)

    def isChecked(self):
        if self.isAttached():
            propName = "checked"
        else:
            propName = "defaultChecked"

        return DOM.getBooleanAttribute(self.inputElem, propName)

    def isEnabled(self):
        return not DOM.getBooleanAttribute(self.inputElem, "disabled")

    def setEnabled(self, enabled):
        DOM.setBooleanAttribute(self.inputElem, "disabled", not enabled)

    def setFocus(self, focused):
        if focused:
            Focus.focus(self, self.inputElem)
        else:
            Focus.blur(self, self.inputElem)

    def setHTML(self, html):
        DOM.setInnerHTML(self.labelElem, html)

    def setName(self, name):
        DOM.setAttribute(self.inputElem, "name", name)

    def setTabIndex(self, index):
        Focus.setTabIndex(self, self.inputElem, index)

    def setText(self, text):
        DOM.setInnerText(self.labelElem, text)

    def onDetach(self):
        self.setChecked(self.isChecked())
        ButtonBase.onDetach(self)


