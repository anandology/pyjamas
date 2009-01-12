"""
The ``ui.Label`` class is used to display unformatted text.  Unlike the
``ui.HTML`` class, it does not interpret HTML format codes.  If you pass False
as the second parameter when creating your label, word wrapping will be
disabled, forcing all the text to be on one line.
"""
from ui import SimplePanel, Label

class LabelDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        label = Label("This is a label", wordWrap=False)
        self.add(label)

