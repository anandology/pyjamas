import pyjd # dummy in pyjs

from pyjamas.ui.Button import Button
from pyjamas.ui.RootPanel import RootPanel
from pyjamas import Window


def onButtonClick(sender):
	Window.alert("function called")

class Object(object):
    pass

class OnClickTest:
    def onModuleLoad(self):
        def localFunc(sender):
            Window.alert("anon object + local func called")
        obj = Object()
        setattr(obj, 'onClick', localFunc)
        self.b = Button("function callback", onButtonClick)
        self.b2 = Button("object callback", self)
        self.b3 = Button("anon object + local func callback", obj)
        RootPanel().add(self.b)
        RootPanel().add(self.b2)
        RootPanel().add(self.b3)

    def onClick(self, sender):
        Window.alert("object called")

if __name__ == '__main__':
    pyjd.setup("./OnClickTest.html") # dummy in pyjs
    app = OnClickTest()
    app.onModuleLoad()
    pyjd.run() # dummy in pyjs
