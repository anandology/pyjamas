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

from pyjamas.webio import interfaces
from pyjamas.webio import logger


class Echo(interfaces.Protocol):

    def connectionMade(self):
        logger.debug('connection made')
        self.transport.write('Welcome!')

    def dataReceived(self, data):
        logger.debug('dataReceived: %s' % data)
        self.transport.write('Echo: %s' % data)

    def connectionLost(self):
        logger.debug('conn lost')




