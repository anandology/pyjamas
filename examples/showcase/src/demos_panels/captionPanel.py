"""
The ``ui.CaptionPanel`` class implements a panel that displays a caption
in the upper left corner of the border.

"""
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.CaptionPanel import CaptionPanel
from pyjamas.ui.HTML import HTML

class CaptionPanelDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        contents = HTML("""<h3>The Zen of Python, by Tim Peters</h3>
<p>Beautiful is better than ugly.<br />
Explicit is better than implicit.<br />
Simple is better than complex.<br />
Complex is better than complicated.<br />
Flat is better than nested.<br />
Sparse is better than dense.<br />
Readability counts.<br />
Special cases aren't special enough to break the rules.<br />
Although practicality beats purity.<br />
Errors should never pass silently.<br />
Unless explicitly silenced.<br />
In the face of ambiguity, refuse the temptation to guess.<br />
There should be one-- and preferably only one --obvious way to do it.<br />
Although that way may not be obvious at first unless you're Dutch.<br />
Now is better than never.<br />
Although never is often better than *right* now.<br />
If the implementation is hard to explain, it's a bad idea.<br />
If the implementation is easy to explain, it may be a good idea.<br />
Namespaces are one honking great idea -- let's do more of those!</p>
""")

        panel = CaptionPanel("Caption-Panel", contents)

        self.add(panel)

