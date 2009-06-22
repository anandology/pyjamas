class Grid(HTMLTable):

    def addRows(self, table, numRows, columns):
        JS("""
        var td = $doc.createElement("td");
        td.innerHTML = "&nbsp;";
        var row = $doc.createElement("tr");
        for(var cellNum = 0; cellNum < columns; cellNum++) {
            var cell = td.cloneNode(true);
            row.appendChild(cell);
        }
        table.appendChild(row);
        for(var rowNum = 1; rowNum < numRows; rowNum++) {
            table.appendChild(row.cloneNode(true));
        }
        """)


