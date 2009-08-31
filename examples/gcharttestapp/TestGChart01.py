import GChartTestAppUtil

from pyjamas.chart.GChart import GChart
from pyjamas.chart import GChartConsts
from pyjamas.chart import AnnotationLocation
from pyjamas.chart import SymbolType

from pyjamas.ui.Button import Button

msg = [["Check: all chart elements except labels red",
"Check: missing image icon appears on points and plot area.",
"Check: no missing image icon appears on chart area or points",
"Check: missing image icons appear on points and plot area iff IP connection is down (otherwise, 3D pies)"],
["Check: all points red",
"Check: missing image icon appears on all points",
"Check: no missing image icon appears on chart",
"Check: missing image icons appear on points iff IP connection is down (otherwise, 3D pies)."],
["Check: plot area red",
"Check: missing image icon appears on plot area",
"Check: no missing image icon appears on plot area",
"Check: missing image icon appears on plot area iff IP connection is down (otherwise, 3D pies)."]]

imageURL = [
    "red.gif",
    "no-such-file.gif",
    "gchart.gif",
    "http://chart.apis.google.com/chart?cht=p3&chd=t:100&chs=500x200"
]

"""* Simple a chart with just one point on it, used for testing
** methods for telling GChart to look for the blank gif in
** the host page, rather than the module base, directory. """
class TestGChart01 (GChart):
    def __init__(self, imageId, targetArea):
        GChart.__init__(self, XChartSize=500,YChartSize=200)
        self.setChartTitle(GChartTestAppUtil.getTitle(self)+" imageId="+str(imageId)+ " targetArea=" + str(targetArea))

        self.setChartFootnotes(msg[targetArea][imageId])
        self.addCurve()
        if targetArea==0:
            self.setBlankImageURL(imageURL[imageId])

        elif targetArea == 1:
            self.getCurve().getSymbol().setImageURL(imageURL[imageId])

        elif targetArea == 2:
            self.setPlotAreaImageURL(imageURL[imageId])

        if targetArea==0:
            if self.getBlankImageURL() != imageURL[imageId]:
                raise IllegalStateException("getBlankImageURL method failed.")


        elif targetArea == 1:
            if self.getCurve().getSymbol().getImageURL() != imageURL[imageId]:
                raise IllegalStateException("getImageURL method failed.")


        elif targetArea == 2:
            if self.getPlotAreaImageURL() != imageURL[imageId]:
                raise IllegalStateException("getPlotAreaImageURL method failed.");



        self.getCurve().getSymbol().setModelHeight(1)
        self.getCurve().getSymbol().setModelWidth(1)
        self.getCurve().getSymbol().setBorderWidth(0)
        self.getCurve().addPoint(1, 1)
        self.getCurve().addPoint(2, 2)
        self.getCurve().addPoint(3, 3)
        self.getCurve().setLegendLabel("Curve 0")
        # restore default blank image URL for any future tests
        self.update()
        self.setBlankImageURL(GChartConsts.DEFAULT_BLANK_IMAGE_URL)



