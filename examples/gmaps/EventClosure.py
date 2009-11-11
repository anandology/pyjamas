# Copyright (C) 2009 Daniel Carvalho <idnael@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from pyjamas.ui.RootPanel import RootPanel, RootPanelCls
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas import DOM
from pyjamas.Timer import Timer
from __pyjamas__ import JS

from random import random

from pyjamas.gmaps.Map import Map, MapTypeId, MapOptions
from pyjamas.gmaps.Base import LatLng, LatLngBounds
from pyjamas.gmaps.Marker import Marker, MarkerOptions
from pyjamas.gmaps.InfoWindow import InfoWindow, InfoWindowOptions

class EventClosure(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)
        self.setSize('100%', '100%')

        options = MapOptions()
        options.zoom = 4
        options.center = LatLng(-25.363882, 131.044922)
        options.mapTypeId = MapTypeId.ROADMAP

        self.map = Map(self.getElement(), options)
        
        # Add 5 markers to the map at random locations
        southWest = LatLng(-31.203405, 125.244141)
        northEast = LatLng(-25.363882, 131.044922)
        bounds = LatLngBounds(southWest, northEast)
        print "boundsx", bounds

        # this is not working well!! it opens the entire world...
        self.map.fitBounds(bounds)

        # this is the same...
        #JS("""
        #  var southWest = new $wnd.google.maps.LatLng(-31.203405,125.244141);
        #  var northEast = new $wnd.google.maps.LatLng(-25.363882, 131.044922);
        #  var bounds = new $wnd.google.maps.LatLngBounds(southWest, northEast);
        #  this.map.fitBounds(bounds);
        #""")

        lngSpan = northEast.lng() - southWest.lng()
        latSpan = northEast.lat() - southWest.lat()

        for i in range(0, 5):
            location = LatLng(southWest.lat() + latSpan * random(),
              southWest.lng() + lngSpan * random())

            options = MarkerOptions()
            options.position = location
            options.map = self.map

            marker = Marker(options)
            marker.setTitle(str(i + 1))

            self.attachSecretMessage(marker, i);


    def attachSecretMessage(self, marker, number):
        message = ["This", "is", "the", "secret", "message"]

        options = InfoWindowOptions()
        options.content = message[number]

        infoWindow = InfoWindow(options)
        
        marker.addListener('click', lambda: infoWindow.open(self.map, marker))

       
if __name__ == '__main__':
    
    root = RootPanel()
    root.add(EventClosure())
