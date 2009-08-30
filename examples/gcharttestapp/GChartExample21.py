


from pyjamas.ui.Button import Button
from pyjamas.ui.HTML import HTML
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.chart.GChart import GChart
from pyjamas.chart import AnnotationLocation
from pyjamas.chart import SymbolType

"""*
*
* In this example, whenever the user clicks on a point, a
* hover widget that allows them to increase or decrease
* the y value of that point appears below the chart.
* <p>
*
* The chart uses <tt>setHoverTouchingEnabled(False)</tt> to
* disable GChart's "auto-select-on-mouseover" feature. This
* assures that, when the user clicks on a point, that point
* remains selected, as required, when their mouse moves
* below the chart to interact with the y-value-changing
* hover widget.<p>
*
* In general, by disabling hover touching in this manner,
* you can make a GChart act much like a single-selection
* listbox, with points playing the role of list items.
* <p>
*
* The screen shot shows what the chart looks like after the
* user clicks on a center bar, and then clicks the
* "Increment Y" button a few times.
*
*
"""

# hover widget that changes y value of selected point
class YChanger (HorizontalPanel):

    def __init__(self, chart):
        self.chart = chart
        HorizontalPanel.__init__(self)
        # y-changing, x,y coordinate displaying, widget
        self.incrementY = Button("Increment Y")
        self.coordinates = HTML(""); # x,y of selected point
        self.decrementY = Button("Decrement Y")
        self.incrementY.addClickListener(self)
        self.decrementY.addClickListener(self)
        self.add(self.incrementY)
        self.add(self.coordinates)
        self.add(self.decrementY)
    
    def onClick(self, sender):
        if sender == self.incrementY:
            self.chart.getTouchedPoint().setY(
                                self.chart.getTouchedPoint().getY() - 1)
        else:
            self.chart.getTouchedPoint().setY(
                                self.chart.getTouchedPoint().getY() + 1)
        self.chart.update()
    
    # The 2 HoverUpdateable interface methods:
    def hoverCleanup(self, hoveredAwayFrom):
    
    def hoverUpdate(self, hoveredOver):
        # update (x,y) display when they click point
        coordinates.setHTML(hoveredOver.getHovertext())
    

class GChartExample21(GChart):
    
    def __init__(self):
        GChart.__init__(self)
        self.setChartSize(300, 300)
        self.setBorderStyle("none")
        """
        * So selection changing requires the user to click
        * (not just mouseover a point). This allows the
        * selection to stay put while user moves to click the
        * y-changing buttons.
        *
        """
        self.setHoverTouchingEnabled(False)
        self.addCurve()
        # make a y-changer pop up when they click a point
        self.getCurve().getSymbol().setHoverWidget(YChanger(self))
        # Configure hover annotation so it appears below chart
        self.getCurve().getSymbol().setHoverAnnotationSymbolType(
                                    SymbolType.ANCHOR_SOUTH)
        self.getCurve().getSymbol().setHoverLocation(AnnotationLocation.SOUTH)
        self.getCurve().getSymbol().setHoverYShift(-30)
        # 3px, external point selection border
        self.getCurve().getSymbol().setHoverSelectionBorderWidth(-3)
        
        # configure curve as a baseline-based bar chart
        self.getCurve().getSymbol().setSymbolType(SymbolType.VBAR_BASELINE_EAST)
        self.getCurve().getSymbol().setModelWidth(1)
        self.getCurve().getSymbol().setBorderWidth(1)
        self.getCurve().getSymbol().setBorderColor("black")
        self.getCurve().getSymbol().setBackgroundColor("blue")
        # add a simple y = 2*x curve
        for iPoint in range(10):
            self.getCurve().addPoint(iPoint, 2*iPoint)

