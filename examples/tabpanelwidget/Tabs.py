import pyjd # dummy in pyjs

from pyjamas.ui.TabPanel import TabPanel
from pyjamas.ui import HasAlignment
from pyjamas.ui.Image import Image
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.HTML import HTML
from pyjamas.ui.Composite import Composite
#from pyjamas.ui import DecoratorPanel
from pyjamas.ui import MouseListener
from pyjamas.ui import Event
from pyjamas import Window
from pyjamas.ui.decoratorpanel import DecoratedTabPanel, DecoratorPanel
from pyjamas.ui.decoratorpanel import DecoratorTitledPanel

#class PrettyTab(DecoratorPanel):
class PrettyTab(Composite):

    def __init__(self, text, imageUrl):

        DecoratorPanel.__init__(self, DecoratorPanel.DECORATE_ALL)

        p = HorizontalPanel()
        p.setSpacing(3)
        self.img = Image(imageUrl)
        self.txt = HTML(text)
        p.add(self.img)
        p.add(self.txt)

        self.add(p)

    def addClickListener(self, listener):

        self.img.addClickListener(listener)
        self.txt.addClickListener(listener)

class Tabs:

    def onModuleLoad(self):

        #red = PrettyTab("1638", "images/user_red.png")
        #red.setStyleName('gwt-TabBarItem')

        #green = PrettyTab("1640", "images/user_green.png")
        #red.setStyleName('gwt-TabBarItem')
        red = "1638"
        green = "1640"

        self.fTabs = DecoratedTabPanel(Size=("600px", "100%"))
        self.fTabs.add(self.createImage("rembrandt/JohannesElison.jpg"), red, True)
        self.fTabs.add(self.createImage("rembrandt/SelfPortrait1640.jpg"), green, True)
        self.fTabs.add(self.createImage("rembrandt/LaMarcheNocturne.jpg"), "1642")
        self.fTabs.add(self.createImage("rembrandt/TheReturnOfTheProdigalSon.jpg"), "1662")
        self.fTabs.selectTab(0)

        dp = DecoratorTitledPanel("Tabs", "bluetitle", "bluetitleicon",
                      ["bluetop", "bluetop2", "bluemiddle", "bluebottom"])
        dp.add(self.fTabs)
        RootPanel().add(dp)

    def createImage(self, imageUrl):
        image = Image(imageUrl)
        image.setStyleName("ks-images-Image")
        
        p = VerticalPanel()
        p.setHorizontalAlignment(HasAlignment.ALIGN_CENTER)
        p.setVerticalAlignment(HasAlignment.ALIGN_MIDDLE)
        p.add(image)

        return p

if __name__ == '__main__':
    pyjd.setup("./public/Tabs.html")
    app = Tabs()
    app.onModuleLoad()
    pyjd.run()

