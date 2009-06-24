from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Button import Button
from pyjamas import Window
from pyjamas import loader

def greet(fred):
    Window.alert("Hello, AJAX!")

class Hello:
    def onModuleLoad(self):
        b = Button("Click me", greet)
        RootPanel().add(b)

if __name__ == '__main__':
    h = Hello()
    h.onModuleLoad()
    loader.run()
