from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Controls import VerticalDemoSlider
from pyjamas import Window
from textconsole import TextWindow
from Screen import Screen

def slider_app():
    b = VerticalDemoSlider(0, 100)
    b.setWidth("20px")
    b.setHeight("100px")
    return b

def text_app():
    w = TextWindow(80, 20, 400, 300)
    RootPanel().add(w)
    w.setText(0, 0, "hello")
    w.setText(0, 1, "fred")
    w.setText(0, 5, "goodbye")
    for i in range(40):
        for j in range(2):
            w.setText(i, j+10, ".")
    return w

if __name__ == '__main__':
    s = Screen(Window.getClientWidth(), Window.getClientHeight())
    w = text_app()
    a = s.add_app(w, "text 1", 400, 300)
    a.show()
    w = text_app()
    a = s.add_app(w, "text 2", 400, 300)
    a.show()
    w = slider_app()
    a = s.add_app(w, "s", 20, 100)
    a.show()
