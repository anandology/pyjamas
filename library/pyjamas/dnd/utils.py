from __pyjamas__ import wnd, doc
from pyjamas.ui.Widget import Widget
from pyjamas import DOM

def isIn(element, x, y):
    """
    Given an element and an absolute x and y, return True if the
    (x,y) coordinate is within the element. Otherwise, return False.
    """
    top = DOM.getAbsoluteTop(element)
    height = DOM.getIntAttribute(element, 'offsetHeight')
    if y >= top and y <= top + height:
        left = DOM.getAbsoluteLeft(element)
        width = DOM.getIntAttribute(element, 'offsetWidth')
        if x >= left and x <= left + width:
            return True
    return False


def isCanceled(event):
    """
    Has the DragEvent been canceled?
    Coding this package was much easier with this function.
    """
    return not event.returnValue

def findDraggable(element, x, y):
    """
    Find the element within a widget's main element that is
    draggable and under the mouse cursor. We need this for event delegation.

    """
    for elt in DOM.IterWalkChildren(element):
        try:
            draggable = elt.draggable
        except:
            draggable = False
        if draggable:
            if isIn(elt, x, y):
                return elt
    return None

def cloneElement(element):
    clone = element.cloneNode(True)
#    if not element.tagName.lower() == 'canvas':
#        copyStyles(element, clone)
    return clone

def getComputedStyle(element, style=None):
    """
    Get computed style of an element, like in
    http://efreedom.com/Question/1-1848445/Duplicating-Element-Style-JavaScript
    """
    element_style = doc().defaultView.getComputedStyle(element, None)
    #element_style = doc().defaultView.getComputedStyle(element, None)
    if style:
        return element_style[style]
    return element_style

def copyStyles(elem1, elem2):
    """
    Copy styles from one element to another, like in
    http://efreedom.com/Question/1-1848445/Duplicating-Element-Style-JavaScript
    """
    element_style = getComputedStyle(elem1)
    if element_style:
        element_style = dict(element_style)
    else:
        return
    for style in element_style:
        try:
            value = element_style[style]
            if isinstance(value, str):
                if not style == 'cssText':
                    DOM.setStyleAttribute(elem2, style, value)
                    if value == 'font':
                        DOM.setStyleAttribute(elem2, 'fontSize',
                            DOM.getStyleAttribute(elem1, 'fontSize'))
        except:
            pass

def getTargetInChildren(element, x, y):
    """
    x and y are absolute coordinates within the document.
    Return the last child of element that contains (x,y).
    Return None if not found.
    """
    return_elt = None
    for elt in DOM.IterWalkChildren(element):
        hit = isIn(elt, x, y)
        if hit:
            return_elt = elt
    return return_elt

def getElementUnderMouse(widget, x,y):
        """
        Return the most specific element in widget that contains (x,y).
        """
        element = widget.getElement()
        hit = isIn(element, x, y)
        if hit:
            child_elem = getTargetInChildren(element, x, y)
            if child_elem:
                return child_elem
            return element
        return None

def eventCoordinates(event):
    """ Get the absolute coordinates of a mouse event.
    http://www.quirksmode.org/js/events_properties.html#position
    """
    return event.pageX, event.pageY

def getScrollOffsets():
    # this is only needed in ie
    pass



class DraggingWidget(Widget):
    """
    A widget for holding the dragging feedback elements.
    """
    def __init__(self, element=None):
        Widget.__init__(self, Element=DOM.createElement('div'))
        self.children = []
        if element is not None:
            clone = cloneElement(element)
            self.addChild(clone)
        self.setStyleAttribute('position', 'absolute')

    def addChild(self, element):
        DOM.appendChild(self.getElement(),element)
        self.children.append(element)

    def setImage(self,element):
        container = self.getElement()
        clone = cloneElement(element)
        while self.children:
            child = self.children.pop()
            DOM.removeChild(container, child)
        self.addChild(clone)

    def addElement(self, element):
        clone = cloneElement(element)
        self.addChild(clone)

    def updateCursor(self, operation):
        # TODO: change cursors.  Probably means making custom cursors.
        if operation == 'copy':
            pass
        elif operation == 'link':
            pass
        elif operation == 'move':
            pass
        else:
            self.setStyleAttribute('cursor', 'auto')

class DOMStringList(object):
    """
DOMStringList implementation
http://www.w3.org/TR/2003/WD-DOM-Level-3-Core-20030226/core.html#DOMStringList
    """
    def __init__(self, iterable=None):
        self._data = []
        if iterable:
            for item in iterable:
                self._data.append(str(item))

    def _getLength(self):
        return len(self._data)

    length = property(_getLength)

    def item(self, index):
        try:
            return self._data[index]
        except:
            return None
    def __str__(self):
        return str(self._data)

class Uri_list(object):
    """
    text/uri-list implementation

    see http://www.rfc-editor.org/rfc/rfc2483.txt
    """
    def __init__(self, data=None):
        self._data = []
        if data:
            # presume crlf-delimited data
            for item in data.split('\r\n'):
                self._data.append(item.strip())

    def add_url(self, url):
        self._data.append(url)

    def get_first_url(self):
        for item in self._data:
            if item[0] != '#':
                return item
        return ''

    def __str__(self):
        if self._data:
            return '\r\n'.join(self._data) + '\r\n'
        return ''