"""
    Horizontal Split Panel: Left and Right layouts with a movable splitter.

/*
 * Copyright 2008 Google Inc.
 * 
 * Licensed under the Apache License, Version 2.0 (the "License") you may not
 * use this file except in compliance with the License. You may obtain a copy of
 * the License at
 * 
 * http:#www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 * License for the specific language governing permissions and limitations under
 * the License.
 */
"""

from pyjamas.splitpanel import SplitPanel
import DOM
from DeferredCommand import DeferredCommand
from Timer import Timer

class ImplHorizontalSplitPanel:
    """ The standard implementation for horizontal split panels.
    """
    def __init__(self, panel):
        self.panel = panel

        DOM.setStyleAttribute(panel.getElement(), "position", "relative")

        self.expandToFitParentHorizontally(panel.getWidgetElement(0))
        self.expandToFitParentHorizontally(panel.getWidgetElement(1))
        self.expandToFitParentHorizontally(panel.getSplitElement())

        self.panel.expandToFitParentUsingCssOffsets(panel.container)

        # Right now, both panes are stacked on top of each other
        # on either the left side or the right side of the containing
        # panel. This happens because both panes have position:absolute 
        # and no left/top values. The panes will be on the left side 
        # if the directionality is LTR, and on the right side if the 
        # directionality is RTL. In the LTR case, we need to snap the 
        # right pane to the right of the container, and in the RTL case,
        # we need to snap the left pane to the left of the container.      

        if True: # TODO: (LocaleInfo.getCurrentLocale().isRTL()):
            self.panel.setLeft(self.panel.getWidgetElement(0), "0px")        
        else:
            self.panel.setRight(self.panel.getWidgetElement(1), "0px")

    def expandToFitParentHorizontally(self, elem):
      self.panel.addAbsolutePositoning(elem)
      zeroSize = "0px"
      self.panel.setTop(elem, zeroSize)
      self.panel.setBottom(elem, zeroSize)


    def onAttach(self):
        pass
    def onDetach(self):
        pass

    def onSplitterResize(self, px):
        self.setSplitPositionUsingPixels(px)

    def setSplitPosition(self, pos):
        leftElem = self.panel.getWidgetElement(0)
        self.panel.setElemWidth(leftElem, pos)
        self.setSplitPositionUsingPixels(self.panel.getOffsetWidth(leftElem))

    def setSplitPositionUsingPixels(self, px):
        """ Set the splitter's position in units of pixels.
              
              px represents the splitter's position as a distance
              of px pixels from the left edge of the container. This is
              true even in a bidi environment. Callers of this method
              must be aware of this constraint.
        """
        splitElem = self.panel.getSplitElement()

        rootElemWidth = self.panel.getOffsetWidth(self.panel.container)
        splitElemWidth = self.panel.getOffsetWidth(splitElem)

        # This represents an invalid state where layout is incomplete. This
        # typically happens before DOM attachment, but I leave it here as a
        # precaution because negative width/height style attributes produce
        # errors on IE.
        if (rootElemWidth < splitElemWidth):
            return

        # Compute the new right side width.
        newRightWidth = rootElemWidth - px - splitElemWidth

        # Constrain the dragging to the physical size of the panel.
        if (px < 0):
            px = 0
            newRightWidth = rootElemWidth - splitElemWidth
        elif (newRightWidth < 0):
            px = rootElemWidth - splitElemWidth
            newRightWidth = 0

        rightElem = self.panel.getWidgetElement(1)

        # Set the width of the left side.
        self.panel.setElemWidth(self.panel.getWidgetElement(0), px + "px")

        # Move the splitter to the right edge of the left element.
        self.panel.setLeft(splitElem, px + "px")

        # Move the right element to the right of the splitter.
        self.panel.setLeft(rightElem, (px + splitElemWidth) + "px")

        self.updateRightWidth(rightElem, newRightWidth)


    def updateRightWidth(self, rightElem, newRightWidth):
        # No need to update the width of the right side this will be
        # recomputed automatically by CSS. This is helpful, as we do not
        # have to worry about watching for resize events and adjusting the
        # right-side width.
        pass
  
