""" Pyjamas UI BuilderPanel: takes a PyJsGlade builder spec and adds widgets
    requested using the methods just like in any other Panel class.

Copyright (C) 2010 Luke Kenneth Casson Leighton <lkcl@lkcl.net>

The purpose of this class is to be able to set up a Panel of any type
that can be dynamically created using Builder, and then add child widgets
once again by their name as specified in the Builder spec file.

This class therefore has all of the usual Panel functions (add,
remove, insert, __iter__, getWidget) as well as those required
for it to be instantiable via Builder itself (!) such as
addIndexedItem, getIndex and getIndexedChild.

"""

from pyjamas.ui.BuilderWidget import BuilderWidget

class BuilderPanel(BuilderWidget):

    def __init__(self, **kwargs):
        self.panel_instance_name = None
        BuilderWidget.__init__(self, **kwargs)

    def add(self, child_instance_name, *args, **kwargs):
        """ versatile adding-function, copes with:
            HTMLPanel.add(widget, id)
            HTMLTable.add(item, row, col)
            HorizontalPanel.add(item)
            VerticalPanel.add(item)
            VerticalSplitPanel.add(item)
            HorizontalSplitPanel.add(item)
            DeckPanel.add(item)
            TabPanel.add(item)
            DockPanel.add(widget, direction)
            StackPanel.add(widget, stackText, asHTML)
            AbsolutePanel.add(widget, left, top)
            FlowPanel.add(widget)
            CaptionPanel.add(widget)
            ScrollPanel.add(widget)
        """
        widget = self.b.createInstance(child_instance_name)
        self.widget.add(widget, *args, **kwargs)

    def insert(self, child_instance_name, *args, **kwargs):
        widget = self.b.createInstance(child_instance_name)
        self.widget.insert(widget, *args, **kwargs)

    def remove(self, widget, *args, **kwargs):
        """ versatile removing-function, copes with:
            HTMLPanel.remove(widget) # if it had one
            HTMLTable.remove(item)
            HorizontalPanel.remove(item)
            VerticalPanel.remove(item)
            VerticalSplitPanel.remove(item) # if it had one
            HorizontalSplitPanel.remove(item) # if it had one
            DeckPanel.remove(item)
            TabPanel.remove(item)
            DockPanel.remove(item)
            StackPanel.remove(item, index=None)
            AbsolutePanel.remove(item)
            FlowPanel.add(widget)
        """
        self.widget.remove(widget, *args, **kwargs)

    def __iter__(self):
        return self.b.__iter__()

    def getChildren(self):
        return self.b.getChildren()

    def setPanelInstanceName(self, panel_instance_name):
        self.panel_instance_name = panel_instance_name

    def getPanel(self):
        if self.panel_instance_name is None:
            return self.widget
        wids = self.b.widget_instances[self.instance_name]
        return wids[self.panel_instance_name]

    def addIndexedItem(self, index, instance_name):
        widget = self.b.createInstance(child_instance_name)
        self.widget.addIndexedItem(index, widget)

    def getIndex(self, *args):
        return self.widget.getIndex(*args)

    def getIndexedChild(self, *args):
        return self.widget.getIndexedChild(*args)

    def getWidget(self, *args):
        return self.widget.getWidget(*args)

    def getWidgetCount(self):
        return self.widget.getWidgetCount()

    def getWidgetIndex(self, *args):
        return self.widget.getWidgetIndex(*args)

    def setWidgetPosition(self, *args):
        return self.widget.setWidgetPosition(*args)

