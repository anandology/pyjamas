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
from pyjamas.gmaps.InfoWindow import InfoWindow, InfoWindowOptions


class EventProperties(SimplePanel):

    def __init__(self):
        SimplePanel.__init__(self)
        self.setSize('100%', '100%')

        self.myLatLng = LatLng(-25.363882, 131.044922)

        options = MapOptions()
        options.zoom = 4
        options.center = self.myLatLng
        options.mapTypeId = MapTypeId.ROADMAP

        self.map = Map(self.getElement(), options)
        self.map.addListener("zoom_changed", self.zoomChanged)

        options = InfoWindowOptions()
        options.content = "Zoom Level Test"
        options.position = self.myLatLng

        self.infoWindow = InfoWindow(options)
        self.infoWindow.open(self.map)

        self.map.addListener("zoom_changed", self.zoomChanged)

    def zoomChanged(self):
        zoomLevel = self.map.get_zoom()
        self.map.setCenter(self.myLatLng)
        self.infoWindow.setContent("Zoom: " + str(zoomLevel))

        if zoomLevel == 0:
            self.map.setZoom(10)


if __name__ == '__main__':

    root = RootPanel()
    root.add(EventProperties())
