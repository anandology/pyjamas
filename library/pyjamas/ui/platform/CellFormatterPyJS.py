class CellFormatter:

    def getCellElement(self, table, row, col):
        JS("""
        var out = table.rows[row].cells[col];
        return (out == null ? null : out);
        """)

