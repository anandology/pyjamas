""" Control Widgets.  Presently comprises a Vertical Slider and derivatives.

    HorizontalSlider and HorizontalSlider2 added by Bill Winder
    AreaSlider and AreaSlider2 added by Bill Winder

    Copyright (C) 2008, 2009, 2010 Luke Kenneth Casson Leighton <lkcl@lkcl.net>
    Copyright (C) 2010 - Cedric Gestes <gestes@aldebaran-robotics.com>
    Copyright (C) 2009, 2010 - Bill Winder <wgwinder@gmail.com>


    To do: All controls with draggable=True do not fire the OnFocus methon on single click.
    the control does not activate the OnFocus method. Clicking the handle does fire OnFocus, however.

"""

from pyjamas import Factory
from pyjamas import DOM
from pyjamas.ui import MouseListener
from pyjamas.ui.InputControl import InputControl


class MouseInputControl(InputControl):

    def __init__(self, min_value, max_value, start_value=None, step=None,
                       **kwargs):

        if not kwargs.has_key("StyleName"):
            kwargs['StyleName'] = "gwt-MouseInputControl"
        InputControl.__init__(self, min_value, max_value, start_value,
                                step, **kwargs)

        self.addMouseListener(self)
        self.setDragable(True)

    def onFocus(self, sender):
        self.addStyleName("gwt-MouseInputControl-focussed")

    def onLostFocus(self, sender):
        self.removeStyleName("gwt-MouseInputControl-focussed")
        self.dragging = False
        DOM.releaseCapture(self.getElement())

    def moveControl(self, mouse_x, mouse_y, first_move=False):
        height_range = 100.0
        val_diff = self.max_value - self.min_value
        if first_move:
            # back-calculate value to offset so that control doesn't jump
            value = self.value
            self.height_offset = mouse_y - height_range + \
                      (height_range * (value - self.min_value)) / val_diff

        relative_y = mouse_y - self.height_offset
        #widget_height = self.getOffsetHeight()
        #relative_y = mouse_y - (widget_height / 2) - self.height_offset
        if relative_y < 0:
            relative_y = 0
        if relative_y >= height_range:
            relative_y = height_range

        relative_y = height_range - relative_y # turn round (bottom to top)

        new_value = ((val_diff * relative_y) / height_range) + self.min_value
        new_value = self.processValue(new_value)

        self.setControlPos(new_value)
        self.setValue(new_value)

Factory.registerClass('pyjamas.ui.MouseInputControl', 'InputControl', InputControl)
