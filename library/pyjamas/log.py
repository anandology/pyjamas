# Use this to output (cumulatively) text at the bottom of the HTML page

from pyjamas import DOM

def getBodyElement():
    JS(" return $doc.body; ")

def write(text):
    add_elem()
    global data, element
    text = text.replace("\n", r"<br />\n")
    data += text
    DOM.setInnerHTML(element, data)

def writebr(text):
    write(text + r"\n")

data = ""
element = None

def add_elem():
    global element
    if element is not None:
        return
    element = DOM.createDiv()
    DOM.appendChild(getBodyElement(), element)
