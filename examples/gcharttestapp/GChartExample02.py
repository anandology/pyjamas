from GChartTestAppUtil import rnd

from pyjamas.chart import GChartUtil
from pyjamas.chart.GChart import GChart
from pyjamas.chart import AnnotationLocation
from pyjamas.chart import SymbolType

from pyjamas.ui.Button import Button

groupLabels = [ \
"<html>2007<br><small><small>O Seven",
"<html>2008<br><small><small>Owe Ate",
"<html>2009<br><i><small><small>Oh Nein!"]
barLabels = [ "Q1", "Q2", "Q3", "Q4"]
barColors = [ "red", "blue", "green", "silver"]
MAX_REVENUE = 1000
WIDTH = 300
HEIGHT = 200

"""*
* Defines a traditional "quarterly revenues" grouped bar-chart.
"""
class GChartExample02(GChart):
    def __init__(self):
        GChart.__init__(self)


        self.updateButton = Button("<b><big>Generate New Simulated Revenues</big></b>")
        
        self.setChartSize(WIDTH, HEIGHT)
        self.setChartTitle("<b><big><big>" +
                    "Simulated Quarterly Revenues" +
                    "</big></big><br>&nbsp;</b>")
        self.updateButton.addClickListener(self)
    
        self.setChartFootnotes(updateButton)
        for iCurve in range(len(barLabels)):
            self.addCurve()     # one curve per quarter
            self.getCurve().getSymbol().setSymbolType(SymbolType.VBAR_SOUTHWEST)
            self.getCurve().getSymbol().setBackgroundColor(barColors[iCurve])
            self.getCurve().setLegendLabel(barLabels[iCurve])
            self.getCurve().getSymbol().setHovertextTemplate(
                GChartUtil.formatAsHovertext(barLabels[iCurve] + " revenue=${y}"))
            self.getCurve().getSymbol().setModelWidth(1.0)
            self.getCurve().getSymbol().setBorderColor("black")
            self.getCurve().getSymbol().setBorderWidth(1)
            for jGroup in range(len(groupLabels)):
                # the '+1' creates a bar-sized gap between groups
                self.getCurve().addPoint(1+iCurve+jGroup*(len(barLabels)+1),
                                        rnd()*MAX_REVENUE)
                self.getCurve().getPoint().setAnnotationText(barLabels[iCurve])
                self.getCurve().getPoint().setAnnotationLocation(
                                    AnnotationLocation.NORTH)
            
        
        
        for i in range(len(groupLabels)):
            # formula centers tick-label horizontally on each group
            self.getXAxis().addTick(
                        len(barLabels)/2. + i*(len(barLabels)+1),
                        groupLabels[i])
        
        self.getXAxis().setTickLabelFontSize(20)
        self.getXAxis().setTickLabelThickness(40)
        self.getXAxis().setTickLength(6);    # small tick-like gap...
        self.getXAxis().setTickThickness(0); # but with invisible ticks
        self.getXAxis().setAxisMin(0);       # keeps first bar on chart
        
        self.getYAxis().setAxisMin(0);           # Based on sim revenue range
        self.getYAxis().setAxisMax(MAX_REVENUE); # of 0 to MAX_REVENUE.
        self.getYAxis().setTickCount(11)
        self.getYAxis().setHasGridlines(True)
        self.getYAxis().setTickLabelFormat("$#,###")
    


    def onClick(self, event):
        for iCurve in range(self.getNCurves()):
            for iPoint in range(self.getCurve(iCurve).getNPoints()):
                self.getCurve(iCurve).getPoint(iPoint).setY(rnd()*MAX_REVENUE)
            
        self.update()
        self.updateButton.setFocus(True)
