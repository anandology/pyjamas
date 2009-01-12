"""
The ``ui.TextBox`` class implements a standard one-line input field.

There are many useful methods defined by ``ui.TextBox`` and its parent classes.
For example, ``getText()`` returns the current contents of the input field, and
``setText()`` lets you set the field's contents to a given string.

``setVisibleLength()`` lets you set the width of the field, in characters.
Similarly, ``setMaxLength()`` lets you set the maximum number of characters the
user can enter into the field.

"""
from ui import SimplePanel, TextBox

class TextBoxDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        field = TextBox()
        field.setVisibleLength(20)
        field.setMaxLength(10)

        self.add(field)

