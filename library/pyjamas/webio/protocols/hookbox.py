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

from rtjp import RtjpProtocol
from __pyjamas__ import doc
from webio import connect as jsioConnect

def connect(url, cookieString):
    if not url.endswith('/'):
        url += '/'
    p = HookBoxProtocol(url, cookieString)
    jsioConnect(p, 'csp', {'url':url + 'csp'})
    def connectionLost(reason, wasConnected):
        p._connectionLost('csp', reason, wasConnected)
    p.connectionLost = connectionLost
    return p

class HookBoxProtocol(RtjpProtocol):

    def __init__(self, url, cookieString=None):
        super(HookBoxProtocol, self).__init__('\r\n')
        self.url = url
        if cookieString:
            self.cookieString = cookieString
        else:
            try:
                self.cookieString = doc().cookie
            except:
                self.cookieString = ''
        self.connected = False
        self._subscriptions = {}
        self._buffered_subs = []
        self._publishes = []
        self._messages = []
        self._errors = {}
        self.username = None

    def subscribe(self, channel_name):
        if not self.connected:
            self._buffered_subs.append(channel_name)
        else:
            fId = self.sendFrame('SUBSCRIBE', {'channel_name' : channel_name})

    def publish(self, channel_name, data):
        if self.connected:
            self.sendFrame('PUBLISH', {'channel_name': channel_name,
                                       'payload': data})
        else:
            self._publishes.append([channel_name, data])

    def message(self, name, payload):
        if self.connected:
            self.sendFrame('MESSAGE', {'name': name,
                                       'payload':payload})
        else:
            self._messages.append([name, payload])

    def frameReceived(self, fId, fName, fArgs):
        if fName == 'MESSAGE':
            self.onMessaged(fArgs)
        elif fName == 'CONNECTED':
            self.connected = True
            self.username = fArgs['name']
            while self._buffered_subs:
                chan = self._buffered_subs.pop(0)
                self.sendFrame('SUBSCRIBE', {'channel_name':chan})
            while self._publishes:
                pub = self._publishes.pop(0)
                self.publish(pub[0], pub[1])
            while self._messages:
                msg = self._messages.pop(0)
                self.message(msg[0], msg[1])
        elif fName == 'SUBSCRIBE':
            if fArgs['user'] == self.username:
                s = Subscription(self, fArgs)
                self._subscriptions[fArgs['channel_name']] = s
                def cancelSubscription():
                    self.sendFrame('UNSUBSCRIBE', {'channel_name':
                        fArgs['channel_name']})
                s.onCancel = cancelSubscription
                self.onSubscribed(fArgs['channel_name'], s)
            else:
                self._subscriptions[fArgs['channel_name']].frame(fName, fArgs)
        elif fName == 'STATE_UPDATE':
            pass
        elif fName == 'PUBLISH':
            sub = self._subscriptions[fArgs['channel_name']]
            sub.frame(fname, fArgs)
        elif fName == 'UNSUBSCRIBE':
            sub = self._subscriptions[fArgs['channel_name']]
            sub.canceled = True
            sub.frame(fName, fArgs)
            if fArgs['user'] == self.username:
                del self._subscriptions[fArgs['channel_name']]
                self.onUnsubscribed(sub, fArgs)
        elif fName == 'ERROR':
            self.onError(fArgs)
        elif fName == 'SET_COOKIE':
            doc().cookie = fArgs['cookie']

    def _connectionLost(self, transportName, reason, wasConnected):
        if not wasConnected:
            logger.debug("connection failed: %s" % transportName)
            if transportName == 'websocket':
                logger.debug('retry with csp')
                def clcsp(self, reason):
                    return self._connectionLost('csp', reason, wasConnected)
                self.connectionLost = clcsp
                jsioConnect(self, 'csp',{'url':self.url + 'csp'})
        else:
            logger.debug('connection lost')
            self.connected = False
            self.onClose()

    def disconnect(self):
        self.transport.loseConnection()

class Subscription(object):
    def __init__(self, conn, args):
        self.channelName = args['channel_name']
        self.history = args['history']
        self.historySize = args['history_size']
        self.state = args['state']
        self.presence = args['presence']
        self.canceled = False
        def publish(data):
            conn.publish(self.channelName, data)
        self.publish = publish

    def onPublish(self, args):
        pass

    def onSubscribe(self, args):
        pass

    def onUnsubscribe(self, args):
        pass

    def onState(self, args):
        pass

    def updateHistory(self, name, args):
        if self.historySize:
            self.history.append([name, {'user': args['user'],
                'payload': args['payload']}])
            while len(self.history) > self.historySize:
                self.history.pop(0)

    def frame(self, name, args):
        logger.debug('received frame %s %s' % (name, args))
        if name == 'PUBLISH':
            self.updateHistory(name, args)
            self.onPublish(args)
        elif name == 'UNSUBSCRIBE':
            self.updateHistory(name, args)
            user = args['user']
            if user in self.presence:
                self.presence.remove(user)
            self.onUnsubscribe(args)
        elif name == 'SUBSCRIBE':
            self.updateHistory(name, args)
            self.presence.append(args['user'])
            self.onSubscribe(args)
        elif name == 'STATE_UPDATE':
            for key in args['deletes']:
                del self.state[key]
            for key in args['updates']:
                self.state[key] = args['updates'][key]
            self.onState(args)

    def cancel(self):
        if not self.canceled:
            logger.debug('calling _onCancel()')
            self._onCancel()

    def _onCancel(self):
        pass



