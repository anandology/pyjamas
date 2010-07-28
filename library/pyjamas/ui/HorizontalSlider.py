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
from VerticalSlider import VerticalSlider


class HorizontalSlider(VerticalSlider):

    def __init__(self, min_value, max_value, start_value=None, step=None,
                       **kwargs):

        VerticalSlider.__init__(self, min_value, max_value, start_value,
                                    **kwargs)
        self.setHandleStyle(None, "10px", "100%", None)

    def moveControl(self, mouse_x, mouse_y, first_move=False):
        handle_width = DOM.getIntAttribute(self.handle, "offsetWidth")
        widget_width = self.getOffsetWidth()
        length_range = widget_width - 10 # handle width is hard-coded
        relative_x = mouse_x - (handle_width / 2)
        if relative_x < 0:
            relative_x = 0
        if relative_x >= length_range:
            relative_x = length_range

        val_diff = self.max_value - self.min_value
        new_value = ((val_diff * relative_x) / length_range) + self.min_value
        new_value = self.processValue(new_value)

        self.setControlPos(new_value)
        self.setValue(new_value)

    def setControlPos(self, value):
        widget_width = self.getOffsetWidth()
        length_range = widget_width - 10 # handle width is hard-coded
        val_diff = self.max_value - self.min_value
        relative_x = length_range * (value - self.min_value) / val_diff

        # limit the position to be in the widget!
        if relative_x < 0:
            relative_x = 0
        if relative_x >= length_range:
            relative_x = length_range

        # move the handle
        DOM.setStyleAttribute(self.handle, "left", "%dpx" % relative_x)
        DOM.setStyleAttribute(self.handle, "position", "absolute")

Factory.registerClass('pyjamas.ui.HorizontalSlider', HorizontalSlider)
