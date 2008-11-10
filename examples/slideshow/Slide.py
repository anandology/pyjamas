from Sink import Sink, SinkInfo
from pyjamas.ui import HTML, VerticalPanel
from SlideLoader import SlideLoader
from HTTPRequest import HTTPRequest
from pyjamas import Window

def ts(txt):
    l = txt.split('\n')
    return '<br />'.join(l)

class Slide(Sink):
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
        HTTPRequest().asyncPost("%s.txt" % name, "", SlideLoader(self))

    def setSlide(self, text):
        self.loaded = True
        ul_stack1 = 0
        ul_stack2 = 0
        txt = ''
        text += '\n'
        for line in text.split("\n"):
            line = line.strip()
            ul_line = False
            ul_line2 = False
            add = False
            if not line:
                line = "&nbsp;"
            elif line[:2] == '= ' and line[-2:] == ' =':
                line = "<h1 class='slide_heading1>%s</h1>" % line[2:-2]
            elif line[:3] == '== ' and line[-3:] == ' ==':
                line = "<h2 class='slide_heading2>%s</h2>" % line[3:-3]
            elif line[:2] == '* ':
                if not ul_stack1:
                    txt += "<ul class='slide_list1'>\n"
                line = "<li class='slide_listitem1'/>%s\n" % ts(line[2:])
                ul_stack1 = True
                ul_line = True
            elif line[:3] == '** ':
                if not ul_stack2:
                    txt += "<ul class='slide_list2'>\n"
                line = "<li class='slide_listitem2'/>%s\n" % ts(line[2:])
                ul_stack2 = True
                ul_line2 = True
                ul_line = True
            else:
                line = "<p class='slide_para'>%s</p>" % line
            if ul_stack2 and not ul_line2:
                ul_stack2 = False
                txt += "</ul>\n"
            if ul_stack1 and not ul_line:
                ul_stack1 = False
                txt += "</ul>\n"
            if not ul_stack2 and not ul_stack1:
                add = True
            txt += line
            if add:
                self.vp.add(HTML(txt))
                txt = ''

    def onError(self, text, code):
        self.vp.add(HTML("TODO: Slide '%s' not loaded" % self.name))
        self.vp.add(HTML(text))
        self.vp.add(HTML(code))
        
def init(name, desc):
    return SinkInfo(name, desc, Slide)

