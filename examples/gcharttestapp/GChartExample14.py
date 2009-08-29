import math

from pyjamas.chart import GChartUtil
from pyjamas.chart.GChart import GChart
from pyjamas.chart import AnnotationLocation
from pyjamas.chart import SymbolType
from pyjamas.chart import Double

from pyjamas.DeferredCommand import DeferredCommand
from pyjamas.ui.Button import Button


"""* Sine curve with lots of points on it, to illustrate the
** incremental update technique.
** <p>
**
** Prior to GChart 2.1, this approach would not have worked
** GChart 2.1 allows curves that have not changed since the
** last update (as long as they occur before the first curve
** that HAS changed) to be skipped over in re-updates. So you
** don't lose much time by updating incrementally in this
** manner, and you gain much better user feedback during
** that all-important first page display.
** <p>
**
** Whenever possible, try to avoid very numbers of HTML
** elements in your charts (swapping in data as needed in
** response to user requests instead). That way, this kind
** of delay can be avoided entirely, and you won't have to
** implement an incrementally updating chart at all.
**
**
*"""

PERIOD = 100
N_PERIODS = 5
DELTA_TIME = 1
DELTA_PHASE = 8
firstTime = True

class IncrementalUpdate:
    def __init__(self, gchart, iCurve, phaseShift, n):
        self.gchart = gchart
        self.iCurve = iCurve
        self.phaseShift = phaseShift
        self.n = n
    
    def execute(self):
        for iC in range(self.iCurve, self.iCurve+self.n):
            if self.gchart.getNCurves() <= iCurve:
                #            gchart.getCurve(0).getPoint(0).setY(
                #                gchart.getCurve(0).getPoint(0).getY())
                self.gchart.addCurve()
                # copy symbol properties from curve 0, except, None
                # legend label (so only one curve row on legend)
                self.gchart.getCurve().getSymbol().setSymbolType(
                        self.gchart.getCurve(0).getSymbol().getSymbolType())
                self.gchart.getCurve().getSymbol().setBorderWidth(
                        self.gchart.getCurve(0).getSymbol().getBorderWidth())
                self.gchart.getCurve().getSymbol().setBackgroundColor(
                        self.gchart.getCurve(0).getSymbol().getBackgroundColor())
                self.gchart.getCurve().getSymbol().setFillSpacing(
                        self.gchart.getCurve(0).getSymbol().getFillSpacing())
                self.gchart.getCurve().getSymbol().setFillThickness(
                        self.gchart.getCurve(0).getSymbol().getFillThickness())
                self.gchart.getCurve().getSymbol().setHeight(
                        self.gchart.getCurve(0).getSymbol().getHeight())
                self.gchart.getCurve().getSymbol().setWidth(
                        self.gchart.getCurve(0).getSymbol().getWidth())
            
            for i in range(0, PERIOD, DELTA_TIME):
                y = math.sin((2*math.pi*(iC*PERIOD+i+self.phaseShift))/PERIOD)
                if self.gchart.getCurve(iC).getNPoints()*DELTA_TIME <= i:
                    self.gchart.getCurve(iC).addPoint(iC*PERIOD+i+self.phaseShift, y)
                else:
                    self.gchart.getCurve(iC).getPoint(i/DELTA_TIME).setY(y)
                
            
        
        self.gchart.update()
    
    


class GChartExample14 (GChart):
    def __init__(self):
        GChart.__init__(self)

    
        self.phase = 0
        self.btn = Button("Update", self)
        def onClick(self, event):
            self.phase += DELTA_PHASE
            for i in range(N_PERIODS):
                DeferredCommand().add(IncrementalUpdate(self, i, self.phase, 1))
            
        self.setChartFootnotes(self.btn)
        
        self.setChartSize(1000,100)
        self.setChartTitle("<big><i>Sine vs Time</i></big>")
        self.setPadding("2px")
        
        self.getXAxis().setAxisLabel("<small><i>Time (seconds)</i></small>")
        self.getXAxis().setHasGridlines(True)
        self.getXAxis().setTickCount(6)
        self.getXAxis().setTickLabelFormat("#.##")
        self.getXAxis().setAxisMin(0)
        self.getXAxis().setAxisMax(PERIOD*N_PERIODS)
        
        self.getYAxis().setHasGridlines(True)
        self.getYAxis().setTickCount(5)
        self.getYAxis().setAxisMin(-1)
        self.getYAxis().setAxisMax(1)
        self.getYAxis().setTickLabelThickness(10)
        
        self.addCurve()
        self.getCurve().getSymbol().setSymbolType(SymbolType.VBAR_BASELINE_CENTER)
        self.getCurve().getSymbol().setBorderWidth(0)
        self.getCurve().getSymbol().setBackgroundColor("blue")
        self.getCurve().getSymbol().setFillSpacing(Double.NaN)
        self.getCurve().getSymbol().setFillThickness(0)
        self.getCurve().getSymbol().setHeight(1)
        self.getCurve().getSymbol().setWidth(1)
        
        for i in range(N_PERIODS):
            DeferredCommand().add(IncrementalUpdate(self, i, 0, 1))
        
        #     for int phaseShift=0; phaseShift < N_PERIODS*PERIOD; phaseShift+=DELTA_PHASE)
        #         DeferredCommand.addCommand(IncrementalUpdate(this,0, phaseShift, N_PERIODS))
    


