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

from pyjamas.webio.interfaces import Protocol
from pyjamas.webio.buffer import Buffer

class BufferedProtocol(Protocol):
    def __init__(self):
        super(Protocol, self).__init__()
        self.buffer = Buffer()

    def bufferUpdated(self):
        """
        override this instead of dataReceived in descendent classes
        """
        pass

    def dataReceived(self, data):
        self.buffer.append(data)
        self.bufferUpdated()

