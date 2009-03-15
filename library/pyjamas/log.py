from pyjamas import DOM

def getBodyElement():
    JS(" return $doc.body; ")

def write(text):
    global data, element
    text = text.replace("\n", r"<br />\n")
    data += text
    DOM.setInnerHTML(element, data)

def writebr(text):
    write(text + r"\n")

data = ""
element = DOM.createDiv()
DOM.appendChild(getBodyElement(), element)
