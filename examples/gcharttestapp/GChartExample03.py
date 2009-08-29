
from pyjamas.chart.GChart import GChart
from pyjamas.chart import SymbolType
from pyjamas.chart.GChartConsts import Y_AXIS, Y2_AXIS




"""*
* Defines a chart with a scatterplot on one y-axis, and a
*  barchart on the other.
"""
class GChartExample03(GChart):
    def __init__(self):
        GChart.__init__(self)

        do_axis2 = True

        self.setChartTitle("<h2>10x and x<sup>2</sup></h2>")
        self.setChartSize(300, 300)
        self.addCurve()
        self.getCurve().setLegendLabel("<i>10x</i>")
        self.getCurve().setYAxis(Y_AXIS)
        self.getCurve().getSymbol().setSymbolType(SymbolType.VBAR_SOUTH)
        self.getCurve().getSymbol().setBackgroundColor("#DDF")
        self.getCurve().getSymbol().setBorderColor("red")
        self.getCurve().getSymbol().setBorderWidth(1)
        self.getCurve().getSymbol().setModelWidth(0.5)
        for i in range(10):
            self.getCurve().addPoint(i,i*10)
        
        if do_axis2:
            self.addCurve()
            self.getCurve().setLegendLabel("<i>x<sup>2</sup></i>")
            self.getCurve().setYAxis(Y2_AXIS)
            self.getCurve().getSymbol().setSymbolType(SymbolType.BOX_CENTER)
            self.getCurve().getSymbol().setWidth(5)
            self.getCurve().getSymbol().setHeight(5)
            self.getCurve().getSymbol().setBorderWidth(0)
            self.getCurve().getSymbol().setBackgroundColor("navy")
            self.getCurve().getSymbol().setFillThickness(2)
            self.getCurve().getSymbol().setFillSpacing(5)
            
            for i in range(self.getCurve(0).getNPoints()):
                self.getCurve().addPoint(i,i*i)
            
        
        self.getXAxis().setAxisLabel("<i>x</i>")
        self.getXAxis().setHasGridlines(True)
        self.getXAxis().setTickThickness(0); # hide tick marks...
        self.getXAxis().setTickLength(3);    # but leave a small gap
        self.getYAxis().setAxisLabel("<i>10x</i>")
        self.getYAxis().setAxisMax(100)
        self.getYAxis().setAxisMin(0)
        self.getYAxis().setTickLabelFormat("#.#")
        self.getYAxis().setTickCount(11)
        if do_axis2:
            self.getY2Axis().setAxisLabel("<i>x<sup>2</sup></i>")
            self.getY2Axis().setHasGridlines(True)
            # last bar 'sticks out' over right edge, so extend 'grid' right:
            self.getY2Axis().setTickLength(15)
    


