from pyjamas.ui import RootPanel, HTML, Label, HasAlignment, Button
from pyjamas.ui import HorizontalPanel, AbsolutePanel, ScrollPanel, Grid
from pyjamas.ui import TabPanel
from pyjamas.ui import DockPanel, HasHorizontalAlignment
from pyjamas import Window

from pyjamas.horizsplitpanel import HorizontalSplitPanel

from pyjamas.JSONService import JSONProxy

from Trees import Trees

class RightGrid(DockPanel):

    def __init__(self):
        DockPanel.__init__(self)
        self.grid = Grid()
        title = HTML("test title")
        self.add(title, DockPanel.NORTH)
        self.setCellHorizontalAlignment(title,
                                        HasHorizontalAlignment.ALIGN_CENTER)
        self.add(self.grid, DockPanel.CENTER)
        self.grid.setBorderWidth("0px")
        self.grid.setCellSpacing("0px")
        self.grid.setCellPadding("4px")

    def set_items(self, items):

        max_rows = 0
        max_cols = 0

        for i in range(len(items)):
            item = items[i]
            col = item[0]
            row = item[1]
            data = item[2]
            format_row = -1
            format_col = -1
            if col+1 > max_cols:
                format_col = max_cols
                self.grid.resizeColumns(col+1)
                max_cols = col+1

            if row+1 >= max_rows:
                format_row = max_rows
                self.grid.resizeRows(row+1)
                max_rows = row+1

            if format_col >= 0:
                for k in range(format_col, max_cols):
                    for j in range(max_rows):
                        self.formatCell(j, k)
            if format_row >= 0:
                for j in range(max_cols):
                    for k in range(format_row, max_rows):
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
        self.tabs = TabPanel()
        self.add(self.tabs, DockPanel.CENTER)

    def clear_items(self):

        self.grids = {}
        while self.tabs.getWidgetCount() > 0:
            self.tabs.remove(0)

    def setup_panels(self, datasets):

        self.grids = {}
        for i in range(len(datasets)):
            item = datasets[i]
            fname = item[0]
            self.grids[i] = RightGrid()
            self.tabs.add(self.grids[i], fname)
        
    def add_items(self, items, name, index):

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

        self.tree_width = 300

        self.tp = HorizontalPanel()
        self.tp.setWidth("%dpx" % (self.tree_width-20))
        self.tp.setBorderWidth("1px")
        self.treeview = Trees()
        self.treeview.fTree.addTreeListener(self)
        self.sp = ScrollPanel()
        self.tp.add(self.treeview)
        self.sp.add(self.tp)

        self.horzpanel1 = HorizontalPanel()
        self.horzpanel1.setSize("100%", "100%")
        self.horzpanel1.setBorderWidth("1px")

        self.hp = HorizontalPanel()
        self.hp.setWidth("800px")
        self.hp.setHeight("100%")
        self.horzpanel2 = HorizontalSplitPanel()
        self.horzpanel2.setSize("100%", "100%")
        self.horzpanel2.setSplitPosition("200px")
        self.hp.add(self.horzpanel2)
        self.hp.setBorderWidth("1px")

        self.rp = RightPanel()

        self.horzpanel2.setLeftWidget(HTML(""))
        #self.horzpanel2.setRightWidget(HTML(randomText))
        self.horzpanel2.setRightWidget(self.rp)

        self.horzpanel1.add(self.sp)
        self.horzpanel1.add(self.hp)

        self.midpanel = MidPanel(self)

        RootPanel().add(self.horzpanel1)

        width = Window.getClientWidth()
        height = Window.getClientHeight()

        self.onWindowResized(width, height)
        Window.addWindowResizeListener(self)
  

    def onWindowResized(self, width, height):
        self.hp.setWidth("%dpx" % (width - self.tree_width))
        self.hp.setHeight("%dpx" % (height - 20))
        self.sp.setHeight("%dpx" % (height - 20))

    def onTreeItemStateChanged(self, item):
        if item.isSelected():
            self.onTreeItemSelected(item)

    def onTreeItemSelected(self, item):

        obj = item.getUserObject()
        if len(obj.children) != 0:
            self.clear_mid_panel()
            return

        self.remote.get_midpanel_data(obj.root + "/" + obj.text, self)
        self.clear_right_panel()

    def clear_right_panel(self):
        self.horzpanel2.setRightWidget(HTML(""))

    def clear_mid_panel(self):
        self.clear_right_panel()
        self.horzpanel2.setLeftWidget(HTML(""))

    def set_mid_panel(self, response):

        self.midpanel.set_items(response)

        self.horzpanel2.setLeftWidget(self.midpanel)

    def select_right_grid(self, location, name):
        self.horzpanel2.setRightWidget(self.rp)
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

