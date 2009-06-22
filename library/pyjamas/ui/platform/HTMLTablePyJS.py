class HTMLTable(Panel):

    def getDOMCellCountImpl(self, element, row):
        JS("""
        return element.rows[row].cells.length;
        """)

    def getDOMRowCountImpl(self, element):
        JS("""
        return element.rows.length;
        """)
