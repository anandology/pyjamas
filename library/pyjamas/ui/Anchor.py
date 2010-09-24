""" Anchor Widget, use this to create the equivalent of the <a></a> tag.

Copyright(C) 2010, Martin Hellwig
Copyright(C) 2010, Luke Leighton <lkcl@lkcl.net>

License: Apache Software Foundation v2

Here is an example for using it with an image:
---------------------------------------------------------
if __name__ == '__main__':
    from pyjamas.ui.RootPanel import RootPanel
    from pyjamas.ui.Image import Image
    root = RootPanel()
    image_url = "http://www.dcuktec.com/static/images/logo.png"
    image = Image(image_url)
    anchor = Anchor()
    anchor.add(image)
    anchor.href.set('http://www.dcuktec.com')
    root.add(anchor)
---------------------------------------------------------
"""

from pyjamas import DOM
from pyjamas.ui.Widget import Widget
from ClickListener import ClickHandler

class _Attribute(object):
    "Attribute definition class with method set and remove"
    def __init__(self, element, attribute, 
                 attribute_type=None, type_restriction=None):
        self.element = element
        self.attribute = attribute
        self._type = attribute_type
        self._restriction = type_restriction
        
    def get(self):
        "Get the value"
        return DOM.getAttribute(self.element, self.attribute)
        
    def set(self, value):
        "Set the value"
        DOM.setAttribute(self.element, self.attribute, value)
        
    def remove(self):
        "Remove the attribute from the element" 
        DOM.removeAttribute(self.element, self.attribute)
        
class _Attributes(object):
    "Attribute container class"
    def __init__(self, element):
        self.name = _Attribute(element, 'name', 'cdata', 'cs')
        self.href = _Attribute(element, 'href', 'uri', 'ct')
        self.hreflang = _Attribute(element, 'hreflang', 'langcode', 'ci')
        self.type = _Attribute(element, 'type', 'content-type', 'ci')
        self.rel = _Attribute(element, 'rel', 'link-types' ,'ci')
        self.rev = _Attribute(element, 'rev', 'link-types', 'ci')
        self.charset = _Attribute(element, 'charset', 'charset', 'ci')
        self.target = _Attribute(element, 'target', 'target', 'ci')
        
class Anchor(Widget, ClickHandler, _Attributes):
    """Anchor attribute, use this to create the equivalent of the <a></a> tag.
    The attributes: name, href. hreflang, type, rel, rev, charset are in the
    namespace of the Anchor instance.
    These attributes themselves have the functions 'set' and 'remove'
    For example:
    anchor = Anchor()
    anchor.href.set('http://www.dcuktec.com')
    """
    def __init__(self, **kwargs):
        element = kwargs.pop('Element', None) or DOM.createAnchor()
        kwargs['StyleName'] = kwargs.pop('StyleName', 'gwt-Anchor')
        _Attributes.__init__(self, element)
        self.setElement(element)
        self.widget = None
        Widget.__init__(self, **kwargs)
        ClickHandler.__init__(self)
        
    def setWidget(self, widget):
        """ Add child widget
        """
        widget.removeFromParent()
        widget.setParent(self)
        self.widget = widget
        DOM.appendChild(self.getElement(), widget.getElement())
        
    def removeWidget(self):
        """ remove child widget
        """
        self.widget.removeFromParent()
        DOM.removeChild(self.getElement(), self.widget.getElement())
        self.widget = None

