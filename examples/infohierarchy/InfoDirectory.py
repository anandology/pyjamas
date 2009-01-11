from pyjamas.ui import RootPanel, HTML, Label, HasAlignment, Button
from pyjamas.ui import HorizontalPanel, AbsolutePanel, ScrollPanel, Grid
from pyjamas.ui import TabPanel, SimplePanel, FlexTable, Image
from pyjamas.ui import DockPanel
from pyjamas.ui import HasHorizontalAlignment, HasVerticalAlignment, HasAlignment
from pyjamas.ui import HasAlignment
from pyjamas import Window

#from pyjamas.horizsplitpanel import HorizontalSplitPanel

from pyjamas.JSONService import JSONProxy

from Trees import Trees

from Timer import Timer

class CollapserPanel(SimplePanel):
    def __init__(self, sink):
        SimplePanel.__init__(self)
        self.sink = sink 
        self.caption = HTML()
        self.child = None 
        self.showing = False
        self.dragging = False
        self.dragStartX = 0
        self.dragStartY = 0
        self.panel = FlexTable()

        self.collapse = Image("./images/cancel.png")
        self.collapse.addClickListener(self)
        dock = DockPanel()
        dock.setSpacing(0)
        
        dock.add(self.collapse, DockPanel.EAST)
        dock.add(self.caption, DockPanel.WEST)

        dock.setCellHorizontalAlignment(self.collapse, HasAlignment.ALIGN_RIGHT)
        dock.setCellVerticalAlignment(self.collapse, HasAlignment.ALIGN_TOP)
        dock.setCellHorizontalAlignment(self.caption, HasAlignment.ALIGN_LEFT)
        dock.setCellWidth(self.caption, "100%")
        dock.setWidth("100%")
        dock.setHeight("100%")

        self.panel.setWidget(0, 0, dock)
        self.panel.setHeight("100%")
        self.panel.setWidth("100%")
        self.panel.setBorderWidth(0)
        self.panel.setCellPadding(0)
        self.panel.setCellSpacing(0)
        self.panel.getCellFormatter().setHeight(1, 0, "100%")
        self.panel.getCellFormatter().setWidth(1, 0, "100%")
        self.panel.getCellFormatter().setAlignment(1, 0, HasHorizontalAlignment.ALIGN_LEFT, HasVerticalAlignment.ALIGN_TOP)
        SimplePanel.setWidget(self, self.panel)

        self.setStyleName("gwt-DialogBox")
        self.caption.setStyleName("Caption")
        self.collapse.setStyleName("Close")
        dock.setStyleName("Header")
        #self.caption.addMouseListener(self)
        self.collapsed = False

        self.collapsed_width = "15px"
        self.uncollapsed_width = "100%"

    def setInitialWidth(self, width):
        self.uncollapsed_width = width
        SimplePanel.setWidth(self, width)
        self.sink.setCollapserWidth(self, width)

    def setHeight(self, height):
        SimplePanel.setHeight(self, height)

    def onClick(self, sender):
        if self.collapsed == False:
            self.collapse.setUrl("./tree_closed.gif")
            self.collapsed = True
            self.caption.setVisible(False)
            if self.child:
                self.child.setVisible(False)
            self.setWidth(self.collapsed_width)
            self.sink.setCollapserWidth(self, self.collapsed_width)
        else:
            self.collapse.setUrl("./images/cancel.png")
            self.collapsed = False
            self.caption.setVisible(True)
            if self.child:
                self.child.setVisible(True)
            self.setWidth(self.uncollapsed_width)
            self.sink.setCollapserWidth(self, self.uncollapsed_width)

    def setHTML(self, html):
        self.caption.setHTML(html)

    def setText(self, text):
        self.caption.setText(text)

    def remove(self, widget):
        if self.child != widget:
            return False

        self.panel.remove(widget)
        return True

    def doAttachChildren(self):
        SimplePanel.doAttachChildren(self)
        self.caption.onAttach()

    def doDetachChildren(self):
        SimplePanel.doDetachChildren(self)
        self.caption.onDetach()

    def setWidget(self, widget):
        if self.child != None:
            self.panel.remove(self.child)

        if widget != None:
            self.panel.setWidget(1, 0, widget)

        self.child = widget


