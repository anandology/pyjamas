class TextBoxBase:
    def getCursorPos(self):
        try :
            elem = this.getElement()
            tr = elem.document.selection.createRange()
            if tr.parentElement().uniqueID != elem.uniqueID:
                return -1
            return -tr.move("character", -65535)
        except :
            return 0

    def getSelectionLength(self):
        try :
            elem = this.getElement()
            tr = elem.document.selection.createRange()
            if tr.parentElement().uniqueID != elem.uniqueID:
                return 0
            return tr.text.length
        except :
            return 0

    def setSelectionRange(self, pos, length):
        try :
            elem = this.getElement()
            tr = elem.createTextRange()
            tr.collapse(true)
            tr.moveStart('character', pos)
            tr.moveEnd('character', length)
            tr.select()
        except :
            pass

