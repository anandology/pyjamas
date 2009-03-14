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
from __pyjamas__ import JS, console

from pyjamas.ui.Composite import Composite

class DisclosurePanel(Composite):
    def __init__(self, headerText, isOpen):
        self.mainPanel = VerticalPanel()
        self.header = ClickableHeader(self)
        self.contentWrapper = SimplePanel()
        self.mainPanel.add(self.header)
        self.mainPanel.add(self.contentWrapper)
        self.isOpen = isOpen
        self.headerObj = DefaultHeader(headerText, self)
        self.setHeader(self.headerObj)
        self.setContentDisplay()
        self.initWidget(self.mainPanel)

    def add(self, widget):
        if self.getContent() is None:
            self.setContent(widget)

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

        self.content = widget
        if self.content is not None:
            self.contentWrapper.setWidget(self.content)

    def setHeader(self, widget):
        self.header.setWidget(widget)

    def setOpen(self, isOpen):
        if self.isOpen != isOpen:
            self.isOpen = isOpen
        self.setContentDisplay()

    def setContentDisplay(self):
        self.contentWrapper.setVisible(self.isOpen)
        self.headerObj.updateState()


