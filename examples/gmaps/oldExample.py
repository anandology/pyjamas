from pyjamas.ui.RootPanel import RootPanelCls
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas import DOM
from pyjamas.JSONService import JSONProxy
from pyjamas import Window
from __pyjamas__ import JS

### GOOGLE MAPS WRAPPERS ###
def GMap2(el, options):
    if options:
        JS("""return new $wnd.GMap2(@{{el}},@{{options}});""")
    else:
        JS("""return new $wnd.GMap2(@{{el}});""")

def GLatLng(lat,long):
    JS("return new $wnd.GLatLng(@{{lat}},long);")

def GPolyline(points,color,width):
    JS("return new $wnd.GPolyline(@{{points}},@{{color}},@{{width}});")

def jsList():
    JS("return [];")

### JQUERY WRAPPERS/HELPERS ###
def jQuery():
    JS("return $wnd.jQuery;")

def jsOpts(options):
    JS("return {};")

def getStart(ui):
    JS("return @{{ui}}.values[0]")
def getEnd(ui):
    JS("return @{{ui}}.values[1]")

class Greed:
    def onModuleLoad(self):
        self.remote = DataService()
        vPanel = VerticalPanel()


        # create div to hold map
        mapPanel = SimplePanel()
        mapPanel.setSize('700px','400px')

        # initiate getting gps data from web2py
        self.remote.getPoints(self)

        # create slider div
        slider = SimplePanel()
        self.slider = slider

        # add map and slide to main panel
        vPanel.add(mapPanel)
        vPanel.add(slider)

        # add everything to page's GreedyPyJs div
        root = RootPanelCls(DOM.getElementById("GreedPyJs"))
        root.add(vPanel)

        # Create initial google map
        self.map = GMap2(mapPanel.getElement())
        self.map.setCenter(GLatLng(37.4419, -122.1419), 13)


        # create place to hold gps positions
        # these will be in tuples: (date, latitude, longitude)
        self.positions=[]

    def logger(self, event, ui):
        """
        When user slides slider, this function will be called
        to update the map with the new date range
        """

        v1 = getStart(ui)
        v2 = getEnd(ui)
        self.draw(v1,v2)


    def onRemoteResponse(self, response, request_info):
        if request_info.method == 'getPoints':
            # set the positions variable and draw the slider
            self.positions = response

            sliderOpts = jsOpts()
            sliderOpts.range = True
            #sliderOpts.slide = getattr(self, 'logger')
            sliderOpts.min = 0
            sliderOpts.max = len(response) - 1
            sliderOpts.slide = getattr(self,'logger')

            jQuery()(self.slider.getElement()).slider(sliderOpts)

    def draw(self, start, end):
        # Plot the lines on the google map
        self.map.clearOverlays()
        points = jsList()
        for index in range(start,end):
            # create a list of gps points
            points.push(GLatLng(self.positions[index][1], self.positions[index][2]))
        polyline = GPolyline(points, "#ff0000", 2)
        self.map.addOverlay(polyline)
        self.map.setCenter(GLatLng(self.positions[0][1], self.positions[0][2], 13))

    def onRemoteError(self, code, message, request_info):
        pass

class DataService(JSONProxy):
    def __init__(self):
        JSONProxy.__init__(self, "/maps/default/call/jsonrpc", ["getPoints"])

if __name__ == '__main__':
    app = Greed()
    app.onModuleLoad()
