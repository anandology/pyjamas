# Copyright 2009 Daniel Carvalho <idnael@gmail.com>
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
from pyjamas.ui.RootPanel import RootPanel,RootPanelCls
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.DockPanel import DockPanel
from pyjamas.ui.HorizontalPanel import HorizontalPanel

from pyjamas import DOM
from pyjamas.Timer import Timer
from pyjamas.ui.Button import Button
from pyjamas.ui.TextBox import TextBox

from pyjamas import Window

from pyjamas.gmaps.Map import Map,MapTypeId,MapOptions
from pyjamas.gmaps.Base import LatLng
from pyjamas.gmaps.Geocoder import Geocoder, GeocoderRequest, GeocoderStatus
from pyjamas.gmaps.Marker import Marker, MarkerOptions

class GeocodingSimple(DockPanel):
    def __init__(self):
        DockPanel.__init__(self)
        self.setSize('100%','100%')

        self.geocoder=Geocoder()

        # widgets

        topPanel=HorizontalPanel()
        self.add(topPanel,DockPanel.NORTH)

        self.address=TextBox()
        self.address.setText("Sydney, NSW")
        self.address.addChangeListener(self.codeAddress)

        topPanel.add(self.address)

        button=Button("Geocode")
        button.addClickListener(self.codeAddress)

        topPanel.add(button)

        # now, the map

        mapPanel=SimplePanel()
        mapPanel.setSize('600','400')
        self.add(mapPanel,DockPanel.CENTER)

        options=MapOptions(zoom=8, center=LatLng(-34.397, 150.644), 
                           mapTypeId=MapTypeId.ROADMAP)

        self.map = Map(mapPanel.getElement(),options)

    def codeAddress(self):
        address = self.address.getText()

        print "codeAddress ",address

        if self.geocoder:
            request=GeocoderRequest(address= address)
            self.geocoder.geocode( request, self.geocodeResult)

    def geocodeResult(self,results,status):
        print "geocodeResult"

        if status == GeocoderStatus.OK:

            for res in results:
                print res.formatted_address
                print res.geometry.location.lat()
                print res.geometry.location.lng()
                for compo in res.address_components:
                    print "- "+compo.short_name
                print ""

            self.map.setCenter(results[0].geometry.location)

            marker = Marker(MarkerOptions(map=self.map, position= results[0].geometry.location))

        else:
            Window.alert("Geocode was not successful for the following reason: " + status)

if __name__ == '__main__':
    
    root=RootPanel()
    root.add(GeocodingSimple())
