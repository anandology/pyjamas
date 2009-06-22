class FlexTable(HTMLTable):

    def addCells(self, table, row, num):
        JS("""
        var rowElem = table.rows[row];
        for(var i = 0; i < num; i++){
            var cell = $doc.createElement("td");
            rowElem.appendChild(cell);
        }
        """)


