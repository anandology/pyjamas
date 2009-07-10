"""
The ``ui.FlowPanel`` is a panel that allows its contents to "flow" from left to
right, and then from top to bottom, like words on a page.

Because of the way it works, only the width of a FlowPanel needs to be
specified; it will automatically take up as much height as is needed to fit the
panel's contents.

Unfortunately, the implementation of the FlowPanel is actually quite limited,
because of the way other widgets are typically implemented.  Many widgets are
wrapped up in a ``<div>`` element, which is a block-level element that
overrules the ``<span>`` element used by the FlowPanel, which is an inline
element.  As a result, if you add a ``ui.Label`` to a FlowPanel, for example,
it will still appear on a line by itself rather than flowing with the other
elements.  Because of this, you may want to avoid using FlowPanel unless you
are certain that the items you are adding will flow correctly.
"""
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.FlowPanel import FlowPanel
from pyjamas.ui.Button import Button

class FlowPanelDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        flow = FlowPanel(Width="400px")

        flow.add(Button("Item 1"))
        flow.add(Button("Item 2"))
        flow.add(Button("Item 3"))
        flow.add(Button("Item 4"))
        flow.add(Button("Item 5"))
        flow.add(Button("Item 6"))
        flow.add(Button("Item 7"))
        flow.add(Button("Item 8"))
        flow.add(Button("Item 9"))
        flow.add(Button("Item 10"))

        self.add(flow)

