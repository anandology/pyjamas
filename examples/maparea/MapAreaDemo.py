import pyjd

from pyjamas import DOM

from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.HTML import HTML
from pyjamas.ui.Label import Label
from pyjamas.ui.Map import ImageMap, MapArea
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.ScrollPanel import ScrollPanel
from pyjamas.ui.MenuBar import MenuBar
from pyjamas.ui.Image import Image
from pyjamas.ui.ContextMenuPopupPanel import ContextMenuPopupPanel

from pyjamas import log


class MapAreaDemo:

    def onModuleLoad(self):
        # build image display
        width = 200 #px
        height = 215 #px
        scale = 1.5
        img = Image(
            "babykatie_small.jpg", 
            Width="%dpx" % int(scale * width),
            Height="%dpx" % int(scale * height),
        )
        img.element.setAttribute("usemap", "#themap")
        img.element.setAttribute("ismap", "1")
        imagepanel = ScrollPanel()
        imagepanel.add(img)

        # build message display
        msgpanel = VerticalPanel()
        msgpanel.add(Label("move mouse over baby katie's eyes, nose and mouth."))
        msgarea1 = Label("movement messages")
        msgpanel.add(msgarea1)
        msgarea2 = Label("click messages")
        msgpanel.add(msgarea2)

        imageClickHandler = MapClickHandler(msgarea1, msgarea2)

        # build imagemap
        map = ImageMap("themap",
            Width="%dpx" % int(scale * width),
            Height="%dpx" % int(scale * height),
        )
        areas = [ \
            NamedMapArea(
                "right eye", 
                "circle", 
                [scale * i for i in [73, 97, 7]],
            ),
            NamedMapArea(
                "left eye", 
                "circle", 
                [scale * i for i in [116, 88, 5]],
            ),
            NamedMapArea(
                "nose", 
                "rect", 
                [scale * i for i in [88, 97, 115, 115]],
                Href="http://lkcl.net",
            ),
            NamedMapArea(
                "mouth", 
                "polygon", 
                [scale * i for i in [82, 129, 102, 124, 119, 119, 121, 125, 103, 132, 79, 133]],
            ),
            ]
        for nma in areas:
            nma.addMouseListener(imageClickHandler)
            nma.addClickListener(imageClickHandler)
            map.add(nma)

        # layout page
        hpanel = HorizontalPanel()
        hpanel.add(map)
        hpanel.add(imagepanel)
        hpanel.add(msgpanel)
                    
        RootPanel().add(hpanel)


class NamedMapArea(MapArea):
    """ An area inside an imagemap with a name
    """
    
    def __init__(self, areaname, shape, coords, Href="", **kwargs):
        self.areaname = areaname
        coords = ", ".join(["%d" % int(i) for i in coords])
        MapArea.__init__(self, shape, coords, Href=Href, **kwargs)
    

class MapClickHandler:

    def __init__(self, msgarea1, msgarea2):
        self.msgarea1 = msgarea1
        self.msgarea2 = msgarea2

    def _mouseActionMessage(self, name, action, x=None, y=None):
        #msg =  "%s %s (%d,%d)" % (name, action, x, y)  # throws JS errors
        msg = name + ' ' + action + ' (' + str(x) + ', ' + str(y) + ')'
        self.msgarea1.setText(msg)
        log.writebr(msg)

    def onMouseMove(self, sender, x, y):
        self._mouseActionMessage(sender.areaname, "move", x, y)
        
    def onMouseDown(self, sender, x, y):
        self._mouseActionMessage(sender.areaname, "down", x, y)

    def onMouseUp(self, sender, x, y):
        self._mouseActionMessage(sender.areaname, "up", x, y)

    def onMouseEnter(self, sender):
        self._mouseActionMessage(sender.areaname, "enter")

    def onMouseLeave(self, sender):
        self._mouseActionMessage(sender.areaname, "leave")

    def onClick(self, sender):
        msg = "you clicked on baby katie's " + sender.areaname
        self.msgarea2.setText(msg)
        log.writebr(msg)
    

if __name__ == '__main__':
    pyjd.setup("http://127.0.0.1/examples/maparea/public/MapAreaDemo.html")
    app = MapAreaDemo()
    app.onModuleLoad()
    pyjd.run()
