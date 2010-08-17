""" Example UI Builder: replace or edit ui.xml without recompiling the app

Copyright (C) 2010 Luke Kenneth Casson Leighton <lkcl@lkcl.net>"

It's also possible to simply place the text into the app (which obviously
forces a recompile) and pass it as an argument to Builder:

    text = """<?xml ....><pyjsglade>....</pyjsglade>"""
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

class EventTest(object):

    def onHTMLMouseMoved(self, sender, x, y):
        print "moved", sender, x, y

    def onInputBoxFocus(self, sender):
        print "input box focus", sender

    def onHTMLClicked(self, sender):
        print "clicked", sender

    def onUILoaded(self, text):
        self.b = Builder(text)
        self.ui = self.b.createInstance("AppFrame", self)
        RootPanel().add(self.ui)

    def onUILoadingTimeout(self, text, code):
        print "timeout loading UI", text, code

    def onUILoadError(self, text, code):
        print "error loading UI", text, code


if __name__ == '__main__':
    pyjd.setup("public/Builder.html?fred=foo#me")
    et = EventTest()
    HTTPUILoader(et).load("ui.xml")
    
    pyjd.run()
