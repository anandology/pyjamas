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

from pyjamas.gmaps.Map import Map, MapTypeId, MapOptions
from pyjamas.gmaps.Base import LatLng


class EventSimple(SimplePanel):

    def __init__(self):
        SimplePanel.__init__(self)
        self.setSize('100%', '100%')

        options = MapOptions()
        options.zoom = 4
        options.center = LatLng(-25.363882, 131.044922)
        options.mapTypeId = MapTypeId.ROADMAP

        self.map = Map(self.getElement(), options)

        self.map.addListener("zoom_changed", self.zoomChanged)

        self.map.addListener("click", self.clicked)

    def zoomChanged(self):
        print "zoom to " + str(self.map.getZoom())
        Timer(1500, self.moveToDarwin)

    def moveToDarwin(self, timer):
        darwin = LatLng(-12.461334, 130.841904)
        self.map.setCenter(darwin)

    def clicked(self):
        self.map.setZoom(8)


if __name__ == '__main__':

    root = RootPanel()
    root.add(EventSimple())
