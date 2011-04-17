import pyjd # dummy in pyjs
from HangManWidget import HangManWidget
from pyjamas.ui.RootPanel import RootPanel


class HangMan:
    def onModuleLoad(self):
        self.webspace=HangManWidget() 
        RootPanel().add(self.webspace)
    

if __name__ == '__main__':
    # for pyjd, set up a web server and load the HTML from there:
    # this convinces the browser engine that the AJAX will be loaded
    # from the same URI base as the URL, it's all a bit messy...
    pyjd.setup("public/HangMan.html")
    app = HangMan()
    app.onModuleLoad()
    pyjd.run()
