import pyjd # dummy in pyjs

from pyjamas.ui.TabBar import TabBar
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
from pyjamas.ui.DecoratorPanel import DecoratedTabPanel, DecoratorPanel
from pyjamas.ui.DecoratorPanel import DecoratorTitledPanel

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
        self.fTabs.add(self.createImage("rembrandt/JohannesElison.jpg"),
                        red, True, name="johannes")
        self.fTabs.add(self.createImage("rembrandt/SelfPortrait1640.jpg"),
                        green, True, name="self")
        self.fTabs.add(self.createImage("rembrandt/LaMarcheNocturne.jpg"),
                        "1642", name="lamarche")
        self.fTabs.add(self.createImage(
                        "rembrandt/TheReturnOfTheProdigalSon.jpg"),"1662",
                        "prodigal")
        self.fTabs.add(HTML("shouldn't be here!"), None) # None means separator
        self.fTabs.add(HTML("This is a Test.<br />Tab should be on right"),
                       "Test", "test")
        self.fTabs.selectTab(0)

        dp = DecoratorTitledPanel("Tabs", "bluetitle", "bluetitleicon",
                      ["bluetop", "bluetop2", "bluemiddle", "bluebottom"])
        dp.add(self.fTabs)
        RootPanel().add(dp)

        self.fTabs.addTabListener(self)

    def createImage(self, imageUrl):
        image = Image(imageUrl)
        image.setStyleName("ks-images-Image")
        
        p = VerticalPanel()
        p.setHorizontalAlignment(HasAlignment.ALIGN_CENTER)
        p.setVerticalAlignment(HasAlignment.ALIGN_MIDDLE)
        p.add(image)

        return p

    def onTabSelected(self, sender, tabIndex):
        pass

    def onBeforeTabSelected(self, sender, tabIndex):
        # 6 because one of them is the separator.
        if self.fTabs.getWidgetCount() == 6:
            self.fTabs.add(HTML("2nd Test.<br />Tab should be on right"),
                           "2nd Test", name="test2")
            return True
        self.fTabs.remove("test2")
        return tabIndex != 6 # don't allow change to tab 6 - we're removing it!

if __name__ == '__main__':
    pyjd.setup("./public/Tabs.html")
    app = Tabs()
    app.onModuleLoad()
    pyjd.run()

