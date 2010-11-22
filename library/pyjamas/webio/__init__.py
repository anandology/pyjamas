# Copyright (C) 2010 Jim Washington
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

# basics for webio

from pyjamas.JSONParser import JSONParser
from pyjamas import Window
import logging

logger = logging.getLogger('webio')
json = JSONParser()

class READYSTATE(object):
    WAITING = -1
    CONNECTING = 0
    OPEN = 1
    CLOSING = 2
    CLOSED = 3

#ctx = webio.__env.global
def getBaseUri():
    baseUri = Window.getLocation().getHref()
    z = baseUri.split('/')
    z = '/'.join(z[:-2]) + '/'
    while not z.endswith('/'):
        z += '/'
    return z

def getObj(objectName, transportName):
    try:
        obj = __import__ ('components.' + transportName + '.' + objectName)
    except ImportError:
        logger.error('invalid transport %s' % transportName)
    return obj

#def getListener(transportName):
#    return getObj('Listener', transportName)

def getConnector(transportName):
    return getObj('Connector', transportName)

#def listen(server, transportName, opts):
#    listenerClass = getListener(transportName)
#    listener = listenerClass(server, opts)
#    listener.listen()
#    return listener

def connect(protocolInstance, transportName, opts=None):
    ctor = getConnector(transportName)
    connector = ctor(protocolInstance, opts)
    connector.connect()
    return connector
