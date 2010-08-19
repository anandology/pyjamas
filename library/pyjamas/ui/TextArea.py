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
from __pyjamas__ import JS
from pyjamas import Factory
from pyjamas import DOM

from TextBoxBase import TextBoxBase

class TextArea(TextBoxBase):
    """
    HTML textarea widget, allowing multi-line text entry.
    Use setText/getText to
    get and access the current text.
    """

    _props = [("rows", "Rows", "VisibleLines", None),
             ("cols", "Columns", "CharacterWidth", None),
            ]

    def __init__(self, **ka):
        ka['StyleName'] = ka.get('StyleName', "gwt-TextArea")
        element = ka.pop('Element', None) or DOM.createTextArea()
        TextBoxBase.__init__(self, element, **ka)

    @classmethod
    def _getProps(self):
        return TextBoxBase._getProps() + self._props

    def getCharacterWidth(self):
        return DOM.getIntAttribute(self.getElement(), "cols")

    def getCursorPos(self):
        return TextBoxBase.getCursorPos(self)

    def getVisibleLines(self):
        return DOM.getIntAttribute(self.getElement(), "rows")

    def setCharacterWidth(self, width):
        DOM.setIntAttribute(self.getElement(), "cols", width)

    def setVisibleLines(self, lines):
        DOM.setIntAttribute(self.getElement(), "rows", lines)

Factory.registerClass('pyjamas.ui.TextArea', 'TextArea', TextArea)