class ImplIE6HorizontalSplitPanel(ImplHorizontalSplitPanel):
    """ The IE6 implementation for horizontal split panels.
    """

    def __init__(self, panel):
        
        self.panel = panel
        self.isResizeInProgress = false
        self.splitPosition = 0

        elem = panel.getElement()

        # Prevents inherited text-align settings from interfering with the
        # panel's layout. The setting we choose must be bidi-sensitive,
        # as left-alignment is the default with LTR directionality, and
        # right-alignment is the default with RTL directionality.            
        if True: # TODO (LocaleInfo.getCurrentLocale().isRTL()) {
            DOM.setStyleAttribute(elem, "textAlign", "right")
        else:
            DOM.setStyleAttribute(elem, "textAlign", "left")  

        DOM.setStyleAttribute(elem, "position", "relative")

        # Technically, these are snapped to the top and bottom, but IE doesn't
        # provide a reliable way to make that happen, so a resize listener is
        # wired up to control the height of these elements.
        self.addAbsolutePositoning(panel.getWidgetElement(0))
        self.addAbsolutePositoning(panel.getWidgetElement(1))
        self.addAbsolutePositoning(panel.getSplitElement())

        self.expandToFitParentUsingPercentages(panel.container)

        if True: # TODO (LocaleInfo.getCurrentLocale().isRTL()):
        # Snap the left pane to the left edge of the container. We 
        # only need to do this when layout is RTL if we don't, the 
        # left pane will overlap the right pane.
            panel.setLeft(panel.getWidgetElement(0), "0px")

    def onAttach(self):
        self.addResizeListener(self.panel.container)
        self.onResize()

    def onDetach(self):
        DOM.setElementAttribute(self.panel.container, "onresize", null)

    def onTimer(self, sender):
        self.setSplitPositionUsingPixels(       self.splitPosition)
        self.isResizeInProgress = False

    def onSplitResize(self, px):
        if not self.isResizeInProgress:
            self.isResizeInProgress = true
            Timer(self, 20)
        self.splitPosition = px

    def setSplitPositionUsingPixels(self, px):
        if True: # TODO (LocaleInfo.getCurrentLocale().isRTL()) {
            splitElem = self.panel.getSplitElement()

            rootElemWidth = self.panel.getOffsetWidth(self.panel.container)
            splitElemWidth = self.panel.getOffsetWidth(splitElem)

            # This represents an invalid state where layout is incomplete. This
            # typically happens before DOM attachment, but I leave it here as a
            # precaution because negative width/height style attributes produce
            # errors on IE.
            if (rootElemWidth < splitElemWidth):
                return

            # Compute the new right side width.
            newRightWidth = rootElemWidth - px - splitElemWidth

            # Constrain the dragging to the physical size of the panel.
            if (px < 0):
                px = 0
                newRightWidth = rootElemWidth - splitElemWidth
            elif (newRightWidth < 0):
                px = rootElemWidth - splitElemWidth
                newRightWidth = 0

            # Set the width of the right side.
            self.panel.setElemWidth(self.panel.getWidgetElement(1), newRightWidth + "px")

            # Move the splitter to the right edge of the left element. 
            self.panel.setLeft(splitElem, px + "px")    

            # Update the width of the left side        
            if (px == 0):

              # This takes care of a qurky RTL layout bug with IE6. 
              # During DOM construction and layout, onResize events
              # are fired, and this method is called with px == 0. 
              # If one tries to set the width of the 0 element to
              # before layout completes, the 1 element will
              # appear to be blanked out.
              
                DeferredCommand.addCommand(self)
            else:
                self.panel.setElemWidth(self.panel.getWidgetElement(0), px + "px")

        else:
            ImplHorizontalSplitPanel.setSplitPositionUsingPixels(self, px)

    def execute(self):
        self.panel.setElemWidth(self.panel.getWidgetElement(0), "0px")

    def updateRightWidth(self, rightElem, newRightWidth):
        self.panel.setElemWidth(rightElem, newRightWidth + "px")

    def addResizeListener(self, container):
        JS("""
            this.container.onresize = function() {
                           __ImplIE6HorizontalSplitPanel_onResize();
                                      }
        """)

    def onResize(self):
      leftElem = self.panel.getWidgetElement(0)
      rightElem = self.panel.getWidgetElement(1)

      height = self.getOffsetHeight(self.panel.container) + "px"
      self.panel.setElemHeight(rightElem, height)
      self.panel.setElemHeight(self.panel.getSplitElement(), height)
      self.panel.setElemHeight(leftElem, height)
      self.setSplitPositionUsingPixels(self.getOffsetWidth(leftElem))      

