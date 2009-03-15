""" Control Widgets.  Presently comprises a Vertical Slider Demo.

    Copyright (C) 2008 - Luke Kenneth Casson Leighton <lkcl@lkcl.net>

"""

import math
from pyjamas import DOM
from pyjamas.ui.FocusWidget import FocusWidget
from pyjamas.ui.MouseListener import MouseListener
from pyjamas.ui.Event import Event
from pyjamas.ui.Focus import Focus
from pyjamas.ui.KeyboardListener import KeyboardListener

from pyjamas.ui.TextBox import TextBox

from pyjamas.log import writebr

class Control(FocusWidget):

    def __init__(self, element, min_value, max_value,
                       start_value=None, step=None):

        FocusWidget.__init__(self, element)
        self.sinkEvents( Event.FOCUSEVENTS | Event.ONCLICK | Event.MOUSEEVENTS)

        self.min_value = min_value
        self.max_value = max_value
        if start_value is None:
            start_value = min_value
        if step is None:
            step = (self.max_value - self.min_value) / 20
        self.step = step
        self.value = start_value
        self.valuechange_listeners = []
        self.mouseListeners = []
        self.dragging = False
        
        self.setTabIndex(0)

    def onBrowserEvent(self, event):
        type = DOM.eventGetType(event)
        if type == "mousedown" or type == "mouseup" or type == "mousemove" or type == "mouseover" or type == "mouseout":
            MouseListener().fireMouseEvent(self.mouseListeners, self, event)
        else:
            FocusWidget.onBrowserEvent(self, event)

    def onFocus(self, sender):
        pass

    def onLostFocus(self, sender):
        pass

    def onClick(self, sender, event):
        pass

    def processValue(self, value):
        """ rounds and limits the value to acceptable range
        """
        value = math.floor((value - self.min_value) / self.step)
        value = (value * self.step) + self.min_value
        value = max(value, self.min_value)
        value = min(value, self.max_value)
        return value

    def setValue(self, new_value, notify=1):

        old_value = self.value
        self.value = new_value

        if not notify:
            return

        for listener in self.valuechange_listeners:
            listener.onControlValueChanged(self, old_value, new_value)

    def addControlValueListener(self, listener):
        self.valuechange_listeners.append(listener)

    def removeControlValueListener(self, listener):
        self.valuechange_listeners.remove(listener)

    def addMouseListener(self, listener):
        self.mouseListeners.append(listener)

    def removeMouseListener(self, listener):
        self.mouseListeners.remove(listener)

    def moveControl(self, x, y):
        pass

    def onClick(self, sender, event):
        # work out the relative position of cursor
        mouse_x = DOM.eventGetClientX(event) 
        mouse_y = DOM.eventGetClientY(event) 
        self.moveControl(mouse_x - self.getAbsoluteLeft(),
                         mouse_y - self.getAbsoluteTop())

    def onMouseMove(self, sender, x, y):
        if not self.dragging:
            return
        self.moveControl(x, y)
        
    def onLoseFocus(self, sender):
        self.dragging = False
        DOM.releaseCapture(self.getElement())
        VerticalDemoSlider.onLoseFocus(self, sender)

    def onMouseDown(self, sender, x, y):
        self.dragging = True
        DOM.setCapture(self.getElement())
        self.setFocus(True);
        DOM.eventPreventDefault(DOM.eventGetCurrentEvent());
        self.moveControl(x, y)

    def onMouseUp(self, sender, x, y):
        self.dragging = False
        DOM.releaseCapture(self.getElement())

    def onMouseEnter(self, sender):
        pass
    def onMouseLeave(self, sender):
        pass
    def onKeyDown(self, sender, keycode, modifiers):
        pass
    def onKeyUp(self, sender, keycode, modifiers):
        pass

    def onKeyPress(self, sender, keycode, modifiers):
        if keycode == KeyboardListener.KEY_UP:
            new_value = self.processValue(self.value + self.step)
            self.setControlPos(new_value)
            self.setValue(new_value)
        elif keycode == KeyboardListener.KEY_DOWN:
            new_value = self.processValue(self.value - self.step)
            self.setControlPos(new_value)
            self.setValue(new_value)


