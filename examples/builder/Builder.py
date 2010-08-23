""" Example UI Builder: replace or edit ui.xml without recompiling the app

Copyright (C) 2010 Luke Kenneth Casson Leighton <lkcl@lkcl.net>"

It's also possible to simply place the text into the app (which obviously
forces a recompile) and pass it as an argument to Builder:

    text = '''<?xml ....><pyjsglade>....</pyjsglade>'''
    self.b = Builder(text)
    self.ui = self.b.createInstance("AppFrame", self)

The advantage of doing this is that the UI will be created immediately
rather than be delayed waiting for an AJAX HTTPRequest.

The UI file simply contains the event callbacks, by name.  An app instance
object is passed in: createInstance uses getattr to find those functions
and automatically links listeners to the widgets that get created.
"""

import pyjd # this is dummy in pyjs.
from pyjamas.builder.Builder import Builder, HTTPUILoader
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.BuilderPanel import BuilderPanel


class Caption1Events(object):

    def __init__(self, app=None):
        self.app = app

    def onHTMLMouseMoved(self, sender, x, y):
        print "moved", sender, x, y

    def onInputBoxFocus(self, sender):
        print "input box focus", sender

    def onHTMLClicked(self, sender):
        print "clicked", sender
        #left = self.fDialogButton.getAbsoluteLeft() + 10
        #top = self.fDialogButton.getAbsoluteTop() + 10
        self.app.login.setWidth("600px")
        self.app.login.setHeight("400px")
        self.app.login.setPopupPosition(10, 10)
        self.app.login.show()
        for v in dir(self.app.login):
            print "db", v, getattr(self.app.login, v)
        print self.app.login.getOffsetWidth()
        print self.app.login.getOffsetHeight()
        print self.app.login.getAbsoluteLeft()
        print self.app.login.getAbsoluteTop()

class BuilderEvents(object):

    def __init__(self, app=None):
        self.app = app

    def onAddClicked(self, sender):
        print "add", sender
        grid = self.app.bp.getPanel()
        row = grid.getRowCount() + 1
        grid.resize(row, 1)
        self.app.bp.add("builderrow", row, 0)
        print "counts", grid.getRowCount(), grid.getColumnCount()

    def onRemoveClicked(self, sender):
        print "remove", sender
        widget = sender.getParent() # bit of a cheat
        grid = self.app.bp.getPanel()
        (row, col) = grid.getIndex(widget) # find widget row,col
        grid.removeRow(row)


class EventTest(Caption1Events):

    def onHTMLMouseMoved(self, sender, x, y):
        pass

    def onUILoaded(self, text):
        self.b = Builder(text)
        caption1events = Caption1Events(self)
        builderevents = BuilderEvents(self)
        self.caption1 = self.b.createInstance("CaptionPanel1", caption1events)
        self.caption2 = self.b.createInstance("CaptionPanel2", self)
        self.login = self.b.createInstance("AppLogin", self)
        self.bp = BuilderPanel(PanelInstanceName="Grid1",
                               InstanceName="builderpanel",
                               Builder=self.b,
                               EventReceiver=builderevents)
        RootPanel().add(self.caption1)
        RootPanel().add(self.caption2)
        RootPanel().add(self.bp)

    def onUILoadingTimeout(self, text, code):
        print "timeout loading UI", text, code

    def onUILoadError(self, text, code):
        print "error loading UI", text, code


if __name__ == '__main__':
    pyjd.setup("public/Builder.html?fred=foo#me")
    et = EventTest()
    HTTPUILoader(et).load("builder.xml")
    
    pyjd.run()
