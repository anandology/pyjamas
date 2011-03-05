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

from pyjamas.ui.TextBoxBase import TextBoxBase

class TextBox(TextBoxBase):
    '''
    Use Kind to set a HTML5 type

    Attributes supported:
        Kind
        MaxLength
        Min
        Max
        Placeholder
        Required
        Step
        VisibleLength
    '''

    _props = [("kind", "Kind", "Kind", None),
              ("maxLength", "Max Length", "MaxLength", None),
              ("min", "Min", "Min", None),
              ("max", "Max", "Max", None),
              ("placeholder", "Place Holder", "PlaceHolder", None),
              ("step", "Step", "Step", None),
              ("visibleLength", "Visible Length", "VisibleLength", None),
            ]

    def __init__(self, **ka):
        ka['StyleName'] = ka.get('StyleName', "gwt-TextBox")
        element = ka.pop('Element', None) or DOM.createInputText()
        TextBoxBase.__init__(self, element, **ka)

    @classmethod
    def _getProps(self):
        return TextBoxBase._getProps() + self._props

    def getMaxLength(self):
        return DOM.getIntAttribute(self.getElement(), "maxLength")

    def getKind(self):
        return DOM.getAttribute(self.getElement(), "type")

    def getMin(self):
        return DOM.getAttribute(self.getElement(), "min")

    def getMax(self):
        return DOM.getAttribute(self.getElement(), "max")

    def getPlaceholder(self):
        return DOM.getAttribute(self.getElement(), "placeholder")

    def getStep(self):
        return DOM.getAttribute(self.getElement(), "step")

    def getVisibleLength(self):
        return DOM.getIntAttribute(self.getElement(), "size")

    def setMaxLength(self, length):
        DOM.setIntAttribute(self.getElement(), "maxLength", length)

    def setKind(self, kind):
        DOM.setAttribute(self.getElement(), "type", kind)

    def setMin(self, min):
        DOM.setAttribute(self.getElement(), "min", min)

    def setMax(self, max):
        DOM.setAttribute(self.getElement(), "max", max)

    def setPlaceholder(self, placeholder):
        DOM.setIntAttribute(self.getElement(), "placeholder", placeholder)

    def setStep(self, step):
        DOM.setAttribute(self.getElement(), "step", step)

    def setVisibleLength(self, length):
        DOM.setIntAttribute(self.getElement(), "size", length)


Factory.registerClass('pyjamas.ui.TextBox', 'TextBox', TextBox)

