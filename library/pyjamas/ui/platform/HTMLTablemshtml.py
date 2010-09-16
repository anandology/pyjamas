# Contributed by Phil Charlesworth 2010-09-15
# Copyright (C) 2010 Phil Charlesworth
#
# python-COM returns different objects representing the DOM elements,
# because DCOM returns different objects representing the DOM elements.
# therefore it is necessary to use uniqueID for the hash map.

class HTMLTable(Panel):

    def setWidget(self, row, column, widget):
        self.prepareCell(row, column)
        if widget is None:
            return

        widget.removeFromParent()
        td = self.cleanCell(row, column)
        widget_hash = widget
        element = widget.getElement()
        widgethash[key] = element.uniqueID
        self.widgetMap[widget_hash] = widget
        self.adopt(widget, td)

    def removeWidget(self, widget):
        self.disown(widget)
        element = widget.getElement()
        key = widgetElement.uniqueID
        del self.widgetMap[widgethash.get(key)]
        del widgethash[key]
        return True

    def computeKeyForElement(self, widgetElement):
        return widgethash.get(widgetElement.uniqueID)

