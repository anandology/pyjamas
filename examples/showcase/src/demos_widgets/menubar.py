"""
The ``ui.MenuBar`` and ``ui.MenuItem`` classes allow you to define menu bars in
your application.

There are several important things to be aware of when adding menus to your
application:

 * You have to use a stylesheet to define the look of your menu.  The default
   style is terrible, as it makes the menu unusable.  The following stylesheet
   entries were used for the example code below:

        .gwt-MenuBar {
          background-color: #C3D9FF;
          border: 1px solid #87B3FF;
          cursor: default;
        }

        .gwt-MenuBar .gwt-MenuItem {
          padding: 1px 4px 1px 4px;
          font-size: smaller;
          cursor: default;
        }

        .gwt-MenuBar .gwt-MenuItem-selected {
          background-color: #E8EEF7;
        }

 * By default, each menu item can be associated with a class, whose ``execute``
   method will be called when that item is selected.  Note that a helper class,
   ``MenuCmd``, is defined below to allow more than one menu item handler
   method to be defined within a single class.

 * You add menu items directly, passing the item label and the associated
   command to ``MenuBar.addItem()``.  For adding sub-menus, you need to wrap
   the sub-menu up in a ``MenuItem``, as shown below.

 * You can use HTML codes in a menu item's label by calling
   ``MenuBar.addItem(label, True, cmd)`` instead of ``MenuBar.addItem(label,
   cmd)``.  Similarly, you can use HTML styling in a menu's title by calling
   ``MenuItem(label, True, submenu)``, as in the second-to-last line of
   ``MenubarDemo.__init__``, below.
"""
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.MenuBar import MenuBar
from pyjamas.ui.MenuItem import MenuItem
from pyjamas import Window

class MenubarDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        menu1 = MenuBar(vertical=True)
        menu1.addItem("Item 1", MenuCmd(self, "onMenu1Item1"))
        menu1.addItem("Item 2", MenuCmd(self, "onMenu1Item2"))

        menu2 = MenuBar(vertical=True)
        menu2.addItem("Apples", MenuCmd(self, "onMenu2Apples"))
        menu2.addItem("Oranges", MenuCmd(self, "onMenu2Oranges"))

        menubar = MenuBar(vertical=False)
        menubar.addItem(MenuItem("Menu 1", menu1))
        menubar.addItem(MenuItem("<i>Menu 2</i>", True, menu2))
        self.add(menubar)

    def onMenu1Item1(self):
        Window.alert("Item 1 selected")

    def onMenu1Item2(self):
        Window.alert("Item 2 selected")

    def onMenu2Apples(self):
        Window.alert("Apples selected")

    def onMenu2Oranges(self):
        Window.alert("Oranges selected")


class MenuCmd:
    def __init__(self, object, handler):
        self._object  = object
        self._handler = handler

    def execute(self):
        handler = getattr(self._object, self._handler)
        handler()

