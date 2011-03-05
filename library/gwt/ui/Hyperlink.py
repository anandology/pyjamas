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
from pyjamas import History

from pyjamas.ui.Widget import Widget
from pyjamas.ui import Event
from pyjamas.ui.ClickListener import ClickHandler

class Hyperlink(Widget, ClickHandler):

    def __init__(self, text="", asHTML=False, Element=None, **kwargs):

        if Element is None:
            Element = DOM.createDiv()
        self.anchorElem = DOM.createAnchor()
        self.setElement(Element)
        DOM.appendChild(self.getElement(), self.anchorElem)

        if not kwargs.has_key('StyleName'): kwargs['StyleName']="gwt-Hyperlink"
        if text:
            if asHTML:
                kwargs['HTML'] = text
            else:
                kwargs['Text'] = text
        if not kwargs.has_key('TargetHistoryToken'):
            kwargs['TargetHistoryToken'] = None

        Widget.__init__(self, **kwargs)
        ClickHandler.__init__(self)

    def onBrowserEvent(self, event):
        Widget.onBrowserEvent(self, event)
        event_type = DOM.eventGetType(event)
        if event_type == "click":
            DOM.eventPreventDefault(event)
            if self.targetHistoryToken is not None:
                History.newItem(self.targetHistoryToken)

    def getHTML(self):
        return DOM.getInnerHTML(self.anchorElem)

    def setHTML(self, html):
        DOM.setInnerHTML(self.anchorElem, html)

    def getText(self):
        return DOM.getInnerText(self.anchorElem)

    def setText(self, text):
        DOM.setInnerText(self.anchorElem, text)

    def getTargetHistoryToken(self):
        return self.targetHistoryToken

    def setTargetHistoryToken(self, targetHistoryToken):
        self.targetHistoryToken = targetHistoryToken
        if targetHistoryToken is None:
            targetHistoryToken = ''
        DOM.setAttribute(self.anchorElem, "href", "#" + targetHistoryToken)

Factory.registerClass('pyjamas.ui.Hyperlink', 'Hyperlink', Hyperlink)

