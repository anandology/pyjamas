import pyjd # dummy in pyjs

from pyjamas.ui.Button import Button
from pyjamas.ui.RootPanel import RootPanel
from pyjamas import Window


def onButtonClick(sender):
	Window.alert("function called")


class OnClickTest:
	def onModuleLoad(self):
		self.b = Button("function callback", onButtonClick)
		self.b2 = Button("object callback", self)
		RootPanel().add(self.b)
		RootPanel().add(self.b2)

	def onClick(self, sender):
		Window.alert("object called")






if __name__ == '__main__':
    pyjd.setup("./OnClickTest.html") # dummy in pyjs
    app = OnClickTest()
    app.onModuleLoad()
    pyjd.run() # dummy in pyjs
