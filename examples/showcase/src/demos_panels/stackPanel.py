"""
The ``ui.StackPanel`` class displays a "stack" of sub-panels where only one
sub-panel is open at a time.

The StackPanel relies heavily on stylesheet definitions to make it look good;
the default look of a StackPanel without any styles defined is almost unusable.
The following stylesheet definitions were used for the example given below:

    .gwt-StackPanel {
        border: 5px solid #999999;
        background-color: #CCCCCC;
        border-collapse: collapse;
    }

    .gwt-StackPanel .gwt-StackPanelItem {
        border: 2px solid #000099;
        background-color: #FFFFCC;
        cursor: pointer;
        font-weight: normal;
    }

    .gwt-StackPanel .gwt-StackPanelItem-selected {
        border: 3px solid #FF0000;
        background-color: #FFFF66;
        cursor: default;
        font-weight: bold;
    }

You can programatically change the currently-open panel by calling the
``setStackVisible(index, visible)`` method.  To find out which panel is
currently open, call ``getSelectedIndex()``.  To retrieve the widget at a given
index, call ``getWidget(index)``.  Finally, you can change the label for a
stack item by calling ``setStackText(index, text)``.
"""
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.StackPanel import StackPanel
from pyjamas.ui.HTML import HTML

class StackPanelDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        stack = StackPanel(Width="100%", Height="300px")

        stack.add(HTML('The quick<br>brown fox<br>jumps over the<br>lazy dog.'),
                  "Stack 1")
        stack.add(HTML('The<br>early<br>bird<br>catches<br>the<br>worm.'),
                  "Stack 2")
        stack.add(HTML('The smart money<br>is on the<br>black horse.'),
                  "Stack 3")

        self.add(stack)

