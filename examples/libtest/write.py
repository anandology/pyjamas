import sys
import re

tag_re = re.compile("<.*?>")

def write(text):
    pass

def writebr(text):
    pass


data = ""
element = None

def write_web(text):
    global data, element
    from __pyjamas__ import JS
    data += text
    JS("@{{element}}.innerHTML = @{{data}}; ")

def writebr_web(text):
    write(text + "<br />\n")

def init_web():
    from __pyjamas__ import JS
    global element
    JS("""@{{element}} = $doc.createElement("div");
           $doc.body.appendChild(@{{element}}); """)

def write_std(text):
    text = tag_re.sub("",text)
    print text,

def writebr_std(text):
    text = tag_re.sub("",text)
    print text

if sys.platform in ['mozilla', 'ie6', 'opera', 'oldmoz', 'safari']:
    init_web()
    write = write_web
    writebr = writebr_web
else:
    write = write_std
    writebr = writebr_std
