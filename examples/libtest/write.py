import sys

if sys.platform in ['mozilla', 'ie6', 'opera', 'oldmoz', 'safari']:
    from pyjamas import DOM
    def getBodyElement():
        JS(" return $doc.body; ")

    def write(text):
        global data, element
        data += text
        DOM.setInnerHTML(element, data)

    def writebr(text):
        write(text + r"<br />\n")

    data = ""
    element = DOM.createDiv()
    DOM.appendChild(getBodyElement(), element)

else:
    def write(text):
        sys.stdout.write(text)
    def writebr(text):
        sys.stdout.write(text + "\n")

