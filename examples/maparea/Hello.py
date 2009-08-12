import pyjd

from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Button import Button
from pyjamas.ui.HTML import HTML
from pyjamas import Window

from Map import dosomething

def greet(fred):
    Window.alert("Hello, AJAX!")

if __name__ == '__main__':
    pyjd.setup("./public/Hello.html")
    b = Button("Click me", greet)
    RootPanel().add(b)
    RootPanel().add(HTML("move mouse over top left corner of baby katie"))
    RootPanel().add(dosomething())
    pyjd.run()
