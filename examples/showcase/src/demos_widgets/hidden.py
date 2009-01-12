"""
The ``ui.Hidden`` class represents a hidden form field.

This is really only useful when the hidden field is part of a ``ui.FormPanel``.
"""
from ui import SimplePanel, FormPanel, VerticalPanel, Hidden, Button, NamedFrame

class HiddenDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        self.form = FormPanel()
        self.form.setAction("http://google.com/search")
        self.form.setTarget("results")

        panel = VerticalPanel()
        panel.add(Hidden("q", "python pyjamas"))
        panel.add(Button("Search", getattr(self, "onBtnClick")))

        results = NamedFrame("results")
        panel.add(results)

        self.form.add(panel)
        self.add(self.form)


    def onBtnClick(self):
        self.form.submit()

