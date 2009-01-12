"""
The ``ui.HTML`` class displays HTML-formatted text.  To display unformatted
text, use ``ui.Label``.
"""
from ui import SimplePanel, HTML

class HtmlDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        html = HTML("Hello, <b><i>World!</i></b>")
        self.add(html)