class VerticalDemoSlider(Control):

    def __init__(self, min_value, max_value, start_value=None, step=None):

        element = DOM.createDiv()
        Control.__init__(self, element, min_value, max_value, start_value, step)

        self.setStyleName("gwt-VerticalSlider")

        DOM.setStyleAttribute(element, "position", "relative")
        DOM.setStyleAttribute(element, "overflow", "hidden")

        self.handle = DOM.createDiv()
        DOM.appendChild(element, self.handle)

        DOM.setStyleAttribute(self.handle, "border", "1px")
        DOM.setStyleAttribute(self.handle, "width", "100%")
        DOM.setStyleAttribute(self.handle, "height", "10px")
        DOM.setStyleAttribute(self.handle, "backgroundColor", "#808080")

        self.addClickListener(self)
        self.addFocusListener(self)

    def onFocus(self, sender):
        self.addStyleName("gwt-VerticalSlider-focussed")

    def onLostFocus(self, sender):
        self.removeStyleName("gwt-VerticalSlider-focussed")

    def moveControl(self, mouse_x, mouse_y):

        handle_height = DOM.getIntAttribute(self.handle, "offsetHeight")
        widget_height = self.getOffsetHeight()
        height_range = widget_height - 10 # handle height is hard-coded
        relative_y = mouse_y - (handle_height / 2)
        if relative_y < 0:
            relative_y = 0
        if relative_y >= height_range:
            relative_y = height_range

        relative_y = height_range - relative_y # turn round (bottom to top)

        val_diff = self.max_value - self.min_value
        new_value = ((val_diff * relative_y) / height_range) + self.min_value
        new_value = self.processValue(new_value)

        self.setControlPos(new_value)
        self.setValue(new_value)

    def setControlPos(self, value):

        widget_height = self.getOffsetHeight()
        height_range = widget_height - 10 # handle height is hard-coded
        val_diff = self.max_value - self.min_value
        relative_y = height_range * (value - self.min_value) / val_diff

        # limit the position to be in the widget!
        if relative_y < 0:
            relative_y = 0
        if relative_y >= height_range:
            relative_y = height_range

        relative_y = height_range - relative_y # turn round (bottom to top)

        # move the handle
        DOM.setStyleAttribute(self.handle, "top", "%dpx" % relative_y)
        DOM.setStyleAttribute(self.handle, "position", "absolute")

class VerticalDemoSlider2(VerticalDemoSlider):

    def __init__(self, min_value, max_value, start_value=None):

        VerticalDemoSlider.__init__(self, min_value, max_value, start_value)
        self.addMouseListener(self)
        self.addKeyboardListener(self)

class InputControl(Control):

    def __init__(self, min_value, max_value, start_value=None, step=None):

        self.input = TextBox()
        self.input.addKeyboardListener(self)
        #element = DOM.createDiv()
        element = self.input.getElement() # YUK!!!
        Control.__init__(self, element, min_value, max_value, start_value, step)

        self.setStyleName("gwt-InputControl")

        self.addClickListener(self)
        self.addFocusListener(self)
        self.addKeyboardListener(self)

    def onFocus(self, sender):
        self.addStyleName("gwt-InputControl-focussed")

    def onLostFocus(self, sender):
        self.removeStyleName("gwt-InputControl-focussed")

    def setControlPos(self, value):

        self.input.setText(value)

    def onKeyPress(self, sender, keycode, modifiers):
        if keycode == KeyboardListener.KEY_ENTER:
            new_value = float(self.input.getText())
            new_value = self.processValue(new_value)
            writebr(new_value)
            self.setControlPos(new_value)
            self.setValue(new_value)
        else:
            Control.onKeyPress(self, sender, keycode, modifiers)


