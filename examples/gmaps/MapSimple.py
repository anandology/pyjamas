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

from pyjamas.gmaps.Map import Map, MapTypeId, MapOptions
from pyjamas.gmaps.Base import LatLng

if __name__ == '__main__':
    mapPanel = SimplePanel()
    mapPanel.setSize('100%', '100%')
    
    options = MapOptions(zoom = 8, center = LatLng(-34.397, 150.644), mapTypeId = MapTypeId.ROADMAP)

    #options = MapOptions()
    #options.zoom = 8
    #options.center = LatLng(-34.397, 150.644)
    #options.mapTypeId = MapTypeId.ROADMAP

    map = Map(mapPanel.getElement(), options)

    #root = RootPanelCls(DOM.getElementById("here"))
    root = RootPanel()
    root.add(mapPanel)
