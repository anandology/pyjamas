class PopupPanel:
    
    # PopupImpl.onShow
    def onShowImpl(self, popup):
        JS("""
        var frame = $doc.createElement('iframe');
        frame.scrolling = 'no';
        frame.frameBorder = 0;
        frame.style.position = 'absolute';
        
        popup.__frame = frame;
        frame.__popup = popup;
        frame.style.setExpression('left', 'this.__popup.offsetLeft');
        frame.style.setExpression('top', 'this.__popup.offsetTop');
        frame.style.setExpression('width', 'this.__popup.offsetWidth');
        frame.style.setExpression('height', 'this.__popup.offsetHeight');
        popup.parentElement.insertBefore(frame, popup);
        """)

    # PopupImpl.onHide
    def onHideImpl(self, popup):
        JS("""
        var frame = popup.__frame;
        frame.parentElement.removeChild(frame);
        popup.__frame = null;
        frame.__popup = null;
        """)


class TextBoxBase:
    def getCursorPos(self):
        JS("""
        try {
            var elem = this.getElement();
            var tr = elem.document.selection.createRange();
            if (tr.parentElement().uniqueID != elem.uniqueID)
                return -1;
            return -tr.move("character", -65535);
        }
        catch (e) {
            return 0;
        }
        """)

    def getSelectionLength(self):
        JS("""
        try {
            var elem = this.getElement();
            var tr = elem.document.selection.createRange();
            if (tr.parentElement().uniqueID != elem.uniqueID)
                return 0;
            return tr.text.length;
        }
        catch (e) {
            return 0;
        }
        """)

    def setSelectionRange(self, pos, length):
        JS("""
        try {
            var elem = this.getElement();
            var tr = elem.createTextRange();
            tr.collapse(true);
            tr.moveStart('character', pos);
            tr.moveEnd('character', length);
            tr.select();
        }
        catch (e) {
        }
        """)

class TextArea:
    def getCursorPos(self):
        JS("""
        try {
            var elem = this.getElement();
            var tr = elem.document.selection.createRange();
            var tr2 = tr.duplicate();
            tr2.moveToElementText(elem);
            tr.setEndPoint('EndToStart', tr2);
            return tr.text.length;
        }
        catch (e) {
            return 0;
        }
        """)


class FormPanel:
    def getTextContents(self, iframe):
        JS("""
        try {
            if (!iframe.contentWindow.document)
                return null;
        
            return iframe.contentWindow.document.body.innerText;
        } catch (e) {
            return null;
        }
        """)

    def hookEvents(self, iframe, form, listener):
        JS("""
        if (iframe) {
            iframe.onreadystatechange = function() {
                if (!iframe.__formAction)
                    return;
        
                if (iframe.readyState == 'complete') {
                    listener.onFrameLoad();
                }
            };
        }

        form.onsubmit = function() {
            if (iframe)
                iframe.__formAction = form.action;
            return listener.onFormSubmit();
        };
        """)

    def unhookEvents(self, iframe, form):
        JS("""
        if (iframe)
            iframe.onreadystatechange = null;
        form.onsubmit = null;
        """)

