
# vim: set ts=4 sw=4 expandtab:

from ApplicationConstants import Notification

from pyjamas.ui.DockPanel import DockPanel
from pyjamas.ui.RootPanel import RootPanelCls
from pyjamas.ui.MenuBar import MenuBar
from pyjamas.ui.MenuItem import MenuItem
from pyjamas.ui.VerticalPanel import VerticalPanel

from pyjamas.ui.Button import Button

from Menu import Menu
from DatePicker import DatePicker
from TimeGrid import TimeGrid
from Summary import Summary


class AppFrame(RootPanelCls):

    menuBar = None
    datePicker = None
    timeGrid = None
    summary = None

    def __init__(self):
        try:
            RootPanelCls.__init__(self)

            vpanel = VerticalPanel()
            self.menuBar = Menu()
            vpanel.add(self.menuBar)

            self.datePicker = DatePicker()
            vpanel.add(self.datePicker)

            self.timeGrid = TimeGrid()
            vpanel.add(self.timeGrid)

            self.summary = Summary()
            vpanel.add(self.summary)

            self.add(vpanel)
        except:
            raise
