from pyjamas.Canvas.GWTCanvas import GWTCanvas
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.DOM import getFirstChild
from pyjamas import Window
from pyjamas.ui.HTML import HTML
import math
from __pyjamas__ import jsinclude

# Include the processing.js in the module scope
jsinclude("processing.js")
from __javascript__ import Processing # defined by processing.js


p = None
radius = 50.0
delay = 16

def setup():
    global p,radius,delay,X,Y,nX,nY
    p.size(200,200)
    p.strokeWeight( 10 )
    p.frameRate( 15 )
    X = p.width / 2
    Y = p.width / 2
    nX = X
    nY = Y  

def draw():
    global p,radius,delay,X,Y,nX,nY
    radius = radius + math.sin( p.frameCount / 4 )
    X+=(nX-X)/delay
    Y+=(nY-Y)/delay
    p.background( 100 )
    p.fill( 0, 121, 184 )
    p.stroke(255)
    p.ellipse(X, Y, radius, radius )
    
def mouseMoved():
    global p,nX,nY
    nX = p.mouseX
    nY = p.mouseY

class ProcessingCanvas(GWTCanvas):
    def __init__(self):
        GWTCanvas.__init__(self, 150, 150, 150, 150)
        self.c = getFirstChild(self.getElement())
        self.p = Processing (self.c)
        global p
        p = self.p
    
if __name__ == '__main__':
    note = HTML("""
Note that this is an example of using processing.js.<br>
See <a href=http://ejohn.org/blog/processingjs/>http://ejohn.org/blog/processingjs/</a> for more info.<br>
Since processing.js is built for state-of-the-art browser<br>
that properly implement canvas, IE is not supported.<br>
<br>
""")
    RootPanel().add(note)
    PC = ProcessingCanvas()
    PC.p.setup = setup
    PC.p.draw = draw
    PC.p.mouseMoved = mouseMoved
    PC.p.init()
    RootPanel().add(PC)
