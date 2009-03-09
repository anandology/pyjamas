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

from pyjamas.ui.Widget import Widget

class DefaultHeader(Widget):
    def __init__(self, text, disclosurePanel):
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

    def getText(self):
        return DOM.getInnerText(self.labelTD)

    def setText(self, text):
        DOM.setInnerText(self.labelTD, text)

    def updateState(self):
        if self.disclosurePanel.getOpen():
            DOM.setAttribute(self.imgElem, "src", self.imageBase + "disclosurePanelOpen.png")
        else:
            DOM.setAttribute(self.imgElem, "src", self.imageBase + "disclosurePanelClosed.png")
        

