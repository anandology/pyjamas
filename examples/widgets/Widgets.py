import pyjd # dummy in pyjs
from pyjamas.ui.Button import Button
from pyjamas.ui.RootPanel import RootPanel
from pyjamas import Window
from pyjamas.ui.Image import Image
from pyjamas.ui.HTML import HTML
from pyjamas.Canvas.GWTCanvas import GWTCanvas
from pyjamas.Canvas.ImageLoader import loadImages
from pyjamas.Canvas.Color import Color
from pyjamas.Timer import Timer
from pyjamas import DOM
import time

class Widgets:
    def onModuleLoad(self):

        img_url = Window.getLocation().getSearchVar("img")
        if not img_url:
            img_url = 'images/chrome_clock.png'
        self.solar = SolarCanvas(img_url)
        
        RootPanel().add(self.solar)
        self.onShow()

    def onShow(self):
        self.solar.isActive = True
        self.solar.onTimer()
    
    def onHide(self):
        self.solar.isActive = False


class SolarCanvas(GWTCanvas):

    def __init__(self, img_url):
        GWTCanvas.__init__(self, 300, 300, 300, 300)
        loadImages([img_url], self)
        self.width = 150
        self.height = 150
        
        self.isActive = True
        self.onTimer()

    def onImagesLoaded(self, imagesHandles):
        self.clock = imagesHandles[0]
        el = self.clock.getElement()
        self.width = DOM.getIntAttribute(el, "width")
        self.height = DOM.getIntAttribute(el, "height")
        self.setWidth("%d" % self.width)
        self.setHeight("%d" % self.height)
 
    def onError(self, sender):
        Window.alert("error of some kind (probably missing image at url)")

    def onTimer(self, sender=None):
        if not self.isActive:
            return
        
        Timer(1000, self)
        self.draw()

    def getTimeSeconds(self):
        return time.time() % 60.0

    def getTimeMilliseconds(self):
        return (time.time() * 1000.0) % 1.0

    def getTimeMinutes(self):
        return (time.time() / 60) % 60.0

    def getTimeHours(self):
        return (time.time() / 3600) % 12.0

    def draw(self):
        pi = 3.14159265358979323
        if not getattr(self, 'clock', None):
            return
        
        self.setGlobalCompositeOperation('destination-over')

        # clear canvas
        self.clear()
        
        self.saveContext()
        self.setFillStyle(Color('rgba(0,0,0,0.4)'))
        self.setStrokeStyle(Color('rgba(0,153,255,0.4)'))
        self.translate(self.width/2,self.height/2)
        
        secs = self.getTimeSeconds()
        mins = self.getTimeMinutes() + secs / 60.0
        hours = self.getTimeHours() + mins / 60.0

        # Seconds
        self.saveContext()
        self.setFillStyle(Color('rgba(255,0,0,0.4)'))
        self.rotate( ((2*pi)/60)*secs + pi)
        self.fillRect(-1,-(self.width * 0.04),2, self.width * 0.38) 
        self.restoreContext()
        
        # Minutes
        self.saveContext()
        self.rotate( ((2*pi)/60)*mins + pi)
        self.fillRect(-1,-1,3,self.width * 0.35) 
        self.restoreContext()
        
        # Hours
        self.saveContext()
        self.rotate( ((2*pi)/12)*hours + pi)
        self.fillRect(-2,-2,4,self.width * 0.2) 
        self.restoreContext()
        
        self.restoreContext()
        
        self.drawImage(self.clock.getElement(),0,0)


def AppInit():

    img_url = Window.getLocation().getSearchVar("img")
    if not img_url:
        img_url = 'images/chrome_clock.png'
    solar = SolarCanvas(img_url)
    
    solar.isActive = True
    solar.onTimer()

    return solar


if __name__ == '__main__':
    pyjd.setup("./public/Widgets.html")
    app = Widgets()
    app.onModuleLoad()
    pyjd.run()
