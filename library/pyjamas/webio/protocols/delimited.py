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

from webio.net import Protocol
from webio import logger


class DelimitedProtocol(Protocol):
    def __init__(self, delimiter=None):
        if delimiter is None:
            delimiter = '\r\n'
        self.delimiter = delimiter
        self.buffer = ''

    def connectionMade(self):
        logger.debug("connectionMade")

    def dataReceived(self, data):
        if not data:
            return
        logger.debug('dataReceived: (%s) %s' % (len(data),data))
        self.buffer += data
        while self.delimiter in self.buffer:
            idx = self.buffer.find(self.delimiter)
            line  = self.buffer[0,idx]
            self.buffer = self.buffer[idx+len(self.delimiter):]
            self.lineReceived(line)

    def lineReceived(self, line):
        logger.debug("Not implemented, lineReceived: %s" % line)

    def sendLine(self, line):
        logger.debug("WRITE" + line + self.delimiter)
        self.transport.write(line + self.delimiter)

    def connectionLost(self):
        logger.debug("connectionLost")


