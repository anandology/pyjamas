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

from webio import interfaces
from pyjamas import Window

class Listener(interfaces.Listener):
    ID = 0
    tabStyle = {
		'background': '#442',
		'border': '1px solid #885',
		'margin': '0px 0px -1px 3px',
		'MozBorderRadius': '3px 0px 0px 3px',
		'WebkitBorderRadius': '3px 0px 0px 3px',
		'boxSizing': 'border-box',
		'borderRightWidth': '0px',
		'padding': '2px 0px 2px 5px',
		'cursor': 'pointer'
	}
    def __init__(self, server, opts):
        super(Listener, self).__init__(server, opts)
        self._clients = {}
        self._numTabs = 0
        self._frames = []



