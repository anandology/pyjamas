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

from pyjamas.webio import logger, json

class EmptyBufferError(Exception):
    pass

class Buffer(object):
    def __init__(self, rawBuffer=None):
        if rawBuffer is not None:
            self._rawBuffer = rawBuffer
        else:
            self._rawBuffer = ''

    def getLength(self):
        return len(self._rawBuffer)

    def append(self, data):
        logger.debug('append %s' % json.encode(data))
        self._rawBuffer += data

    def peekBytes(self, num=None):
        if num is not None:
            return self._rawBuffer[:num]
        else:
            return self._rawBuffer

    def peekToDelimiter(self, delimiter='\n'):
        i = self._rawBuffer.find(delimiter)
        if i == -1:
            s = 'delimiter %s not present in buffer.' % delimiter
            raise EmptyBufferError(s)
        return self._rawBuffer[:i]

    def consumeBytes(self, num):
        output = self.peekBytes(num)
        self._rawBuffer = self._rawBuffer[len(output):]
        return output

    def consumeMaxBytes(self, num):
        if len(self._rawBuffer) > num:
            output = self._rawBuffer[:num]
            self._rawBuffer = self._rawBuffer[num:]
        else:
            output = self._rawBuffer
            self._rawBuffer = ''
        return output

    def consumeAllBytes(self):
        output = self._rawBuffer
        self._rawBuffer = ''
        return output

    def consumeToDelimiter(self, delimiter='\n'):
        output = self.peekToDelimiter(delimiter)
        self._rawBuffer = self._rawBuffer[len(output):]
        return output

    def consumeThroughDelimiter(self, delimiter='\n'):
        dl = len(delimiter)
        return self.consumeToDelimiter(delimiter) + self.consumeBytes(dl)

    def hasBytes(self, num=1):
        return len(self._rawBuffer) >= num

    def hasDelimiter(self, delimiter='\n'):
        return not self._rawBuffer.find(delimiter) == -1





