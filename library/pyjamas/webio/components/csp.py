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

import webio
from webio.csp.client import CometSession
from webio import logger


class Connector(webio.interfaces.Connector):
    def connect(self):
        self._state = webio.interfaces.STATE.CONNECTING
        conn = CometSession()
        def csoc():
            self.cometSessionOnConnect(conn)
        conn.onconnect = csoc
        conn.ondisconnect = self.onDisconnect

        logger.debug("opening the connection")
        self._opts['encoding'] = 'plain'
        url = self._opts['url']
        del self._opts['url']
        conn.connect(url, self._opts)

    def cometSessionOnConnect(self, conn):
        logger.debug("conn has opened")
        self.onConnect(Transport(conn))


class Transport(webio.interfaces.Transport):
    def __init__(self, conn):
        self._conn = conn

    def makeConnection(self, protocol):
        self._conn.onread = protocol.dataReceived

    def write(self, data, encoding=None):
        if self._encoding == 'utf8':
            data = data.encode('utf8')
        self._conn.write(data)

    def loseConnection(self, protocol=None):
        self._conn.close()


