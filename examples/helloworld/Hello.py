#from pyjamas.ui import Button, RootPanel
from pyjamas import Window
import pyjamas.ui

def greet(sender):
    Window.alert("Hello, AJAX!")

class Hello:
    def onModuleLoad(self):
        b = ui.Button("Click me", greet)
        ui.RootPanel().add(b)
