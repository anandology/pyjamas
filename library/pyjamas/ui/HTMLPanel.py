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

HTMLPanel_sUid = 0

class HTMLPanel(ComplexPanel):
    def __init__(self, html, **kwargs):
        # NOTE! don't set a default style on this panel, because the
        # HTML might expect to have one already.
        #if not kwargs.has_key('StyleName'): kwargs['StyleName']="gwt-HTMLPanel"
        if html: kwargs['HTML'] = html

        self.setElement(DOM.createDiv())
        ComplexPanel.__init__(self, **kwargs)

    def setHTML(self, html):
        DOM.setInnerHTML(self.getElement(), html)

    def add(self, widget, id):
        element = self.getElementById(self.getElement(), id)
        if element is None:
            # throw new NoSuchElementException()
            return
        ComplexPanel.add(self, widget, element)

    @staticmethod
    def createUniqueId():
        global HTMLPanel_sUid

        HTMLPanel_sUid += 1
        return "HTMLPanel_%d" % HTMLPanel_sUid

    def getElementById(self, element, id):
        element_id = DOM.getAttribute(element, "id")
        if element_id is not None and element_id == id:
            return element

        child = DOM.getFirstChild(element)
        while child is not None:
            ret = self.getElementById(child, id)
            if ret is not None:
                return ret
            child = DOM.getNextSibling(child)

        return None


