from Sink import Sink, SinkInfo
from pyjamas.ui import HTML, VerticalPanel
from SlideLoader import SlideLoader
from HTTPRequest import HTTPRequest

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
        for line in text.split("\n"):
            line = line.strip()
            if not line:
                line = "&nbsp;"
            elif line[:2] == '= ' and line[-2:] == ' =':
                line = "<h1 class='slide_heading1>%s</h1>" % line[2:-2]
            elif line[:3] == '== ' and line[-3:] == ' ==':
                line = "<h2 class='slide_heading2>%s</h2>" % line[3:-3]
            self.vp.add(HTML(line))

    def onError(self, text, code):
        self.vp.add(HTML("TODO: Slide '%s' not loaded" % self.name))
        self.vp.add(HTML(text))
        self.vp.add(HTML(code))
        
def init(name, desc):
    return SinkInfo(name, desc, Slide)

