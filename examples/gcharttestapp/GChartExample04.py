import math

from pyjamas.chart.GChart import GChart
from pyjamas.chart import GChartUtil

# GWT 1.4's Math class does not include JDK's
# Math.log10--so emulate it.
def log10(x):
    return math.log(x)/math.log(10.0)

"""*
* Defines a traditional "semi-log" chart by using custom
* ticks on the y axis, in conjunction with log-transformed
* y data.
"""
class GChartExample04(GChart):
    def __init__(self):
        GChart.__init__(self, 300, 450)
        self.setChartTitle("<h2>2<sup>x</sup> vs x</h2>")
        self.addCurve()
        self.getCurve().getSymbol().setHovertextTemplate(
                        GChartUtil.formatAsHovertext("${y}=2^${x}"))
        self.getCurve().setLegendLabel("<b>2<sup>x</sup></b>")
        self.getCurve().getSymbol().setBackgroundColor("red")
        self.getCurve().getSymbol().setBorderColor("black")
        self.getCurve().getSymbol().setWidth(9)
        self.getCurve().getSymbol().setHeight(9)
        
        # add (log10-transformed) powers of 2 from 1/4 to 8
        for i in range(-2, 4):
            self.getCurve().addPoint(i,log10(math.pow(2,i)))
        
        # GChart's "=10^" NumberFormat prefix inverts the log10
        # transform
        self.getYAxis().setTickLabelFormat("=10^#.##")
        # add conventional log-scaled ticks from .1 to 10
        self.getYAxis().addTick(log10(0.1))
        x = 0.1
        while x < 10:
            for y in range(2, 11):
                self.getYAxis().addTick(log10(x*y))
            x *= 10
        
        self.getXAxis().setAxisLabel("<b>x</b>")
        self.getXAxis().setHasGridlines(True)
        self.getXAxis().setTickCount(6)
        
        self.getYAxis().setAxisLabel("<b>2<sup>x</sup></b>")
        self.getYAxis().setHasGridlines(True)
        
    


