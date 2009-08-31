import math

from pyjamas.chart import GChartUtil
from pyjamas.chart.GChart import GChart
from pyjamas.chart import AnnotationLocation
from pyjamas.chart import SymbolType

from pyjamas.ui.Button import Button
from pyjamas.ui.FocusPanel import FocusPanel
from pyjamas.ui.Grid import Grid
from pyjamas.ui import KeyboardListener
from pyjamas import DOM




"""*
* Example of how to add direct keyboard support to a GChart
* by wrapping it within a FocusPanel.
* <p>
*
* The example allows lets the user press the left and right arrow keys
* to move the selected point to the previous or next point after the
* currently selected point.
*
* For the more common case where you are handling mouse click
* events only, as of v2.61, GChart implements both GWT's
* HasMouse*Handlers and HasClickHandlers interfaces (c.f.
* GChartExample24.java) so this wrapper technique is usually not
* needed.
*
"""

N_POINTS = 100
BLUE = "#318ce0"
SKY_BLUE = "#c6defa"

class ChildGChart(GChart):

    def __init__(self):
        GChart.__init__(self)

        self.setChartTitle(
        "Click on chart, then use left/right arrows to switch selected point")
        self.setHoverTouchingEnabled(True)
        self.setChartSize(500, 150)
        self.setPadding("10px")
        self.getXAxis().setTickCount(11)
        self.getYAxis().setTickCount(11)
        self.addCurve()
        for i in range(N_POINTS+1):
            self.getCurve().addPoint(i, math.sin((2* math.pi * i)/N_POINTS))

        self.getCurve().getSymbol().setWidth(5)
        self.getCurve().getSymbol().setBorderColor(BLUE)
        self.getCurve().getSymbol().setBackgroundColor(SKY_BLUE)
        self.getCurve().getSymbol().setHoverSelectionBackgroundColor(BLUE)
        self.getCurve().getSymbol().setHoverSelectionBorderColor(SKY_BLUE)
        self.getCurve().getSymbol().setSymbolType(
                                SymbolType.VBAR_BASELINE_CENTER)
        self.getCurve().getSymbol().setHoverLocation(
                                AnnotationLocation.NORTH)
        self.getCurve().getSymbol().setHoverYShift(5)
        self.setPixelSize(self.getXChartSizeDecorated(),
                            self.getYChartSizeDecorated())



class GChartExample25 (FocusPanel):

    def __init__(self):
        FocusPanel.__init__(self)
        self.theChild = ChildGChart()
        self.theChild.update()
        self.setWidget(self.theChild)
        self.addKeyboardListener(self)
        self.addMouseListener(self)

    def onKeyDown(self, sender, keycode, modifiers):
        event = DOM.eventGetCurrentEvent()
        DOM.eventPreventDefault(event)
        # ignore mouse position when arrow-key pressing
        if self.theChild.getHoverTouchingEnabled():
            self.theChild.setHoverTouchingEnabled(False)

        p = self.theChild.getTouchedPoint()
        c = self.theChild.getCurve(); # only one curve on chart
        iPoint = 0
        if p is not None:
            iPoint = c.getPointIndex(p)
        if keycode == KeyboardListener.KEY_LEFT:
            iPoint = (iPoint + N_POINTS) % (N_POINTS+1)
        elif keycode == KeyboardListener.KEY_RIGHT:
            iPoint = (iPoint + 1) % (N_POINTS+1)

        self.theChild.touch(c.getPoint(iPoint))
        self.theChild.update()

    def onMouseMove(self, sender, x, y):
        event = DOM.eventGetCurrentEvent()
        DOM.eventPreventDefault(event)
        # mousing auto re-enables mouse-over hover feedback
        if not self.theChild.getHoverTouchingEnabled():
            self.theChild.setHoverTouchingEnabled(True)
            self.theChild.update()

    def setOptimizeForMemory(self, optimize):
        self.theChild.setOptimizeForMemory( optimize)
    def update(self):
        self.theChild.update()
