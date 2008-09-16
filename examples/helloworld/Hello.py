from pyjamas.ui import Button, RootPanel
from pyjamas import Window

def greet(sender):
    Window.alert("Hello, AJAX!")

class Hello:
    def onModuleLoad(self):
        b = Button("Click me", greet)
        RootPanel().add(b)
