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

from pyjamas.webio.protocols.buffered import BufferedProtocol
from pyjamas.webio import logger, connect
from pyjamas import Window
from __pyjamas__ import wnd

multiplexer = None
count = 0


def removeMultiplexer():
    global multiplexer
    multiplexer = None

def getMultiplexer(baseUri, forceTransport = None):
    logger.debug('getMultiplexer(%s, %s)' % (baseUri, forceTransport))
    global multiplexer
    global count
    while not baseUri.endswith('/'):
        baseUri += '/'
    if multiplexer is not None:
        count += 1
        return multiplexer
    multiplexer = MultiplexingProtocol(baseUri)
    _transport = forceTransport
    ws = None
    if _transport is None:
        try:
            ws = wnd().WebSocket
            _transport = 'ws'
        except AttributeError:
            _transport = 'csp'
        logger.debug('_transport is %s' % _transport)
    uri = baseUri
    if _transport == 'ws':
        if baseUri.startswith('https'):
            uri = baseUri.replace('https', 'wss', 1)
        elif baseUri.startswith('http'):
            uri = baseUri.replace('http', 'ws', 1)
        logger.debug("connecting with ws")
        connect(multiplexer, 'websocket', {'url': uri, 'wsConstructor': ws})
        multiplexer.mode = 'ws'
    elif _transport == 'csp':
        logger.debug('connecting with csp')
        connect(multiplexer, 'csp', {'url': uri + 'csp'})
        multiplexer.mode = 'csp'

def releaseMultiplexer():
    global count
    global multiplexer
    count -= 1
    if count == 0:
        multiplexer.transport.loseConnection()
        multiplexer = None

OPEN_FRAME = '0'
CLOSE_FRAME = '1'
DATA_FRAME = '2'
DELIMITER = ','

class Connection(object):
    def __init__(self, multiplexer, id):
        self._multiplexer = multiplexer
        self._id = str(id)

    def send(self, data):
        self._multiplexer.sendFrame(self._id, DATA_FRAME, data)

    def close(self):
        self._multiplexer.closeConnection(self._id)

    def onFrame(self, data):
        pass

    def onClose(self, code):
        pass

    def onOpen(self):
        pass


class MultiplexingProtocol(BufferedProtocol):
    def __init__(self, baseUri):
        super(MultiplexingProtocol, self).__init__()
        self._baseUri = baseUri
        self._connections = {}
        self._last_id = -1
        self._size = -1
        self._connected = False
        self.mode = None

    def openConnection(self):
        logger.debug('opening multiplexing connection')
        self._last_id += 1
        id = self._last_id
        conn = Connection(self, id)
        self._connections[id] = conn
        if self._connected:
            logger.debug('already opened. triggering now')
            self._sendOpen(id)
        return conn

    def closeConnection(self, id):
        conn = self._connections.get(id, None)
        if conn is None:
            return
        if self._connected:
            self._sendClose(id)

    def _sendOpen(self, id):
        self.sendFrame(id, OPEN_FRAME)

    def _sendClose(self, id):
        self.sendFrame(id, CLOSE_FRAME)

    def sendFrame(self, id, type, payload=""):
        if not self._connected:
            raise Exception('multiplexer not connected')
        idPayload = str(id) + DELIMITER + type + DELIMITER + payload
        frame = str(len(idPayload)) + DELIMITER + idPayload
        self.transport.write(frame)

    def connectionMade(self, fn=None):
        logger.debug("connectionMade on multiplexer")
        self._connected = True
        for id in self._connections.keys():
            self._sendOpen(id)

    def onClose(self):
        removeMultiplexer()

    def _connectionLost(self, transportName, reason, wasConnected):
        if wasConnected:
            self.onClose()
        elif self.mode == 'ws':
            connect(self, 'csp', {'url':self._baseUri+'csp'})
            self.mode = 'csp'

    def _dispatchPayload(self, payload):
        i = payload.find(DELIMITER)
        if i == -1:
            return
        id = int(payload[:i])
        j = payload.find(DELIMITER, i+1)
        if j == -1:
            return
        frameType = payload[i+1:j]
        data = payload[j+1:]
        conn = self._connections.get(id, None)
        if conn is None:
            return
        try:
            z = int(frameType)
        except ValueError:
            return
        if frameType == OPEN_FRAME:
            conn.onOpen()
        elif frameType == CLOSE_FRAME:
            del self._connections[id]
            conn.onClose()
        elif frameType == DATA_FRAME:
            conn.onFrame(data)

    def bufferUpdated(self):
        while True:
            if self._size == -1:
                if self.buffer.hasDelimiter(DELIMITER):
                    self._size = int(self.buffer.consumeToDelimiter(DELIMITER))
                    self.buffer.consumeBytes(len(DELIMITER))
                else:
                    break
            if self.buffer.hasBytes(self._size):
                payload = self.buffer.consumeBytes(self._size)
                self._dispatchPayload(payload)
                self._size = -1
            else:
                break
