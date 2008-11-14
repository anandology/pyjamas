from Sink import Sink, SinkInfo
from pyjamas.ui import HTML, VerticalPanel
from BookLoader import ChapterLoader
from pyjamas.HTTPRequest import HTTPRequest
from pyjamas import Window

def escape(txt, esc=1):
    if not esc:
        return txt
    txt = txt.replace("&", "&amp;")
    txt = txt.replace("<", "&lt;")
    txt = txt.replace(">", "&gt;")
    txt = txt.replace("%", "&#37;")
    return txt

def urlmap(txt, esc=1):
    idx = txt.find("http://")
    if idx == -1:
        idx = txt.find("https://")
    if idx == -1:
        return escape(txt, esc)
    for i in range(idx+7, len(txt)):
        c = txt[i]
        if c == ' ' or c == '\n' or c == '\t' or c == ',' or c == '<' or c == ')' or c == '(' or c == '>':
            i -= 1
            break
        # full-stop space test
        if i != len(txt)-1:
            c1 = txt[i+1]
            if (c1 == ' ' or c1 == '\n') and (c == '.' or c == ':'):
                i -= 1
                break

    i += 1

    beg = txt[:idx]
    if i == len(txt):
        url = txt[idx:]
        end = ''
    else:
        url = txt[idx:i]
        end = txt[i:]
    txt = escape(beg, esc) + "<a href='%s'>" % url
    txt += "%s</a>" % escape(url) + urlmap(end, esc)
    return txt
 
def ts(txt, esc=1):
    l = txt.split('\n')
    r = []
    for line in l:
        line = line.replace("%", "&#37;")
        r.append(urlmap(line, esc))
    return '<br />'.join(r)

def qr(line):
    return line.replace("'", "&#39;")

class Chapter(Sink):
    def __init__(self):

        Sink.__init__(self)

        text="<div class='infoProse'>This is the Kitchen Sink sample.  "

        self.vp = VerticalPanel()
        self.initWidget(self.vp)
        self.loaded = False

    def onShow(self):

        if self.loaded:
            return 

        name = self.name.replace(" ", "_")
        name = name.lower()
        HTTPRequest().asyncPost("%s.txt" % name, "", ChapterLoader(self))

    def setChapter(self, text):
        self.loaded = True
        ul_stack1 = 0
        ul_stack2 = 0
        doing_code = 0
        custom_style = False
        txt = ''
        para = ''
        text += '\n'
        for line in text.split("\n"):
            if doing_code:
                if line == "}}":
                    doing_code = 0
                    custom_style = False
                    line = "</pre>"
                    txt += line
                    self.vp.add(HTML(txt))
                    txt = ''
                    continue
                if line:
                    if not custom_style:
                        txt += escape(line)
                    else:
                        txt += line
                txt += "\n"
                continue
                
            line = line.strip()
            ul_line = False
            ul_line2 = False
            addline = ''
            add = False
            addpara = False
            if not line:
                line = ""
                addpara = True
            elif line[:2] == "{{":
                doing_code = 1
                addpara = True
                if len(line) > 4 and line[2] == '-':
                    addline = "<pre class='chapter_%s'>" % line[3:]
                    custom_style = True
                elif len(line) > 2:
                    addline = "<pre class='chapter_code'>%s" % line[2:]
                else:
                    addline = "<pre class='chapter_code'>"
            elif line[:2] == '= ' and line[-2:] == ' =':
                addline = "<h1 class='chapter_heading1>%s</h1>" % qr(line[2:-2])
                add = True
                addpara = True
            elif line[:3] == '== ' and line[-3:] == ' ==':
                addline = "<h2 class='chapter_heading2>%s</h2>" % qr(line[3:-3])
                add = True
                addpara = True
            elif line[:2] == '* ':
                if not ul_stack1:
                    txt += "<ul class='chapter_list1'>\n"
                addline = "<li class='chapter_listitem1'/>%s\n" % ts(line[2:], 0)
                ul_stack1 = True
                ul_line = True
                addpara = True
            elif line[:3] == '** ':
                if not ul_stack2:
                    txt += "<ul class='chapter_list2'>\n"
                addline = "<li class='chapter_listitem2'/>%s\n" % ts(line[2:], 0)
                ul_stack2 = True
                ul_line2 = True
                ul_line = True
            if ul_stack2 and not ul_line2:
                ul_stack2 = False
                txt += "</ul>\n"
            if ul_stack1 and not ul_line:
                ul_stack1 = False
                txt += "</ul>\n"
            if addline:
                txt += addline + "\n"
            elif line:
                line = line.replace("%", "&#37;")
                para += line + "\n"
            if not ul_stack2 and not ul_stack1 and not doing_code :
                add = True
            if para and addpara:
                para = "<p class='chapter_para'>%s</p>" % urlmap(para, 0)
                self.vp.add(HTML(para))
                para = ''
            if add:
                self.vp.add(HTML(txt))
                txt = ''

    def onError(self, text, code):
        self.vp.clear()
        self.vp.add(HTML("TODO: Chapter '%s' not loaded" % self.name))
        self.vp.add(HTML(text))
        self.vp.add(HTML(code))
        
def init(name, desc):
    return SinkInfo(name, desc, Chapter)

