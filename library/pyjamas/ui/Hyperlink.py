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
from pyjamas import History

from pyjamas.ui.Widget import Widget
from pyjamas.ui import Event

class Hyperlink(Widget):

    def __init__(self, text="", asHTML=False, targetHistoryToken="",
                       usediv=True, **kwargs):
        self.clickListeners = []
        self.targetHistoryToken = ""

        self.nodiv = nodiv
        self.anchorElem = DOM.createAnchor()
        if self.nodiv:
            self.setElement(self.anchorElem)
        else:
            self.setElement(DOM.createDiv())
            DOM.appendChild(self.getElement(), self.anchorElem)

        if not kwargs.has_key('StyleName'): kwargs['StyleName']="gwt-Hyperlink"
        if text:
            if asHTML:
                kwargs['HTML'] = text
            else:
                kwargs['Text'] = text
        if targetHistoryToken:
            kwargs['TargetHistoryToken'] = targetHistoryToken

        Widget.__init__(self, **kwargs)
        self.sinkEvents(Event.ONCLICK)

    def addClickListener(self, listener):
        self.clickListeners.append(listener)

    def getHTML(self):
        return DOM.getInnerHTML(self.anchorElem)

    def getTargetHistoryToken(self):
        return self.targetHistoryToken

    def getText(self):
        return DOM.getInnerText(self.anchorElem)

    def onBrowserEvent(self, event):
        if DOM.eventGetType(event) == "click":
            for listener in self.clickListeners:
                if hasattr(listener, 'onClick'): listener.onClick(self)
                else: listener(self)
            History.newItem(self.targetHistoryToken)
            DOM.eventPreventDefault(event)

    def removeClickListener(self, listener):
        self.clickListeners.remove(listener)

    def setHTML(self, html):
        DOM.setInnerHTML(self.anchorElem, html)

    def setTargetHistoryToken(self, targetHistoryToken):
        self.targetHistoryToken = targetHistoryToken
        DOM.setAttribute(self.anchorElem, "href", "#" + targetHistoryToken)

    def setText(self, text):
        DOM.setInnerText(self.anchorElem, text)


