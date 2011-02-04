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
#
# transliterated/translated from the original jsio-3.2/net/csp/client.js
# by Jim Washington November, 2010

import base64
from pyjamas.Timer import Timer
from pyjamas.webio import errors
from pyjamas.webio import json, logger
import transports

class READYSTATE(object):
    INITIAL = 0
    CONNECTING = 1
    CONNECTED = 2
    DISCONNECTING = 3
    DISCONNECTED = 4

class CometSession(object):
    id = 0
    kDefaultBackoff = 50
    kDefaultTimeoutInterval = 45000
    kDefaultHandshakeTimeout = 10000

    def __init__(self):
        CometSession.id += 1
        self._id = CometSession.id
        self._url = None
        self.readyState = READYSTATE.INITIAL
        self._sessionKey = None
        self._transport = None
        self._options = {}

        self._utf8ReadBuffer = ''
        self._writeBuffer = ''

        self._packetsInFlight = None
        self._lastEventId = None
        self._lastSentId = None

        self._handshakeLater = None
        self._handshakeBackoff = None
        self._handshakeRetryTimer = None
        self._handshakeTimeoutTimer = None

        self._timeoutTimer = None

        self._writeBackoff = self.kDefaultBackoff
        self._cometBackoff = self.kDefaultBackoff

        self._nullInBuffer = False
        self._nullInFlight = False
        self._nullSent = False
        self._nullReceived = False

    def setEncoding(self, encoding):
        if self._options.get('encoding', None) == encoding:
            return
        if encoding not in ['utf8', 'plain']:
            raise errors.InvalidEncodingError("invalid encoding requested")
        if encoding == 'plain' and hasattr(self, '_buffer'):
            buffer = self._utf8ReadBuffer
            self._utf8ReadBuffer = ''
            self._doOnRead(buffer)
        self._options['encoding'] = encoding

    def connect(self, url, options=None):
        while url.startswith('/'):
            url = url[1:]
        self._url = url
        if options:
            self._options = options
        else:
            self._options = {}
        self._options['encoding'] = self._options.get('encoding', 'utf8')
        self.setEncoding(self._options['encoding'])
        self._options['connectTimeout'] = self._options.get('connectTimeout',
                            self.kDefaultHandshakeTimeout)
        transportClass = transports.chooseTransport(url, self._options)
        self._transport = transportClass()
        self._transport.handshakeFailure = self._handshakeFailure
        self._transport.handshakeSuccess = self._handshakeSuccess
        self._transport.cometFailure = self._cometFailure
        self._transport.cometSuccess = self._cometSuccess
        self._transport.sendFailure = self._writeFailure
        self._transport.sendSuccess = self._writeSuccess

        self.readyState = READYSTATE.CONNECTING

        self._transport.handshake(self._url, self._options)

        self._handshakeTimeoutTimer = Timer(
                delayMillis=self._options.get('connectTimeout', 45000),
                notify=self._handshakeTimeout)

    def write(self, data, encoding=None):
        if not self.readyState == READYSTATE.CONNECTED:
            raise errors.ReadyStateError("Not connected")
        if encoding:
            encoding = encoding
        else:
            encoding = self._options.get('encoding', 'utf8')
        data.encode(encoding)
        self._writeBuffer += data
        self._doWrite(False)

    def _protocolError(self, msg):
        """
        Close due to protocol error.

		send a null packet to the server
		don't wait for a null packet back.
        """
        logger.debug("_protocolError: %s" % msg)
        self.readyState = READYSTATE.DISCONNECTED
        self._doWrite(True)
        self._doOnDisconnect(errors.ServerProtocolError(msg))

    def _receivedNullPacket(self):
        logger.debug('_receivedNullPacket')
        # send a null packet back to the server
        self._receivedNull = True
        # send our own null packet back. (maybe)
        if (not (self._nullInFlight or self._nullInBuffer or self._nullSent)):
            self.readyState = READYSTATE.DISCONNECTING
            self._doWrite(True)
        else:
            self.readyState = READYSTATE.DISCONNECTED
        # fire an onclose
        self._doOnDisconnect(errors.ConnectionClosedCleanly())

    def _sentNullPacket(self):
        logger.debug('_sentNullPacket')
        self._nullSent = True
        if (self._nullSent and self._nullReceived):
            self.readyState = READYSTATE.DISCONNECTED

    def close(self, err):
        logger.debug('close called: %s readyState: %s' % (err, self.readyState))
        if self.readyState == READYSTATE.CONNECTING:
            self._handshakeRetryTimer.cancel()
            self._handshakeTimeoutTimer.cancel()
            self.readyState = READYSTATE.DISCONNECTED
            self._doOnDisconnect(err)
        elif self.readyState == READYSTATE.CONNECTED:
            self.readyState = READYSTATE.DISCONNECTING
            self._doWrite(True)
            self._timeoutTimer.cancel()
        elif self.readyState == READYSTATE.DISCONNECTED:
            raise errors.ReadyStateError('Session is already closed.')

        self._sessionKey = None
        # self._opened = False
        self.readyState = READYSTATE.DISCONNECTED

        self._doOnDisconnect(err)

    def _handshakeTimeout(self):
        logger.debug("handshake timeout")
        self._handshakeTimeoutTimer = None
        self._doOnDisconnect(errors.ServerUnreachable())

    def _handshakeSuccess(self, data):
        logger.debug("handshake success %s" % data)
        if self.readyState != READYSTATE.CONNECTING:
            logger.debug("Received handshake success in invalid ready state %s"
                         % self.readyState)
            return
        self._handshakeTimeoutTimer.cancel()
        self._handshakeTimeoutTimer = None
        self._sessionKey = data['response']['session']
        # self._opened = True
        self.readyState = READYSTATE.CONNECTED
        self._doOnConnect()
        self._doConnectComet()

    def _handshakeFailure(self, data):
        logger.debug("handshake failure %s" % data)
        if self.readyState != READYSTATE.CONNECTING:
            return
        if data['status'] == 404:
            self._handshakeTimeoutTimer.cancel()
            return self._doOnDisconnect(errors.ServerUnreachable())
        logger.debug("retrying in %s" % self._handshakeBackoff)
        def retry():
            self._handshakeRetryTimer = None
            self._transport.handshake(self._url, self._options)
        self._handshakeRetryTimer = Timer(delayMillis=self._handshakeBackoff,
                                          notify=retry)
        self._handshakeBackoff *= 2

    def _writeSuccess(self):
        if not self.readyState == READYSTATE.CONNECTED:
            if not self.readyState == READYSTATE.DISCONNECTING:
                return
        if self._nullInFlight:
            return self._sentNullPacket()
        self._resetTimeoutTimer()
        self.writeBackoff = self.kDefaultBackoff
        self._packetsInFlight = None
        if self._writeBuffer or self._nullInBuffer:
            self._doWrite(self._nullInBuffer)

    def _writeFailure(self):
        if not self.readyState == READYSTATE.CONNECTED:
            if not self.readyState == READYSTATE.DISCONNECTING:
                return
        def retry():
            self._writeTimer = None
            self.__doWrite(self._nullInBuffer)
        self._writeTimer = Timer(delayMillis=self._writeBackoff,
                                 notify=retry)
        self._writeBackoff *= 2

    def _doWrite(self, sendNull):
        if self._packetsInFlight:
            if sendNull:
                self._nullInBuffer = True
                return
            return
        self.__doWrite(sendNull)

    def __doWrite(self, sendNull):
        logger.debug('_writeBuffer: %s' % self._writeBuffer)
        if not self._packetsInFlight:
            if self._writeBuffer:
                self._lastSentId += 1
                self._packetsInFlight = [self._transport.encodePacket(
                        self._lastSentId, self._writeBuffer, self._options)]
                self._writeBuffer = ''
        if sendNull and not(self._writeBuffer):
            if not self._packetsInFlight:
                self._packetsInFlight = []
            self._lastSentId += 1
            self._packetsInFlight.append([self._lastSentId, 0, None])
            self._nullInFlight = True
        if not self._packetsInFlight:
            logger.debug('no packets to send')
            return
        logger.debug('sending packets %s' % json.encode(self._packetsInFlight))
        if not self._lastEventId:
            lastEventId = 0
        else:
            lastEventId = self._lastEventId
        self._transport.send(self._url, self._sessionKey, lastEventId,
                             json.encode(self._packetsInFlight), self._options)

    def _doConnectComet(self):
        logger.debug("_doConnectComet")
        if not self._lastEventId:
            lastEventId = 0
        else:
            lastEventId = self._lastEventId
        self._transport.comet(self._url, self._sessionKey, lastEventId,
                              self._options)

    def _cometFailure(self, data):
        if not self.readyState == READYSTATE.CONNECTED:
            return
        if data['status'] == 404:
            if data['response'] == 'Session not found':
                return self.close(errors.ExpiredSession(data))
        def retry():
            self._doConnectComet()
        self._cometTimer = Timer(delayMillis=self._cometBackoff, notify=retry)
        self._cometBackoff *= 2

    def _cometSuccess(self, data):
        if not self.readyState == READYSTATE.CONNECTED:
            if not self.readyState == READYSTATE.DISCONNECTING:
                return
        logger.debug("comet success: %s" % data)
        self._cometBackoff = self.kDefaultBackoff
        self._resetTimeoutTimer()

        response = data['response']
        for packet in response:
            logger.debug('process packet %s' % packet)
            if packet is None:
                return self.close(errors.ServerProtocolError(data))
            ackId = packet[0]
            encoding = packet[1]
            data = packet[2]
            if isinstance(self._lastEventId, int):
                if ackId <= self._lastEventId:
                    continue
                elif ackId != self._lastEventId + 1:
                    return self._protocolError("Ack id too high")
            self._lastEventId = ackId
            if data is None:
                return self._receivedNullPacket()
            if encoding == 1:
                # base64 encoding
                try:
                    logger.debug('before base64decode: %s' % data)
                    data = base64.urlsafe_b64decode(data)
                    logger.debug('after base64decode: %s' % data)
                except:
                    return self._protocolError("cannot decode base64 payload")
            if self._options['encoding'] == 'utf8':
                self._utf8ReadBuffer += data
                result = self._utf8ReadBuffer.decode('utf8')
                data = result[0]
                self._utf8ReadBuffer = result[1:]
            logger.debug('dispatching data: %s' % data)
            try:
                self._doOnRead(data)
            except Exception(e):
                logger.error('application code threw an error',
                             ' (re-throwing in timeout) %s' % e)
                def reThrow():
                    logger.debug('timeout fired, throwing error %s' % e)
                    raise e
                Timer(0,reThrow)
        self._doConnectComet()

    def _doOnRead(self, data):
        if hasattr(self, 'onread'):
            logger.debug('calling onread function %s' % data)
            self.onread(data)
        else:
            logger.debug("skipping onread callback (function missing)")

    def _doOnDisconnect(self, err):
        if hasattr(self, 'ondisconnect'):
            logger.debug("calling ondisconnect function %s" % err)
            self.ondisconnect(err)
        else:
            logger.debug("skipping ondisconnect callback (function missing)")

    def _doOnConnect(self):
        if hasattr(self, 'onconnect'):
            logger.debug("calling onconnect function")
            try:
                self.onConnect()
            except Exception(e):
                logger.debug("onconnect caused error")
                def reThrow():
                    raise e
                Timer(0,reThrow)
        else:
            logger.debug("skipping onconnect callback (function missing)")

    def _resetTimeoutTimer(self):
        self._timeoutTimer.cancel()
        def timeOut():
            logger.debug("connection timeout expired")
            self.close(errors.ConnectionTimeout())
        self._timeoutTimer = Timer(self._getTimeoutInterval, timeOut)

    def _getTimeoutInterval(self):
        return self.kDefaultTimeoutInterval




