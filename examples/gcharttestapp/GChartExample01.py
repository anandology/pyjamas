
from pyjamas.chart.GChart import GChart
from pyjamas.chart import SymbolType

"""*
* Defines a bar-chart of x*x vs. x, with gridlines.
"""
class GChartExample01(GChart):
    def __init__(self):
        GChart.__init__(self)
        self.setChartTitle("<b>x<sup>2</sup> vs x</b>")
        self.setChartSize(150, 150)
        self.addCurve()
        for i in range(10):
            self.getCurve().addPoint(i,i*i)
        self.getCurve().setLegendLabel("x<sup>2</sup>")
        self.getCurve().getSymbol().setSymbolType(SymbolType.VBAR_SOUTH)
        self.getCurve().getSymbol().setBackgroundColor("red")
        self.getCurve().getSymbol().setBorderColor("black")
        self.getCurve().getSymbol().setModelWidth(1.0)
        self.getXAxis().setAxisLabel("<b>x</b>")
        self.getXAxis().setHasGridlines(True)
        self.getYAxis().setAxisLabel("<b>x<sup>2</sup></b>")
        self.getYAxis().setHasGridlines(True)
    


