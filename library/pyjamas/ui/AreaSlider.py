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
from pyjamas.ui import Focus
from DoubleControl import DoubleControl


class AreaSlider(DoubleControl):

    def __init__(self, min_value, max_value,
                 start_value=None, step=None,
                 **kwargs):

        if not kwargs.has_key("StyleName"):
            kwargs['StyleName'] = "gwt-VerticalSlider"

        if kwargs.has_key('Element'):
            # XXX FIXME: Focus.createFocusable is here for a reason...
            element = kwargs.pop('Element')
        else:
            element = Focus.createFocusable()
        DOM.setStyleAttribute(element, "position", "relative")
        DOM.setStyleAttribute(element, "overflow", "hidden")

        self.handle = DOM.createDiv()
        DOM.appendChild(element, self.handle)

        self.setHandleStyle("1px", "100%", "10px", "#808080")

        # must use DoubleControl; otherwise, this init is = Vertical init,
        # plus a change in the handle style
        # this should be refactored, so that the AreaSlider
        # can be built on VerticalSlider
        DoubleControl.__init__(self, element, min_value, max_value,
                               start_value, step,
                               **kwargs)

        self.addClickListener(self)
        self.addFocusListener(self)
        self.addMouseListener(self)

        #Redefine VDS's styles for handle
        self.setHandleStyle("1px", "10px", "10px", "#808080")

    def setHandleStyle(self, border, width, height, backgroundColor):
        if border is not None:
            DOM.setStyleAttribute(self.handle, "border", border)
        if width is not None:
            DOM.setStyleAttribute(self.handle, "width", width)
        if height is not None:
            DOM.setStyleAttribute(self.handle, "height", height)
        if backgroundColor is not None:
            DOM.setStyleAttribute(self.handle, "backgroundColor", backgroundColor)

    def setValue(self, new_value, notify=1):
        old_value = [self.value_x, self.value_y]

        self.value_x = new_value[0]
        self.value_y = new_value[1]

        if not notify:
            return

        for listener in self.valuechange_listeners:
            # how to handle this? ???
            listener.onControlValueChanged(self, old_value, new_value)

    def onFocus(self, sender):
        self.addStyleName("gwt-VerticalSlider-focussed")

    def onLostFocus(self, sender):
        self.removeStyleName("gwt-VerticalSlider-focussed")
        self.dragging = False
        DOM.releaseCapture(self.getElement())

    def moveControl(self, mouse_x, mouse_y):
        handle_height = DOM.getIntAttribute(self.handle, "offsetHeight")
        widget_height = self.getOffsetHeight()
        height_range = widget_height - 10 # handle height is hard-coded
        relative_y = mouse_y - (handle_height / 2)
        if relative_y < 0:
            relative_y = 0
        if relative_y >= height_range:
            relative_y = height_range

        # turn round (bottom to top) for x
        relative_y = height_range - relative_y

        handle_width = DOM.getIntAttribute(self.handle, "offsetWidth")
        widget_width = self.getOffsetWidth()
        length_range = widget_width - 10 # handle width is hard-coded
        relative_x = mouse_x - (handle_width / 2)
        if relative_x < 0:
            relative_x = 0
        if relative_x >= length_range:
            relative_x = length_range

        val_diff_x = self.max_value_x - self.min_value_x
        new_value_x = ((val_diff_x * relative_x) / length_range) + \
                      self.min_value_x

        val_diff_y = self.max_value_y - self.min_value_y
        new_value_y = ((val_diff_y * relative_y) / height_range) + \
                      self.min_value_y

        new_value = [new_value_x, new_value_y]
        new_value = self.processValue(new_value)
        self.setControlPos(new_value)
        self.setValue(new_value)

    def setControlPos(self, value):
        value_x = value[0]
        value_y = value[1]

        widget_width = self.getOffsetWidth()
        length_range = widget_width - 10 # handle width is hard-coded
        val_diff_x = self.max_value_x - self.min_value_x
        relative_x = length_range * (value_x - self.min_value_x) / val_diff_x

        # limit the position to be in the widget!
        if relative_x < 0:
            relative_x = 0
        if relative_x >= length_range:
            relative_x = length_range

        widget_height = self.getOffsetHeight()
        height_range = widget_height - 10 # handle height is hard-coded
        val_diff_y = self.max_value_y - self.min_value_y
        relative_y = height_range * (value_y - self.min_value_y) / val_diff_y

        # limit the position to be in the widget!
        if relative_y < 0:
            relative_y = 0
        if relative_y >= height_range:
            relative_y = height_range

        relative_y = height_range - relative_y # turn round (bottom to top)

        # move the handle
        DOM.setStyleAttribute(self.handle, "top", "%dpx" % relative_y)
        DOM.setStyleAttribute(self.handle, "left", "%dpx" % relative_x) 
        DOM.setStyleAttribute(self.handle, "position", "absolute")

Factory.registerClass('pyjamas.ui.AreaSlider', AreaSlider)
