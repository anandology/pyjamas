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
from Composite import Composite
import Factory
from Widget import Widget
from SimplePanel import SimplePanel
from VerticalPanel import VerticalPanel 
from pyjamas.ui import Event
from pyjamas import DOM
import pygwt

class ClickableHeader(SimplePanel):
    def __init__(self, disclosurePanel):
        SimplePanel.__init__(self, DOM.createAnchor())
        self.disclosurePanel = disclosurePanel
        element = self.getElement()
        DOM.setAttribute(element, "href", "javascript:void(0);");
        DOM.setStyleAttribute(element, "display", "block")
        self.sinkEvents(Event.ONCLICK)
        self.setStyleName("header")

    def onBrowserEvent(self, event):
        type = DOM.eventGetType(event)
        if type == "click":
            DOM.eventPreventDefault(event)
            newstate = not self.disclosurePanel.getOpen()
            self.disclosurePanel.setOpen(newstate)

Factory.registerClass('pyjamas.ui.ClickableHeader', ClickableHeader)

class DefaultHeader(Widget):
    def __init__(self, text, disclosurePanel):
        Widget.__init__(self)
        self.disclosurePanel = disclosurePanel
        self.imageBase = pygwt.getModuleBaseURL()

        self.root = DOM.createTable()
        self.tbody = DOM.createTBody()
        self.tr = DOM.createTR()
        self.imageTD = DOM.createTD()
        self.labelTD = DOM.createTD()
        self.imgElem = DOM.createImg()

        self.updateState()

        self.setElement(self.root)
        DOM.appendChild(self.root, self.tbody)
        DOM.appendChild(self.tbody, self.tr)
        DOM.appendChild(self.tr, self.imageTD)
        DOM.appendChild(self.tr, self.labelTD)
        DOM.appendChild(self.imageTD, self.imgElem)

        self.setText(text)

        disclosurePanel.addEventHandler(self)
        self.updateState()

    def getText(self):
        return DOM.getInnerText(self.labelTD)

    def setText(self, text):
        DOM.setInnerText(self.labelTD, text)

    def onOpen(self, panel):
        self.updateState()

    def onClose(self, panel):
        self.updateState()

    def updateState(self):
        if self.disclosurePanel.getOpen():
            DOM.setAttribute(self.imgElem, "src",
                             self.imageBase + "disclosurePanelOpen.png")
        else:
            DOM.setAttribute(self.imgElem, "src",
                             self.imageBase + "disclosurePanelClosed.png")
        

Factory.registerClass('pyjamas.ui.DefaultHeader', DefaultHeader)

class DisclosurePanel(Composite):

    def __init__(self, headerText, isOpen=False, **kwargs):

        self.handlers = []
        self.content = None

        self.mainPanel = VerticalPanel()

        self.header = ClickableHeader(self)
        self.contentWrapper = SimplePanel()
        self.mainPanel.add(self.header)
        self.mainPanel.add(self.contentWrapper)
        DOM.setStyleAttribute(self.contentWrapper.getElement(),
                              "padding", "0px");
        DOM.setStyleAttribute(self.contentWrapper.getElement(),
                              "overflow", "hidden");

        self.isOpen = isOpen

        self.headerObj = DefaultHeader(headerText, self)
        self.setHeader(self.headerObj)

        if not kwargs.has_key('StyleName'): kwargs['StyleName']="gwt-DisclosurePanel"
        Composite.__init__(self, self.mainPanel, **kwargs)

        self.setContentDisplay()

    def add(self, widget):
        if self.getContent() is None:
            self.setContent(widget)

    def addEventHandler(self, handler):
        self.handlers.append(handler)

    def removeEventHandler(self, handler):
        self.handlers.remove(handler)

    def clear(self):
        self.setContent(None)

    def getContent(self):
        return self.content

    def getHeader(self):
        return self.header.getWidget()

    def getOpen(self):
        return self.isOpen

    def remove(self, widget):
        if widget == self.getContent():
            self.setContent(None)
            return True
        return False

    def setContent(self, widget):
        if self.content is not None:
            self.contentWrapper.setWidget(None)
            self.content.removeStyleName("content")

        self.content = widget
        if self.content is not None:
            self.contentWrapper.setWidget(self.content)
            self.content.addStyleName("content")
            self.setContentDisplay()

    def setHeader(self, widget):
        self.header.setWidget(widget)

    def setOpen(self, isOpen):
        if self.isOpen == isOpen:
            return
        self.isOpen = isOpen
        self.setContentDisplay()
        self.fireEvent()

    def fireEvent(self):
        for handler in self.handlers:
            if self.isOpen:
                handler.onOpen(self)
            else:
                handler.onClose(self)

    def setContentDisplay(self):
        if self.isOpen:
            self.addStyleName("open")
            self.removeStyleName("closed")
        else:
            self.addStyleName("closed")
            self.removeStyleName("open")
        self.contentWrapper.setVisible(self.isOpen)

Factory.registerClass('pyjamas.ui.DisclosurePanel', DisclosurePanel)

