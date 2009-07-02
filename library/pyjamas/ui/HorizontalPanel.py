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

from pyjamas.ui.CellPanel import CellPanel
from pyjamas.ui import HasHorizontalAlignment
from pyjamas.ui import HasVerticalAlignment

class HorizontalPanel(CellPanel):

    def __init__(self):
        CellPanel.__init__(self)

        self.horzAlign = HasHorizontalAlignment.ALIGN_LEFT
        self.vertAlign = HasVerticalAlignment.ALIGN_TOP

        self.tableRow = DOM.createTR()
        DOM.appendChild(self.getBody(), self.tableRow)

        DOM.setAttribute(self.getTable(), "cellSpacing", "0")
        DOM.setAttribute(self.getTable(), "cellPadding", "0")

    def add(self, widget):
        self.insert(widget, self.getWidgetCount())

    def getHorizontalAlignment(self):
        return self.horzAlign

    def getVerticalAlignment(self):
        return self.vertAlign

    def getWidget(self, index):
        return self.children[index]

    def getWidgetCount(self):
        return len(self.children)

    def getWidgetIndex(self, child):
        return self.children.index(child)

    def insert(self, widget, beforeIndex):
        widget.removeFromParent()

        td = DOM.createTD()
        DOM.insertChild(self.tableRow, td, beforeIndex)

        CellPanel.insert(self, widget, td, beforeIndex)

        self.setCellHorizontalAlignment(widget, self.horzAlign)
        self.setCellVerticalAlignment(widget, self.vertAlign)

    def remove(self, widget):
        if isinstance(widget, int):
            widget = self.getWidget(widget)

        if widget.getParent() != self:
            return False

        td = DOM.getParent(widget.getElement())
        DOM.removeChild(self.tableRow, td)

        CellPanel.remove(self, widget)
        return True

    def setHorizontalAlignment(self, align):
        self.horzAlign = align

    def setVerticalAlignment(self, align):
        self.vertAlign = align


