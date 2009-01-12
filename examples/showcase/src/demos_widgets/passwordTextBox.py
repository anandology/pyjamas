"""
The ``ui.PasswordTextBox`` class implements a standard password input field.

Like its cousins the ``ui.TextBox`` and ``ui.TextArea`` classes,
``ui.PasswordTextBox`` defines many useful methods which you may find useful.

The most important methods are probably ``setText()`` and ``getText()`` which
set and retrieve the contents of the input field, and ``setMaxLength()`` to
specify how many characters the user can type into the field.

Note that for some reason, the ``setVisibleLength()`` method is not defined for
a password field.  This means that you have to specify the width of the field
in pixels, as is shown below.
"""
from ui import SimplePanel, PasswordTextBox

class PasswordTextBoxDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        field = PasswordTextBox()
        field.setWidth("100px")
        self.add(field)

