"""
The ``ui.Grid`` class implements a panel which lays its contents out in a
grid-like fashion, very like an HTML table.

You can use the ``setHTML(row, col, html)`` method to set the HTML-formatted
text to be displayed at the given row and column within the grid.  Similarly,
you can call ``setText(row, col, text)`` to display plain (unformatted) text at
the given row and column.
"""
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.Grid import Grid

class GridDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        grid = Grid(5, 5)
        grid.setHTML(0, 0, '<b>Hello, World!</b>')
        grid.setBorderWidth(2)
        grid.setCellPadding(4)
        grid.setCellSpacing(1)

        for row in range(1, 5):
            for col in range(1, 5):
                grid.setText(row, col, str(row) + "*" + str(col) + " = " + str(row*col))

        self.add(grid)

