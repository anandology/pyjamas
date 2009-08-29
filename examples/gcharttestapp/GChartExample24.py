from pyjamas.chart import GChartUtil
from pyjamas.chart.GChart import GChart
from pyjamas.chart import AnnotationLocation
from pyjamas.chart import SymbolType
from pyjamas.chart import Double

import math

from pyjamas import DOM
from pyjamas.ui.Hyperlink import Hyperlink
from pyjamas.ui.Button import Button
from pyjamas.ui import Event
from pyjamas.ui.FlowPanel import FlowPanel
from pyjamas.ui.Grid import Grid
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui import MouseListener


"""*
* Example that adds an interactive pan and zoom capability to a
* GChart. Basically, axis limits are adjusted appropriately in
* response to mouse pan and zoom related activities. A zoom
* selection cursor is implemented via a single-point box
* curve configured appropriately. Hover widgets are used to
* create +/- zoom control buttons that are auto-hidden when the
* mouse is outside of the zoom selection cursor.
* <p>
*
* Here's how the end user sees it:
*
* <ol>
*
* <li> Panning: Users drag to pan in the standard manner.
*
* <p>
*
* <li> The zooming features are best described in terms of user
* and experienced user zooming scenarios (other scenarios
* exist).
* <p>
*
* Typical user zooming scenario:
* <p>
*
* <ol>
*  <li>User clicks on chart, which creates default zoom cursor centered
* on mouse half the size of the plot area
*  <li>User uses + or - buttons at center of zoom-cursor to
* zoom in or out. First zoom in or out auto-pans plot area so
* that selection cursor is centered in plot area. Zoom in and
* out are exact inverses of each other so they can always self.get
* back to where they started from.
*   <li>User moves mouse outside the selection cursor to make
* +/- zoom controll buttons go away if they are occluding the view
*   <li>User clicks anywhere on chart to dismiss selection cursor
* or simply starts drag-panning which also auto-dismisses selection
* cursor.
* </ol>
*
* <p>
* Typical experienced user zooming scenario:
* <p>
*
* <ol>
*  <li> User Drags while holding Ctrl key to create selection
* rectangle (normally, no +/- buttons will appear because mouse
* will be just outside selection rectangle after such a
* drag-select).
*
*  <li> User uses mouse wheel to zoom in an out; behavior is exactly
* the same as for clicking plus or minus zoom controller
* buttons.
*
*  <li> Alt-Click immediately reverts to the initial plot area
*  window, clearing any selection cursor (go back to initial
*  state).
*
* <li> User cancels zoom mode via click or dragging as described earlier.
*
* </ol>
* </ol>
* <p>
*
* This example was created in response to GChart issue #38. It
* has the basic features of pan and zoom discussed in that
* issue, but does not include every feature suggested by the
* original author (no cross-hairs cursors, for example). This
* example is intended to self.get you started. I expect that, with
* some effort, all of the features discussed in issue #38, as
* well as other features that some other GChart users may
* require, can be added via appropriate code. If you come up with
* useful variations on this pan and zoom theme, please share
* your code or ideas via a comment to issue #38 or start a new
* "how to do pan and zoom" related issue.
* <p>
*
* Finally, note that the simple approach of this example
* requires that all chart points be loaded into memory. Though
* such limits are VERY client platform specific, on the slowest
* client platforms (e.g. an old machine running IE6) you cannot
* expect reasonable responsiveness with more than a thousand
* points or so. Of course paging data in from a server, using
* compressed data during zoom, and so on, could in principle
* overcome such limits, but that's far beyond the scope of this
* simple approach.
*
*
"""
class Point(object):
    def __init__(self):
        self.x = 0
        self.y = 0

class Region(object):
    def __init__(self):
        self.xMin = 0
        self.xMax = 0
        self.yMin = 0
        self.yMax = 0

