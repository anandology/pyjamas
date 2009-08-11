
# vim: set ts=4 sw=4 expandtab:

from ApplicationConstants import Notification

from pyjamas.ui.MenuBar import MenuBar
from pyjamas.ui.MenuItem import MenuItem
from pyjamas.ui.VerticalPanel import VerticalPanel

class Menu(MenuBar):

    def __init__(self):
        try:
            MenuBar.__init__(self, vertical=False)

            menuFile = MenuBar(vertical=True)
            menuFile.addItem("Open ...", MenuCmd(self, "onOpen"))
            menuFile.addItem("Save as ...", MenuCmd(self, "onSaveAs"))
            menuFile.addItem("Preferences", MenuCmd(self, "onPreferences"))
            self.addItem(MenuItem("File", menuFile))

            menuView = MenuBar(vertical=True)
            menuView.addItem("Edit", MenuCmd(self, "onEdit"))
            menuView.addItem("Summary", MenuCmd(self, "onSummary"))
            self.addItem(MenuItem("View", menuView))

            menuHelp = MenuBar(vertical=True)
            menuHelp.addItem("Contents", MenuCmd(self, "onContents"))
            menuHelp.addItem("About", MenuCmd(self, "onAbout"))
            self.addItem(MenuItem("Help", menuHelp))

        except:
            raise

    def onOpen(self):
        self.mediator.sendNotification(Notification.MENU_FILE_OPEN)

    def onSaveAs(self):
        self.mediator.sendNotification(Notification.MENU_FILE_SAVEAS)

    def onPreferences(self):
        self.mediator.sendNotification(Notification.MENU_FILE_PREFS)

    def onEdit(self):
        self.mediator.sendNotification(Notification.MENU_VIEW_EDIT)

    def onSummary(self):
        self.mediator.sendNotification(Notification.MENU_VIEW_SUM)

    def onContents(self):
        self.mediator.sendNotification(Notification.MENU_HELP_CONTENTS)

    def onAbout(self):
        self.mediator.sendNotification(Notification.MENU_HELP_ABOUT)

class MenuCmd:
    def __init__(self, object, handler):
        self._object  = object
        self._handler = handler

    def execute(self):
        handler = getattr(self._object, self._handler)
        handler()
