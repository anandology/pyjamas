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
from __pyjamas__ import console
from pyjamas import Factory
from pyjamas import DOM

from Widget import Widget

class Hidden(Widget):

    _props = [("name", "Name", "Name", None),
             ("value", "Value", "Value", None),
             ("defaultValue", "Default Value", "DefaultValue", None),
            ]

    def __init__(self, name=None, value=None, **kwargs):

        name = kwargs.get("Name", name)
        if name is not None:
            kwargs['Name'] = name
        value = kwargs.get("Value", value)
        if value is not None:
            kwargs['Value'] = kwargs.get("Value", value)
        element = kwargs.pop('Element', None) or DOM.createElement("input")
        self.setElement(element)
        DOM.setAttribute(element, "type", "hidden")

        Widget.__init__(self, **kwargs)

    @classmethod
    def _getProps(self):
        return Widget._getProps() + self._props

    def getDefaultValue(self):
        return DOM.getAttribute(self.getElement(), "defaultValue")

    def getName(self):
        return DOM.getAttribute(self.getElement(), "name")

    def getValue(self):
        return DOM.getAttribute(self.getElement(), "value")

    def setDefaultValue(self, defaultValue):
        DOM.setAttribute(self.getElement(), "defaultValue", defaultValue)

    def setName(self, name):
        if name is None:
            raise ValueError("Name cannot be null")
            console.error("Name cannot be null")
        elif len(name) == 0:
            raise ValueError("Name cannot be an empty string.")
            console.error("Name cannot be an empty string.")
        DOM.setAttribute(self.getElement(), "name", name)

    def setValue(self, value):
        DOM.setAttribute(self.getElement(), "value", value)

Factory.registerClass('pyjamas.ui.Hidden', 'Hidden', Hidden)

