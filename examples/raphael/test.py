""" test.py

    Simple testing framework for the raphael wrapper.
"""
from pyjamas.ui.HTML        import HTML
from pyjamas.ui.RootPanel   import RootPanel
from pyjamas.ui.SimplePanel import SimplePanel

import math
from pyjamas.Timer import Timer
from pyjamas import Window

from pyjamas.raphael.raphael import Raphael


#############################################################################

class TestPanel(SimplePanel):
    """ Our testing panel.
    """
    def __init__(self):
        """ Standard initialiser.
        """
        SimplePanel.__init__(self)

        # Taken from the "spinner" Raphael demo:

        colour           = "#000000"
        width            = 15
        r1               = 35
        r2               = 60
        cx               = r2 + width
        cy               = r2 + width
        self.numSectors  = 12
        self.canvas      = Raphael(r2*2 + width*2, r2*2 + width*2)
        self.sectors     = []
        self.opacity     = []
        beta             = 2 * math.pi / self.numSectors

        pathParams = {'stroke'         : colour,
                      'stroke-width'   : width,
                      'stroke-linecap' : "round"}

        for i in range(self.numSectors):
            alpha = beta * i - math.pi/2
            cos   = math.cos(alpha)
            sin   = math.sin(alpha)
            path  = self.canvas.path(data=None, attrs=pathParams)
            path.moveTo(cx + r1 * cos, cy + r1 * sin)
            path.lineTo(cx + r2 * cos, cy + r2 * sin)
            self.opacity.append(1 / self.numSectors * i)
            self.sectors.append(path)

        period = 1000/self.numSectors

        self._timer = Timer(notify=self)
        self._timer.scheduleRepeating(period)

        self.add(self.canvas)


    def onTimer(self, timer):
        """ Respond to our timer firing.
        """
        self.opacity.insert(0, self.opacity.pop())
        for i in range(self.numSectors):
            self.sectors[i].setAttr("opacity", self.opacity[i])

#############################################################################

if __name__ == "__main__":
    panel = TestPanel()
    RootPanel().add(panel)

