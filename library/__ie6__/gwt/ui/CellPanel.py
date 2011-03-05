
class CellPanel:
    def setBorderWidth(self, width):
        if width is None:
            DOM.setAttribute(self.table, "border", None)
        else:
            DOM.setAttribute(self.table, "border", str(width))
