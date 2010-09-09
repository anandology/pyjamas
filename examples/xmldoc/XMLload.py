# Modifications to allow execution under pyjd on Windows (mshtml) 2010-09-08
# See Issue 481 - Copyright (c) Phil Charlesworth 2010 
import pyjd

from pyjamas.ui.Button import Button
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.HTML import HTML
from pyjamas.ui.DockPanel import DockPanel
from pyjamas.ui import HasAlignment
from pyjamas.ui.Hyperlink import Hyperlink
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.ScrollPanel import ScrollPanel
from pyjamas import Window
from pyjamas.HTTPRequest import HTTPRequest
from pyjamas.XMLDoc import create_xml_doc


class XMLloader:
    def __init__(self, panel):
        self.panel = panel

    def onCompletion(self, doc):
        self.panel.doStuff(create_xml_doc(doc))

    def onError(self, text, code):
        self.panel.onError(text, code)

    def onTimeout(self, text):
        self.panel.onTimeout(text)


class XMLload:

    def onModuleLoad(self):
        
        HTTPRequest().asyncGet("contacts.xml", XMLloader(self))

    def onError(self, text, code):
        # FIXME
        pass

    def onTimeout(self, text):
        # FIXME
        pass

    def doStuff(self, xmldoc):

        contacts = xmldoc.getElementsByTagName("contact")
        len = contacts.length;
        for i in range(len):
            contactsDom = contacts.item(i)
            firstNames = contactsDom.getElementsByTagName("firstname")
            firstNameNode = firstNames.item(0)
            firstName = firstNameNode.firstChild.nodeValue
            RootPanel().add(HTML("firstname: %s" % str(firstName)))



if __name__ == '__main__':
    pyjd.setup("./public/XMLload.html")
    app = XMLload()
    app.onModuleLoad()
    pyjd.run()
