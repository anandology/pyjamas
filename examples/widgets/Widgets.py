from pyjamas.ui.Button import Button
from pyjamas.ui.RootPanel import RootPanel
from pyjamas import Window
from pyjamas.ui.Image import Image
from pyjamas.ui.HTML import HTML
from pyjamas.Canvas2D import Canvas, CanvasImage, ImageLoadListener
from pyjamas.Timer import Timer
from pyjamas import DOM

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


class SolarCanvas(Canvas):

    def __init__(self, img_url):
        Canvas.__init__(self, 300, 300)
        self.clock = CanvasImage(img_url)
        self.width = 150
        self.height = 150
        
        self.loader = ImageLoadListener(self)
        self.loader.add(self.clock)
        
        self.isActive = True
        self.onTimer()

    def onLoad(self):
        el = self.clock.getElement()
        self.width = DOM.getAttribute(el, "width")
        self.height = DOM.getIntAttribute(el, "height")
        self.setWidth("%dpx" % self.width)
        self.setHeight("%dpx" % self.height)
 
    def onError(self, sender):
        Window.alert("error of some kind (probably missing image at url)")

    def onTimer(self):
        if not self.isActive:
            return
        
        Timer(1000, self)
        self.draw()

    def getTimeSeconds(self):
        JS("""
        var x = new Date();
        return x.getSeconds();
        """)

    def getTimeMinutes(self):
        JS("""
        var x = new Date();
        return x.getMinutes();
        """)

    def getTimeHours(self):
        JS("""
        var x = new Date();
        return x.getHours();
        """)

    def getTimeMilliseconds(self):
        JS("""
        var x = new Date();
        return x.getMilliseconds();
        """)

    def draw(self):
        pi = 3.14159265358979323
        if not self.loader.isLoaded():
            return
        
        self.context.globalCompositeOperation = 'destination-over'

        # clear canvas
        self.context.clearRect(0,0,self.width,self.height) 
        
        self.context.save()
        self.context.fillStyle = 'rgba(0,0,0,0.4)'
        self.context.strokeStyle = 'rgba(0,153,255,0.4)'
        self.context.translate(self.width/2,self.height/2)
        
        secs = self.getTimeSeconds()
        mins = self.getTimeMinutes() + secs / 60.0
        hours = self.getTimeHours() + mins / 60.0

        # Seconds
        self.context.save()
        self.context.fillStyle = 'rgba(255,0,0,0.4)'
        self.context.rotate( ((2*pi)/60)*secs + pi)
        self.context.fillRect(-1,-(self.width * 0.04),2, self.width * 0.38) 
        self.context.restore()
        
        # Minutes
        self.context.save()
        self.context.rotate( ((2*pi)/60)*mins + pi)
        self.context.fillRect(-1,-1,3,self.width * 0.35) 
        self.context.restore()
        
        # Hours
        self.context.save()
        self.context.rotate( ((2*pi)/12)*hours + pi)
        self.context.fillRect(-2,-2,4,self.width * 0.2) 
        self.context.restore()
        
        self.context.restore()
        
        self.context.drawImage(self.clock,0,0)


def AppInit():

    img_url = Window.getLocation().getSearchVar("img")
    if not img_url:
        img_url = 'images/chrome_clock.png'
    solar = SolarCanvas(img_url)
    
    solar.isActive = True
    solar.onTimer()

    return solar


if __name__ == '__main__':
    app = Widgets()
    app.onModuleLoad()

