
class TextBoxBase(FocusWidget):

    def getCursorPos(self):
        JS("""
        try {
            var element = this.getElement()
            return element.selectionStart;
        } catch (e) {
            return 0;
        }
        """)

    def getSelectionLength(self):
        JS("""
        try{
            var element = this.getElement()
            return element.selectionEnd - element.selectionStart;
        } catch (e) {
            return 0;
        }
        """)

