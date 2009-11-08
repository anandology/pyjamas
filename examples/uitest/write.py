data = ""
global element

from __pyjamas__ import doc

def escape(s):
    s = s.replace("&", "&amp;")
    s = s.replace("<", "&lt;")
    s = s.replace(">", "&gt;")
    s = s.replace('"', "&quot;")
    return s

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

