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
from pyjamas import DOM
from pyjamas import Factory

from ComplexPanel import ComplexPanel
from pyjamas.ui import HasHorizontalAlignment
from pyjamas.ui import HasVerticalAlignment


class CellPanel(ComplexPanel):

    props = [("horzAlign", "Horizontal alignment", "HorizontalAlignment", None),
              ("vertAlign", "Vertical alignment", "VerticalAlignment", None),
              ("border", "Border width", "BorderWidth", int),
              ("spacing", "Spacing", "Spacing", None),
              ("padding", "Padding", "Padding", None)
             ]

    def __init__(self, **kwargs):

        kwargs['Spacing'] = kwargs.get('Spacing', 0)
        kwargs['Padding'] = kwargs.get('Padding', 0)
        kwargs['HorizontalAlignment'] = kwargs.get('HorizontalAlignment',
                            HasHorizontalAlignment.ALIGN_LEFT)
        kwargs['VerticalAlignment'] = kwargs.get('VerticalAlignment',
                            HasVerticalAlignment.ALIGN_TOP)

        element = None
        if kwargs.has_key('Element'):
            element = kwargs.pop('Element')
        if element is None:
            element = DOM.createTable()
        self.table = element
        self.setElement(self.table)
        self.body = DOM.createTBody()
        DOM.appendChild(self.table, self.body)

        ComplexPanel.__init__(self, **kwargs)

    @classmethod
    def _getProps(self):
        return ComplexPanel._getProps() + self._props

    def getTable(self):
        return self.table

    def getBody(self):
        return self.body

    def getBorderWidth(self):
        return DOM.getAttribute(self.table, "border")

    def getCellHeight(self, widget):
        td = DOM.getParent(widget.getElement())
        return DOM.getAttribute(td, "height")

    def getCellWidth(self, widget):
        td = DOM.getParent(widget.getElement())
        return DOM.getAttribute(td, "width")

    def getSpacing(self):
        return self.spacing

    def getPadding(self):
        return self.padding

    def getCellHorizontalAlignment(self, widget):
        td = self.getWidgetTd(widget)
        if td is None:
            return None
        return DOM.getAttribute(td, "align")

    def getCellVerticalAlignment(self, widget):
        td = self.getWidgetTd(widget)
        if td is None:
            return None
        return DOM.getStyleAttribute(td, "verticalAlign")

    def getWidgetTd(self, widget):
        if widget.getParent() != self:
            return None
        return DOM.getParent(widget.getElement())

    def setBorderWidth(self, width):
        if width is None or width == "":
            DOM.removeAttribute(self.table, "border")
        else:
            DOM.setAttribute(self.table, "border", "%d" % width)

    def setCellHeight(self, widget, height):
        td = DOM.getParent(widget.getElement())
        if height is None:
            DOM.removeAttribute(td, "height")
        else:
            DOM.setAttribute(td, "height", height)

    def setCellHorizontalAlignment(self, widget, align):
        td = self.getWidgetTd(widget)
        if td is not None:
            if align is None:
                DOM.removeAttribute(td, "align")
            else:
                DOM.setAttribute(td, "align", align)

    def setCellVerticalAlignment(self, widget, align):
        td = self.getWidgetTd(widget)
        if td is not None:
            if align is None:
                DOM.setStyleAttribute(td, "verticalAlign", "")
            else:
                DOM.setStyleAttribute(td, "verticalAlign", align)

    def setCellWidth(self, widget, width):
        td = DOM.getParent(widget.getElement())
        if width is None:
            DOM.removeAttribute(td, "width")
        else:
            DOM.setAttribute(td, "width", width)

    def setSpacing(self, spacing):
        self.spacing = spacing
        if spacing is None:
            DOM.removeAttribute(self.table, "cellSpacing")
        else:
            DOM.setAttribute(self.table, "cellSpacing", str(spacing))

    def setPadding(self, padding):
        self.padding = padding
        if padding is None:
            DOM.removeAttribute(self.table, "cellPadding")
        else:
            DOM.setAttribute(self.table, "cellPadding", str(padding))

    def setHorizontalAlignment(self, align):
        self.horzAlign = align

    def setVerticalAlignment(self, align):
        self.vertAlign = align

    def getHorizontalAlignment(self):
        return self.horzAlign

    def getVerticalAlignment(self):
        return self.vertAlign


Factory.registerClass('pyjamas.ui.CellPanel', CellPanel)

