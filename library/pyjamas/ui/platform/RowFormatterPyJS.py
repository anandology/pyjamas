class RowFormatter:

    def getRow(self, element, row):
        JS("""
        return element.rows[row];
        """)

