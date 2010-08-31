import pyjd
import sys
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.HTML import HTML
from pyjamas.ui.HTMLLinkPanel import HTMLLinkPanel
from pyjamas.ui.TextArea import TextArea
from pyjamas.ui.Label import Label
from pyjamas.ui.KeyboardListener import KeyboardHandler
from pyjamas.JSONService import JSONProxy

from pyjamas import log
from pyjamas import History

from markdown import makeHTML, makeWikiLinks

class WikiBox(HTMLLinkPanel):

    def setHTML(self, text):
        text = makeWikiLinks(text)
        text = makeHTML(text)
        HTMLLinkPanel.setHTML(self, text)
        self.replaceLinks(use_page_href=False)

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
            initToken = 'welcomepage'
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
        log.writebr('remote error! ' + str(message))
        log.writebr('remote error! ' + str(request_info))

    def onKeyUp(self, sender, keycode, modifiers): 
        if sender == self.t:
            self.h.setHTML(self.t.getText())

class DataService(JSONProxy):
    def __init__(self):
        JSONProxy.__init__(self, '/json', ['find_one','insert'])

if __name__ == '__main__':
    pyjd.setup("http://127.0.0.1:8080/Wiki.html")
    Wiki()
    pyjd.run()

