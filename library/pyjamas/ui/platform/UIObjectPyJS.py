class UIObject:

    def isVisible(self, element=None):
        """Determine whether this element is currently visible, by checking the CSS
        property 'display'"""
        if not element:
            element = self.element
        return element.style.display != "none"

