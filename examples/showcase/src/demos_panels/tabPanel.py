"""
The ``ui.TabPanel`` class implements a tabbed window, where clicking on a tab
causes the associated contents to be displayed.

The TabPanel relies heavily on cascading stylesheet definitions to operate.
The following stylesheet definitions are used by the example shown below:

    .gwt-TabPanel {
    }

    .gwt-TabPanelBottom {
      border: 1px solid #87B3FF;
    }

    .gwt-TabBar {
      background-color: #C3D9FF;
    }

    .gwt-TabBar .gwt-TabBarFirst {
      height: 100%;
      padding-left: 3px;
    }

    .gwt-TabBar .gwt-TabBarRest {
      padding-right: 3px;
    }

    .gwt-TabBar .gwt-TabBarItem {
      border-top: 1px solid #C3D9FF;
      border-bottom: 1px solid #C3D9FF;
      padding: 2px;
      cursor: pointer;
    }

    .gwt-TabBar .gwt-TabBarItem-selected {
      font-weight: bold;
      background-color: #E8EEF7;
      border-top: 1px solid #87B3FF;
      border-left: 1px solid #87B3FF;
      border-right: 1px solid #87B3FF;
      border-bottom: 1px solid #E8EEF7;
      padding: 2px;
      cursor: default;
    }

"""
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.TabPanel import TabPanel
from pyjamas.ui.HTML import HTML

class TabPanelDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        tabs = TabPanel(Width="100%", Height="250px")
        tabs.add(HTML("The quick brown fox jumps over the lazy dog."), "Tab 1")
        tabs.add(HTML("The early bird catches the worm."), "Tab 2")
        tabs.add(HTML("The smart money is on the black horse."), "Tab 3")

        tabs.selectTab(0)

        self.add(tabs)

