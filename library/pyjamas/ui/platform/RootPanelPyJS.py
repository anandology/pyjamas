class RootPanelCls(AbsolutePanel):
    def getBodyElement(self):
        JS("""
        return $doc.body;
        """)
