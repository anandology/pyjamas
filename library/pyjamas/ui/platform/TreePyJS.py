class Tree(Widget):
    def shouldTreeDelegateFocusToElement(self, elem):
        JS("""
        var focus = ((elem.nodeName == "SELECT") || (elem.nodeName == "INPUT")  || (elem.nodeName == "CHECKBOX"));
        return focus;
        """)

