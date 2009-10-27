# Copyright 2006 James Tauber and contributors
# Copyright (C) 2009 Luke Kenneth Casson Leighton <lkcl@lkcl.net>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import sys
if sys.platform not in ['mozilla', 'ie6', 'opera', 'oldmoz', 'safari']:
    from __pyjamas__ import doc
from pyjamas import Factory

from pyjamas import DOM

from HTMLTable import HTMLTable
from RowFormatter import RowFormatter
from FlexCellFormatter import FlexCellFormatter 

class FlexTable(HTMLTable):
    def __init__(self, **kwargs):
        if not kwargs.has_key('CellFormatter'):
            kwargs['CellFormatter'] = FlexCellFormatter(self)
        HTMLTable.__init__(self, **kwargs)

    def addCell(self, row):
        self.insertCell(row, self.getCellCount(row))

    def getCellCount(self, row):
        self.checkRowBounds(row)
        return self.getDOMCellCount(self.getBodyElement(), row)

    def getFlexCellFormatter(self):
        return self.getCellFormatter()

    def getRowCount(self):
        return self.getDOMRowCount()

    def removeCells(self, row, column, num):
        i = 0
        while i < num:
            self.removeCell(row, column)
            i += 1

    def prepareCell(self, row, column):
        self.prepareRow(row)
        #if column < 0: throw new IndexOutOfBoundsException("Cannot create a column with a negative index: " + column);

        cellCount = self.getCellCount(row)
        required = column + 1 - cellCount
        if required > 0:
            self.addCells(self.getBodyElement(), row, required)

    def prepareRow(self, row):
        #if row < 0: throw new IndexOutOfBoundsException("Cannot create a row with a negative index: " + row);

        rowCount = self.getRowCount()
        #for i in range(rowCount, row + 1):
        i = rowCount
        while i <= row:
            self.insertRow(i)
            i += 1

    def addCells(self, table, row, num):
        rowElem = table.rows.item(row)
        i = 0
        while i < num:
            cell = doc().createElement("td")
            rowElem.appendChild(cell)
            i += 1

Factory.registerClass('pyjamas.ui.FlexTable', FlexTable)

