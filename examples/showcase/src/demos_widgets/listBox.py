"""
The ``ui.ListBox`` class allows the user to select one or more items from a
list.  There are two variations of the ListBox: a normal list of items the user
can click on, and a dropdown menu of items.  Both variations are shown in the
example below.

You add items to a list by calling ``ListBox.addItem()``.  This can take the
label to display, and also an optional value to associate with that item in the
list.  ``ListBox.getSelectedIndex()`` returns the index of the currently
selected item, or -1 if nothing is selected.  ``ListBox.getItemText(n)``
returns the text for the given item in the list, while ``ListBox.getValue(n)``
returns the value associated with the given list item.  To detect when the user
selects something from a ListBox, call ``addChangeLister()``.  And finally,
``ListBox.clear()`` clears the current contents of the ListBox.
"""
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.ListBox import ListBox
from pyjamas import Window

class ListBoxDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        hPanel = HorizontalPanel()
        hPanel.setSpacing(10)

        self.list1 = ListBox()
        self.list1.setVisibleItemCount(10)
        self.list1.addItem("Item 1")
        self.list1.addItem("Item 2")
        self.list1.addItem("Item 3")
        self.list1.addChangeListener(getattr(self, "onList1ItemSelected"))

        self.list2 = ListBox()
        self.list2.setVisibleItemCount(0)
        self.list2.addItem("Item A")
        self.list2.addItem("Item B")
        self.list2.addItem("Item C")
        self.list2.addChangeListener(getattr(self, "onList2ItemSelected"))

        hPanel.add(self.list1)
        hPanel.add(self.list2)
        self.add(hPanel)


    def onList1ItemSelected(self, event):
        item = self.list1.getItemText(self.list1.getSelectedIndex())
        Window.alert("You selected " + item + " from list 1")


    def onList2ItemSelected(self, event):
        item = self.list2.getItemText(self.list2.getSelectedIndex())
        Window.alert("You selected " + item + " from list 2")

