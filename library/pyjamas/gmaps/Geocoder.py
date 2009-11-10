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
from __pyjamas__ import JS

from pyjamas.gmaps.Utils import gmapsJsObjectToPy, dictToJs

from pyjamas.JSONParser import JSONParser

GeocoderStatus       = JS("$wnd.google.maps.GeocoderStatus")
GeocoderLocationType = JS("$wnd.google.maps.GeocoderLocationType")


#def geocoderResultsToPy(jsResults):
#    listFields=JS('[ "results","types","address_components"]')
#    dictFields=JS('[ "results[]","address_components[]","geometry"]')
#
#    return gmapsJsObjectToPy2(jsResults,"results",listFields,dictFields)



geocoderResultsFields=dictToJs({"results":'l', "types":'l', "address_components":'l',
                                "results[]":'d', "address_components[]":'d', "geometry":'d',
                                "result":'d'})

def geocoderResultToPy(jsResult):
    return gmapsJsObjectToPy(jsResult,"result",geocoderResultsFields)

def geocoderResultsToPy(jsResults):
    return gmapsJsObjectToPy(jsResults,"results",geocoderResultsFields)

class Geocoder:
    def __init__(self):
        self.geocoder=JS("new $wnd.google.maps.Geocoder();")

    def geocode(self,request, callback):
        self.geocoder.geocode(request,lambda jsResults,status: callback(geocoderResultsToPy(jsResults),status))
    

def GeocoderRequest(**params):
    return dictToJs(params)

