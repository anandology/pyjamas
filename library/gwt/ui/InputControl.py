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
from pyjamas.ui import KeyboardListener
from pyjamas.ui.TextBox import TextBox
from pyjamas.ui.Control import Control


class InputControl(Control):

    def __init__(self, min_value, max_value, start_value=None, step=None,
                       **kwargs):

        if not kwargs.has_key("StyleName"):
            kwargs['StyleName'] = "gwt-InputControl"
        self.input = TextBox()
        self.input.addKeyboardListener(self)
        #element = DOM.createDiv()
        if kwargs.has_key('Element'):
            # XXX FIXME: unlikely to work!
            element = kwargs.pop('Element')
        else:
            element = self.input.getElement() # YUK!!!
        Control.__init__(self, element, min_value, max_value, start_value, step,
                               **kwargs)

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
            DOM.eventPreventDefault(DOM.eventGetCurrentEvent())
            txt = self.input.getText()
            if not txt:
                return
            new_value = float(txt)
            new_value = self.processValue(new_value)
            self.setControlPos(new_value)
            self.setValue(new_value)
        else:
            Control.onKeyPress(self, sender, keycode, modifiers)

Factory.registerClass('pyjamas.ui.InputControl', 'InputControl', InputControl)
