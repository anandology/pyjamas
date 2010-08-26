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

from pyjamas import log
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
        log.writebr("panel args pre-mess " + repr(args) + " " + repr(kwargs))
        pargs = list(args)
        widget = self.b.createInstance(child_instance_name, self.event_receiver)
        log.writebr("panel " + self.getPanel().__class__.__name__)
        log.writebr("panel add fn " + self.getPanel().add.__class__.__name__)
        log.writebr("panel args " + repr(pargs) + " " + repr(kwargs))
        self.getPanel().add(widget, *pargs, **kwargs)
        return widget

    def insert(self, child_instance_name, *args, **kwargs):
        widget = self.b.createInstance(child_instance_name, self.event_receiver)
        self.getPanel().insert(widget, *args, **kwargs)
        return widget

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
        self.getPanel().remove(widget, *args, **kwargs)

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

    # these next three functions are part of the standard Builder API
    # and are required for panels to be manageable by PyJsGlade.
    def addIndexedItem(self, index, instance_name):
        widget = self.b.createInstance(child_instance_name, self.event_receiver)
        self.getPanel().addIndexedItem(index, widget)

    def getIndexedChild(self, index):
        return self.getPanel().getIndexedChild(index)

    def getWidgetIndex(self, widget):
        return self.getPanel().getWidgetIndex(widget)

    def getWidget(self, *args):
        return self.getPanel().getWidget(*args)

    def getWidgetCount(self):
        return self.getPanel().getWidgetCount()

    def setWidgetPosition(self, *args):
        return self.getPanel().setWidgetPosition(*args)

