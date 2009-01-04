from pyjamas.ui import Button, RootPanel
from pyjamas import Window
from pyjamas.ui import Image, HTML, VerticalPanel, HorizontalPanel
from Canvas import Canvas, CanvasImage, ImageLoadListener
from pyjamas.Timer import Timer
from math import floor, cos, sin


class Widgets:
    def onModuleLoad(self):

        self.solar = SolarCanvas()
        
        RootPanel().add(self.solar)
        self.onShow()

    def onShow(self):
        self.solar.isActive = True
        self.solar.onTimer()
    
    def onHide(self):
        self.solar.isActive = False


class SolarCanvas(Canvas):
    def __init__(self):
        Canvas.__init__(self, 300, 300)     
        self.clock = CanvasImage('images/Clock.png')
        
        self.loader = ImageLoadListener()
        self.loader.add(self.clock)
        
        self.isActive = True
        self.onTimer()

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
        self.context.clearRect(0,0,100,100) 
        
        self.context.save()
        self.context.fillStyle = 'rgba(0,0,0,0.4)'
        self.context.strokeStyle = 'rgba(0,153,255,0.4)'
        self.context.translate(50,50)
        
        secs = self.getTimeSeconds()
        mins = (self.getTimeMinutes() * 60) + secs
        hours = (self.getTimeHours() * 3600) + mins
        mins = mins / 60.0
        hours = hours / 3600.0

        # Seconds
        self.context.save()
        self.context.fillStyle = 'rgba(255,0,0,0.4)'
        self.context.rotate( ((2*pi)/60)*secs + pi)
        self.context.fillRect(-1,-1,2,38) 
        self.context.restore()
        
        # Minutes
        self.context.save()
        self.context.rotate( ((2*pi)/60)*mins + pi)
        self.context.fillRect(-1,-1,3,35) 
        self.context.restore()
        
        # Hours
        self.context.save()
        self.context.rotate( ((2*pi)/60)*hours + pi)
        self.context.fillRect(-2,-2,4,20) 
        self.context.restore()
        
        self.context.restore()
        
        self.context.drawImage(self.clock,0,0)

