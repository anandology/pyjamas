"""
The ``ui.FlexTable`` class implements a table that can have different numbers
of cells in each row, and single cells can span multiple rows and columns.

Each FlexTable has a ``FlexCellFormatter`` which you can use to format the
cells in the table.  The ``FlexCellFormatter`` has methods to set the row or
column spans for a cell, as well as change the cell alignment, as shown below.

Note that if you use row or column spanning, the cells on the rest of that row
or column will be moved over.  This can cause some surprising results.  Imagine
that you have a table like this:

    +---+---+---+
    | A | B | C |
    +---+---+---+
    | D | E | F |
    +---+---+---+

If you set up Cell 0,0 to span two columns, like this:

    flexTable.getFlexCellFormatter().setColSpan(0, 0, 2)

This will cause the table to end up looking like this:

    +-------+---+---+
    |   A   | B | C |
    +---+---+---+---+
    | D | E | F |
    +---+---+---+

you might expect cell B to be above cell E, but to make this happen you need to
place cell E at (1, 2) rather than (1, 1).

Each FlexTable also has a ``RowFormatter`` which can be used to change style
names, attributes, and the visibility of rows in the table.
"""
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.FlexTable import FlexTable
from pyjamas.ui import HasAlignment
from pyjamas.ui.Button import Button

class FlexTableDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        self._table = FlexTable()
        self._table.setBorderWidth(1)
        self._table.setWidth("100%")

        cellFormatter = self._table.getFlexCellFormatter()
        rowFormatter = self._table.getRowFormatter()

        self._table.setHTML(0, 0, "<b>Mammals</b>")
        self._table.setText(1, 0, "Cow")
        self._table.setText(1, 1, "Rat")
        self._table.setText(1, 2, "Dog")

        cellFormatter.setColSpan(0, 0, 3)
        cellFormatter.setHorizontalAlignment(0, 0, HasAlignment.ALIGN_CENTER)

        self._table.setWidget(2, 0, Button("Hide", getattr(self, "hideRows")))
        self._table.setText(2, 1, "1,1")
        self._table.setText(2, 2, "2,1")
        self._table.setText(3, 0, "1,2")
        self._table.setText(3, 1, "2,2")

        cellFormatter.setRowSpan(2, 0, 2)
        cellFormatter.setVerticalAlignment(2, 0, HasAlignment.ALIGN_MIDDLE)

        self._table.setWidget(4, 0, Button("Show", getattr(self, "showRows")))

        cellFormatter.setColSpan(4, 0, 3)

        rowFormatter.setVisible(4, False)

        self.add(self._table)


    def hideRows(self):
        rowFormatter = self._table.getRowFormatter()
        rowFormatter.setVisible(2, False)
        rowFormatter.setVisible(3, False)
        rowFormatter.setVisible(4, True)


    def showRows(self):
        rowFormatter = self._table.getRowFormatter()
        rowFormatter.setVisible(2, True)
        rowFormatter.setVisible(3, True)
        rowFormatter.setVisible(4, False)

