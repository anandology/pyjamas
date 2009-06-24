class TreeItem(UIObject):

    def __init__Impl(self, html):

        DOM.setAttribute(self.getElement(), "position", "relative")
        DOM.setStyleAttribute(self.contentElem, "display", "inline")
        DOM.setStyleAttribute(self.getElement(), "whiteSpace", "nowrap")
        DOM.setAttribute(self.itemTable, "whiteSpace", "nowrap")
        DOM.setStyleAttribute(self.childSpanElem, "whiteSpace", "nowrap")
        self.setStyleName(self.contentElem, "gwt-TreeItem", True)

        if html != None:
            if pyjslib.isString(html):
                self.setHTML(html)
            else:
                self.setWidget(html)


