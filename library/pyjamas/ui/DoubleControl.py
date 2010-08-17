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
from FocusWidget import FocusWidget
from pyjamas.ui import Focus
from MouseListener import MouseHandler
from pyjamas.ui import KeyboardListener
from Control import Control


class DoubleControl(Control):

    def __init__(self, element, min_value, max_value,
                       start_value_xy=None, step_xy=None, **kwargs):

        self.min_value_x = min_value[0]
        self.min_value_y = min_value[1]

        self.max_value_x = max_value[0]
        self.max_value_y = max_value[1]

        if start_value_xy is None:
            self.start_value_x = self.min_value_x
            self.start_value_y = self.min_value_y
        else:
            self.start_value_x = start_value_xy[0]
            self.start_value_y = start_value_xy[1]

        if step_xy is None:
            self.step_x = (self.max_value_x - self.min_value_x) / 20
            self.step_y = (self.max_value_y - self.min_value_y) / 20
        else:
            self.step_x = step_xy[0]
            self.step_y = step_xy[1]

        self.value_x = self.start_value_x
        self.value_y = self.start_value_y

        self.valuechange_listeners = []
        self.dragging = False
        self.drag_enabled = False

        if not kwargs.has_key("TabIndex"): kwargs['TabIndex'] = 0
        FocusWidget.__init__(self, element, **kwargs)
        MouseHandler.__init__(self)

    def processValue(self, value):

        """ rounds and limits the value to acceptable range
        """
        value_x = value[0]
        value_y = value[1]

        value_x = math.floor((value_x - self.min_value_x) / self.step_x)
        value_x = (value_x * self.step_x) + self.min_value_x
        value_x = max(value_x, self.min_value_x)
        value_x = min(value_x, self.max_value_x)

        value_y = math.floor((value_y - self.min_value_y) / self.step_y)
        value_y = (value_y * self.step_y) + self.min_value_y
        value_y = max(value_y, self.min_value_y)
        value_y = min(value_y, self.max_value_y)

        return [value_x, value_y]

    def setValue(self, (new_value_x,new_value_y), notify=1):

        old_value = [self.value_x, self.value_y]

        self.value_x = new_value[0]
        self.value_y = new_value[1]

        if not notify:
            return

        for listener in self.valuechange_listeners:
            listener.onControlValueChanged(self, old_value, new_value)

    def onControlValueChanged(self, value_old_xy, value_new_xy):
        pass

    def onKeyDown(self, sender, keycode, modifiers):
        if keycode == KeyboardListener.KEY_UP:
            DOM.eventPreventDefault(DOM.eventGetCurrentEvent())
            new_value = \
                self.processValue((self.value_x + self.step_x,
                                   self.value_y + self.step_y))
            self.setControlPos(new_value)
            self.setValue(new_value)
        elif keycode == KeyboardListener.KEY_DOWN:
            DOM.eventPreventDefault(DOM.eventGetCurrentEvent())
            new_value = \
               self.processValue((self.value_x - self.step_x,
                                  self.value_y-self.step_y))
            self.setControlPos(new_value)
            self.setValue(new_value)

Factory.registerClass('pyjamas.ui.DoubleControl', 'DoubleControl', DoubleControl)
