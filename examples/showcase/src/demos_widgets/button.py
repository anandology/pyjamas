"""
The ``ui.Button`` class is used to show a button.  When the user clicks on the
button, the given listener function is called.

Note that you can use the ``getattr()`` function to specify which method you
want called when the button is clicked.  This is the best way to write button
click handlers if you have more than one button on your panel.  If you have
only one button, you can use ``btn = Button("...", self)`` instead, and define
a method called ``onClick()`` to respond to the button click.

Another useful method is ``Button.setEnabled(enabled)``, which enables or
disables the button depending on the value of its parameter.
"""
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.Button import Button
from pyjamas import Window

class ButtonDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        btn = Button("Click Me", getattr(self, "onButtonClick"))
        self.add(btn)


    def onButtonClick(self):
        Window.alert("Ouch!")

