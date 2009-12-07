
# vim: set ts=4 sw=4 expandtab:

import pyjamas.ui.Grid

class Grid(pyjamas.ui.Grid.Grid):

    def __init__(self, topHeader = True, leftBorder=True):
        pyjamas.ui.Grid.Grid.__init__(self)
        self.selectedRow = 0
        if topHeader:
            self.top = 1
        else:
            self.top = 0
        if leftBorder:
            self.left = 1
        else:
            self.left = 0

    def createGrid(self, rows, cols):
        self.resize(rows+self.top, cols+self.left)
        self.values = {}
        self.getRowFormatter().addStyleName(0, "gwt-BorderRow")
        for row in range(rows):
            self.values[row] = {}
            self.values[row][0] = row
            self.getRowFormatter().addStyleName(row+1, "gwt-UnselectedRow")
            self.getCellFormatter().addStyleName(row+1, 0, "gwt-BorderCell")
            self.setHTML(row+1, 0, "<b>%s</b>" % (row+1))
            for col in range(0,cols):
                self.setCellValue(row, col, "")

    def setColLabelValue(self, col, value):
        self.setHTML(0, col+self.left, '<b>%s</b>'% value)

    def setRowLabelValue(self, row, value):
        self.setHTML(row+self.top, 0, '<b>%s</b>' % value)

    def setCellValue(self, row, col, value):
        self.values[row][col] = value
        if value == "":
            value = "&nbsp;"
        self.setHTML(row+self.top, col+self.left, value)

    def clearGrid(self):
        for row in range(1, self.getRowCount()):
            for col in range(1, self.getColumnCount()):
                self.clearCell(row, col)
        self.selectRow(-1)

    def selectRow(self, row):
        self.styleRow(self.selectedRow, False)
        self.styleRow(row, True)
        self.selectedRow = row

    def styleRow(self, row, selected):
        if row > 0 and row < self.getRowCount():
            if selected:
                self.getRowFormatter().addStyleName(row, "gwt-SelectedRow")
            else:
                self.getRowFormatter().removeStyleName(row, "gwt-SelectedRow")
            
