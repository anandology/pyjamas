"""
``ui.AbsolutePanel`` is a panel that positions its children using absolute
pixel positions.  This allows the panel's children to overlap.

Note that the AbsolutePanel does not automatically resize itself to fit its
children.  There is no straightforward way of doing this unless all the
children are explicitly sized; the easier workaround is just to call
``panel.setWidth(width)`` and ``panel.setHeight(height)`` explicitly after
adding the children, choosing an appropriate width and height based on the
children you have added.
"""
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.AbsolutePanel import AbsolutePanel
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.HTML import HTML
from pyjamas import DOM


class AbsolutePanelDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        panel = AbsolutePanel(Width="100%", Height="100px")

        panel.add(self.makeBox("Child 1"), 20, 10)
        panel.add(self.makeBox("Child 2"), 30, 30)

        self.add(panel)


    def makeBox(self, label):
        wrapper = VerticalPanel(BorderWidth=1)
        wrapper.add(HTML(label))
        DOM.setAttribute(wrapper.getTable(), "cellPadding", "10")
        DOM.setAttribute(wrapper.getTable(), "bgColor", "#C3D9FF")

        return wrapper

