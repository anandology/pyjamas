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

from pyjamas.webio import connect

#ctx = webio.__env.global


class Protocol(object):
    transport = None
    def connectionMade(self, func=None):
        if func:
            return func()

    def dataReceived(self, data):
        return data

    def connectionLost(self, reason=None):
        if reason:
            return reason


class Client(object):
    def __init__(self, protocol):
        self._protocol = protocol

    def connect(self, transportName, *opts):
        self._remote = self._protocol()
        self._remote._client = self
        connect(self._remote, transportName, *opts)


class Transport(object):
    _encoding = 'plain'

    def write(self, data, encoding):
        raise NotImplementedError()

    def getPeer(self):
        raise NotImplementedError()

    def setEncoding(self, encoding):
        self._encoding = encoding

    def getEncoding(self):
        return self._encoding


class Listener(object):
    def __init__(self, server, opts):
        self._server = server
        self.__opts = opts

    def onConnect(self, transport):
        p = self._server.buildProtocol()
        p.transport = transport
        p.server = self._server
        transport.protocol = p
        transport.makeConnection(p)
        p.connectionMade()

    def listen(self):
        raise NotImplementedError()

    def stop(self):
        pass


class STATE(object):
    INITIAL = 0
    DISCONNECTED = 1
    CONNECTING = 2
    CONNECTED = 3


class Connector(object):
    def __init__(self, protocol, opts=None):
        if opts is None:
            opts = {}
        self._protocol = protocol
        self._opts = opts
        self._state = STATE.INITIAL

    def onConnect(self, transport):
        self._state = STATE.CONNECTED
        transport.makeConnection(self._protocol)
        self._protocol.transport = transport
        try:
            self._protocol.connectionMade()
        except:
            raise

    def onDisconnect(self, err):
        wasConnected = self._state == STATE.CONNECTED
        self._state = STATE.DISCONNECTED
        try:
            self._protocol.connectionLost(err, wasConnected)
        except:
            raise

    def getProtocol(self):
        return self._protocol
