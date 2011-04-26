# Copyright (C) 2009 Daniel Carvalho <idnael@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pyjamas.ui.RootPanel import RootPanel, RootPanelCls
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.DockPanel import DockPanel
from pyjamas.ui.HorizontalPanel import HorizontalPanel

from pyjamas import DOM
from pyjamas.Timer import Timer
from pyjamas.ui.ListBox import ListBox

from pyjamas import Window

from pyjamas.gmaps.Map import Map, MapTypeId, MapOptions
from pyjamas.gmaps.Base import LatLng

from pyjamas.gmaps.DirectionsService import DirectionsService, \
    DirectionsRequest, DirectionsTravelMode, DirectionsStatus
from pyjamas.gmaps.DirectionsRenderer import DirectionsRenderer

from __pyjamas__ import JS


class DirectionsSimple(DockPanel):

    def __init__(self):
        DockPanel.__init__(self)
        self.setSize('100%', '100%')

        # widgets

        topPanel = HorizontalPanel()
        self.add(topPanel, DockPanel.NORTH)

        places = {
            "chicago, il": "Chicago",

            "st louis, mo": "St Louis",
            "joplin, mo": "Joplin, MO",
            "oklahoma city, ok": "Oklahoma City",
            "amarillo, tx": "Amarillo",
            "gallup, nm": "Gallup, NM",
            "flagstaff, az": "Flagstaff, AZ",

            "winona, az": "Winona",
            "kingman, az": "Kingman",
            "barstow, ca": "Barstow",
            "san bernardino, ca": "San Bernardino",
            "los angeles, ca": "Los Angeles"}

        self.start = ListBox()
        self.end = ListBox()

        for value in places:
            self.start.addItem(places[value], value)
            self.end.addItem(places[value], value)

        self.start.addChangeListener(self.calcRoute)
        self.end.addChangeListener(self.calcRoute)

        topPanel.add(self.start)
        topPanel.add(self.end)

        # now, the map

        mapPanel = SimplePanel()
        mapPanel.setSize('800', '500')
        self.add(mapPanel, DockPanel.CENTER)

        chigado = LatLng(41.850033, -87.6500523)
        options = MapOptions(zoom=7, center=chigado,
                           mapTypeId=MapTypeId.ROADMAP)

        self.map = Map(mapPanel.getElement(), options)

        # initialize the renderer
        self.directionsDisplay = DirectionsRenderer()
        self.directionsDisplay.setMap(self.map)

        self.directionsService = DirectionsService()

    def calcRoute(self):
        start = self.start.getValue(self.start.getSelectedIndex())
        end = self.end.getValue(self.end.getSelectedIndex())

        print "calcRoute start:", start, "end:", end

        request = DirectionsRequest(origin=start, destination=end, \
            travelMode=DirectionsTravelMode.DRIVING)

        self.directionsService.route(request, self.directionsResult)

    def directionsResult(self, response, status):
        print "directionsResult:"

        if status == DirectionsStatus.OK:

            Hf = response.Hf
            print Hf.origin, Hf.destination, Hf.travelMode

            for route in response.routes:
                attrs = dir(route)
                attrs.sort()
                for attr in attrs:
                    print '%s: %r' % (attr, getattr(route, attr))
            print "\n"

            self.directionsDisplay.setDirections(response)


if __name__ == '__main__':

    root = RootPanel()
    root.add(DirectionsSimple())
