import math

from pyjamas.ui import Event
from pyjamas.ui.Button import Button
from pyjamas.ui.DialogBox import DialogBox
from pyjamas.ui.DockPanel import DockPanel
from pyjamas.ui.FlexTable import FlexTable
from pyjamas.ui import HasHorizontalAlignment
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.ListBox import ListBox
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.chart.GChart import GChart
from pyjamas.chart import AnnotationLocation
from pyjamas.chart import SymbolType
from pyjamas.chart import TouchedPointUpdateOption

LABEL_COL = 0;  # for the label/object pairs
OBJECT_COL = 1; # associated with the property
N_COLS = 2;     # editing form

N_SLICES = 5

"""*
* This example displays a pie chart that, when you click on any slice,
* opens a dialog that lets you modify the color, shading pattern, and
* size of of that slice. That dialog also contains "Prev Slice" and "Next
* Slice" buttons that, by invoking GChart's <tt>touch</tt> method,
* programmatically emulate the user sequentially "touching" (selecting)
* slices with their mouse.
*
* <p>
*
* The slice properties dialog in this example is an ordinary GWT modal
* dialog (a <tt>DialogBox</tt> with modal=True, autoHide=True). It self.gets
* GChart to inform it of click events on the chart by implementing the
* standard GWT <tt>ClickHandler</tt> interface, and then passing
* itself to GChart's <tt>addClickHandler</tt> method. The dialog's
* <tt>onClick</tt> method shows itself (via <tt>DialogBox.show</tt>)
* and then uses GChart's <tt>getTouchedPoint</tt> method to self.get a
* reference to the clicked-on slice that it uses to load that slice's
* properties into the form. As the user makes changes via the form,
* they are copied back into the chart and the chart's <tt>update</tt>
* method is invoked to immediately show the changes on the chart.
* <p>
*
* GChart's "currently touched point" (available via
* <tt>getTouchedPoint</tt>) ordinarily moves in lock-step with current
* mouse location, and thus falls short of a True point selection
* capability. This example works around this limitation by exploiting
* the fact that a GWT modal dialog "eats" all mouse events while it is
* open. So, when the modal dialog is opened, the mouse location seen by
* GChart, and hence the "currently touched" point is frozen. This lets
* us use GChart's currently touched point as if it were the "selected"
* point in this example.
*
"""

"""
* A helper class to facilitate property editing via drop-down
* lists in this example (there's nothing GChart-specific here):
"""
class ObjectSelectorDropdownList(ListBox):

    def __init__(self, labelObjectPairs):
        ListBox.__init__(self)
        self.labelObjectPairs = labelObjectPairs
        self.setVisibleItemCount(1); # makes it a drop-down list
        # add each label as an item on the drop-down list
        for i in range(len(labelObjectPairs)):
            self.addItem( labelObjectPairs[i][LABEL_COL])

    #  returns object at given index
    def getObject(self, index):
        result = self.labelObjectPairs[index][OBJECT_COL]
        return result


    # returns the currently selected object in the drop-down list
    def getSelectedObject(self):
        result = self.getObject(getSelectedIndex())
        return result


    # makes given object the selected one (assumes it's on list--once)
    def setSelectedObject(self, selectedObject):
        for i in range(len(self.labelObjectPairs)):
            if selectedObject == labelObjectPairs[i][OBJECT_COL]:
                self.setSelectedIndex(i)
                return


        raise IllegalArgumentException(
        "selectedObject specified was not found on the labelObjectPairs list.")



    # number of label, object pairs
    def getNObjects(self):
        return len(self.labelObjectPairs)


 # class ObjectSelectorDropdownList
#
# holds color information associated with color selection drop-down
class ColorSpec:
    def __init__(self, backgroundColor, borderColor):
        self.backgroundColor = backgroundColor
        self.borderColor =borderColor



