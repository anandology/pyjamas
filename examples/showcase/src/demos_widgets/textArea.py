"""
The ``ui.TextArea`` class implements a standard multi-line input field.

The ``setCharacterWidth()`` method sets the width of the input field, in
characters, while ``setVisibleLines()`` sets the height of the field, in lines.

Use the ``getText()`` method to retrieve the field's current text, and
``setText()`` to set it.  There are many other useful methods defined by
``ui.TextArea`` and its parent classes; see the module documentation for more
details.
"""
from ui import SimplePanel, TextArea

class TextAreaDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        field = TextArea()
        field.setCharacterWidth(20)
        field.setVisibleLines(4)
        self.add(field)