class ZoomController (HorizontalPanel ):
    def __init__(self, chart, **kwargs):
        self.chart = chart
        HorizontalPanel.__init__(self, **kwargs)
        self.bzoomIn = Button("<big>+</big>", self)
        self.bzoomOut = Button("<big>-</big>", self)
        self.bzoomIn.setTitle(
        "Zoom in (expands selected region so it fills plot area)")
        self.bzoomOut.setTitle(
        "Zoom out (shrinks plot area so it fits in selected region)")
        self.add(self.bzoomIn)
        self.add(self.bzoomOut)
    
    def onClick(self, sender):
        if sender == self.bzoomIn:
            self.chart.zoomIn()
        else:
            self.chart.zoomOut()
    
    def hoverCleanup(self, hoveredAwayFrom):
        pass
    
    def hoverUpdate(self, hoveredOver):
        pass
        
    
MIN_SELECTION_FRACTION_X = 0.1
MIN_SELECTION_FRACTION_Y = 0.1
N_POINTS = 100
    

class GChartExample24(GChart):
    
    def updateCursor(self):
        dx = self.p2.x - self.p1.x
        dy = self.p2.y - self.p1.y
        if not self.moving  and  math.abs(dx) >= MIN_SELECTION_FRACTION_X* (getXAxis().getAxisMax()-getXAxis().getAxisMin())  and  math.abs(dy) >= MIN_SELECTION_FRACTION_Y* (getYAxis().getAxisMax()-getYAxis().getAxisMin()):
            self.getCurve(SELECTION_CURVE).setVisible(True)
            self.getCurve(SELECTION_CURVE).getSymbol().setSymbolType(
            SymbolType.BOX_CENTER)
            self.getCurve(SELECTION_CURVE).getSymbol().setBorderColor("gray")
            self.getCurve(SELECTION_CURVE).getSymbol().setBorderWidth(2)
            self.getCurve(SELECTION_CURVE).getSymbol().setModelWidth(math.abs(dx))
            self.getCurve(SELECTION_CURVE).getSymbol().setModelHeight(math.abs(dy))
            self.getCurve(SELECTION_CURVE).getPoint(0).setX((self.p1.x + self.p2.x)/2)
            self.getCurve(SELECTION_CURVE).getPoint(0).setY((self.p1.y + self.p2.y)/2)
        
        elif self.moving:
            if self.getCurve(SELECTION_CURVE).isVisible():
                self.getCurve(SELECTION_CURVE).setVisible(False)
            
            xMin = self.getXAxis().getAxisMin() - dx
            xMax =  self.getXAxis().getAxisMax() - dx
            yMin =  self.getYAxis().getAxisMin() - dy
            yMax =  self.getYAxis().getAxisMax() - dy
            self.getXAxis().setAxisMin(xMin)
            self.getXAxis().setAxisMax(xMax)
            self.getYAxis().setAxisMin(yMin)
            self.getYAxis().setAxisMax(yMax)
        
        
        
        update()
        
    
    
    def __init__(self):
        GChart.__init__(self)
        self.sinkEvents( Event.MOUSEEVENTS )
        self.mouseListeners = []

        self.SELECTION_CURVE = 0 # curve index of selection cursor
        self.p1 = Point(); # first corner (@mousedown) of selection rect
        self.p2 = Point(); # second corner (@mouseup) of selection rect
        self.selecting = False
        self.moving = False
        self.ctrlPressed = False; # as evaluated at mouse down
        self.altPressed = False
        # (# zoom ins) - (# zoom outs) since selection rect created
        # lets us know when to restore initial plot area limits/cursor
        self.zoomIndex = 0
        self.zoomController = ZoomController(self)
        # min plot area fraction zoom selection cursor must capture
        
        self.initialPlotRegion = Region()
        self.initialSelectionRegion = Region()
    
        self.setChartTitle(
        "Drag to pan; Press Ctrl while drag-selecting a rectangle to zoom")
        self.setChartSize(500, 150)
        a = Hyperlink()
        a.setPixelSize(10, 500)
        self.getYAxis().setAxisLabel(a)
        # another option is to use clipToDecoratedChart(True) instead.
        self.setClipToPlotArea(True)
        self.addCurve()
        for i in range(N_POINTS):
            self.getCurve().addPoint(i, math.sin((2* math.pi * i)/N_POINTS)*
                        math.sin(10*(2* math.pi * i)/N_POINTS))
        
        self.getCurve().getSymbol().setSymbolType(SymbolType.LINE)
        
        # will use this curve to create the selection cursor
        self.addCurve()
        self.getCurve().addPoint(-Double.MAX_VALUE, -Double.MAX_VALUE)
        self.getCurve().setVisible(False)
        # preferentially selects cursor over ordinary curves:
        self.getCurve().getSymbol().setDistanceMetric(0,0)
        self.getCurve().getSymbol().setHoverWidget(self.zoomController)
        self.getCurve().getSymbol().setHoverLocation( AnnotationLocation.CENTER)
        # hides hover-buttons when mouse is outside zoom-cursor
        self.getCurve().getSymbol().setBrushSize(0, 0)
        self.SELECTION_CURVE = self.getNCurves()-1
        # give them some x-panning space
        self.getXAxis().setAxisMin(0.25*N_POINTS)
        self.getXAxis().setAxisMax(0.75*N_POINTS)
        
        self.getYAxis().setTickLabelThickness(50)
        self.getYAxis().setAxisMin(-0.5)
        self.getYAxis().setAxisMax(0.5)
        
        """
        addClickHandler()
        """
        self.mouseListeners.append(self)
        
    def onBrowserEvent(self, event):
        type = DOM.eventGetType(event)
        if type == "mousedown" or type == "mouseup" or type == "mousemove" or type == "mouseover" or type == "mouseout":
            MouseListener.fireMouseEvent(self.mouseListeners, self, event)
        else:
            GChart.onBrowserEvent(self, event)
    
    def onMouseUp(self, sender, x, y):
        event = DOM.eventGetCurrentEvent()
        DOM.eventPreventDefault(event)
        if self.selecting  or  self.moving:
            self.p2.x = self.getXAxis().getMouseCoordinate()
            self.p2.y = self.getYAxis().getMouseCoordinate()
            self.updateCursor()
            self.selecting = False
            self.moving = False
        
    
    def onMouseWheel(self, sender, x, y):
        event = DOM.eventGetCurrentEvent()
        DOM.eventPreventDefault(event)
        if self.getCurve(self.SELECTION_CURVE).isVisible():
            if event.isNorth():
                self.zoomIn()
            
            elif event.isSouth():
                self.zoomOut()
        
    
    def onMouseDown(self, sender, x, y):
        """
        * Most browsers, by default, support the ability to
        * to "drag-copy" any web page image to the desktop.
        * But GChart's rendering makes extensive use of
        * images, so we need to override this default.
        *
        """
        event = DOM.eventGetCurrentEvent()
        DOM.eventPreventDefault(event)
        self.ctrlPressed = DOM.eventGetCtrlKey(event)
        self.altPressed = DOM.eventGetAltKey(event)
        x = self.getXAxis().getMouseCoordinate()
        y = self.getYAxis().getMouseCoordinate()
        if (min(self.p1.x, self.p2.x) <= x  and 
            x <= max(self.p1.x, self.p2.x)  and  
            min(self.p1.y, self.p2.y) <= y  and  
            y <= max(self.p1.y, self.p2.y)):
            return; # ignore mouse down inside selection rectangle
        
        self.p1.x = self.p2.x = x
        self.p1.y = self.p2.y = y
        xMin = self.getXAxis().getAxisMin()
        xMax = self.getXAxis().getAxisMax()
        yMin = self.getYAxis().getAxisMin()
        yMax = self.getYAxis().getAxisMax()
        self.initialPlotRegion.xMin = xMin
        self.initialPlotRegion.xMax = xMax
        self.initialPlotRegion.yMin = yMin
        self.initialPlotRegion.yMax = yMax
        if self.ctrlPressed:
            self.selecting = True
            self.moving = False
        else:
            self.selecting = False
            self.moving = True
        
        self.updateCursor()
        
    
    def onMouseMove(self, sender, x, y):
        event = DOM.eventGetCurrentEvent()
        DOM.eventPreventDefault(event)
        if self.selecting  or  self.moving:
            self.p2.x = self.getXAxis().getMouseCoordinate()
            self.p2.y = self.getYAxis().getMouseCoordinate()
            self.updateCursor()
            if self.moving:
                self.p1.x = self.p2.x = self.getXAxis().getMouseCoordinate()
                self.p1.y = self.p2.y = self.getYAxis().getMouseCoordinate()
            
        
    
    def onClick(self, event):
        x = self.getXAxis().getMouseCoordinate()
        y = self.getYAxis().getMouseCoordinate()
        if self.altPressed:
            self.getXAxis().setAxisMin(0.25*N_POINTS)
            self.getXAxis().setAxisMax(0.75*N_POINTS)
            self.getYAxis().setAxisMin(-0.5)
            self.getYAxis().setAxisMax(.5)
            self.getCurve(self.SELECTION_CURVE).setVisible(False)
            self.update()
        
        elif self.getCurve(self.SELECTION_CURVE).isVisible():
            self.p1.x = self.p2.x = x
            self.p1.y = self.p2.y = y
            self.getCurve(self.SELECTION_CURVE).setVisible(False)
            self.update()
        
        else:
            xMin = self.getXAxis().getAxisMin()
            xMax = self.getXAxis().getAxisMax()
            yMin = self.getYAxis().getAxisMin()
            yMax = self.getYAxis().getAxisMax()
            self.p1.x = x - (xMax - xMin)/4; # half-size zoom cursor
            self.p2.x = x + (xMax - xMin)/4
            self.p1.y = y - (yMax - yMin)/4
            self.p2.y = y + (yMax - yMin)/4
            moving = selecting = False
            self.zoomIndex = 0
            self.getCurve(self.SELECTION_CURVE).setVisible(True)
            self.updateCursor()
        
        self.moving = self.selecting = False
    

    def zoomIn(self):
        
        if -1 == self.zoomIndex:
            # return to starting (0 index) state
            self.getXAxis().setAxisMin(self.initialPlotRegion.xMin)
            self.getXAxis().setAxisMax(self.initialPlotRegion.xMax)
            self.getYAxis().setAxisMin(self.initialPlotRegion.yMin)
            self.getYAxis().setAxisMax(self.initialPlotRegion.yMax)
            self.p1.x = self.initialSelectionRegion.xMin
            self.p2.x = self.initialSelectionRegion.xMax
            self.p1.y = self.initialSelectionRegion.yMin
            self.p2.y = self.initialSelectionRegion.yMax
        
        else:
            xMin = self.getXAxis().getAxisMin()
            xMax = self.getXAxis().getAxisMax()
            yMin = self.getYAxis().getAxisMin()
            yMax = self.getYAxis().getAxisMax()
            if 0 == self.zoomIndex:
                # moving away from starting state
                self.initialPlotRegion.xMin = xMin
                self.initialPlotRegion.xMax = xMax
                self.initialPlotRegion.yMin = yMin
                self.initialPlotRegion.yMax = yMax
                self.initialSelectionRegion.xMin = min(self.p1.x, self.p2.x)
                self.initialSelectionRegion.xMax = max(self.p1.x, self.p2.x)
                self.initialSelectionRegion.yMin = min(self.p1.y, self.p2.y)
                self.initialSelectionRegion.yMax = max(self.p1.y, self.p2.y)
                dx = xMax - xMin
                dy = yMax - yMin
                # center plot area on selection cursor
                xMin = (self.p1.x + self.p2.x - dx)/2
                xMax = (self.p1.x + self.p2.x + dx)/2
                yMin = (self.p1.y + self.p2.y - dy)/2
                yMax = (self.p1.y + self.p2.y + dy)/2
            
            
            pXMin = min(self.p1.x, self.p2.x)
            pXMax = max(self.p1.x, self.p2.x)
            pYMin = min(self.p1.y, self.p2.y)
            pYMax = max(self.p1.y, self.p2.y)
            
            newPXSize = (pXMax-pXMin)*(pXMax-pXMin)/(xMax - xMin)
            newPYSize = (pYMax-pYMin)*(pYMax-pYMin)/(yMax - yMin)
            
            xCenter = (self.p1.x + self.p2.x)/2
            yCenter = (self.p1.y + self.p2.y)/2
            self.p1.x = xCenter - newPXSize/2
            self.p2.x = xCenter + newPXSize/2
            self.p1.y = yCenter - newPYSize/2
            self.p2.y = yCenter + newPYSize/2
            
            self.getXAxis().setAxisMin(pXMin)
            self.getXAxis().setAxisMax(pXMax)
            self.getYAxis().setAxisMin(pYMin)
            self.getYAxis().setAxisMax(pYMax)
            
        
        updateCursor()
        self.zoomIndex += 1
    
    def zoomOut(self):
        if 1 == self.zoomIndex:
            # return to starting (0 index) state
            self.getXAxis().setAxisMin(self.initialPlotRegion.xMin)
            self.getXAxis().setAxisMax(self.initialPlotRegion.xMax)
            self.getYAxis().setAxisMin(self.initialPlotRegion.yMin)
            self.getYAxis().setAxisMax(self.initialPlotRegion.yMax)
            self.p1.x = self.initialSelectionRegion.xMin
            self.p2.x = self.initialSelectionRegion.xMax
            self.p1.y = self.initialSelectionRegion.yMin
            self.p2.y = self.initialSelectionRegion.yMax
        
        else:
            xMin = self.getXAxis().getAxisMin()
            xMax = self.getXAxis().getAxisMax()
            yMin = self.getYAxis().getAxisMin()
            yMax = self.getYAxis().getAxisMax()
            if 0 == self.zoomIndex:
                self.initialPlotRegion.xMin = xMin
                self.initialPlotRegion.xMax = xMax
                self.initialPlotRegion.yMin = yMin
                self.initialPlotRegion.yMax = yMax
                self.initialSelectionRegion.xMin = min(self.p1.x, self.p2.x)
                self.initialSelectionRegion.xMax = max(self.p1.x, self.p2.x)
                self.initialSelectionRegion.yMin = min(self.p1.y, self.p2.y)
                self.initialSelectionRegion.yMax = max(self.p1.y, self.p2.y)
                dx = xMax - xMin
                dy = yMax - yMin
                xCenter = (self.p1.x + self.p2.x)/2
                yCenter = (self.p1.y + self.p2.y)/2
                # center plot area on selection cursor
                xMin =  xCenter - dx/2
                xMax =  xCenter + dx/2
                yMin =  yCenter - dy/2
                yMax =  yCenter + dy/2
            
            pXMin = min(self.p1.x, self.p2.x)
            pXMax = max(self.p1.x, self.p2.x)
            pYMin = min(self.p1.y, self.p2.y)
            pYMax = max(self.p1.y, self.p2.y)
            
            newXSize = (xMax - xMin)*(xMax - xMin)/(pXMax-pXMin)
            newYSize = (yMax - yMin)*(yMax - yMin)/(pYMax-pYMin)
            
            dx = xMax - xMin
            dy = yMax - yMin
            xCenter = (self.p1.x + self.p2.x)/2
            yCenter = (self.p1.y + self.p2.y)/2
            self.p1.x = xCenter - dx/2
            self.p2.x = xCenter + dx/2
            self.p1.y = yCenter - dy/2
            self.p2.y = yCenter + dy/2
            
            newXMin = (xMin + xMax - newXSize)/2.0
            newXMax = (xMin + xMax + newXSize)/2.0
            newYMin = (yMin + yMax - newYSize)/2.0
            newYMax = (yMin + yMax + newYSize)/2.0
            
            self.getXAxis().setAxisMin(newXMin)
            self.getXAxis().setAxisMax(newXMax)
            self.getYAxis().setAxisMin(newYMin)
            self.getYAxis().setAxisMax(newYMax)
            
            self.p1.x = xMin
            self.p2.x = xMax
            self.p1.y = yMin
            self.p2.y = yMax
        
        self.zoomIndex -= 1
        updateCursor()
    

