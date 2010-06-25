"""
The ``ui.ScrollPanel`` class implements a panel that scrolls its contents.

If you want the scroll bars to be always visible, call
``setAlwaysShowScrollBars(True)``.  You can also change the current scrolling
position programmatically by calling ``setScrollPosition(vPos)`` and
``setScrollHorizontalPosition(hPos)`` to change the horizontal and vertical
scrolling position, respectively.
"""
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.ScrollPanel import ScrollPanel
from pyjamas.ui.HTML import HTML

class ScrollPanelDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        panel = ScrollPanel(Size=("300px", "100px"))

        contents = HTML("<b>Tao Te Ching, Chapter One</b><p>" +
                        "The Way that can be told of is not an unvarying " +
                        "way;<p>The names that can be named are not " +
                        "unvarying names.<p>It was from the Nameless that " +
                        "Heaven and Earth sprang;<p>The named is but the " +
                        "mother that rears the ten thousand creatures, " +
                        "each after its kind.")

        panel.add(contents)
        self.add(panel)

