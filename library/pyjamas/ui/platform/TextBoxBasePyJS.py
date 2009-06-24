
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

    def setSelectionRange(self, pos, length):
        if length < 0:
            # throw new IndexOutOfBoundsException("Length must be a positive integer. Length: " + length);
            console.error("Length must be a positive integer. Length: " + length)

        if (pos < 0) or (length + pos > len(self.getText())):
            #throw new IndexOutOfBoundsException("From Index: " + pos + "  To Index: " + (pos + length) + "  Text Length: " + getText().length());
            console.error("From Index: " + pos + "  To Index: " + (pos + length) + "  Text Length: " + len(self.getText()))

        element = self.getElement()
        element.setSelectionRange(pos, pos + length)

