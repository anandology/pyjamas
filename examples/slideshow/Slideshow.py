from pyjamas.ui import Button, RootPanel, HTML, DockPanel, HasAlignment, Hyperlink, VerticalPanel
from pyjamas import Window
from SinkList import SinkList
from pyjamas.History import History
import Slide
from HTTPRequest import HTTPRequest
from SlideLoader import SlideListLoader

class Slideshow:

    def onHistoryChanged(self, token):
        info = self.sink_list.find(token)
        if info:
            self.show(info, False)
        else:
            self.showInfo()

    def onModuleLoad(self):
        self.curInfo=''
        self.curSink=None
        self.description=HTML()
        self.sink_list=SinkList()
        self.panel=DockPanel()
        
        self.loadSinks()
        self.sinkContainer = DockPanel()
        self.sinkContainer.setStyleName("ks-Sink")

        vp=VerticalPanel()
        vp.setWidth("100%")
        vp.add(self.description)
        vp.add(self.sinkContainer)

        self.description.setStyleName("ks-Intro")

        self.panel.add(self.sink_list, DockPanel.WEST)
        self.panel.add(vp, DockPanel.CENTER)

        self.panel.setCellVerticalAlignment(self.sink_list, HasAlignment.ALIGN_TOP)
        self.panel.setCellWidth(vp, "100%")

        History().addHistoryListener(self)
        RootPanel().add(self.panel)

    def show(self, info, affectHistory):
        if info == self.curInfo: return
        self.curInfo = info

        #Logger.write("showing " + info.getName())
        if self.curSink <> None:
            self.curSink.onHide()
            #Logger.write("removing " + self.curSink)
            self.sinkContainer.remove(self.curSink)

        self.curSink = info.getInstance()
        self.sink_list.setSinkSelection(info.getName())
        self.description.setHTML(info.getDescription())

        if (affectHistory):
            History().newItem(info.getName())

        self.sinkContainer.add(self.curSink, DockPanel.CENTER)
        self.sinkContainer.setCellWidth(self.curSink, "100%")
        self.sinkContainer.setCellHeight(self.curSink, "100%")
        self.sinkContainer.setCellVerticalAlignment(self.curSink, HasAlignment.ALIGN_TOP)
        self.curSink.onShow()
        
    def loadSinks(self):
        HTTPRequest().asyncPost("slides.txt", "", SlideListLoader(self))


    def setSlides(self, slides):
        for l in slides:
            name = l[0]
            desc = l[1]
            self.sink_list.addSink(Slide.init(name, desc))

        #Show the initial screen.
        initToken = History().getToken()
        if len(initToken):
            self.onHistoryChanged(initToken)
        else:
            self.showInfo()


    def showInfo(self):
        self.show(self.sink_list.sinks[0], False)


