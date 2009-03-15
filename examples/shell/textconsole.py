from pyjamas.ui.AbsolutePanel import AbsolutePanel
from pyjamas.ui.Label import Label
from pyjamas import DOM
from pyjamas import log
import math

class TextWindow(AbsolutePanel):

    def __init__(self, cols, rows, width, height):

        AbsolutePanel.__init__(self)
        self.rows = rows
        self.cols = cols
        self.setStyleName("gwt-TextWindow")

        DOM.setStyleAttribute(self.getElement(), 'fontFamily', 'monospace')

        self.setHeight(height)
        self.setWidth(width)

        self.text = {}
        for x in range(self.cols):
            self.text[x] = {}

    def _get_label(self, x, y):

        if not self.text[x].has_key(y):
            xpos = x * self.fontsize
            ypos = y * self.fontheight
            txt = Label(' ')
            self.add(txt, xpos, ypos)
            self.text[x][y] = txt
            
        return self.text[x][y]

    def setChar(self, x, y, char):

        label = self._get_label(x, y)
        label.setText(char)

    def setWidth(self, width):

        self.fontsize = math.floor(width / self.cols)
        AbsolutePanel.setWidth(self, "%dpx" % (self.cols*self.fontsize))

        ratio = self.fontsize / self.fontheight 
        DOM.setStyleAttribute(self.getElement(), 'fontSizeAdjust', ratio)
        #log.writebr(str(ratio))

    def setHeight(self, height):

        self.fontheight = math.floor(height / self.rows)
        AbsolutePanel.setHeight(self, "%dpx" % (self.rows*self.fontheight))

        DOM.setStyleAttribute(self.getElement(), 'fontSize', "%dpx" % self.fontheight)
        #log.writebr(str(self.fontheight))

    def setText(self, x, y, string):

        for i in range(len(string)):
            self.setChar(x+i, y, string[i])

