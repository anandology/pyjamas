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

from delimited import DelimitedProtocol
from webio import json, logger

class RtjpProtocol(DelimitedProtocol):
    def __init__(self):
        delimiter = '\r\n'
        super(RtjpProtocol, self).__init__(delimiter)
        self.frameId = 0

    def connectionMade(self):
        logger.debug("ConnectionMade")

    def frameReceived(self, id, name, *args):
        raise NotImplementedError

    def sendFrame(self, name, *args):
        self.frameId += 1
        logger.debug('sendFrame %s %s' % (name, args))
        self.sendLine(json.encode([self.frameId, name, args]))
        return self.frameId

    def lineReceived(self, line):
        frame = json.decode(line)
        if len(frame) != 3:
            raise TypeError("Invalid frame length")
        if not isinstance(frame[0], int):
            raise TypeError("Invalid frame id")
        if not isinstance(frame[1], basestring):
            raise TypeError("Invalid frame name")
        logger.debug("frameReceived: %s %s %s" % (frame[0], frame[1], frame[2]))
        self.frameReceived(frame[0], frame[1], frame[2])

    def connectionLost(self):
        logger.debug("connectionLost")







