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

from pyjamas.ui.ComplexPanel import ComplexPanel

global HTMLPanel_sUid 
HTMLPanel_sUid = 0

class HTMLPanel(ComplexPanel):
    def __init__(self, html):
        ComplexPanel.__init__(self)
        self.setElement(DOM.createDiv())
        DOM.setInnerHTML(self.getElement(), html)

    def add(self, widget, id):
        element = self.getElementById(self.getElement(), id)
        if element == None:
            # throw new NoSuchElementException()
            return
        ComplexPanel.add(self, widget, element)

    def createUniqueId(self):
        global HTMLPanel_sUid

        HTMLPanel_sUid += 1
        return "HTMLPanel_" + HTMLPanel_sUid

    def getElementById(self, element, id):
        element_id = DOM.getAttribute(element, "id")
        if element_id != None and element_id == id:
            return element

        child = DOM.getFirstChild(element)
        while child != None:
            ret = self.getElementById(child, id)
            if ret != None:
                return ret
            child = DOM.getNextSibling(child)

        return None


