""" Control Widgets.  Presently comprises a Vertical Slider Demo.

    Copyright (C) 2008 - Luke Kenneth Casson Leighton <lkcl@lkcl.net>

"""

from pyjamas import DOM
from pyjamas.ui.FocusWidget import FocusWidget
from pyjamas.ui.MouseListener import MouseListener
from pyjamas.ui.Event import Event

class VerticalDemoSlider(FocusWidget):

    def __init__(self, min_value, max_value, start_value=None):

        element = DOM.createDiv()
        FocusWidget.__init__(self, element)

        self.min_value = min_value
        self.max_value = max_value
        if start_value is None:
            start_value = min_value
        self.value = start_value
        self.valuechange_listeners = []
        
        DOM.setStyleAttribute(element, "position", "relative")
        DOM.setStyleAttribute(element, "overflow", "hidden")

        self.handle = DOM.createDiv()
        DOM.appendChild(element, self.handle)

        DOM.setStyleAttribute(self.handle, "border", "1px")
        DOM.setStyleAttribute(self.handle, "width", "100%")
        DOM.setStyleAttribute(self.handle, "height", "10px")
        DOM.setStyleAttribute(self.handle, "backgroundColor", "#808080")

        self.addClickListener(self)

    def onClick(self, sender, event):

        # work out the relative position of cursor
        mouse_y = DOM.eventGetClientY(event) - \
                   DOM.getAbsoluteTop(sender.getElement())
        self.moveSlider(mouse_y)

    def moveSlider(self, mouse_y):

        relative_y = mouse_y - DOM.getAbsoluteTop(self.getElement())
        widget_height = self.getOffsetHeight()

        # limit the position to be in the widget!
        if relative_y < 0:
            relative_y = 0
        height_range = widget_height - 10 # handle height is hard-coded
        if relative_y >= height_range:
            relative_y = height_range

        # move the handle
        DOM.setStyleAttribute(self.handle, "top", "%dpx" % relative_y)
        DOM.setStyleAttribute(self.handle, "position", "absolute")

        val_diff = self.max_value - self.min_value
        new_value = ((val_diff * relative_y) / height_range) + self.min_value
        self.setValue(new_value)

    def setValue(self, new_value):

        old_value = self.value
        self.value = new_value
        for listener in self.valuechange_listeners:
            listener.onControlValueChanged(self, old_value, new_value)

    def addControlValueListener(self, listener):
        self.valuechange_listeners.append(listener)

    def removeControlValueListener(self, listener):
        self.valuechange_listeners.remove(listener)

class VerticalDemoSlider2(VerticalDemoSlider):

    def __init__(self, min_value, max_value, start_value=None):

        VerticalDemoSlider.__init__(self, min_value, max_value, start_value)
        self.mouseListeners = []
        self.addMouseListener(self)
        self.sinkEvents(Event.MOUSEEVENTS)
        self.dragging = False

        DOM.addEventPreview(self)

    def addMouseListener(self, listener):
        self.mouseListeners.append(listener)

    def removeMouseListener(self, listener):
        self.mouseListeners.remove(listener)

    def onBrowserEvent(self, event):
        type = DOM.eventGetType(event)
        if type == "mousedown" or type == "mouseup" or type == "mousemove" or type == "mouseover" or type == "mouseout":
            MouseListener().fireMouseEvent(self.mouseListeners, self, event)
        else:
            VerticalSliderDemo.onBrowserEvent(self, event)

    def onEventPreview(self, event):
        # preventDefault on mousedown events, outside of the
        # dialog, to stop text-selection on dragging
        type = DOM.eventGetType(event)
        if type == 'mousedown':
            target = DOM.eventGetTarget(event)
            event_targets_control = target and DOM.isOrHasChild(self.getElement(), target)
            if event_targets_control:
                DOM.eventPreventDefault(event)
        return VerticalSliderDemo.onEventPreview(self, event)

    def onMouseMove(self, sender, x, y):
        if not self.dragging:
            return
        self.moveSlider(y)
        
    def onMouseDown(self, sender, x, y):
        self.dragging = True
        DOM.setCapture(self.getElement())
        self.moveSlider(y)

    def onMouseUp(self, sender, x, y):
        self.dragging = False
        DOM.releaseCapture(self.getElement())

    def onMouseEnter(self, sender):
        pass
    def onMouseLeave(self, sender):
        pass

