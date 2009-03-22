from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Button import Button
from pyjamas import Window

def greet(fred):
    Window.alert("Hello, AJAX!")

if __name__ == '__main__':
    b = Button("Click me", greet)
    RootPanel().add(b)
