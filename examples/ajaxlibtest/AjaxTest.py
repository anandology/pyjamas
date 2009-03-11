from pyjamas.ui.Button import Button
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.HTML import HTML
from pyjamas import Window
from pyjamas import DOM
import pyjslib

def greet(sender):
    JS("head = document.getElementsByTagName('head')[0];")
    html = DOM.getInnerHTML(head)
    Window.alert("You should see test.cache.js in this lot:\n" + html)

    JS("""
       test_fn();
        """)

class AjaxTest:

    ClickMe = "Click me"

    def onModuleLoad(self):

        b = Button(ClickMe, greet)
        RootPanel().add(b)

        # dynamically loads public/test.cache.js.
        # note that this does NOT check that the module
        # has actually loaded.  you will need to see e.g.
        # pyjslib.import_wait for that.

        pyjslib.import_module(None, "test")