class RightGrid(DockPanel):

    def __init__(self, title):
        DockPanel.__init__(self)
        self.grid = Grid()
        title = HTML(title)
        self.add(title, DockPanel.NORTH)
        self.setCellHorizontalAlignment(title,
                                        HasHorizontalAlignment.ALIGN_LEFT)
        self.add(self.grid, DockPanel.CENTER)
        self.grid.setBorderWidth("0px")
        self.grid.setCellSpacing("0px")
        self.grid.setCellPadding("4px")

    def clear_items(self):
        self.index = 0
        self.items = {}

    def set_items(self, items):
        self.items = items
        self.index = 0
        self.max_rows = 0
        self.max_cols = 0
        Timer(1, self)

    def onTimer(self, t):
        count = 0
        while count < 10 and self.index < len(self.items):
            self._add_items(self.index)
            self.index += 1
            count += 1
        if self.index < len(self.items):
            Timer(1, self)

    def _add_items(self, i):

        item = self.items[i]
        col = item[0]
        row = item[1]
        data = item[2]
        format_row = -1
        format_col = -1
        if col+1 > self.max_cols:
            format_col = self.max_cols
            self.grid.resizeColumns(col+1)
            self.max_cols = col+1

        if row+1 >= self.max_rows:
            format_row = self.max_rows
            self.grid.resizeRows(row+1)
            self.max_rows = row+1

        if format_col >= 0:
            for k in range(format_col, self.max_cols):
                for j in range(self.max_rows):
                    self.formatCell(j, k)
        if format_row >= 0:
            for j in range(self.max_cols):
                for k in range(format_row, self.max_rows):
                    self.formatCell(k, j)

        self.grid.setHTML(row, col, data)

    def formatCell(self, row, col):
        if col == 0 and row != 0:
            self.grid.setHTML(row, col, "%d" % row)
        if row != 0 and col != 0:
            self.grid.setHTML(row, col, "&nbsp;")
            fmt = "rightpanel-cellformat"
        if col == 0 and row == 0:
            fmt = "rightpanel-cellcornerformat"
        elif row == 0:
            fmt = "rightpanel-celltitleformat"
        elif col == 0:
            fmt = "rightpanel-cellleftformat"
        self.grid.getCellFormatter().setStyleName(row, col, fmt)

class RightPanel(DockPanel):

    def __init__(self):
        DockPanel.__init__(self)
        self.grids = {}
        self.g = Grid()
        self.g.setCellSpacing("0px")
        self.g.setCellPadding("8px")
        self.title = HTML("&nbsp;")
        self.title.setStyleName("rightpanel-title")
        self.add(self.title, DockPanel.NORTH)
        self.setCellWidth(self.title, "100%")
        self.setCellHorizontalAlignment(self.title,
                                        HasHorizontalAlignment.ALIGN_LEFT)
        self.add(self.g, DockPanel.CENTER)

    def setTitle(self, title):
        self.title.setHTML(title)
        
    def clear_items(self):

        for i in range(len(self.grids)):
            self.grids[i].clear_items()
        self.grids = {}
        self.g.resize(0, 0)

    def setup_panels(self, datasets):

        self.grids = {}
        self.data = {}
        self.names = {}
        self.loaded = {}
        size = len(datasets)
        self.g.resize(size, 1)
        for i in range(size):
            item = datasets[i]
            fname = item[0]
            self.grids[i] = RightGrid(fname)
            self.g.setWidget(i, 0, self.grids[i])
   
    def add_items(self, items, name, index):
        self.data[index] = items
        self.names[index] = name
        self.grids[index].set_items(items)

class MidPanel(Grid):

    def __init__(self, sink):
        Grid.__init__(self)
        self.resize(1, 1)
        self.addTableListener(self)
        self.sink = sink
        self.selected_row = -1

    def set_items(self, items):

        if self.selected_row != -1:
            self.styleRow(self.selected_row, False)

        self.item_names = []
        self.item_locations = []
        self.resizeRows(len(items))
        for i in range(len(items)):
            item = items[i]
            name = item[0]
            location = item[1]
            self.setHTML(i, 0, name)
            self.item_names.append(name)
            self.item_locations.append(location)

    def onCellClicked(self, sender, row, col):
        self.styleRow(self.selected_row, False)
        self.selected_row = row
        self.styleRow(self.selected_row, True)
        self.sink.select_right_grid(self.item_locations[row],
                                    self.item_names[row])
        
    def styleRow(self, row, selected):
        if (row != -1):
            if (selected):
                self.getRowFormatter().addStyleName(row, "midpanel-SelectedRow")
            else:
                self.getRowFormatter().removeStyleName(row, "midpanel-SelectedRow")

