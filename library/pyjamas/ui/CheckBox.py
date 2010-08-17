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
from pyjamas import Factory

from ButtonBase import ButtonBase
from pyjamas.ui import Event
from pyjamas.ui import Focus

_CheckBox_unique_id=0;

class CheckBox(ButtonBase):

    _props = [("name", "Name", "Name", None),
            ]
    def __init__(self, label=None, asHTML=False, **ka):
        ka['StyleName'] = ka.get('StyleName', "gwt-CheckBox")
        if label:
            if asHTML:
                ka['HTML'] = label
            else:
                ka['Text'] = label
        element = ka.pop('Element', None) or DOM.createInputCheck()
        self.initElement(element, **ka)

    @classmethod
    def _getProps(self):
        return ButtonBase._getProps() + self._props

    def initElement(self, element, **ka):
        self.inputElem = element
        self.labelElem = DOM.createLabel()
        element = ka.pop('Element', None) or DOM.createSpan()
        ButtonBase.__init__(self, element, **ka)

        self.unsinkEvents(Event.FOCUSEVENTS | Event.ONCLICK)
        DOM.sinkEvents(self.inputElem, Event.FOCUSEVENTS | Event.ONCLICK |
                       DOM.getEventsSunk(self.inputElem))

        DOM.appendChild(self.getElement(), self.inputElem)
        DOM.appendChild(self.getElement(), self.labelElem)

        uid = "check%d" % self.getUniqueID()
        DOM.setAttribute(self.inputElem, "id", uid)
        DOM.setAttribute(self.labelElem, "htmlFor", uid)

    # emulate static
    def getUniqueID(self):
        global _CheckBox_unique_id
        _CheckBox_unique_id += 1
        return _CheckBox_unique_id;

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
            Focus.focus(self.inputElem)
        else:
            Focus.blur(self.inputElem)

    def setHTML(self, html):
        DOM.setInnerHTML(self.labelElem, html)

    def setName(self, name):
        DOM.setAttribute(self.inputElem, "name", name)

    def setTabIndex(self, index):
        Focus.setTabIndex(self.inputElem, index)

    def setText(self, text):
        DOM.setInnerText(self.labelElem, text)

    def onDetach(self):
        self.setChecked(self.isChecked())
        ButtonBase.onDetach(self)

Factory.registerClass('pyjamas.ui.CheckBox', 'CheckBox', CheckBox)

