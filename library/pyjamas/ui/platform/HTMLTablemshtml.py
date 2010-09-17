# Contributed by Phil Charlesworth 2010-09-15
# Copyright (C) 2010 Phil Charlesworth
#
# python-COM returns different objects representing the DOM elements,
# because DCOM returns different objects representing the DOM elements.
# therefore it is necessary to use uniqueID for the hash map.

class HTMLTable(Panel):

    def computeKeyForElement(self, widgetElement):
        if hasattr(widgetElement,'uniqueID'):
            return widgethash.get(widgetElement.uniqueID)

    def _mapWidget(self, widget):
        widget_hash = widget
        element = widget.getElement()
        widgethash[element.uniqueID] = widget_hash
        self.widgetMap[widget_hash] = widget

    def _unmapWidget(self, widget):
        element = widget.getElement()
        key = element.uniqueID
        del self.widgetMap[widgethash.get(key)]
        del widgethash[key]

