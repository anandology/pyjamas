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


from pyjamas.gmaps.Map import Map, MapTypeId, MapOptions, \
    MapTypeControlOptions, NavigationControlOptions, \
    MapTypeControlStyle, NavigationControlStyle


from pyjamas.gmaps.Base import LatLng


class ControlOptions(SimplePanel):

    def __init__(self):
        SimplePanel.__init__(self)
        self.setSize('100%', '100%')

        options = MapOptions(
            zoom=4, center=LatLng(-25.363882, 131.044922),
            mapTypeId=MapTypeId.ROADMAP,

            mapTypeControl=True,
            mapTypeControlOptions=MapTypeControlOptions(
                style=MapTypeControlStyle.DROPDOWN_MENU),

            navigationControl=True,
            navigationControlOptions=NavigationControlOptions(
                style=NavigationControlStyle.SMALL))
        # the same, in a extensive way:

        #options = MapOptions()

        #options.zoom = 4
        #options.center = LatLng(-25.363882, 131.044922)
        #options.mapTypeId = MapTypeId.ROADMAP

        #options.mapTypeControl = True
        #options.mapTypeControlOptions = MapTypeControlOptions()
        #options.mapTypeControlOptions.style =
        #   MapTypeControlStyle.DROPDOWN_MENU

        #options.navigationControl = True
        #options.navigationControlOptions = NavigationControlOptions()
        #options.navigationControlOptions.style = \
        #    NavigationControlStyle.SMALL

        self.map = Map(self.getElement(), options)


if __name__ == '__main__':

    root = RootPanel()
    root.add(ControlOptions())
