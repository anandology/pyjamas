from pyjamas import Window
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Button import Button

def greet(sender):
    Window.alert("Hello, AJAX!")

class Hello:
    def onModuleLoad(self):
        b = Button("Click me", greet)
        RootPanel().add(b)
