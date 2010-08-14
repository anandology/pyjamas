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
from pyjamas.ui.InnerText import InnerText

from Widget import Widget
from MouseListener import MouseHandler
from ClickListener import ClickHandler

class Label(Widget, MouseHandler, ClickHandler, InnerText):

    props = [("label", "Text", "Text", None),
             ("wordwrap", "Word Wrap", "WordWrap", None),
             ("horzAlign", "Horizontal Alignment", "HorizontalAlignment", None),
            ]

    def __init__(self, text=None, wordWrap=True, **kwargs):
        kwargs['StyleName'] = kwargs.get('StyleName', "gwt-Label")
        kwargs['WordWrap'] = kwargs.get('WordWrap', wordWrap)
        kwargs['HorizontalAlignment'] = kwargs.get('HorizontalAlignment', "")
        kwargs['Text'] = kwargs.get("Text", text)
        self.setElement(kwargs.pop('Element', None) or DOM.createDiv())

        Widget.__init__(self, **kwargs)
        MouseHandler.__init__(self)
        ClickHandler.__init__(self)

    def _getProps(self):
        return Widget.props + self.props

    def getHorizontalAlignment(self):
        return self.horzAlign

    def getWordWrap(self):
        ws = DOM.getStyleAttribute(self.getElement(), "whiteSpace")
        return ws != "nowrap"

    def setHorizontalAlignment(self, align):
        self.horzAlign = align
        DOM.setStyleAttribute(self.getElement(), "textAlign", align)

    def setWordWrap(self, wrap):
        style = wrap and "normal" or "nowrap"
        DOM.setStyleAttribute(self.getElement(), "whiteSpace", style)

Factory.registerClass('pyjamas.ui.Label', Label)

