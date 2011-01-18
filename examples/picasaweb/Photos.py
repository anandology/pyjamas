# Picasaweb and other gdata services use RESTful methods which is great
# for them but presents a problem as far as getting the JSON data without
# using the regular pyjamas JSONRPC classes we know and love. Easy if you
# have a backend that can do the get but not so easy to do everything 
# client-side since we have to get around Single Origin Policy by dynamically 
# adding script tags to the DOM. Check out public/PicasaWeb.html since this 
# necessitates a static script tag and a var too.
# At this point it works but I'm sure some DOM genius can find some
# room for improvement... jkh http://jameskhedley.com
from pyjamas.ui.HTML import HTML
from pyjamas.ui.TextBox import TextBox
from pyjamas.ui.Label import Label
from pyjamas.ui.Button import Button
from pyjamas.ui.VerticalPanel import VerticalPanel  
from pyjamas.ui.HorizontalPanel import HorizontalPanel 
from pyjamas.ui.DisclosurePanel import DisclosurePanel 
from pyjamas.ui.Grid import Grid
from pyjamas.ui.Composite import Composite
from pyjamas.Timer import Timer
from pyjamas import DOM
from pyjamas.JSONParser import JSONParser
from __pyjamas__ import JS

class Photos(Composite):
    def __init__(self):
        Composite.__init__(self)

        self.albums = []
        self.photos = []
        self.grid = Grid(4, 4, CellPadding=4, CellSpacing=4)
        self.grid.addTableListener(self)
        self.drill = 0
        self.pos = 0
        self.up = Button("Up", self) 
        self.next = Button("Next", self) 
        self.prev = Button("Prev", self) 
        self.timer = Timer(notify=self)
        self.userid = "jameskhedley"
        self.album_url = "http://picasaweb.google.com/data/feed/base/user/" + self.userid + "?alt=json-in-script&kind=album&hl=en_US&callback=restCb"
        self.doRESTQuery(self.album_url, self.timer)

        self.vp = VerticalPanel()
        self.disclosure = DisclosurePanel("Click for boring technical details.") 
        self.disclosure.add(HTML('''<p>OK so you want to write client JS to do a RESTful HTTP query from picasa right?
				 Well you can't because of the Same Origin Policy. Basically this means that
				 because the domain of the query and the domain of the hosted site are different,
				 then that could well be a cross-site scripting (XSS) attack. So, the workaround is to
				 do the call from a script tag so the JSON we get back is part of the document. 
				 But since we don't know what URL to hit yet, once we find out then we have to inject
				 a new script tag dynamically which the browser will run as soon as we append it.
				 To be honest I'm not 100% why Google use RESTful services and not JSON-RPC or somesuch,
				 which would be easier. Well, easier for me.'''))
        
        self.IDPanel = HorizontalPanel()
        self.IDPanel.add(Label("Enter google account:"))
        self.IDButton = Button("Go", self)
        
        self.IDBox = TextBox()
        self.IDBox.setText(self.userid)
        self.IDPanel.add(self.IDBox)
        self.IDPanel.add(self.IDButton)
        self.vp.add(self.IDPanel)
        self.vp.add(self.disclosure)
        self.vp.add(self.grid)

        self.initWidget(self.vp)

    def doRESTQuery(self, url, timer):
        """this is a totally different from an RPC call in that we have to
           dynamically add script tags to the DOM when we want to query the 
           REST API. These rely on callbacks in the DOM so we can either add 
           them dynamically or pre-define them in public/Main.html. 
           Once we've done that have to wait for the response.
           Which means we need to provide a listener for the timer"""

        JS("$wnd.receiver = 'wait'")
        new_script = DOM.createElement("script")
        DOM.setElemAttribute(new_script, "src", url)
        DOM.setElemAttribute(new_script, "type","text/javascript")
        JS("$wnd.document.body.appendChild(@{{new_script}})")
        self.timer.schedule(100)

    def onCellClicked(self, sender, row, col):
        if self.drill==0:
            self.drill += 1 
            self.vp.clear()
            self.grid.clear()
            self.vp.add(self.up)
            self.vp.add(self.grid)
            gridcols = self.grid.getColumnCount()
            album = self.albums[row+col+(row*(gridcols-1))]
            url = "http://picasaweb.google.com/data/feed/base/user/" + self.userid + "/albumid/" + album["id"] + "?alt=json-in-script&kind=photo&hl=en_US&callback=restCb"
            self.doRESTQuery(url, self.timer)
        elif self.drill==1:
            self.drill += 1
            gridcols = self.grid.getColumnCount()
            self.pos =row+col+(row*(gridcols-1))
            photo = self.photos[self.pos]
            self.vp.clear()
            self.fullsize = HTML('<img src="' + photo["full"] + '"/>')
            hp = HorizontalPanel()
            hp.add(self.up)
            hp.add(self.prev)
            hp.add(self.next)
            hp.setSpacing(8)
            self.vp.add(hp)
            self.vp.add(self.fullsize)

    def onClick(self, sender):
        if sender == self.IDButton:
            self.userid = self.IDBox.getText()
            if self.userid == "" or self.userid.isdigit():
                return
            self.drill = 0
            self.album_url = "http://picasaweb.google.com/data/feed/base/user/" + self.userid + "?alt=json-in-script&kind=album&hl=en_US&callback=restCb"
            self.grid.clear()
            self.doRESTQuery(self.album_url, self.timer)
        else:
            if self.drill == 2:
                if sender == self.up:
                    self.drill=1
                    self.vp.clear()
                    self.vp.add(self.up)
                    self.vp.add(self.grid)
                    self.fillGrid(self.photos, "photos")
                else:
                    if sender == self.next:
                        if self.pos >= len(self.photos):
                            return
                        self.pos +=1
                    elif sender == self.prev:
                        if self.pos < 1:
                            return
                        self.pos -=1
                    photo = self.photos[self.pos]
                    self.fullsize.setHTML('<img src="' + photo["full"] + '"/>')
            elif self.drill == 1:
                self.drill=0
                self.vp.clear()
                self.vp.add(self.IDPanel)
                self.vp.add(self.disclosure)
                self.vp.add(self.grid)
                self.fillGrid(self.albums, "albums")
            
    def onTimer(self, timer):
        receiver = JS("$wnd.receiver")

        if receiver == 'wait':
           self.timer.schedule(1000)
           return

        JS("$wnd.receiver = 'wait'")

        if self.drill == 0:
            self.parseAlbums(receiver)
            self.fillGrid(self.albums, "albums")
        elif self.drill == 1:
            self.parsePhotos(receiver)
            self.fillGrid(self.photos, "photos")

    def fillGrid(self, items, type):
        self.grid.clear()
        cols = self.grid.getColumnCount()
        self.grid.resizeRows((len(items)/cols)+1)
        rows = self.grid.getRowCount()
        for i in range(len(items)):
            vp = VerticalPanel()
            if type == 'photos':
                vp.add(items[i]['thumb'])
            else:
                vp.add(items[i]['thumb'])
                vp.add(items[i]['title'])
            self.grid.setWidget(int(i/cols), i%cols, vp)

    def parsePhotos(self, items):
        photo_list = JSONParser().jsObjectToPyObject(items)
        self.photos = []
        for i in range(len(photo_list)):
            index = "%s" % i
            aphoto = {}
            aphoto['thumb'] = HTML('<img src="' + photo_list[index]["media$group"]["media$thumbnail"]["1"]["url"] + '"/>')
            aphoto['full'] = photo_list[index]["media$group"]["media$content"]["0"]["url"] 
            self.photos.append(aphoto)

    def parseAlbums(self, items):
        album_list = JSONParser().jsObjectToPyObject(items)
        self.albums = []
        for i in range(len(album_list)):
            index = "%s" % i
            analbum = {}
            analbum['title'] = HTML(album_list[index]["title"]["$t"])
            analbum['thumb'] = HTML('<img src="' + album_list[index]["media$group"]["media$thumbnail"]["0"]["url"] + '"/>')
            url = album_list[index]["id"]["$t"]
            analbum['id'] = url.split('albumid/')[1].split('?alt')[0]
            self.albums.append(analbum)


