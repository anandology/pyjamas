"""
The ``ui.NamedFrame`` class is a variation of the ``ui.Frame`` which lets you
assign a name to the frame.  Naming a frame allows you to refer to that frame
by name in Javascript code, and as the target for a hyperlink.
"""
from ui import SimplePanel, VerticalPanel, NamedFrame, HTML

class NamedFrameDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        vPanel = VerticalPanel()
        vPanel.setSpacing(5)

        frame = NamedFrame("myFrame")
        frame.setWidth("100%")
        frame.setHeight("200px")

        vPanel.add(frame)
        vPanel.add(HTML('<a href="http://google.com" target="myFrame">Google</a>'))
        vPanel.add(HTML('<a href="http://yahoo.com" target="myFrame">Yahoo</a>'))

        self.add(vPanel)
