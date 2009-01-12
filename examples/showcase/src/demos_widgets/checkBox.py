"""
The ``ui.CheckBox`` class is used to show a standard checkbox.  When the user
clicks on the checkbox, the checkbox's state is toggled.

The ``setChecked(checked)`` method checks or unchecks the checkbox depending on
the value of the parameter.  To get the current value of the checkbox, call
``isChecked()``.

You can enable or disable a checkbox using ``setEnabled(enabled)``.  You can
also call ``addClickListener()`` to respond when the user clicks on the
checkbox, as shown below.  This can be useful when building complicated input
screens where checking a checkbox causes other input fields to be enabled.
"""
from ui import SimplePanel, CheckBox
import Window

class CheckBoxDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        self.box = CheckBox("Print Results?")
        self.box.addClickListener(getattr(self, "onClick"))

        self.add(self.box)


    def onClick(self):
        Window.alert("checkbox status: " + self.box.isChecked())

