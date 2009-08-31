import GChartTestAppUtil

from pyjamas.chart.GChart import GChart
from pyjamas.chart import GChartConsts
from pyjamas.chart import SymbolType

# test that clipping of points to plot area works as expected
class TestGChart05 (GChart):
    def __init__(self, testCanvas):
        GChart.__init__(self, XChartSize=300,YChartSize=300)
        self.setChartTitle(GChartTestAppUtil.getTitle(self))
        self.setClipToPlotArea(True)
        self.setChartFootnotes("Check: an unclipped point at each corner.<br> No x-ticks.<br>Line clipped at plot area limits<br>Three clipped-off pies visible<br>Every at-least-partly visible symbol labeled.")
        
        self.getXAxis().setHasGridlines(True)
        self.getY2Axis().setHasGridlines(True)
        self.addCurve()
        if testCanvas:
            self.getCurve().getSymbol().setFillSpacing(0)
        
        self.getCurve().setYAxis(GChartConsts.Y_AXIS)
        self.getCurve().addPoint(0,-95); # clipped
        self.getCurve().getPoint().setAnnotationText(self.getCurve().getPoint().getHovertext())
        self.getCurve().addPoint(0,-90)
        self.getCurve().getPoint().setAnnotationText(self.getCurve().getPoint().getHovertext())
        self.getCurve().addPoint(0,0)
        self.getCurve().getPoint().setAnnotationText(self.getCurve().getPoint().getHovertext())
        self.getCurve().addPoint(0,5);   # clipped
        self.getCurve().getPoint().setAnnotationText(self.getCurve().getPoint().getHovertext())
        
        self.getCurve().setLegendLabel("On Y")
        self.addCurve()
        if testCanvas:
            self.getCurve().getSymbol().setFillSpacing(0)
        
        self.getCurve().setYAxis(GChartConsts.Y2_AXIS)
        self.getCurve().addPoint(90,-50); # clipped
        self.getCurve().getPoint().setAnnotationText(self.getCurve().getPoint().getHovertext())
        self.getCurve().addPoint(90,-45)
        self.getCurve().getPoint().setAnnotationText(self.getCurve().getPoint().getHovertext())
        self.getCurve().addPoint(90,45)
        self.getCurve().getPoint().setAnnotationText(self.getCurve().getPoint().getHovertext())
        self.getCurve().addPoint(90,50);  # clipped
        self.getCurve().getPoint().setAnnotationText(self.getCurve().getPoint().getHovertext())
        self.getCurve().setLegendLabel("On Y2")
        
        # continuous line whose edges self.get clipped off
        self.addCurve()
        self.getCurve().setLegendLabel("clipped line")
        self.getCurve().getSymbol().setBackgroundColor("blue")
        self.getCurve().getSymbol().setBorderColor("blue")
        if testCanvas:
            self.getCurve().getSymbol().setFillSpacing(0)
        
        else:
            self.getCurve().getSymbol().setFillSpacing(10)
        
        self.getCurve().getSymbol().setFillThickness(3)
        self.getCurve().setYAxis(GChartConsts.Y_AXIS)
        #     self.getCurve().addPoint(50,-50)
        self.getCurve().addPoint(0,-100)
        self.getCurve().getPoint().setAnnotationText(self.getCurve().getPoint().getHovertext())
        #     self.getCurve().addPoint(50,-50)
        self.getCurve().addPoint(100,0)
        self.getCurve().getPoint().setAnnotationText(self.getCurve().getPoint().getHovertext())
        
        # this should be entirely visible
        self.addCurve()
        if testCanvas:
            self.getCurve().getSymbol().setFillSpacing(0)
        
        self.getCurve().setLegendLabel("inside pie")
        self.getCurve().getSymbol().setSymbolType(
                            SymbolType.PIE_SLICE_HORIZONTAL_SHADING)
        self.getCurve().getSymbol().setFillThickness(1)
        self.getCurve().getSymbol().setWidth(100)
        self.getCurve().getSymbol().setHeight(0)
        self.getCurve().setYAxis(GChartConsts.Y_AXIS)
        self.getCurve().addPoint(45,0)
        self.getCurve().getPoint().setAnnotationText(self.getCurve().getPoint().getHovertext())
        
        # this should be entirely clipped.
        self.addCurve()
        if testCanvas:
            self.getCurve().getSymbol().setFillSpacing(0)
        
        self.getCurve().setLegendLabel("outside right pie")
        self.getCurve().getSymbol().setSymbolType(
                            SymbolType.PIE_SLICE_HATCHED_SHADING)
        self.getCurve().getSymbol().setFillThickness(1)
        self.getCurve().getSymbol().setWidth(100)
        self.getCurve().getSymbol().setHeight(0)
        self.getCurve().setYAxis(GChartConsts.Y2_AXIS)
        self.getCurve().addPoint(95,0)
        self.getCurve().getPoint().setAnnotationText(self.getCurve().getPoint().getHovertext())
        # this should be entirely clipped
        self.addCurve()
        if testCanvas:
            self.getCurve().getSymbol().setFillSpacing(0)
        
        self.getCurve().setLegendLabel("outside bottom pie")
        self.getCurve().getSymbol().setSymbolType(
                            SymbolType.PIE_SLICE_VERTICAL_SHADING)
        self.getCurve().getSymbol().setFillThickness(1)
        self.getCurve().getSymbol().setWidth(100)
        self.getCurve().getSymbol().setHeight(0)
        self.getCurve().setYAxis(GChartConsts.Y_AXIS)
        self.getCurve().addPoint(45,-95)
        self.getCurve().getPoint().setAnnotationText(self.getCurve().getPoint().getHovertext())
        
        self.getXAxis().setAxisLabel("<small><small><small>X</small></small></small>")
        self.getXAxis().setTickCount(0)
        self.getXAxis().setAxisMin(0.)
        self.getXAxis().setAxisMax(90.)
        self.getYAxis().setAxisMin(-90.)
        self.getYAxis().setAxisMax(0.)
        self.getY2Axis().setAxisMin(-45.)
        self.getY2Axis().setAxisMax(45)
        
    


