
# vim: set ts=4 sw=4 expandtab:

from ApplicationConstants import Notification

from pyjamas.ui.MenuBar import MenuBar
from pyjamas.ui.MenuItem import MenuItem
from pyjamas.ui.VerticalPanel import VerticalPanel

class Menu(MenuBar):

    def __init__(self):
        try:
            MenuBar.__init__(self, vertical=False)

            self.mFileOpen = MenuCmd()
            self.mFileSaveAs = MenuCmd()
            self.mFilePreferences = MenuCmd()
            self.mViewEdit = MenuCmd()
            self.mViewSummary = MenuCmd()
            self.mHelpContents = MenuCmd()
            self.mHelpAbout = MenuCmd()
            menuFile = MenuBar(vertical=True)
            menuFile.addItem("Open ...", self.mFileOpen)
            menuFile.addItem("Save as ...", self.mFileSaveAs)
            menuFile.addItem("Preferences", self.mFilePreferences)
            self.addItem(MenuItem("File", menuFile))

            menuView = MenuBar(vertical=True)
            menuView.addItem("Edit", self.mViewEdit)
            menuView.addItem("Summary", self.mViewSummary)
            self.addItem(MenuItem("View", menuView))

            menuHelp = MenuBar(vertical=True)
            menuHelp.addItem("Contents", self.mHelpContents)
            menuHelp.addItem("About", self.mHelpAbout)
            self.addItem(MenuItem("Help", menuHelp))

        except:
            raise

class MenuCmd:
    def setHandler(self, handler):
        self.handler = handler

    def execute(self):
        self.handler()
