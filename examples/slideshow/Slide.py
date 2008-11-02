from Sink import Sink, SinkInfo
from pyjamas.ui import HTML, VerticalPanel
from SlideLoader import SlideLoader


class Slide(Sink):
    def __init__(self):

        Sink.__init__(self)

        text="<div class='infoProse'>This is the Kitchen Sink sample.  "

        self.vp = VerticalPanel()
        self.initWidget(self.vp)

        name = self.name.replace(" ", "_")
        name = name.lower()
        HTTPRequest().asyncPost(name, "", SlideLoader(self))

    def onShow(self):
        pass

    def setSlide(self, text):
        self.vp.add(HTML(text))

def init(name, desc):
    return SinkInfo(name, desc, Slide)

