
from pyjamas.chart.GChart import GChart

"""*
* Defines a scatter-plot of x*x vs. x.
"""
class GChartExample00(GChart):
    def __init__(self):
        self.setChartTitle("<b>x<sup>2</sup> vs x</b>")
        self.setChartSize(150, 150)
        self.addCurve()
        for i in range(10):
            self.getCurve().addPoint(i,i*i)
        self.getCurve().setLegendLabel("x<sup>2</sup>")
        self.getXAxis().setAxisLabel("x")
        self.getYAxis().setAxisLabel("x<sup>2</sup>")
    


