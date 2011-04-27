import pyjd # this is dummy in pyjs.
from pyjamas.ui.Button import Button
from pyjamas.ui.HTML import HTML
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.Hyperlink import Hyperlink
from pyjamas.ui.Label import Label
from pyjamas.ui.ListBox import ListBox
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.TabPanel import TabPanel
from pyjamas import Window

from buoy import Buoy, BuoyService

import pygwt

class Hovercraft(TabPanel):
    def __init__(self, tabBar=None, *kwargs):
        TabPanel.__init__(self, tabBar, *kwargs)
        self.parent_buoy = None

        self.tabs = [{'hovertype' : ListBox(), 'name' : 'Cost'},
                     {'hovertype' : ListBox(), 'name' : 'Speed'}]

        self.cost = self.tabs[0]['hovertype']
        items = ['cheap','next to cheap','average','above average','expensive','if you have to ask']
        self.cost.setVisibleItemCount(len(items))
        for item in items:
            self.cost.addItem(item)
        self.cost.addChangeListener(self)

        self.speed = self.tabs[1]['hovertype']
        items = ['very slow','slow','average','above average','fast','quick','hyper','turbo','lightening','light']
        self.speed.setVisibleItemCount(len(items))
        for item in items:
            self.speed.addItem(item)
        self.speed.addChangeListener(self)

        for tab in self.tabs:
            h = HorizontalPanel()
            h.add(tab['hovertype'])
            self.add(h, tab['name'])

    def set_speed(self, buoy):
        params = buoy.plan()
        if params:
            v = int(params['v'])
        else:
            v = 1
        self.speed.setSelectedIndex(v-1)
        txt = self.speed.getItemText(v-1)
        last_buoy = buoy.new(txt, {'v' : v})
        last_buoy.end()

    def set_cost(self, buoy):
        params = buoy.plan()
        if params:
            v = int(params['v'])
        else:
            v = 1
        self.cost.setSelectedIndex(v-1)
        txt = self.cost.getItemText(v-1)
        last_buoy = buoy.new(txt, {'v' : v})
        last_buoy.end()

    def onChange(self, sender):
        idx = sender.getSelectedIndex()
        if idx >=0:
            txt = sender.getItemText(idx)
            if sender == self.cost:
                buoy = self.buoy.new(txt,
                                     {'v' : idx+1})
                buoy.end()
            elif sender == self.speed:
                buoy = self.buoy.new(txt,
                                     {'v' : idx+1})
                buoy.end()

    def set(self, parentBuoy):
        self.parent_buoy = parentBuoy
        params = parentBuoy.plan()
        if params:    
            for n, tab in enumerate(self.tabs):
                if tab['name'] in params['hovertype']:
                    self.selectTab(n)
                    break
        else:
            self.selectTab(0)

    def onTabSelected(self, sender, tabIndex):
        page_name = self.tabs[tabIndex]['name']
        self.buoy = self.parent_buoy.new(page_name,
                                         {'hovertype' : self.tabs[tabIndex]['name']})
        params = self.buoy.navigate()
        if 'hovertype' in params:
            if params['hovertype'] == 'Cost':
                self.set_cost(self.buoy)
            elif params['hovertype'] == 'Speed':
                self.set_speed(self.buoy)
        else:
            self.set_cost(self.buoy)

        return TabPanel.onTabSelected(self, sender, tabIndex)

class Ships(HTML):
    def __init__(self, html=None, wordWrap=True, **kwargs):
        HTML.__init__(self, html, wordWrap, **kwargs)

        self.setHTML('Ships are reliable.')

class Surfboard(HTML):
    def __init__(self, html=None, wordWrap=True, **kwargs):
        HTML.__init__(self, html, wordWrap, **kwargs)

        self.setHTML('Surfboards can be cool.')

class TopNav(TabPanel):
    def __init__(self, tabBar=None, **kwargs):
        TabPanel.__init__(self, tabBar, **kwargs)
        self.buoy = None

        # 3 tabs but only Hovercraft() has complexity
        self.tabs = [{'tab' : Hovercraft(), 'name' : 'Hovercraft'},
                     {'tab' : Ships(), 'name' : 'Ship'},
                     {'tab' : Surfboard(), 'name' : 'Surfboard'}]

        for tab in self.tabs:
            self.add(tab['tab'], tab['name'])

    def set(self, parentBuoy):
        self.parent_buoy = parentBuoy
        params = parentBuoy.plan()
        if params:
            for n, tab in enumerate(self.tabs):
                if tab['name'] in params:
                    self.selectTab(n)
                    break
        else:
            self.selectTab(0)

    def onTabSelected(self, sender, tabIndex):
        page_name = self.tabs[tabIndex]['name']

        buoy = self.parent_buoy.new(page_name,
                                    {page_name : None})
        
        
        if tabIndex == 0:
            buoy.navigate()
            self.tabs[tabIndex]['tab'].set(buoy)
        else:
            buoy.end()

        return TabPanel.onTabSelected(self, sender, tabIndex)

class Navigate:

    def onModuleLoad(self):
        self.crumbs = HorizontalPanel(StyleName='breadcrumbs')
        self.crumbs.add(HTML('Home'))
        RootPanel().add(self.crumbs)

        self.buoy = BuoyService('Navigator', crumb='Home')
        self.buoy.add_flare_listener(self)
        self.buoy.set_titles_listener(self)
        self.buoy.set_breadcrumbs_listener(self)
        self.toplevel = TopNav()
        self.toplevel.set(self.buoy)
        self.buoy.cast_off()
        RootPanel().add(self.toplevel)

    def onFlare(self, service, prefixes):
        if self.toplevel:
            self.toplevel.set(service)

    def onTitlesChanged(self, titles):
        browser_title = ''
        for title in reversed(titles):
            browser_title += title + ' - '

        browser_title = browser_title[:-3]
        Window.setTitle(browser_title)

    def onBreadcrumbsChanged(self, crumbs):
        self.crumbs.clear()
        for n, crumb in enumerate(crumbs):
            if n < len(crumbs) - 1:
                self.crumbs.add(Hyperlink(text=crumb['label'], TargetHistoryToken=crumb['token']))
                self.crumbs.add(Label('>'))
            else:
                self.crumbs.add(HTML('<b>%s</b>' % crumb['label']))

if __name__ == '__main__':
    pyjd.setup("public/Navigate.html")
    app = Navigate()
    app.onModuleLoad()
    pyjd.run()
