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

from Widget import Widget
from MouseListener import MouseHandler
from ClickListener import ClickHandler

class Label(Widget, MouseHandler, ClickHandler):

    def __init__(self, text=None, wordWrap=True, **kwargs):
        if not kwargs.has_key('StyleName'): kwargs['StyleName']="gwt-Label"
        if text: kwargs['Text'] = text
        kwargs['WordWrap'] = wordWrap
        self.setElement(DOM.createDiv())
        self.horzAlign = ""

        Widget.__init__(self, **kwargs)
        MouseHandler.__init__(self)
        ClickHandler.__init__(self)

    def getHorizontalAlignment(self):
        return self.horzAlign

    def getText(self):
        return DOM.getInnerText(self.getElement())

    def getWordWrap(self):
        return not (DOM.getStyleAttribute(self.getElement(), "whiteSpace") == "nowrap")

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

Factory.registerClass('pyjamas.ui.Label', Label)

