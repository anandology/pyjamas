data = ""
global element

from __pyjamas__ import doc, escape

def display_log_output():
    global element
    global data
    element = doc().createElement("div")
    doc().body.appendChild(element)
    element.innerHTML = escape(data)

def write(text):
    global data
    data += text

    print "data", data

def writebr(text):
    write(text + "<br />\n")

