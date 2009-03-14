""" ControlDemo Example
"""
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Label import Label
from pyjamas.ui.Controls import VerticalDemoSlider
from pyjamas.ui.Controls import VerticalDemoSlider2
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.VerticalPanel import VerticalPanel

class SliderClass(VerticalPanel):
    def __init__(self, p2):
        VerticalPanel.__init__(self)

        self.setSpacing(10)
        if p2:
            b = VerticalDemoSlider2(0, 100)
        else:
            b = VerticalDemoSlider(0, 100)
        self.add(b)

        b.setWidth("20px")
        b.setHeight("100px")

        b.addControlValueListener(self)

        self.label = Label("Not set yet")
        self.add(self.label)

    def onControlValueChanged(self, slider, old_value, new_value):
        self.label.setText("Value: %d" % int(new_value))


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
