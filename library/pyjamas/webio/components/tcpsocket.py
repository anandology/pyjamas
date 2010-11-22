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

from pyjamas import Window
from pyjamas.webio import json, utf8, READYSTATE
from pyjamas.webio.protocols.multiplexing import getMultiplexer, releaseMultiplexer


class TCPSocket(object):
    _serverUri=None
    def __init__(self, opts):
        if 'serverUri' in opts:
            self._serverUri = opts['serverUri']
        else:
            s = Window.getLocation().getHref()
            z = s.split('/')
            self._serverUri = '/'.join(z[:-2]) + '/'
        while not self._serverUri.endswith('/'):
            self._serverUri += '/'
        self.readyState = READYSTATE.WAITING
        self._buffer = ''
        self._forceTransport = opts['forceTransport']

    def open(self, host, port, isBinary):
        if self._serverUri is None:
            raise Exception("could not determine uri")
        multiplexer = getMultiplexer(self._serverUri, self._forceTransport)
        self._isBinary = isBinary
        self._host = host
        self._port = port
        self._conn = multiplexer.openConnection()
        self._conn.open = self._onOpen
        self._conn.onFrame = self._onFrame
        self._conn.onClose = self._onClose
        self.readyState = READYSTATE.CONNECTING

    def _onClose(self):
        if self.readyState == READYSTATE.CLOSED:
            return
        self.readyState = READYSTATE.CLOSED
        releaseMultiplexer()
        self._trigger("close")

    def _onOpen(self):
        self._conn.send(json.encode({'hostname': self._host,
                                     'port': self._port,
                                     'protocol': 'tcp'}))

    def _onFrame(self, payload):
        ready_state = self.readyState
        if ready_state == READYSTATE.CONNECTING:
            if payload == '1':
                self.readyState = READYSTATE.OPEN
                self._trigger('open')
            else:
                self._onClose()
        elif ready_state == READYSTATE.OPEN:
            self._buffer += payload
            result = utf8.decode(self._buffer)
            payload = result[0]
            self._buffer = self._buffer[1:]
            if payload:
                self._trigger('read', payload)

    def send(self, data):
        if self.readyState >= READYSTATE.CLOSING:
            return
        if not self._isBinary:
            data = utf8.encode(data)
        self._conn.send(data)

    def close(self):
        if self.readyState >= READYSTATE.CLOSING:
            return
        self.readyState = READYSTATE.CLOSING
        self._conn.close()
        self._conn.onClose = self._onClose

    def _trigger(self, signal, data=None):
        fn = getattr(self, 'on' + signal, None)
        if fn:
            if data is not None:
                fn(data)
            else:
                fn()


