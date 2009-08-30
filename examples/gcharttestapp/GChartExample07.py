from pyjamas.chart import GChartUtil
from pyjamas.chart.GChart import GChart
from pyjamas.chart import AnnotationLocation
from pyjamas.chart import SymbolType

"""* Basic pie chart
* <p>
*
* This chart uses the built-in HTML-element based pie chart
* rendering.  As of GChart 2.5, faster drawn, better
* looking, solid-filled pie slices can be produced by
* plugging an external canvas library into GChart.  See the
* <tt>setCanvasFactory</tt> method's javadocs for the
* details, and the various pie charts on GChart's live demo
* for complete working examples.
*
"""
class GChartExample07 (GChart):
    def __init__(self):
        GChart.__init__(self)
        pieMarketShare = [0.65,0.20,0.10,0.05]
        pieTypes = ["Apple", "Cherry", "Pecan", "Bannana"]
        pieColors = ["green", "red", "maroon", "yellow"]
        
        self.setChartSize(300, 200)
        self.setChartTitle("<h3>2008 Sales by Pie Flavor" +
                            "<br>(Puny Pies, Inc.) </h3>")
        self.setLegendVisible(False)
        self.getXAxis().setAxisVisible(False)
        self.getYAxis().setAxisVisible(False)
        self.getXAxis().setAxisMin(0)
        self.getXAxis().setAxisMax(10)
        self.getXAxis().setTickCount(0)
        self.getYAxis().setAxisMin(0)
        self.getYAxis().setAxisMax(10)
        self.getYAxis().setTickCount(0)
        # this line orients the center of the first slice (apple) due east
        self.setInitialPieSliceOrientation(0.75 - pieMarketShare[0]/2)
        for i in range(len(pieMarketShare)):
            self.addCurve()
            self.getCurve().addPoint(5,5)
            self.getCurve().getSymbol().setSymbolType(
                                    SymbolType.PIE_SLICE_OPTIMAL_SHADING)
            self.getCurve().getSymbol().setBorderColor("white")
            self.getCurve().getSymbol().setBackgroundColor(pieColors[i])
            # next two lines define pie diameter in x-axis model units
            self.getCurve().getSymbol().setModelWidth(6)
            self.getCurve().getSymbol().setHeight(0)
            self.getCurve().getSymbol().setFillSpacing(0)
            self.getCurve().getSymbol().setFillThickness(3)
            self.getCurve().getSymbol().setHovertextTemplate(
                    GChartUtil.formatAsHovertext(pieTypes[i] + ", " +
                            "%d%%" % round(100*pieMarketShare[i])))
            self.getCurve().getSymbol().setPieSliceSize(pieMarketShare[i])
            self.getCurve().getPoint().setAnnotationText(pieTypes[i])
            self.getCurve().getPoint().setAnnotationLocation(
                                    AnnotationLocation.OUTSIDE_PIE_ARC)
        
    
    


