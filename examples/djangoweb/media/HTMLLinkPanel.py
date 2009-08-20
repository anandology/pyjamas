from pyjamas.ui.HTMLPanel import HTMLPanel
from pyjamas.ui.Hyperlink import Hyperlink

from pyjamas import Window
from pyjamas import DOM
from pyjamas import log

class HTMLLinkPanel(HTMLPanel):
    def __init__(self, sink, html="", title="", **kwargs):
        self.sink = sink
        self.title = title
        HTMLPanel.__init__(self, html, **kwargs)

    def replaceLinks(self):
        """ replaces <a href="#pagename">sometext</a> with:
            Hyperlink("sometext", "pagename")
        """
        tags = self.findTags("a")
        pageloc = Window.getLocation()
        pagehref = pageloc.getPageHref()
        for el in tags:
            href = el.href
            l = href.split("#")
            if len(l) != 2:
                continue
            if l[0] != pagehref:
                continue
            token = l[1]
            if not token:
                continue
            html = DOM.getInnerHTML(el)
            parent = DOM.getParent(el)
            index = DOM.getChildIndex(parent, el)
            parent.removeChild(el)
            log.writebr("token: %s html: %s" % (token, html))
            hl = Hyperlink(TargetHistoryToken=token,
                           HTML=html)
                           #Element=el)
            self.insert(hl, parent, index)

