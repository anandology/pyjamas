""" ControlDemo Example
"""
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Label import Label
from pyjamas.ui.Controls import VerticalDemoSlider
from pyjamas.ui.Controls import VerticalDemoSlider2
from pyjamas.ui.Controls import InputControl
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.VerticalPanel import VerticalPanel

class SliderClass(VerticalPanel):
    def __init__(self, p2):
        VerticalPanel.__init__(self)

        self.setSpacing(10)
        if p2:
            self.b = VerticalDemoSlider2(0, 100)
        else:
            self.b = VerticalDemoSlider(0, 100)
        self.add(self.b)

        self.b.setWidth("20px")
        self.b.setHeight("100px")

        self.b.addControlValueListener(self)

        self.label = InputControl(0, 100)
        self.add(self.label)

        self.label.addControlValueListener(self)

    def onControlValueChanged(self, sender, old_value, new_value):
        if sender == self.label:
            self.b.setControlPos(new_value)
            self.b.setValue(new_value, 0)
        if sender == self.b:
            self.label.setControlPos(new_value)
            self.label.setValue(new_value, 0)

class ControlDemo:
    def onModuleLoad(self):

        p = HorizontalPanel()
        p.setSpacing(10)

        sc = SliderClass(False)
        p.add(sc)
        sc = SliderClass(True)
        p.add(sc)
        sc = SliderClass(True)
        p.add(sc)

        RootPanel().add(p)


if __name__ == '__main__':
    app = ControlDemo()
    app.onModuleLoad()
