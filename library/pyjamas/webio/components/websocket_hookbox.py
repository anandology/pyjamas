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

from pyjamas.webio import interfaces, errors, utf8, logger
from __pyjamas__ import wnd

class Connector(interfaces.Connector):
    def connect(self):
        self._state = interfaces.STATE.CONNECTING
        url = self._opts['url']
        ctor = self._opts.get('wsConstructor', None)
        if not ctor:
            ctor = wnd().WebSocket
        logger.info('_opts is %s' % self._opts)
        ws = ctor(url)
        ws.onOpen = self.webSocketOnOpen
        ws.onClose = self.webSocketOnClose

    def webSocketOnOpen(self, ws):
        self.onConnect(Transport(ws))

    def webSocketOnClose(self, ws, e):
        data = {'rawError': e, 'webSocket':ws}
        if e.get('wasClean', None):
            err = errors.ServerClosedConnection(
                    'Websocket connection closed. %s' % data)
        else:
           if self._state == interfaces.STATE.CONNECTED:
               err = errors.ConnectionTimeout(
                   'Websocket connection timed out. %s' % data
               )
           else:
               err = errors.ServerUnreachable(
                       'Websocket connection failed. %s' % data)
        logger.debug('conn closed %s' % err)
        self.onDisconnect(err)


class Transport(interfaces.Transport):
    def __init__(self, ws):
        self._ws = ws

    def makeConnection(self, protocol):
        def doMessage(data):
            payload = utf8.encode(data['data'])
            protocol.dataReceived(payload)
        self._ws.onMessage = doMessage

    def write(self, data, encoding):
        if self._encoding == 'plain':
            result = utf8.decode(data)
            data = result
        self._ws.send(data)

    def loseConnection(self, protocol):
        self._ws.close()






