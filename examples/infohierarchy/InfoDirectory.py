from pyjamas.ui import RootPanel, HTML, Label, HasAlignment, Button
from pyjamas.ui import HorizontalPanel, AbsolutePanel, ScrollPanel, Grid
from pyjamas import Window

from pyjamas.horizsplitpanel import HorizontalSplitPanel

from Trees import Trees

class MidPanel(Grid):

    def __init__(self):
        Grid.__init__(self)
        self.resize(1, 1)

    def set_items(self, items):

        self.resizeRows(len(items))
        for i in range(len(items)):
            self.setHTML(i, 0, items[i])

class InfoDirectory:

    def onModuleLoad(self):

        self.tree_width = 300

        self.tp = HorizontalPanel()
        self.tp.setWidth("%dpx" % (self.tree_width-20))
        self.tp.setBorderWidth("1px")
        self.treeview = Trees()
        self.treeview.fTree.addTreeListener(self)
        self.sp = ScrollPanel()
        self.tp.add(self.treeview)
        self.sp.add(self.tp)

        self.horzpanel1 = HorizontalPanel()
        self.horzpanel1.setSize("100%", "100%")
        self.horzpanel1.setBorderWidth("1px")

        self.hp = HorizontalPanel()
        self.hp.setWidth("800px")
        self.hp.setHeight("100%")
        self.horzpanel2 = HorizontalSplitPanel()
        self.horzpanel2.setSize("100%", "100%")
        self.horzpanel2.setSplitPosition("200px")
        self.hp.add(self.horzpanel2)
        self.hp.setBorderWidth("1px")

        randomText = ""
        for i in range(200):
            randomText += "hello %d " % i

        self.horzpanel2.setLeftWidget(HTML(randomText))
        self.horzpanel2.setRightWidget(HTML(randomText))

        self.horzpanel1.add(self.sp)
        self.horzpanel1.add(self.hp)

        self.midpanel = MidPanel()

        RootPanel().add(self.horzpanel1)

        width = Window.getClientWidth()
        height = Window.getClientHeight()

        self.onWindowResized(width, height)
        Window.addWindowResizeListener(self)
  
    def onWindowResized(self, width, height):
        self.hp.setWidth("%dpx" % (width - self.tree_width))
        self.hp.setHeight("%dpx" % (height - 20))
        self.sp.setHeight("%dpx" % (height - 20))

    def onTreeItemStateChanged(self, item):
        if item.isSelected():
            self.onTreeItemSelected(item)

    def onTreeItemSelected(self, item):

        obj = item.getUserObject()
        if len(obj.children) != 0:
            self.clear_mid_panel()
            return

        self.set_mid_panel(obj.text)

    def clear_right_panel(self):
        self.horzpanel2.setRightWidget(HTML(""))

    def clear_mid_panel(self):
        self.clear_right_panel()
        self.horzpanel2.setLeftWidget(HTML(""))

    def set_mid_panel(self, fake_text):

        fake_items = []
        for i in range(len(fake_text)):
            fake_item = "%d - " % (i+1) + fake_text
            fake_items.append(fake_item)

        self.midpanel.set_items(fake_items)

        self.horzpanel2.setLeftWidget(self.midpanel)

