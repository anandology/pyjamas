from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.HTML import HTML
from pyjamas.ui.Label import Label
from pyjamas.ui import HasAlignment
from pyjamas.ui.Button import Button
from pyjamas import Window

from pyjamas.ui.vertsplitpanel import VerticalSplitPanel
from pyjamas.ui.horizsplitpanel import HorizontalSplitPanel

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


if __name__ == '__main__':
    app = SplitPanel()
    app.onModuleLoad()
