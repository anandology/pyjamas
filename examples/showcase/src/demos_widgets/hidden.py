"""
The ``ui.Hidden`` class represents a hidden form field.

This is really only useful when the hidden field is part of a ``ui.FormPanel``.
"""
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.FormPanel import FormPanel
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.Hidden import Hidden
from pyjamas.ui.Button import Button
from pyjamas.ui.NamedFrame import NamedFrame

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


    def onBtnClick(self, event):
        self.form.submit()

