"""
The ``ui.NamedFrame`` class is a variation of the ``ui.Frame`` which lets you
assign a name to the frame.  Naming a frame allows you to refer to that frame
by name in Javascript code, and as the target for a hyperlink.
"""
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.NamedFrame import NamedFrame
from pyjamas.ui.HTML import HTML

class NamedFrameDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        vPanel = VerticalPanel(Spacing=5)

        frame = NamedFrame("myFrame",
                            Width="100%",
                            Height="200px")

        vPanel.add(frame)
        vPanel.add(HTML('<a href="http://google.com" target="myFrame">Google</a>'))
        vPanel.add(HTML('<a href="http://yahoo.com" target="myFrame">Yahoo</a>'))
        vPanel.add(HTML('<a href="http://pyjs.org" target="myFrame">Pyjamas</a>'))

        self.add(vPanel)
