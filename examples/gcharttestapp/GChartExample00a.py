

from pyjamas.chart.GChart import GChart

"""*
* Defines a line-plot of x*x vs. x, with dotted connecting lines.
"""
class GChartExample00a(GChart):
    def __init__(self):
        GChart.__init__(self)
        self.setChartTitle("<b>x<sup>2</sup> vs x</b>")
        self.setChartSize(150, 150)
        self.addCurve()
        self.getCurve().getSymbol().setFillThickness(2)
        self.getCurve().getSymbol().setFillSpacing(5)
        for i in range(10):
            self.getCurve().addPoint(i,i*i)
        self.getCurve().setLegendLabel("x<sup>2</sup>")
        self.getXAxis().setAxisLabel("x")
        self.getYAxis().setAxisLabel("x<sup>2</sup>")
