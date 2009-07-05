"""
The ``ui.Tree`` class lets you add a tree control to your application.

Call ``Tree.addTreeListener()`` to add a tree listener object to a tree, that
listener object's ``onTreeItemSelected()`` method will be called as the user
clicks on that item in the tree control.  Similarly, the listener object's
``onTreeItemStateChanged()`` method will be called whenever the user opens or
closes a branch of the tree.  Both of these methods have to be defined, even if
you don't use them both.

To open a branch of the tree, call ``TreeItem.setState()`` method.  If the
``state`` parameter is True, the branch of the tree will be opened; if it is
False, the branch of the tree will be closed.
"""
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.Tree import Tree
from pyjamas.ui.TreeItem import TreeItem
from pyjamas import DOM
from pyjamas import Window

class TreeDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        tree = Tree()
        tree.addTreeListener(self)

        s1 = self.createItem("Section 1")
        s1.addItem(self.createItem("Item 1.1", value=11))
        s1.addItem(self.createItem("Item 1.2", value=12))

        s2 = self.createItem("Section 2")
        s2.addItem(self.createItem("Item 2.1", value=21))
        s2.addItem(self.createItem("Item 2.2", value=22))

        s1.setState(True, fireEvents=False)
        s2.setState(True, fireEvents=False)

        tree.addItem(s1)
        tree.addItem(s2)
        self.add(tree)


    def createItem(self, label, value=None):
        item = TreeItem(label)
        DOM.setStyleAttribute(item.getElement(), "cursor", "pointer")
        if value is not None:
            item.setUserObject(value)
        return item


    def onTreeItemSelected(self, item):
        value = item.getUserObject()
        Window.alert("You clicked on " + value)


    def onTreeItemStateChanged(self, item):
        pass # We ignore this.

