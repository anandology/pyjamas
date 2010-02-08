from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.HTML import HTML
from pyjamas.ui.TextArea import TextArea
from pyjamas.ui.Label import Label
from pyjamas.ui import InnerHTML
from pyjamas.ui.KeyboardListener import KeyboardHandler
from pyjamas.JSONService import JSONProxy

from __javascript__ import Showdown
from __pyjamas__ import JS
from __pyjamas__ import jsimport

from pyjamas import log
from pyjamas import History

jsimport("showdown.js")

def getShowdown():
    JS("""return new Showdown.converter()""")

class WikiBox(HTML):
    def __init__(self, html=None, wordWrap=True, Element=None, **kwargs):
        self.converter = getShowdown()
        HTML.__init__(self, html, wordWrap, Element, **kwargs)
    def setHTML(self, text):
        newText = self.converter.makeHtml(text)
        InnerHTML.setHTML(self, newText)

class Wiki(KeyboardHandler):
    def __init__(self):
        self.remote = DataService()

        self.title = Label()
        self.h = WikiBox()
        self.t = TextArea()
        self.t.addKeyboardListener(self)
        self.t.addChangeListener(self)
        RootPanel().add(self.title)
        RootPanel().add(self.h)
        RootPanel().add(self.t)
        History.addHistoryListener(self)
        self.name = None
        initToken = History.getToken()
        if not (initToken and len(initToken)):
            initToken = 'welcome'
        self.onHistoryChanged(initToken)

    def onHistoryChanged(self,token):
        self.name = token
        self.title.setText('Wiki page for: ' + token)
        self.remote.find_one(token,self)

    def onChange(self, sender):
        if sender == self.t:
            self.remote.insert(self.name,
                    self.t.getText(),
                    self)

    def onRemoteResponse(self, response, request_info): 
        if request_info.method == 'find_one':
            self.h.setHTML(response['content'])
            self.t.setText(response['content'])

    def onRemoteError(self, code, message, request_info):
        log.writebr('remote error! ' + message)
        log.writebr('remote error! ' + request_info)

    def onKeyUp(self, sender, keycode, modifiers): 
        if sender == self.t:
            self.h.setHTML(self.t.getText())

class DataService(JSONProxy):
    def __init__(self):
        JSONProxy.__init__(self, '../json', ['find_one','insert'])

if __name__ == '__main__':
    Wiki()
