from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Controls import VerticalDemoSlider
from pyjamas import Window
from pyjamas.Timer import Timer
from textconsole import TextWindow
from Screen import Screen

import pyjslib
import sys

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


class ShellApp():
    def __init__(self):

        self.GridTest = None

        self.screen = Screen(Window.getClientWidth(), Window.getClientHeight())
        w = text_app()
        a = self.screen.add_app(w, "text 1", 400, 300)
        a.show()
        w = text_app()
        a = self.screen.add_app(w, "text 2", 400, 300)
        a.show()
        w = slider_app()
        a = self.screen.add_app(w, "s", 20, 100)
        a.show()

        RootPanel().add(self.screen)

        sys.setloadpath('../../gridtest/output/')
        pyjslib.preload_app_modules(sys.getloadpath(), [['GridTest']],
                                    self, 1,
                                    'GridTest')


    def onTimer(self, timer_id):
        self.GridTest = pyjslib.get_module('GridTest')
        if self.GridTest is None:
            Timer(500, self.wait_app_load)
            return

        g = self.GridTest.GridWidget()
        a = self.screen.add_app(g, "grid test", 400, 300)
        a.show()
    
    def importDone(self):
        Timer(500, self)

app = None
if __name__ == '__main__':
    global app
    app = ShellApp()

