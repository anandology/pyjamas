# Canvas wrapper component for Pyjamas
# Ported by Willie Gollino from Canvas component for GWT - Originally by Alexei Sokolov http://gwt.components.googlepages.com/
#
# Canvas API reference:
# http://developer.apple.com/documentation/AppleApplications/Reference/SafariJSRef/Classes/Canvas.html#//apple_ref/js/Canvas.clearRect
#
# Usage Notes:
#   - IE support requires ExplorerCanvas from excanvas.sourceforge.net
#   - place excanvas.js in your apps public folder
#   - add this to your MainModule.html: <!--[if IE]><script src="excanvas.js" type="text/javascript"></script><![endif]-->

from pyjamas import DOM
from pyjamas.ui.Image import Image
from pyjamas.ui.Widget import Widget
from pyjamas.ui import Event
from pyjamas.ui import MouseListener
from pyjamas.ui import KeyboardListener
from pyjamas.ui import Focus
from pyjamas.ui import FocusListener

from __pyjamas__ import JS

class Canvas(Widget):
    def __init__(self, width=0, height=0):
        Widget.__init__(self)
        self.context = None
        
        self.setElement(DOM.createDiv())
        canvas = DOM.createElement("canvas")
        self.setWidth(width)
        self.setHeight(height)
        
        canvas.width=width
        canvas.height=height
        
        DOM.appendChild(self.getElement(), canvas)
        self.setStyleName("gwt-Canvas")
        
        self.init()
        
        self.context.fillStyle = "black"
        self.context.strokeStyle = "black"

        self.focusable = None
        self.focusable = Focus.createFocusable()
        
        self.focusListeners = []
        self.clickListeners = []
        self.mouseListeners = []
        self.keyboardListeners = []
        
        DOM.appendChild(self.getElement(), self.focusable)
        DOM.sinkEvents(canvas, Event.ONCLICK | Event.MOUSEEVENTS | DOM.getEventsSunk(canvas))
        DOM.sinkEvents(self.focusable, Event.FOCUSEVENTS | Event.KEYEVENTS)

    def addClickListener(self, listener):
        self.clickListeners.append(listener)

    def addMouseListener(self, listener):
        self.mouseListeners.append(listener)

    def addFocusListener(self, listener):
        self.focusListeners.append(listener)

    def addKeyboardListener(self, listener):
        self.keyboardListeners.append(listener)

    def onBrowserEvent(self, event):
        type = DOM.eventGetType(event)
        #print "Label onBrowserEvent", type, self.clickListeners
        if type == "click":
            for listener in self.clickListeners:
                if hasattr(listener, 'onClick'): listener.onClick(self)
                else: listener(self, event)
        elif type in MouseListener.MOUSE_EVENTS:
            MouseListener.fireMouseEvent(self.mouseListeners, self, event)
        elif type in FocusListener.FOCUS_EVENTS:
            FocusListener.fireFocusEvent(self.focusListeners, self, event)
        elif KeyboardListener.KEYBOARD_EVENTS:
            KeyboardListener.fireKeyboardEvent(self.keyboardListeners, self,                                                   event)

    def removeClickListener(self, listener):
        self.clickListeners.remove(listener)

    def removeMouseListener(self, listener):
        self.mouseListeners.remove(listener)

    def removeFocusListener(self, listener):
        self.focusListeners.remove(listener)

    def removeKeyboardListener(self, listener):
        self.keyboardListeners.remove(listener)

    def setFocus(self, focused):
        if (focused):
            Focus.focus(self.focusable)
        else:
            Focus.blur(self.focusable)

    def getContext(self):
        return self.context

    def isEmulation(self):
        return False

    def init(self):
        el = self.getElement().firstChild
        ctx = el.getContext("2d")
        
        """
        ctx._createPattern = ctx.createPattern
        ctx.createPattern = function(img, rep) {
            if (!(img instanceof Image)) img = img.getElement(); 
            return self._createPattern(img, rep)
            }

        ctx._drawImage = ctx.drawImage
        ctx.drawImage = function() {
            var a=arguments
            if (!(a[0] instanceof Image)) a[0] = a[0].getElement()
            if (a.length==9) return self._drawImage(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8])
            else if (a.length==5) return self._drawImage(a[0], a[1], a[2], a[3], a[4])
            return self._drawImage(a[0], a[1], a[2])
            }
        """
        self.context = ctx

class CanvasImage(Image):
    def __init__(self, url="", load_listener = None):
        Image.__init__(self, url)
        if load_listener:
            self.addLoadListener(load_listener)     
        self.onAttach()

    def isLoaded(self):
        return self.getElement().complete


class ImageLoadListener:
    def __init__(self, listener = None):
        self.wait_list = []
        self.loadListeners = []
        
        if listener:
            self.addLoadListener(listener)  

    def add(self, sender):
        self.wait_list.append(sender)
        sender.addLoadListener(self)
    
    def addLoadListener(self, listener):
        self.loadListeners.append(listener)

    def isLoaded(self):
        if len(self.wait_list):
            return False
        return True

    def onError(self, sender):
        for listener in self.loadListeners:
            listener.onError(sender)
        
    def onLoad(self, sender):
        self.wait_list.remove(sender)
        
        if self.isLoaded():
            for listener in self.loadListeners:
                listener.onLoad(self)
