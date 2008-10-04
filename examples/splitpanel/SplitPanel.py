from pyjamas.ui import RootPanel, HTML, Label, HasAlignment, Button
from pyjamas import Window

from pyjamas.vertsplitpanel import VerticalSplitPanel

class SplitPanel:

    def onModuleLoad(self):
        self.panel=VerticalSplitPanel()
        
        self.panel.setSize("500px", "350px")
        self.panel.setSplitPosition("30%")

        randomText = ""
        for i in range(200):
            randomText += "hello "

        self.panel.setTopWidget(HTML(randomText))
        self.panel.setBottomWidget(HTML(randomText))

        RootPanel().add(self.panel)
