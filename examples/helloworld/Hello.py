#import pyjd # this is dummy in pyjs.
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Button import Button
from pyjamas import Window
#from __pyjamas__ import JS

def greet(fred):
    print "greet button"
    Window.alert("Hello, AJAX!")

if __name__ == '__main__':
    #pyjd.setup("public/Hello.html")
    print "hoschi"
    #print "-----root-------",  RootPanel
    b = Button("Click me", greet)
    RootPanel().add(b)
    #pyjd.run()
