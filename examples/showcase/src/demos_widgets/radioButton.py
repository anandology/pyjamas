"""
The ``ui.RadioButton`` class is used to show a radio button.  Each radio button
is given a "group" value; when the user clicks on a radio button, the other
radio buttons in that group are deselected, and the clicked on radio button is
selected.

You can use the ``setChecked(checked)`` method to select or deselect a radio
button, and you can call ``isChecked()`` to see if a radio button is currently
selected.  You can also enable or disable a checkbox using
``setEnabled(enabled)``.  And finally, you can call ``addClickListener()`` to
respond when the user clicks on the radio button.
"""
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.RadioButton import RadioButton

class RadioButtonDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        panel1 = VerticalPanel()

        panel1.add(RadioButton("group1", "Red"))
        panel1.add(RadioButton("group1", "Green"))
        panel1.add(RadioButton("group1", "Blue"))

        panel2 = VerticalPanel()
        panel2.add(RadioButton("group2", "Solid"))
        panel2.add(RadioButton("group2", "Liquid"))
        panel2.add(RadioButton("group2", "Gas"))

        hPanel = HorizontalPanel()
        hPanel.add(panel1)
        hPanel.add(panel2)

        self.add(hPanel)

