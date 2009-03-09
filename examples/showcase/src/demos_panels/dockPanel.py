"""
The ``ui.DockPanel`` class divides the panel into five pieces, arranged into
North, South, East, West and center pieces.  In general the outer pieces are
smaller, with the centre holding the main part of the panel's contents, as
shown below.

You can set the alignment and size for each widget within the DockPanel, by
calling ``setCellHorizontalAlignment(widget, alignment)``,
``setCellVerticalAlignment(widget, alignment)``, ``setCellHeight(widget,
height)`` and ``setCellWidth(widget, width)``.  You can also set the default
horizontal and vertical alignment to use for new widgets by calling
``setHorizontalAlignment()`` and ``setVerticalAlignment()`` before the widget
is added.
"""
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.DockPanel import DockPanel
from pyjamas.ui.Label import Label
from pyjamas.ui import HasAlignment

class DockPanelDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        panel = DockPanel()
        panel.setBorderWidth(1)

        north  = Label("North")
        west   = Label("West")
        center = Label("Center")
        east   = Label("East")
        south  = Label("South")

        panel.setHorizontalAlignment(HasAlignment.ALIGN_CENTER)
        panel.setVerticalAlignment(HasAlignment.ALIGN_MIDDLE)

        panel.add(north,  DockPanel.NORTH)
        panel.add(west,   DockPanel.WEST)
        panel.add(center, DockPanel.CENTER)
        panel.add(east,   DockPanel.EAST)
        panel.add(south,  DockPanel.SOUTH)

        panel.setCellHeight(center, "200px")
        panel.setCellWidth(center, "400px")

        self.add(panel)

