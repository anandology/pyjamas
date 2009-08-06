from pyjamas.Canvas2D import Canvas
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.DOM import getFirstChild
import math
import processing.js # YUK!!! 

def setup_globals(self):
    self.radius = 50.0
    self.X=0
    self.Y=0
    self.nX=0
    self.nY=0
    self.delay = 16

def setup(self):
    self.size(200,200)
    self.strokeWeight( 10 )
    self.frameRate( 15 )
    self.X = self.width / 2
    self.Y = self.width / 2
    self.nX = self.X
    self.nY = self.Y  

def draw(self):
    self.radius = self.radius + math.sin( self.frameCount / 4 )
    self.X+=(self.nX-self.X)/self.delay
    self.Y+=(self.nY-self.Y)/self.delay
    self.background( 100 )
    self.fill( 0, 121, 184 )
    self.stroke(255)
    self.ellipse( self.X, self.Y, self.radius, self.radius )
    
def mouseMoved(self):
    self.nX = self.mouseX
    self.nY = self.mouseY
 
    
class ProcessingCanvas(Canvas):
    def __init__(self):
        Canvas.__init__(self,0,0)
        self.c = getFirstChild(self.getElement())
        self.p = Processing (self.c)
        setup_globals(self.p)
        self.p.setup = lambda : setup(self)
        self.p.draw = lambda : draw(self)
        self.p.mouseMoved = lambda : mouseMoved(self)
        self.p.init()
    
if __name__ == '__main__':
    PC = ProcessingCanvas()
    RootPanel().add(PC)
