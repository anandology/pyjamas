from pyjamas import DOM

def getBodyElement():
    JS(""" return $doc.body; """)

def write(text):
    global data, element
    data += text
    DOM.setInnerHTML(element, data)

def writebr(text):
    write(text + r"<BR>\n")

data = ""
element = DOM.createDiv()
DOM.appendChild(getBodyElement(), element)
