"""
Added for pyjamas
"""

import pyjamas.ui.Grid

class Grid(pyjamas.ui.Grid.Grid):

    def __init__(self):
        pyjamas.ui.Grid.Grid.__init__(self)
        self.selectedRow = 0

    def createGrid(self, rows, cols):
        self.resize(rows+1, cols+1)
        self.values = {}
        self.getRowFormatter().addStyleName(0, "user-BorderRow")
        for row in range(rows):
            self.values[row] = {}
            self.values[row][0] = row
            self.getRowFormatter().addStyleName(row+1, "user-UnselectedRow")
            self.getCellFormatter().addStyleName(row+1, 0, "user-BorderCell")
            self.setHTML(row+1, 0, "<b>%s</b>" % (row+1))
            for col in range(0,cols):
                self.setCellValue(row, col, "")

    def setColLabelValue(self, col, value):
        self.setHTML(0, col+1, '<b>%s</b>'% value)

    def setRowLabelValue(self, row, value):
        self.setHTML(row+1, 0, '<b>%s</b>' % value)

    def setCellValue(self, row, col, value):
        self.values[row][col] = value
        if value == "":
            value = "&nbsp;"
        self.setHTML(row+1, col+1, value)

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
                self.getRowFormatter().addStyleName(row, "user-SelectedRow")
            else:
                self.getRowFormatter().removeStyleName(row, "user-SelectedRow")
            
