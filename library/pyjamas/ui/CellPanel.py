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

class CellPanel(ComplexPanel):

    def __init__(self):
        ComplexPanel.__init__(self)

        self.table = DOM.createTable()
        self.body = DOM.createTBody()
        self.spacing = None
        self.padding = None
        DOM.appendChild(self.table, self.body)
        self.setElement(self.table)

    def getTable(self):
        return self.table

    def getBody(self):
        return self.body

    def getSpacing(self):
        return self.spacing

    def getPadding(self):
        return self.padding

    def getWidgetTd(self, widget):
        if widget.getParent() != self:
            return None
        return DOM.getParent(widget.getElement())

    def setBorderWidth(self, width):
        DOM.setAttribute(self.table, "border", "%d" % width)

    def setCellHeight(self, widget, height):
        td = DOM.getParent(widget.getElement())
        DOM.setAttribute(td, "height", height)

    def setCellHorizontalAlignment(self, widget, align):
        td = self.getWidgetTd(widget)
        if td is not None:
            DOM.setAttribute(td, "align", align)

    def setCellVerticalAlignment(self, widget, align):
        td = self.getWidgetTd(widget)
        if td is not None:
            DOM.setStyleAttribute(td, "verticalAlign", align)

    def setCellWidth(self, widget, width):
        td = DOM.getParent(widget.getElement())
        DOM.setAttribute(td, "width", width)

    def setSpacing(self, spacing):
        self.spacing = spacing
        DOM.setAttribute(self.table, "cellSpacing", str(spacing))

    def setPadding(self, padding):
        self.padding = padding
        DOM.setAttribute(self.table, "cellPadding", str(padding))


