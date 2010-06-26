import pyjd # this is dummy in pyjs.
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Button import Button
from pyjamas.ui.HTML import HTML
from pyjamas.ui.Label import Label
from pyjamas import Window

import pygwt

from __pyjamas__ import doc
from pyjamas import DOM

class StyleSheetCssFileChanger:

    def __init__(self, cssFile=''):
        self._e = DOM.createElement('link')
        self._e.setAttribute('rel', 'stylesheet')
        self._e.setAttribute('type', 'text/css')
        self._e.setAttribute('href', cssFile);

        print "css file", cssFile
        doc().getElementsByTagName("head").item(0).appendChild(self._e) 

    def remove(self):
        parent = DOM.getParent(self._e)
        DOM.removeChild(parent, self._e) 
        
class StyleSheetCssChanger:

    def __init__(self, text=''):
        self._e = DOM.createElement('style')
        self._e.setAttribute('type', 'text/css')
        DOM.appendChild(self._e, doc().createTextNode(text))

        doc().getElementsByTagName("head").item(0).appendChild(self._e) 

    def remove(self):
        parent = DOM.getParent(self._e)
        DOM.removeChild(parent, self._e) 
        
newcolours = """
<!--
.teststyle {
  font-size: 100%;
  margin: 20px;
  padding: 20px;
  background-color: #8080ff;
}
-->
"""

morenewcolours = """
<!--
.teststyle {
  font-size: 200%;
  margin: 20px;
  padding: 20px;
  background-color: #ff80ff;
}
-->
"""

global sc
sc = None
def greet(fred):
    global sc
    txt = fred.getText() 
    if txt == "Click me lots":
        sc = StyleSheetCssChanger(newcolours)
        fred.setText("Did it work?")
    elif txt == "Did it work?":
        sc.remove()
        fred.setText("It did!")
    elif txt == "It did!":
        sc = StyleSheetCssChanger(morenewcolours)
        fred.setText("Play again!")
    elif txt != "Ok enough now":
        fred.setText("Ok enough now")
        sc.remove()

if __name__ == '__main__':
    pyjd.setup("public/CSSMess.html?fred=foo#me")
    b = Button("Click me lots", greet, StyleName='teststyle')
    h = HTML("<b>CSSMess World</b> (html)", StyleName='teststyle')
    l = Label("CSSMess World (label)", StyleName='teststyle')
    base = HTML("CSSMess from %s" % pygwt.getModuleBaseURL(),
                                  StyleName='teststyle')
    RootPanel().add(b)
    RootPanel().add(h)
    RootPanel().add(l)
    RootPanel().add(base)
    StyleSheetCssFileChanger("./CSSMess.css")
    pyjd.run()
