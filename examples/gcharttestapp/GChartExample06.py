
from pyjamas.chart.GChart import GChart
from pyjamas.chart import GChartUtil
from pyjamas.chart import AnnotationLocation
from pyjamas.chart import SymbolType

"""*
* Defines a "square pie chart", that is, a
* fat, axes-free, stacked bar chart that is
* often an acceptable alterto a pie-chart.
* <p>
*
* Even though, as of version 2.0, GChart also supports
* round pie charts, square pie charts are still
* much more efficient.
*
"""
class GChartExample06(GChart):
    def __init__(self):
        GChart.__init__(self)
        self.setChartTitle("<b><i>Market Share by Region</i></b>")
        SIZE = 200
        self.setChartSize(SIZE, SIZE)
        region = ["USA", "Canada", "Mexico", "India", "France", "Iceland"]
        # elements in this array must sum to 100.
        percent = [35, 25, 15, 10, 10, 5]
        colors = ["red", "green", "yellow", "fuchsia", "silver", "aqua"]
        sum = 0
        for i in range(len(percent)-1, -1, -1):
            self.addCurve()
            self.getCurve().getSymbol().setSymbolType(SymbolType.BOX_SOUTHEAST)
            self.getCurve().getSymbol().setModelHeight(percent[i])
            self.getCurve().getSymbol().setBackgroundColor(colors[i])
            self.getCurve().getSymbol().setBorderColor(colors[i])
            self.getCurve().getSymbol().setWidth(SIZE)
            self.getCurve().getSymbol().setHoverAnnotationSymbolType(
                                        SymbolType.ANCHOR_MOUSE_SNAP_TO_Y)
            self.getCurve().getSymbol().setHoverLocation(
                                        AnnotationLocation.SOUTHEAST)

            self.getCurve().getSymbol().setHovertextTemplate(
            GChartUtil.formatAsHovertext(region[i] + ", " + percent[i] + "%"))
            self.getCurve().setLegendLabel(region[i])
            self.getCurve().addPoint(0, 100-sum)
            self.getCurve().getPoint().setAnnotationText(region[i])
            self.getCurve().getPoint().setAnnotationFontWeight("bold")
            self.getCurve().getPoint().setAnnotationLocation(
                                            AnnotationLocation.CENTER)
            sum += percent[i]

        self.getXAxis().setTickCount(0)
        self.getXAxis().setTickThickness(0)
        self.getXAxis().setAxisMin(0)
        self.getXAxis().setAxisMax(SIZE)
        self.getYAxis().setTickCount(0)
        self.getYAxis().setTickThickness(0)
        self.getYAxis().setAxisMin(0)
        self.getYAxis().setAxisMax(100)




