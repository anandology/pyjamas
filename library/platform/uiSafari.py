# FocusImplOld
class Focus:

    def blur(self, elem):
        JS("""
        // Attempts to blur elements from within an event callback will
        // generally be unsuccessful, so we invoke blur() from outside of
        // the callback.
        $wnd.setTimeout(function() {
                                       elem.firstChild.blur();
                        },
                        0);
        """)
    
    def createFocusable(self):
        JS("""
        var div = $doc.createElement('div');
        var input = $doc.createElement('input');
        input.type = 'text';
        input.style.width = input.style.height = 0;
        input.style.zIndex = -1;
        input.style.position = 'absolute';

        input.addEventListener(
            'blur',
            function(evt) { if (this.parentNode.onblur) this.parentNode.onblur(evt); },
            false);

        input.addEventListener(
            'focus',
            function(evt) { if (this.parentNode.onfocus) this.parentNode.onfocus(evt); },
            false);

        div.addEventListener(
            'mousedown',
            function(evt) { this.firstChild.focus(); },
            false);
        
        div.appendChild(input);
        return div;
        """)

    def focus(self, elem):
        JS("""
        // Attempts to focus elements from within an event callback will
        // generally be unsuccessful, so we invoke focus() from outside of
        // the callback.
        $wnd.setTimeout(function() {
                                       elem.firstChild.focus();
                        },
                        0);
        """)
    
    def getTabIndex(self, elem):
        JS("""
        return elem.firstChild.tabIndex;
        """)
    
    def setAccessKey(self, elem, key):
        JS("""
        elem.firstChild.accessKey = key;
        """)
    
    def setTabIndex(self, elem, index):
        JS("""
        elem.firstChild.tabIndex = index;
        """)


class FormPanel:
    def getEncoding(self, form):
        JS("""
        return form.enctype;
        """)

    def setEncoding(self, form, encoding):
        JS("""
        form.enctype = encoding;
        """)

