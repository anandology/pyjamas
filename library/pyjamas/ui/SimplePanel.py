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

from pyjamas.ui.Panel import Panel

class SimplePanel(Panel):
    """
        A panel which contains a single widget.  Useful if you have an area where
        you'd like to be able to replace the widget with another, or if you need to
        wrap something in a DIV.
    """
    def __init__(self, element=None):
        Panel.__init__(self)
        if element == None:
            element = DOM.createDiv()
        self.setElement(element)

    def add(self, widget):
        if self.getWidget() != None:
            console.error("SimplePanel can only contain one child widget")
            return
        self.setWidget(widget)

    def getWidget(self):
        if len(self.children):
            return self.children[0]
        return None

    def remove(self, widget):
        if self.getWidget() != widget:
            return False
        self.disown(widget)
        del self.children[0]
        return True

    def getContainerElement(self):
        return self.getElement()

    def setWidget(self, widget):
        if self.getWidget() == widget:
            return

        if self.getWidget() != None:
            self.remove(self.getWidget())

        if widget != None:
            self.adopt(widget, self.getContainerElement())
            self.children.append(widget)


