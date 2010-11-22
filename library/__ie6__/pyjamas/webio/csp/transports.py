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


class Jsonp(BaseTransport):
    def _request(self, req):
        ifr = self._ifr[req['type']]
        win = ifr.contentWindow
        doc = win.document
        body = doc.body
        def cfe(resp):
            self.checkForError(req, resp)
        def ons(resp):
            self.onSuccess(req, resp)

#        setattr(win, req['ebName'], cfe)
#        setattr(win, req['cbName'], ons)
        win[req['ebName']] = cfe
        win[req['cbName']] = ons


        s = DOM.createElement('script')
        DOM.setAttribute(s, 'src', req['url'])
        def orsc(event):
            self.onReadyStateChange(req, s)
        s.onreadystatechange = orsc
        body.appendChild(s)

    def onReadyStateChange(self, req, scriptTag):
        if scriptTag.readyState !='loaded':
            return
        self.checkForError(req)
        scriptTag.onreadystatechange = EMPTY_FUNCTION()
