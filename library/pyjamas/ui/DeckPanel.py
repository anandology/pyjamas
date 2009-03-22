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

class DeckPanel(ComplexPanel):
    def __init__(self):
        ComplexPanel.__init__(self)
        self.visibleWidget = None
        self.setElement(DOM.createDiv())

    def add(self, widget):
        self.insert(widget, self.getWidgetCount())

    def getVisibleWidget(self):
        return self.getWidgetIndex(self.visibleWidget)

    def getWidget(self, index):
        return self.children[index]

    def getWidgetCount(self):
        return len(self.children)

    def getWidgetIndex(self, child):
        return self.children.index(child)

    def insert(self, widget, beforeIndex=None):
        if (beforeIndex < 0) or (beforeIndex > self.getWidgetCount()):
            # throw new IndexOutOfBoundsException();
            return

        ComplexPanel.insert(self, widget, self.getElement(), beforeIndex)

        child = widget.getElement()
        DOM.setStyleAttribute(child, "width", "100%")
        DOM.setStyleAttribute(child, "height", "100%")
        widget.setVisible(False)

    def remove(self, widget):
        if pyjslib.isNumber(widget):
            widget = self.getWidget(widget)

        if not ComplexPanel.remove(self, widget):
            return False

        if self.visibleWidget == widget:
            self.visibleWidget = None

        return True

    def showWidget(self, index):
        self.checkIndex(index)

        if self.visibleWidget != None:
            self.visibleWidget.setVisible(False)

        self.visibleWidget = self.getWidget(index)
        self.visibleWidget.setVisible(True)

    def checkIndex(self, index):
        if (index < 0) or (index >= self.getWidgetCount()):
            # throw new IndexOutOfBoundsException();
            pass