class ImplSafariHorizontalSplitPanel(ImplHorizontalSplitPanel):
    """ 
        The Safari implementation which owes its existence entirely to a single
        WebKit bug: http:#bugs.webkit.org/show_bug.cgi?id=9137.
    """
    def __init__(self, panel):
        
      fullSize = "100%"
      ImplHorizontalSplitPanel.__init__(self, panel)
      self.panel.setElemHeight(self.panel.container, fullSize)
      self.panel.setElemHeight(self.panel.getWidgetElement(0), fullSize)
      self.panel.setElemHeight(self.panel.getWidgetElement(1), fullSize)
      self.panel.setElemHeight(self.panel.getSplitElement(), fullSize)

class HorizontalSplitPanel(SplitPanel):
    """  A panel that arranges two widgets in a single horizontal row
         and allows the user to interactively change the proportion
         of the width dedicated to each of the two widgets. Widgets
         contained within a <code>HorizontalSplitPanel</code> will
         be automatically decorated with scrollbars when necessary.

         Default layout behaviour of HorizontalSplitPanels is to 100% fill
         its parent vertically and horizontally [this is NOT normal!]
    """

    def __init__(self):
        """ Creates an empty horizontal split panel.
        """

        SplitPanel.__init__(self, DOM.createDiv(),
                            DOM.createDiv(),
                            self.preventBoxStyles(DOM.createDiv()),
                            self.preventBoxStyles(DOM.createDiv()))

        self.container = self.preventBoxStyles(DOM.createDiv())

        self.buildDOM()

        self.setStyleName("gwt-HorizontalSplitPanel")

        self.impl = ImplHorizontalSplitPanel(self)

        # By default the panel will fill its parent vertically and horizontally.
        # The horizontal case is covered by the fact that the top level div is
        # block display.
        self.setHeight("100%")

        self.lastSplitPosition = "50%"
        self.initialLeftWidth = 0
        self.initialThumbPos = 0

    def add(self, w):
        """
           * Adds a widget to a pane in the HorizontalSplitPanel. The method
           * will first attempt to add the widget to the left pane. If a 
           * widget is already in that position, it will attempt to add the
           * widget to the right pane. If a widget is already in that position,
           * an exception will be thrown, as a HorizontalSplitPanel can
           * contain at most two widgets.
           * 
           * Note that this method is bidi-sensitive. In an RTL environment,
           * this method will first attempt to add the widget to the right pane,
           * and if a widget is already in that position, it will attempt to add
           * the widget to the left pane.
           * 
           * @param w the widget to be added
           * @throws IllegalStateException
        """
        if self.getStartOfLineWidget() is None:
            self.setStartOfLineWidget(w)
        elif self.getEndOfLineWidget() is None:
            self.setEndOfLineWidget(w)
        else:
            return
          # TODO throw new IllegalStateException(
          #    "A Splitter can only contain two Widgets.")

    def getEndOfLineWidget(self):
        """
           * Gets the widget in the pane that is at the end of the line
           * direction for the layout. That is, in an RTL layout, gets
           * the widget in the left pane, and in an LTR layout, gets
           * the widget in the right pane.
           *
           * @return the widget, <code>null</code> if there is not one.
        """
        return self.getWidget(self.getEndOfLinePos())
   
    def getLeftWidget(self):
        """
           * Gets the widget in the left side of the panel.
           * 
           * @return the widget, <code>null</code> if there is not one.
        """
        return self.getWidget(0)

    def getRightWidget(self):
        """
           * Gets the widget in the right side of the panel.
           * 
           * @return the widget, <code>null</code> if there is not one.
        """
        return self.getWidget(1)

    def getStartOfLineWidget(self):
        """
        * Gets the widget in the pane that is at the start of the line 
        * direction for the layout. That is, in an RTL environment, gets
        * the widget in the right pane, and in an LTR environment, gets
        * the widget in the left pane.   
        *
        * @return the widget, <code>null</code> if there is not one.
        """
        return self.getWidget(self.getStartOfLinePos())

    def setEndOfLineWidget(self, w):
        """
       * Sets the widget in the pane that is at the end of the line direction
       * for the layout. That is, in an RTL layout, sets the widget in
       * the left pane, and in and RTL layout, sets the widget in the 
       * right pane.
       *
       * @param w the widget
        """
        self.setWidget(self.getEndOfLinePos(), w)

    def setLeftWidget(self, w):
        """
           * Sets the widget in the left side of the panel.
           * 
           * @param w the widget
        """
        self.setWidget(0, w)

    def setRightWidget(self, w):
        """
           * Sets the widget in the right side of the panel. 
           * 
           * @param w the widget
        """
        self.setWidget(1, w)
 
    def setSplitPosition(self, pos):
        """
       * Moves the position of the splitter.
       *
       * This method is not bidi-sensitive. The size specified is always
       * the size of the left region, regardless of directionality.
       *
       * @param pos the new size of the left region in CSS units (e.g. "10px",
       *             "1em")
        """
        self.lastSplitPosition = pos
        self.impl.setSplitPosition(pos)

    def setStartOfLineWidget(self, w):
        """
       * Sets the widget in the pane that is at the start of the line direction
       * for the layout. That is, in an RTL layout, sets the widget in
       * the right pane, and in and RTL layout, sets the widget in the
       * left pane.
       *
       * @param w the widget
        """
        self.setWidget(self.getStartOfLinePos(), w)

    def onLoad(self):
        self.impl.onAttach()
        # Set the position realizing it might not work until
        # after layout runs.  This first call is simply to try
        # to avoid a jitter effect if possible.
        self.setSplitPosition(self.lastSplitPosition)
        DeferredCommand().add(self)

    def execute(self):
        self.setSplitPosition(self.lastSplitPosition)

    def onUnload(self):
        self.impl.onDetach()

    def onSplitterResize(self, x, y):
        self.impl.onSplitterResize(self.initialLeftWidth + x -
                                   self.initialThumbPos)

    def onSplitterResizeStarted(self, x, y):
        self.initialThumbPos = x
        self.initialLeftWidth = self.getOffsetWidth(self.getWidgetElement(0))


    def buildDOM(self):

        leftDiv = self.getWidgetElement(0)
        rightDiv = self.getWidgetElement(1)
        splitDiv = self.getSplitElement()

        DOM.appendChild(self.getElement(), self.container)

        DOM.appendChild(self.container, leftDiv)
        DOM.appendChild(self.container, splitDiv)
        DOM.appendChild(self.container, rightDiv)

        # Sadly, this is the only way I've found to get vertical
        # centering in this case. The usually CSS hacks (display:
        # table-cell, vertical-align: middle) don't work in an
        # absolute positioned DIV.
        thumb_html = '<img src="splitPanelThumb.png" />'
        DOM.setInnerHTML(splitDiv,
            "<table class='hsplitter' height='100%' cellpadding='0' " +
                "cellspacing='0'><tr><td align='center' valign='middle'>" +
                thumb_html +
                "</td></tr></table>")

        self.addScrolling(leftDiv)
        self.addScrolling(rightDiv)

    def getEndOfLinePos(self):
        return 0
        # TODO: return (LocaleInfo.getCurrentLocale().isRTL() ? 0 : 1)
  
    def getStartOfLinePos(self):
        return 1
        # TODO: return (LocaleInfo.getCurrentLocale().isRTL() ? 1 : 0)

