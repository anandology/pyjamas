import pyjd # this is dummy in pyjs.
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Button import Button
from pyjamas.ui.HTML import HTML
from pyjamas.ui.Label import Label
from pyjamas.ui.RichTextArea import RichTextArea
from pyjamas import Window

import pygwt

def greet(fred):
    print "greet button"
    Window.alert("Hello, AJAX!")

if __name__ == '__main__':
    pyjd.setup("public/Hello.html?fred=foo#me")
    b = Button("Click me", greet, StyleName='teststyle')
    h = HTML("<b>Hello World</b> (html)", StyleName='teststyle')
    l = Label("Hello World (label)", StyleName='teststyle')
    base = HTML("Hello from %s" % pygwt.getModuleBaseURL(),
                                  StyleName='teststyle')

    rta = RichTextArea()
    rta.setWidth("100%")
    rta.setHeight("250px")
    rta.setHTML("fred <b>hello</b><br />bye")
    rta.setFocus(True)

    RootPanel().add(b)
    RootPanel().add(h)
    RootPanel().add(l)
    RootPanel().add(base)
    RootPanel().add(rta)
    pyjd.run()
