""" test.py

    Simple testing framework for the raphael wrapper.
"""

import pyjd
from pyjamas.ui.RootPanel   import RootPanel
from pyjamas.ui.TabPanel import TabPanel
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.DockPanel import DockPanel
from pyjamas.ui.Label import Label
from pyjamas.ui.HTML import HTML
from pyjamas.ui import HasAlignment
from pyjamas import DOM
from pyjamas import log
#from pyjamas.raphael.raphael import Raphael

import graffle
import events
import spinner


class TabContainer(DockPanel):
    def __init__(self):
        DockPanel.__init__(self, 
                          #BorderWidth=1,Padding=8,
                          HorizontalAlignment=HasAlignment.ALIGN_CENTER,
                          VerticalAlignment=HasAlignment.ALIGN_MIDDLE)
        
class TabRaphaelContainer(TabContainer):
    def __init__(self):
        TabContainer.__init__(self)
        self.status=Label()
        self.add(self.status,DockPanel.SOUTH)
        
    def set_raphael(self,raphael):
        self.raphael=raphael
        self.add(self.raphael,DockPanel.CENTER)
        #panel.setCellHeight(center, "200px")
        #panel.setCellWidth(center, "400px")        
    
    def set_headline(self,headline):
        if hasattr(self,'html'):
            self.html.setHTML(headline)
            #self.html.setText(headline)
        else:
            self.html=HTML(headline)
            self.add(self.html,DockPanel.NORTH)
        
    def set_status(self,status):
        self.status.setText(status)


class ShowCaseApp(object):
    
    def onModuleLoad(self):
        self.tabs = TabPanel()
        tab_overview=TabContainer()
        self.tabs.add(tab_overview, 'Overview')
        
        self.tab_events=TabRaphaelContainer()
        self.tab_events.set_headline('Events Example')
        self.tab_events.set_raphael(events.Events(width=600,height=300))
        self.tab_events.set_status('Execute events on Raphael Elemnts')
        self.tabs.add(self.tab_events, 'Events')

        self.tab_graffle=TabRaphaelContainer()
        self.tab_graffle.set_headline('This is a simple example of the Raphael Graffle')
        self.tab_graffle.set_raphael(graffle.Graffle(width=600,height=300))
        self.tabs.add(self.tab_graffle, 'Graffle')

        self.tab_spinner=TabRaphaelContainer()
        self.tab_spinner.set_headline('This Raphael Spinner Example')
        self.tab_spinner.set_raphael(spinner.Spinner(width=600,height=300))
        self.tabs.add(self.tab_spinner, 'Spinner')
        
        self.tabs.selectTab(0)
        self.tabs.setWidth("100%")
        self.tabs.setHeight("100%")
        RootPanel().add(self.tabs)
    
    def draw(self):
        self.tab_spinner.raphael.draw()
        self.tab_graffle.raphael.draw()
        #self.tab_events.raphael.draw()

        

if __name__ == "__main__":    
    pyjd.setup("public/raphael_showcase.html")
    app=ShowCaseApp()
    app.onModuleLoad()
    app.draw()
    app.tab_graffle.raphael.connect()
    app.tab_events.raphael.connect()    
    pyjd.run()