# the modal dialog that pops up when they click on a slice to edit it
class SliceEditor(DialogBox):
    def __init__(self, chart):
        """ DialogBox CSS Style self.settings used with this example for reference:

        Note: These simplified CSS styles make the dialog's title bar behave a
        little quirkily in IE6 when dragging. For more sophisticated CSS that
        fixes this problem (and also provides a more professional look) see the
        CSS tab of the DialogBox example in the GWT <a href="xxx"> Showcase of
        Features</a> (I just didn't want to copy 5 pages of obscure DialogBox
        CSS into what is after all a Client-side GChart example).

        .gwt-DialogBox .Caption {
            font-size: 18
            color: #eef
            background: #00f repeat-x 0px -2003px
            padding: 4px 4px 4px 8px
            cursor: default
            border-bottom: 2px solid #008
            border-top: 3px solid #448


        .gwt-DialogBox .dialogContent {
            border: 1px solid #008
            background: #ddd
            padding: 3px


        """
        DialogBox.__init__(self, autoHide=True, modal=True)
        self.chart = chart
        self.isFirstTime = True
        mainPanel = VerticalPanel()
        propertyForm = FlexTable()
        commandBar = DockPanel()
        sliceSwitcher = HorizontalPanel()
        self.prevSlice = Button("&lt;Prev Slice")
        self.nextSlice = Button("Next Slice&gt;")
        self.closeButton = Button("Close")

        self.chart.colorSelector.addChangeListener(self)
        self.chart.sliceSizeSelector.addChangeListener(self)
        self.chart.shadingSelector.addChangeListener(self)

        def onChange(self, sender):
            self.chart.copyFormPropertiesIntoChart(self.chart.getTouchedPoint())
            # Changes in slice size can place a different, or no, slice under
            # GChart's "current mouse position". Such chart changes "underneath the
            # mouse" would normally result in a change in the touched point; the
            # TOUCHED_POINT_LOCKED update option keeps that from happening.
            self.chart.update(TouchedPointUpdateOption.TOUCHED_POINT_LOCKED)

        # slice properties table (slice color, shading and size)
        propertyForm.setText(  0, 0, "Color:")
        propertyForm.setWidget(0, 1, self.chart.colorSelector)
        propertyForm.setText(  1, 0, "Shading Pattern:")
        propertyForm.setWidget(1, 1, self.chart.shadingSelector)
        propertyForm.setText(  2, 0, "Slice Size:")
        propertyForm.setWidget(2, 1, self.chart.sliceSizeSelector)
        # add additional properties here, if desired

        # buttons for changing the selected slice from the form
        sliceSwitcher.add(self.prevSlice)
        sliceSwitcher.add(self.nextSlice)

        commandBar.add(sliceSwitcher, DockPanel.WEST)
        commandBar.add(self.closeButton, DockPanel.EAST)
        commandBar.setCellHorizontalAlignment(self.closeButton,
                        HasHorizontalAlignment.ALIGN_RIGHT)
        commandBar.setWidth("100%"); # pushes close button to right edge

        # create main form and place it in DialogBox
        mainPanel.add(propertyForm)
        mainPanel.add(commandBar)
        self.add(mainPanel);  # add the DialogBox' single, defining, widget

    # loads properties associated with point/slice into form
    def copyChartPropertiesIntoForm(self, p):
        # dialog title bar caption:
        self.setText("Slice " + self.getCurveIndex(p.getParent()) +
                                    " Properties")
        colorSelector.setSelectedObject(
        self.getColorSpec( p.getParent().getSymbol().getBackgroundColor(),
                           p.getParent().getSymbol().getBorderColor()))
        shadingSelector.setSelectedObject(
                        p.getParent().getSymbol().getSymbolType())
        sliceSize = math.round(100*p.getParent().getSymbol().getPieSliceSize())
        sliceSizeSelector.setSelectedObject( int(sliceSize))

    # saves current form self.settings into associated point/slice of chart
    def copyFormPropertiesIntoChart(self, p):
        p.getParent().getSymbol().setBackgroundColor(
                    colorSelector.getSelectedObject().backgroundColor)
        p.getParent().getSymbol().setBorderColor(
                    colorSelector.getSelectedObject().borderColor)

        # selection flips border and background colors
        p.getParent().getSymbol().setHoverSelectionBorderColor(
                    colorSelector.getSelectedObject().backgroundColor)
        p.getParent().getSymbol().setHoverSelectionBackgroundColor(
                    colorSelector.getSelectedObject().borderColor)
        p.getParent().getSymbol().setSymbolType(
                                shadingSelector.getSelectedObject())
        sliceSize = int(sliceSizeSelector.getSelectedObject())
        p.getParent().getSymbol().setPieSliceSize(sliceSize/100.)

    def onClick(self, sender):
        if sender == self.prevSlice:
            self.chart.onClickPrevSlice(sender)
        elif sender == self.nextSlice:
            self.chart.onClickNextSlice(sender)
        else:
            self.onClickClose(sender)

    def onClickClose(self, event):
        self.hide()
        self.chart.touch(None);  # clears any selected slice
        self.chart.update(TouchedPointUpdateOption.TOUCHED_POINT_LOCKED)



    # Retrieves an existing ColorSpec object reference, given its colors
    def getColorSpec(self, backgroundColor, borderColor):
        for i in range(colorSelector.getNObjects()):
            cs =  self.chart.colorSelector.getObject(i)
            if backgroundColor == cs.backgroundColor and  borderColor == cs.borderColor:
                return cs


        raise IllegalArgumentException(
        "Attempt to retrieve a non-existing color combination.")



    def onClick(self, event):
        # don't shown property editor if they clicked on nothing
        if None == self.getTouchedPoint():
            return


        # load properties of clicked-on slice into form
        copyChartPropertiesIntoForm(getTouchedPoint())
        if isFirstTime:
            # initially put upper left corner wherever they clicked...
            self.setPopupPosition(
            Window.getScrollLeft()+Event.getCurrentEvent().getClientX(),
            Window.getScrollTop() + Event.getCurrentEvent().getClientY())
            self.show()
            self.isFirstTime= False

        else:
            # ...thereafter, just stay whereever they dragged it to
            self.show()




