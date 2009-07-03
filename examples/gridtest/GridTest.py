import pyjd # this is dummy in pyjs

from pyjamas.ui.Button import Button
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Label import Label
from pyjamas.ui.Grid import Grid
from pyjamas.ui.CellFormatter import CellFormatter
from pyjamas.ui.RowFormatter import RowFormatter
from pyjamas.ui.HTMLTable import HTMLTable
from pyjamas.ui.CheckBox import CheckBox
from pyjamas.ui.AbsolutePanel import AbsolutePanel
from pyjamas import Window

class GridWidget(AbsolutePanel):

    def __init__(self):
        AbsolutePanel.__init__(self)

        self.page=0
        self.min_page=1
        self.max_page=10
        
        self.addb=Button("Next >", self)
        self.subb=Button("< Prev", self)
        
        self.g=Grid()
        self.g.resize(5, 5)
        self.g.setHTML(0, 0, "<b>Grid Test</b>")
        self.g.setBorderWidth(2)
        self.g.setCellPadding(4)
        self.g.setCellSpacing(1)
        
        self.updatePageDisplay()

        self.add(self.subb)
        self.add(self.addb)
        self.add(self.g)

    def onClick(self, sender):
	print sender
        if sender==self.addb:
            self.page+=1
        elif sender==self.subb:
            self.page-=1
        self.updatePageDisplay()
        

    def updatePageDisplay(self):
        if self.page<self.min_page: self.page=self.min_page
        elif self.page>self.max_page: self.page=self.max_page
        total_pages=(self.max_page-self.min_page) + 1
        
        self.g.setHTML(0, 4, "<b>page %d of %d</b>" % (self.page, total_pages))
        
        if self.page>=self.max_page:
            self.addb.setEnabled(False)
        else:
            self.addb.setEnabled(True)
            
        if self.page<=self.min_page:
            self.subb.setEnabled(False)
        else:
            self.subb.setEnabled(True)

        for y in range(1, 5):
            for x in range(5):
                self.g.setText(y, x, "%d (%d,%d)" % (self.page, x, y))

def AppInit():
    return GridWidget()

if __name__ == '__main__':
    pyjd.setup("./GridTest.html")
    g = GridWidget()
    RootPanel().add(g)
    pyjd.run()
