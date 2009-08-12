from pyjamas import DOM

from pyjamas.ui.Widget import Widget
from pyjamas.ui import Event
from pyjamas.ui import MouseListener
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.ScrollPanel import ScrollPanel
from pyjamas.ui.MenuBar import MenuBar
from pyjamas.ui.Image import Image
from pyjamas.ui.ContextMenuPopupPanel import ContextMenuPopupPanel 

from pyjamas import log

# TODO: these need to go into pyjamas.ui

class ImageMap(Widget):
	""" An imagemap
	"""
	def __init__(self, name):
		self.setElement(DOM.createElement("map"))
		Widget.__init__(self)
		self.setName(name)

	def add(self, widget):
		DOM.appendChild(self.getElement(), widget.getElement())
		widget.setParent(self)
	
	def setName(self, name):
		DOM.setAttribute(self.getElement(), "name", name)

class MapArea(Widget):
    """ An area inside an imagemap
    """
    def __init__(self, shape, coords, href=""):

        self.setElement(DOM.createElement("area"))
        Widget.__init__(self)
        self.clickListeners = []
        self.mouseListeners = []

        self.sinkEvents(Event.ONCLICK | Event.MOUSEEVENTS)
        self.setShape(shape)
        self.setCoords(coords)
        self.setHref(href)

    def addClickListener(self, listener):
        self.clickListeners.append(listener)

    def addMouseListener(self, listener):
        self.mouseListeners.append(listener)

    def onBrowserEvent(self, event):
        type = DOM.eventGetType(event)
        pyjamas.log.writebr(type)
        if type == "click":
            for listener in self.clickListeners:
                if(hasattr(listener, "onClick")):
                    listener.onClick(self)
                else:
                    listener(self)
        elif(type == "mousedown" or type == "mouseup" or type == "mousemove" or type == "mouseover" or type == "mouseout"):
            MouseListener.fireMouseEvent(self.mouseListeners, self, event)

    def setShape(self, shape):
        DOM.setAttribute(self.getElement(), "shape", shape) 

    def setCoords(self, coords):
        DOM.setAttribute(self.getElement(), "coords", coords)

    def setHref(self, href):
        if(href == ""):
            DOM.setAttribute(self.getElement(), "href", None)
        else:
            DOM.setAttribute(self.getElement(), "href", href)

############################################
####### MY ATTEMPT AT USING THIS ###########
############################################

class ClickHandler:

    def __init__(self):
        pass

    def onMouseMove(self, sender, x, y):
        log.writebr("move %d %d" % (x, y))

    def onMouseDown(self, sender, x, y):
        log.writebr("down %d %d" % (x, y))

    def onMouseUp(self, sender, x, y):
        log.writebr("up %d %d" % (x, y))

    def onMouseEnter(self, sender, x, y):
        log.writebr("enter %d %d" % (x, y))
        pass

    def onMouseLeave(self, sender, x, y):
        log.writebr("leave %d %d" % (x, y))
        pass

def dosomething():

    imageClickHandle = ClickHandler()

    img = Image("babykatie_small.jpg")

    imagepanel = ScrollPanel()
    imagepanel.add(img)

    hpanel = HorizontalPanel()

    map = ImageMap("themap")

    hpanel.add(map)
    hpanel.add(imagepanel)

    a1 = MapArea("rect", "0, 0, 100, 100")
    a2 = MapArea("rect", "100, 0, 200, 100")
    a1.addMouseListener(imageClickHandle)
    a1.setHref("http://lkcl.net")
    a1.menu = MenuBar(True)
    a1.menu.addItem("Option 1")
    a1.menu.addItem("Option 2")
    a1.pop = ContextMenuPopupPanel(a1.menu)
    a2.addMouseListener(imageClickHandle)
    a2.menu = MenuBar(True)
    a2.menu.addItem("Option 3")
    a2.menu.addItem("Option 4")
    a2.pop = ContextMenuPopupPanel(a2.menu)
    map.setWidth("300px")
    map.setHeight("300px")
    map.add(a1)
    map.add(a2)
    img.element.setAttribute("usemap", "#themap")
    img.element.setAttribute("ismap", "1")
    img.setWidth("300px")
    img.setHeight("300px")

    return hpanel