class GChartExample20 (GChart):




    # the single dialog box that self.gets used to edit any slice
    def __init__(self):
        GChart.__init__(self)

        # labels/values for color selection drop-down list:
        self.colorSelector = ObjectSelectorDropdownList( \
                            [["Red", ColorSpec("red", "#F88")],
                            ["Fuchsia", ColorSpec("#F0F", "#F8F")],
                            ["Lime", ColorSpec("#0F0", "#8F8")],
                            ["Blue", ColorSpec("#00F", "#88F")],
                            ["Aqua", ColorSpec("#0FF", "#8FF")],
                            ["Maroon", ColorSpec("#800", "#C88")],
                            ["Purple", ColorSpec("#808", "#C8C")],
                            ["Green", ColorSpec("#080", "#8C8")],
                            ["Olive", ColorSpec("#880", "#CC8")],
                            ["Navy", ColorSpec("#008", "#88C")],
                            ["Teal", ColorSpec("#088", "#8CC")]])

        # labels/values for slice shading pattern drop-down list
        self.shadingSelector = ObjectSelectorDropdownList( \
            [["Vertical shading", SymbolType.PIE_SLICE_VERTICAL_SHADING],
            ["Horizontal shading", SymbolType.PIE_SLICE_HORIZONTAL_SHADING],
            ["Optimal shading", SymbolType.PIE_SLICE_OPTIMAL_SHADING]])

        # labels/values for pie slice size (as percentage) drop-down list
        self.sliceSizeSelector = ObjectSelectorDropdownList([
                                            ["0%", int(0)],
                                            ["5%", int(5)],
                                            ["10%", int(10)],
                                            ["15%", int(15)],
                                            ["20%", int(20)],
                                            ["25%", int(25)],
                                            ["30%", int(30)],
                                            ["35%", int(35)],
                                            ["40%", int(40)],
                                            ["45%", int(45)],
                                            ["50%", int(50)],
                                            ["55%", int(55)],
                                            ["60%", int(60)],
                                            ["65%", int(65)],
                                            ["70%", int(70)],
                                            ["75%", int(75)],
                                            ["80%", int(80)],
                                            ["85%", int(85)],
                                            ["90%", int(90)],
                                            ["95%", int(95)],
                                            ["100%", int(100)]])

        self.theSliceEditor = SliceEditor(self)

        SOURCE_CODE_LINK = \
        "<a href='GChartExample20.txt' target='_blank'>Source code</a>"
        self.setChartSize(100, 100)
        self.setBorderStyle("none")
        self.setChartTitle("<big>Click pie to edit!</big>")
        self.setChartTitleThickness(20)
        self.setChartFootnotes(SOURCE_CODE_LINK)
        self.setChartFootnotesThickness(20)
        # initial slice sizes
        initSliceSize = [0.3, 0.2, 0.1, 0.2, 0.2]

        self.addClickListener(self.theSliceEditor)

        for iCurve in range(N_SLICES):
            self.addCurve()
            self.getCurve().getSymbol().setBorderWidth(1)
            self.getCurve().getSymbol().setFillThickness(4)
            self.getCurve().getSymbol().setFillSpacing(4)
            self.getCurve().getSymbol().setHoverLocation(
            AnnotationLocation.ON_PIE_ARC)
            self.getCurve().getSymbol().setBorderColor(
                    self.colorSelector.getObject(iCurve).borderColor)
            self.getCurve().getSymbol().setBackgroundColor(
                    self.colorSelector.getObject(iCurve).backgroundColor)
            # selection flips border and background colors
            self.getCurve().getSymbol().setHoverSelectionBackgroundColor(
                    self.colorSelector.getObject(iCurve).borderColor)
            self.getCurve().getSymbol().setHoverSelectionBorderColor(
                    self.colorSelector.getObject(iCurve).backgroundColor)
            self.getCurve().getSymbol().setSymbolType(
                    SymbolType.PIE_SLICE_OPTIMAL_SHADING)
            self.getCurve().getSymbol().setPieSliceSize(initSliceSize[iCurve])
            self.getCurve().getSymbol().setModelHeight(1.0); #diameter = yMax-yMin
            self.getCurve().getSymbol().setModelWidth(0)
            self.getCurve().addPoint(0.5, 0.5);  # pie centered in world units

        self.getXAxis().setAxisMin(0);  # so 0.5,0.5 (see above) centers pie
        self.getXAxis().setAxisMax(1)
        self.getYAxis().setAxisMin(0)
        self.getYAxis().setAxisMax(1)
        self.getXAxis().setHasGridlines(False); # hides axes, ticks, etc.
        self.getXAxis().setAxisVisible(False);  # (not needed for the pie)
        self.getXAxis().setTickCount(0)
        self.getYAxis().setHasGridlines(False)
        self.getYAxis().setAxisVisible(False)
        self.getYAxis().setTickCount(0)
        self.update()


    def onClickPrevSlice(self, event):
        iCurve = self.getCurveIndex(self.getTouchedCurve())
        if (iCurve == 0) :
            iPrev = self.getNCurves()-1
        else:
            iPrev = (iCurve-1)
        self.touch(self.getCurve(iPrev).getPoint(0))
        self.copyChartPropertiesIntoForm(self.getTouchedPoint())
        self.update(TouchedPointUpdateOption.TOUCHED_POINT_LOCKED)

    def onClickNextSlice(self, event):
        iCurve = self.getCurveIndex(self.getTouchedCurve())
        if (iCurve+1 == self.getNCurves()) :
            iNext = 0
        else:
            iNext = (iCurve+1)
        self.touch(self.getCurve(iNext).getPoint(0))
        self.copyChartPropertiesIntoForm(self.getTouchedPoint())
        self.update(TouchedPointUpdateOption.TOUCHED_POINT_LOCKED)