class InfoDirectory:

    def onModuleLoad(self):

        self.remote = InfoServicePython()

        self.tree_width = 200

        self.tp = HorizontalPanel()
        self.tp.setWidth("%dpx" % (self.tree_width))
        self.treeview = Trees()
        self.treeview.fTree.addTreeListener(self)
        self.sp = ScrollPanel()
        self.tp.add(self.treeview)
        self.sp.add(self.tp)
        self.sp.setHeight("100%")

        self.horzpanel1 = HorizontalPanel()
        self.horzpanel1.setSize("100%", "100%")
        self.horzpanel1.setBorderWidth("1px")
        self.horzpanel1.setSpacing("10px")

        self.rp = RightPanel()
        self.rps = ScrollPanel()
        self.rps.add(self.rp)
        self.rps.setWidth("100%")
        self.rp.setWidth("100%")

        self.cp1 = CollapserPanel(self)
        self.cp1.setWidget(self.sp)
        self.cp1.setHTML("&nbsp;")


        self.midpanel = MidPanel(self)
        self.cp2 = CollapserPanel(self)
        self.cp2.setWidget(self.midpanel)
        self.cp2.setHTML("&nbsp;")

        self.horzpanel1.add(self.cp1)
        self.horzpanel1.add(self.cp2)
        self.horzpanel1.add(self.rps)

        self.cp1.setInitialWidth("%dpx" % self.tree_width)
        self.cp2.setInitialWidth("200px")

        RootPanel().add(self.horzpanel1)

        width = Window.getClientWidth()
        height = Window.getClientHeight()

        self.onWindowResized(width, height)
        Window.addWindowResizeListener(self)
  
    def setCollapserWidth(self, widget, width):
        self.horzpanel1.setCellWidth(widget, width)

    def onWindowResized(self, width, height):
        #self.hp.setWidth("%dpx" % (width - self.tree_width))
        #self.hp.setHeight("%dpx" % (height - 20))
        self.cp1.setHeight("%dpx" % (height - 30))
        self.cp2.setHeight("%dpx" % (height - 30))
        self.rps.setHeight("%dpx" % (height - 30))
        self.horzpanel1.setHeight("%dpx" % (height - 20))

    def onTreeItemStateChanged(self, item):
        if item.isSelected():
            self.onTreeItemSelected(item)

    def onTreeItemSelected(self, item):

        obj = item.getUserObject()
        if len(obj.children) != 0:
            self.clear_mid_panel()
            return

        self.remote.get_midpanel_data(obj.root + "/" + obj.text, self)
        self.cp2.setHTML(obj.text)
        self.clear_right_panel()

    def clear_right_panel(self):
        self.horzpanel1.remove(2)
        self.horzpanel1.insert(HTML(""), 2)
        self.rp.setTitle("&nbsp;")

    def clear_mid_panel(self):
        self.clear_right_panel()
        #self.horzpanel2.setLeftWidget(HTML(""))

    def set_mid_panel(self, response):

        self.midpanel.set_items(response)

        self.cp2.setWidget(self.midpanel)

    def select_right_grid(self, location, name):
        self.horzpanel1.remove(2)
        self.horzpanel1.insert(self.rps, 2)
        self.rp.setTitle(name)
        self.remote.get_rightpanel_datanames(location, self)

    def get_rightpanel_datasets(self, datasets):

        self.rp.clear_items()
        self.rp.setup_panels(datasets)

        for i in range(len(datasets)):
            item = datasets[i]
            fname = item[0]
            self.remote.get_rightpanel_data(fname, fname, i, self)
        
    def fill_right_grid(self, data):
        self.rp.add_items(data.get('items'), data.get('name'), data.get('index'))

    def onRemoteResponse(self, response, request_info):
        method = request_info.method
        if method == "get_midpanel_data":
            self.set_mid_panel(response)
        elif method == "get_rightpanel_datanames":
            self.get_rightpanel_datasets(response)
        elif method == "get_rightpanel_data":
            self.fill_right_grid(response)

    def onRemoteError(self, code, message, request_info):
        RootPanel().add(HTML("Server Error or Invalid Response: ERROR " + code))
        RootPanel().add(HTML(message))

class InfoServicePython(JSONProxy):
    def __init__(self):
            JSONProxy.__init__(self, "/infoservice/EchoService.py",
                    ["get_midpanel_data",
                     "get_rightpanel_datanames",
                     "get_rightpanel_data"])

