# -*- coding: iso-8859-1 -*-

import pyjd

#Ui components
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.FlowPanel import FlowPanel
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Label import Label
from pyjamas.ui.Image import Image
from pyjamas.ui.SimplePanel import SimplePanel

from pyjamas import DOM



class FlowPanelDemo:
    """Demos the flow panel. Because of how the Flow Panel works, all elements have to be inline elements.
        Divs, tables, etc. can't be used, unless specified with CSS that they are inline or inline-block.

        Because of how Vertical Panels work (with tables), we use CSS to display tables as inline-blocks.
        IE, excluding IE8, doesn't support inline-blocks, so we have to use a CSS hack
        (see http://blog.mozilla.com/webdev/2009/02/20/cross-browser-inline-block/ for more on the hack)
        However, we use spans instead of divs for the Label by providing an 'element' argument."""
       
    def __init__(self):
        self.root = RootPanel()
        #Flow panel taking up 70% of the page.  CSS centers it.
        self.flow = FlowPanel(Width="70%", StyleName='flow-panel')
       
       
        for x in range(0, 10):
            self.panel = VerticalPanel()
            #Label each image with its number in the sequence
            title = Label("Item %s" % x, element=DOM.createElement('span'), StyleName="title item")
            #Add a neat-o image.
            image = Image('images/pyjamas.png', Width="200px", Height="200px", StyleName="cat-image cat-item")
            #Add to the Vertical Panel the image title
            self.panel.add(title)
            self.panel.add(image)

            self.flow.add(self.panel)

        self.root.add(self.flow)

if __name__ == "__main__":
    pyjd.setup("./public/FlowPanel.html")
    FlowPanelDemo()
    pyjd.run()

