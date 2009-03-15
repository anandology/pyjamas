from popups import DialogBoxModal
from pyjamas.ui.AbsolutePanel import AbsolutePanel
from pyjamas import Window
from pyjamas import log

class Application(DialogBoxModal):
    def __init__(self, screen, title, width, height):
        DialogBoxModal.__init__(self, title)
        self.screen = screen
        self.setText(title)
        #self.setWidth(width)
        #self.setHeight(height)

    def onMouseDown(self, sender, x, y):
        #log.writebr("down %d %d" % (x, y))
        DialogBoxModal.onMouseDown(self, sender, x, y)
        self.dragged = False
        
    def onMouseMove(self, sender, x, y):
        #log.writebr("move %d %d" % (x, y))
        if self.dragStartX != x or self.dragStartY != y:
            if not self.dragged:
                self.screen.raise_app(self)
            self.dragged = True
        DialogBoxModal.onMouseMove(self, sender, x, y)

    def onMouseUp(self, sender, x, y):
        #log.writebr("up %d %d" % (x, y))
        DialogBoxModal.onMouseUp(self, sender, x, y)
        if not self.dragged:
            self.screen.raise_or_lower(self)

    def onClick(self, sender):
        if sender == self.closeButton:
            self.screen.close_app(self)

class Screen(AbsolutePanel):

    def __init__(self, width, height):

        AbsolutePanel.__init__(self)
        self.setWidth(width)
        self.setHeight(height)

        self.window = {}
        self.window_zindex = {}

    def add_app(self, app, title, width, height):

        sa = Application(self, title, width, height)
        sa.setWidget(app)
        self.window[title] = sa
        self.window_zindex[title] = len(self.window)-1

        return sa

    def set_app_zindex(self, title, zi):
        w = self.window[title]
        self.window_zindex[title] = zi
        w.setzIndex(zi)

    def lower_app(self, app):
        app_zi = self.window_zindex[app.identifier]
        for t in self.window_zindex.keys():
            w = self.window[t]
            zi = self.window_zindex[t]
            if zi < app_zi:
                self.set_app_zindex(t, zi+1)

        self.set_app_zindex(app.identifier, 0)

    def raise_app(self, app):
        app_zi = self.window_zindex[app.identifier]
        for t in self.window_zindex.keys():
            w = self.window[t]
            zi = self.window_zindex[t]
            if zi > app_zi:
                self.set_app_zindex(t, zi-1)

        app_zi = len(self.window)-1
        self.set_app_zindex(app.identifier, app_zi)

    def raise_or_lower(self, app):
        
        app_zi = self.window_zindex[app.identifier]
        if app_zi != len(self.window)-1:
            self.raise_app(app)
        else:
            self.lower_app(app)

    def close_app(self, app):
        
        app_zi = self.window_zindex[app.identifier]
        for t in self.window_zindex.keys():
            w = self.window[t]
            zi = self.window_zindex[t]
            if zi > app_zi:
                self.set_app_zindex(t, zi-1)

        t = self.window[app.identifier]
        if not self.remove(t):
            Window.alert("%s not in app" % app.identifier)
        del self.window[app.identifier]

