class HTMLTable(Panel):

    def getDOMCellCountImpl(self, element, row):
        JS("""
        return element.rows[row].cells.length;
        """)

    def getDOMRowCountImpl(self, element):
        JS("""
        return element.rows.length;
        """)

    def setWidget(self, row, column, widget):
        self.prepareCell(row, column)
        if widget == None:
            return

        widget.removeFromParent()
        td = self.cleanCell(row, column)
        widget_hash = hash(widget)
        element = widget.getElement()
        DOM.setAttribute(element, "__hash", widget_hash)
        self.widgetMap[widget_hash] = widget
        self.adopt(widget, td)

    def computeKeyForElement(self, widgetElement):
        return DOM.getElemAttribute(widgetElement, "__hash")

