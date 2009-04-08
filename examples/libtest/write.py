import sys

data = ""

def write_web(text):
    global data
    data += text
    JS(" write.element.innerHTML = write.data; ")

def writebr_web(text):
    write(text + r"<br />\n")

def init_web():
    JS(""" write.element = $doc.createElement("div");
           $doc.body.appendChild(write. element); """)

def write_std(text):
    sys.stdout.write(text)

def writebr_std(text):
    sys.stdout.write(text + "\n")

if sys.platform in ['mozilla', 'ie6', 'opera', 'oldmoz', 'safari']:

    init_web()
    write = write_web
    writebr = writebr_web
    global write
    global writebr

else:
    global write
    global writebr
    write = write_std
    writebr = writebr_std

