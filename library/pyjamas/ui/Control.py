""" Control Widgets.  Presently comprises a Vertical Slider Demo and derivatives.

    HorizontalDemoSlider and HorizontalDemoSlider2 added by Bill Winder
    AreaDemoSlider and AreaDemoSlider2 added by Bill Winder

    Copyright (C) 2008, 2009, 2010 Luke Kenneth Casson Leighton <lkcl@lkcl.net>
    Copyright (C) 2010 - Cedric Gestes <gestes@aldebaran-robotics.com>
    Copyright (C) 2009, 2010 - Bill Winder <wgwinder@gmail.com>


    To do: All controls with draggable=True do not fire the OnFocus methon on single click.
    the control does not activate the OnFocus method. Clicking the handle does fire OnFocus, however.

"""

from pyjamas import Factory
import math
from pyjamas import DOM
from pyjamas import Window
from FocusWidget import FocusWidget
from MouseListener import MouseHandler, MouseWheelHandler
from pyjamas.ui import KeyboardListener
from pyjamas.ui import GlassWidget


class Control(FocusWidget, MouseHandler, MouseWheelHandler):

    def __init__(self, element, min_value, max_value,
                       start_value=None, step=None,
                       **kwargs):

        self.min_value = min_value
        self.max_value = max_value
        if start_value is None:
            start_value = min_value
        if step is None:
            step = (self.max_value - self.min_value) / 20
        self.step = step
        self.value = start_value
        self.valuechange_listeners = []
        self.dragging = False
        self.drag_enabled = False

        if not kwargs.has_key("TabIndex"): kwargs['TabIndex'] = 0
        FocusWidget.__init__(self, element, **kwargs)
        MouseHandler.__init__(self)
        MouseWheelHandler.__init__(self, True)
        self.addMouseWheelListener(self)

    def isDragable(self):
        return self.drag_enabled

    def setDragable(self, dragable):
        if self.drag_enabled == dragable:
            return
        if self.drag_enabled:
            self.removeKeyboardListener(self)
        else:
            self.addKeyboardListener(self)
        self.drag_enabled = dragable

    def onFocus(self, sender):
        pass

    def onLostFocus(self, sender):
        pass

    def onClick(self, sender=None):
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

    def moveControl(self, x, y, first_move=False):
        pass

    def onClick(self, sender=None):
        self.setFocus(True)
        # work out the relative position of cursor
        event = DOM.eventGetCurrentEvent()
        mouse_x = DOM.eventGetClientX(event) + Window.getScrollLeft()
        mouse_y = DOM.eventGetClientY(event) + Window.getScrollTop()
        self.moveControl(mouse_x - self.getAbsoluteLeft(),
                         mouse_y - self.getAbsoluteTop(), True)

    def onMouseWheel(self, sender, velocity):
        print "mouse wheel", sender, velocity
        if self.dragging: # don't accept wheel events if dragging!
            return
        new_value = self.processValue(self.value - self.step * velocity)
        self.setControlPos(new_value)
        self.setValue(new_value)

    def onMouseMove(self, sender, x, y):
        if not self.dragging:
            return
        self.moveControl(x + Window.getScrollLeft(), y + Window.getScrollTop())

    def onLoseFocus(self, sender):
        self.endDragging()

    def onMouseDown(self, sender, x, y):
        # regardless of drag_enabled, onMouseDown must prevent
        # default, in order to avoid losing focus.
        self.setFocus(True)
        DOM.eventPreventDefault(DOM.eventGetCurrentEvent())
        if not self.drag_enabled:
            return
        self.dragging = True
        GlassWidget.show(self)
        self.moveControl(x + Window.getScrollLeft(), y + Window.getScrollTop(),
                         True)

    def onMouseEnter(self, sender):
        pass

    def onMouseLeave(self, sender):
        pass

    def onMouseUp(self, sender, x, y):
        self.endDragging()

    def onMouseGlassEnter(self, sender):
        pass

    def onMouseGlassLeave(self, sender):
        self.endDragging()

    def endDragging(self):
        if not self.dragging:
            return
        self.dragging = False
        GlassWidget.hide()

    def onKeyDown(self, sender, keycode, modifiers):
        if keycode == KeyboardListener.KEY_UP:
            DOM.eventPreventDefault(DOM.eventGetCurrentEvent())
            new_value = self.processValue(self.value + self.step)
            self.setControlPos(new_value)
            self.setValue(new_value)
        elif keycode == KeyboardListener.KEY_DOWN:
            DOM.eventPreventDefault(DOM.eventGetCurrentEvent())
            new_value = self.processValue(self.value - self.step)
            self.setControlPos(new_value)
            self.setValue(new_value)

    def onKeyUp(self, sender, keycode, modifiers):
        pass

    def onKeyPress(self, sender, keycode, modifiers):
        pass

    def _event_targets_control(self, event):
        target = DOM.eventGetTarget(event)
        return target and DOM.isOrHasChild(self.getElement(), target)

    def onEventPreview(self, event):
        etype = DOM.eventGetType(event)
        print "control preview", etype, self._event_targets_control(event), \
                     DOM.getCaptureElement() is not None
        if etype == "keydown":
            return self._event_targets_control(event)
        elif etype == "keyup":
            return self._event_targets_control(event)
        elif etype == "keypress":
            return self._event_targets_control(event)
        elif (   etype == "mousedown"
              or etype == "blur"
             ):
            if DOM.getCaptureElement() is not None:
                return True
            if not self._event_targets_control(event):
                return True
        elif (   etype == "mouseup"
              or etype == "click"
              or etype == "mousemove"
              or etype == "dblclick"
             ):
            if DOM.getCaptureElement() is not None:
                return True
        elif etype == "mouseout":
            if DOM.getCaptureElement() is not None:
                return False
        return self._event_targets_control(event)

Factory.registerClass('pyjamas.ui.Control', Control)
