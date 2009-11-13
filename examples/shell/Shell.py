import pyjd

from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Controls import VerticalDemoSlider
from pyjamas import Window
from pyjamas.Timer import Timer
from textconsole import TextWindow
from Screen import Screen

try:
    import pyjslib
except:
    pass
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

        self.loading_apps = []
        self.loading_app = None
        self.loading_desc = None

        self.load_app('../../gridtest/output/', 'GridTest', 'grid test')
        self.load_app('../../widgets/output/', 'Widgets', 'clock')

    def load_app(self, path, appname, description):
        if self.loading_app is None:
            self.add_app(path, appname, description)
        else:
            self.loading_apps.append((path, appname, description))

    def add_app(self, path, appname, description):

        self.loading_app = appname
        self.loading_desc = description

        try:
            sys.setloadpath(path)
            pyjslib.preload_app_modules(sys.getloadpath(), [[appname]],
                                        self, 1, None)
        except:
            pass

    def onTimer(self, timerid):
        self.importDone()

    def importDone(self):

        mod = pyjslib.get_module(self.loading_app)
        if mod is None:
            Timer(500, self)
            return

        g = mod.AppInit()
        a = self.screen.add_app(g, self.loading_desc, 400, 300)
        a.show()
    
        self.loading_desc = None
        self.loading_app = None

        if self.loading_apps:
            path, appname, description = self.loading_apps.pop()
            self.add_app(path, appname, description )

if __name__ == '__main__':
    pyjd.setup('./public/Shell.html')
    app = ShellApp()
    pyjd.run()
