import DOM
from pyjamas.ui import SimplePanel, TabPanel, TabBar

"""
/**
 * <p>
 * A {@link SimplePanel} that wraps its contents in stylized boxes, which can be
 * used to add rounded corners to a {@link Widget}.
 * </p>
 * <p>
 * Wrapping a {@link Widget} in a "9-box" allows users to specify images in each
 * of the corners and along the four borders. This method allows the content
 * within the {@link DecoratorPanel} to resize without disrupting the look of
 * the border. In addition, rounded corners can generally be combined into a
 * single image file, which reduces the number of downloaded files at startup.
 * This class also simplifies the process of using AlphaImageLoaders to support
 * 8-bit transparencies (anti-aliasing and shadows) in ie6, which does not
 * support them normally.
 * </p>
 * 
 * <h3>CSS Style Rules</h3>
 * <ul class='css'>
 * <li>.gwt-DecoratorPanel { the panel }</li>
 * <li>.gwt-DecoratorPanel .top { the top row }</li>
 * <li>.gwt-DecoratorPanel .topLeft { the top left cell }</li>
 * <li>.gwt-DecoratorPanel .topLeftInner { the inner element of the cell }</li>
 * <li>.gwt-DecoratorPanel .topCenter { the top center cell }</li>
 * <li>.gwt-DecoratorPanel .topCenterInner { the inner element of the cell }</li>
 * <li>.gwt-DecoratorPanel .topRight { the top right cell }</li>
 * <li>.gwt-DecoratorPanel .topRightInner { the inner element of the cell }</li>
 * <li>.gwt-DecoratorPanel .middle { the middle row }</li>
 * <li>.gwt-DecoratorPanel .middleLeft { the middle left cell }</li>
 * <li>.gwt-DecoratorPanel .middleLeftInner { the inner element of the cell }</li>
 * <li>.gwt-DecoratorPanel .middleCenter { the middle center cell }</li>
 * <li>.gwt-DecoratorPanel .middleCenterInner { the inner element of the cell }</li>
 * <li>.gwt-DecoratorPanel .middleRight { the middle right cell }</li>
 * <li>.gwt-DecoratorPanel .middleRightInner { the inner element of the cell }</li>
 * <li>.gwt-DecoratorPanel .bottom { the bottom row }</li>
 * <li>.gwt-DecoratorPanel .bottomLeft { the bottom left cell }</li>
 * <li>.gwt-DecoratorPanel .bottomLeftInner { the inner element of the cell }</li>
 * <li>.gwt-DecoratorPanel .bottomCenter { the bottom center cell }</li>
 * <li>.gwt-DecoratorPanel .bottomCenterInner { the inner element of the cell }</li>
 * <li>.gwt-DecoratorPanel .bottomRight { the bottom right cell }</li>
 * <li>.gwt-DecoratorPanel .bottomRightInner { the inner element of the cell }</li>
 * </ul>
 */
"""
class DecoratorPanel(SimplePanel):
    #The default style name.
    DEFAULT_STYLENAME = "gwt-DecoratorPanel"

    #The default styles applied to each row.
    DEFAULT_ROW_STYLENAMES = [ "top", "middle", "bottom" ]

    def __init__(self, rowStyles=None,
                             containerIndex=1) :
        """ Creates a new panel using the specified style names to
            apply to each row.  Each row will contain three cells
            (Left, Center, and Right). The Center cell in the
            containerIndex row will contain the {@link Widget}.
            
            @param rowStyles an array of style names to apply to each row
            @param containerIndex the index of the container row
        """
      
        if rowStyles == None:
            rowStyles = self.DEFAULT_ROW_STYLENAMES

        SimplePanel.__init__(self, DOM.createTable())

        # Add a tbody
        self.table = self.getElement()
        self.tbody = DOM.createTBody()
        DOM.appendChild(self.table, self.tbody)
        DOM.setIntAttribute(self.table, "cellSpacing", 0)
        DOM.setIntAttribute(self.table, "cellPadding", 0)

        # Add each row
        for i in range(len(rowStyles)): 
            row = self.createTR(rowStyles[i])
            DOM.appendChild(self.tbody, row)
            if i == containerIndex:
                self.containerElem = DOM.getFirstChild(DOM.getChild(row, 1))

        # Set the overall style name
        self.setStyleName(self.DEFAULT_STYLENAME)

    def createTR(self, styleName) :
        """ Create a new row with a specific style name. The row
            will contain three cells (Left, Center, and Right), each
            prefixed with the specified style name.
         
            This method allows Widgets to reuse the code on a DOM
            level, without creating a DecoratorPanel Widget.
         
            @param styleName the style name
            @return the new row {@link Element}
        """
        trElem = DOM.createTR()
        self.setStyleName(trElem, styleName)
        DOM.appendChild(trElem, self.createTD(styleName + "Left"))
        DOM.appendChild(trElem, self.createTD(styleName + "Center"))
        DOM.appendChild(trElem, self.createTD(styleName + "Right"))
        return trElem

    def createTD(self, styleName) :
        """ Create a new table cell with a specific style name.
         
            @param styleName the style name
            @return the new cell {@link Element}
        """
        tdElem = DOM.createTD()
        inner = DOM.createDiv()
        DOM.appendChild(tdElem, inner)
        self.setStyleName(tdElem, styleName)
        self.setStyleName(inner, styleName + "Inner")
        return tdElem

    def getCellElement(self, row, cell) :
      """   Get a specific Element from the panel.
       
        @param row the row index
        @param cell the cell index
        @return the Element at the given row and cell
      """
      tr = DOM.getChild(self.tbody, row)
      td = DOM.getChild(tr, cell)
      return DOM.getFirstChild(td)

    def getContainerElement(self):
        return self.containerElem

class DecoratedTabBar(TabBar):

    TAB_ROW_STYLES = ["tabTop", "tabMiddle"]

    STYLENAME_DEFAULT = "gwt-DecoratedTabBar"

    def __init__(self):
        """ Creates an empty {@link DecoratedTabBar}.
        """
        TabBar.__init__(self)
        self.setStyleName(self.STYLENAME_DEFAULT)

    def createTabTextWrapper(self):
        return DecoratorPanel(self.TAB_ROW_STYLES, 1)

class DecoratedTabPanel(TabPanel):
    DEFAULT_STYLENAME = "gwt-DecoratedTabPanel"

    def __init__(self):
        TabPanel.__init__(self, DecoratedTabBar())

        self.setStyleName(self.DEFAULT_STYLENAME)
        self.getTabBar().setStyleName(DecoratedTabBar.STYLENAME_DEFAULT)

    def createTabTextWrapper(self):
        return DecoratorPanel(DecoratedTabBar.TAB_ROW_STYLES, 1)
