# Copyright (C) 2009 JJ Kunce (http://code.google.com/u/jjkunce)
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

from ComplexPanel import ComplexPanel
from Widget import Widget
from MouseListener import MouseHandler
from ClickListener import ClickHandler

class ImageMap(ComplexPanel):
    """ An imagemap
    """
    def __init__(self, Name, **kwargs):
        kwargs['Name'] = Name
        self.setElement(DOM.createElement("map"))
        ComplexPanel.__init__(self, **kwargs)

    def add(self, widget):
        self.insert(widget, self.getWidgetCount())

    def insert(self, widget, beforeIndex):
        widget.removeFromParent()
        ComplexPanel.insert(self, widget, self.getElement(), beforeIndex)
    
    def setName(self, name):
        DOM.setAttribute(self.getElement(), "name", name)

class MapArea(Widget, MouseHandler, ClickHandler):
    """ An area inside an imagemap
    """
    def __init__(self, Shape, Coords, **kwargs):
        if not kwargs.has_key('Href'):
            kwargs['Href'] = ""
        kwargs['Shape'] = Shape
        kwargs['Coords'] = Coords
        self.setElement(DOM.createElement("area"))
        Widget.__init__(self, **kwargs)
        MouseHandler.__init__(self, preventDefault=True)
        ClickHandler.__init__(self, preventDefault=True)

    def setShape(self, shape):
        DOM.setAttribute(self.getElement(), "shape", shape) 

    def setCoords(self, coords):
        DOM.setAttribute(self.getElement(), "coords", coords)

    def setHref(self, href):
        DOM.setAttribute(self.getElement(), "href", href)

