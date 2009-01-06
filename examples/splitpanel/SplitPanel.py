from pyjamas.ui import RootPanel, HTML, Label, HasAlignment, Button
from pyjamas import Window

from pyjamas.vertsplitpanel import VerticalSplitPanel
from pyjamas.horizsplitpanel import HorizontalSplitPanel

class SplitPanel:

    def onModuleLoad(self):
        self.vertpanel=VerticalSplitPanel()
        self.vertpanel.setSize("500px", "350px")
        self.vertpanel.setSplitPosition("30%")

        self.horzpanel=HorizontalSplitPanel()
        self.horzpanel.setSize("500px", "350px")
        self.horzpanel.setSplitPosition("30%")

        randomText = ""
        for i in range(200):
            randomText += "hello %d " % i

        self.vertpanel.setTopWidget(HTML(randomText))
        self.vertpanel.setBottomWidget(HTML(randomText))

        self.horzpanel.setLeftWidget(HTML(randomText))
        self.horzpanel.setRightWidget(HTML(randomText))

        RootPanel().add(self.vertpanel)
        RootPanel().add(self.horzpanel)
