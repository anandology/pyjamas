from pyjamas.ui.HTML        import HTML
from pyjamas.ui.RootPanel   import RootPanel
from pyjamas.ui.SimplePanel import SimplePanel

import math
from pyjamas.Timer import Timer
from pyjamas import Window

from pyjamas.raphael.raphael import Raphael
from pyjamas import log
import pyjd

#############################################################################

class Spinner(SimplePanel):
    """ Our testing panel.
    """
    def __init__(self,width=600,height=300):
        """ Standard initialiser.
        """
        SimplePanel.__init__(self)

        # Taken from the "spinner" Raphael demo:
        self.width            = 15
        self.r1               = 35
        self.r2               = 60
        self.cx               = self.r2 + self.width
        self.cy               = self.r2 + self.width
        self.numSectors  = 12
        self.canvas      = Raphael(self.r2*2 + self.width*2, self.r2*2 + self.width*2)
        self.sectors     = []
        self.opacity     = []
        self.add(self.canvas)

    def draw(self):
        colour           = "#000000"
        beta             = 2 * math.pi / self.numSectors

        pathParams = {'stroke'         : colour,
                      'stroke-width'   : self.width,
                      'stroke-linecap' : "round"}

        for i in range(self.numSectors):
            alpha = beta * i - math.pi/2
            cos   = math.cos(alpha)
            sin   = math.sin(alpha)
            data=','.join(['M',str(self.cx + self.r1 * cos),str(self.cy + self.r1 * sin),'L',str(self.cx + self.r2 * cos),str(self.cy + self.r2 * sin)])
            path  = self.canvas.path(data=data,attrs=pathParams)
            self.opacity.append(1.0 * i / self.numSectors )
            self.sectors.append(path)

        period = 1000/self.numSectors
        self._timer = Timer(notify=self)
        self._timer.scheduleRepeating(period)        

    def onTimer(self, timerID):
        """ Respond to our timer firing.
        """
        self.opacity.insert(0, self.opacity.pop())
        for i in range(self.numSectors):
            self.sectors[i].setAttr("opacity", self.opacity[i])

#############################################################################

if __name__ == "__main__":    
    pyjd.setup("public/spinner.html")
    spinner=Spinner()
    RootPanel().add(spinner)
    spinner.draw()
    pyjd.run()

