# Copyright 2006 James Tauber and contributors
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
from pyjamas import DOM

def blur(elem):
    elem.blur()

def createFocusable():
    e = DOM.createDiv()
    e.tabIndex = 0
    return e

def focus(elem):
    elem.focus()

def getTabIndex(elem):
    return elem.tabIndex

def setAccessKey(elem, key):
    elem.accessKey = key

def setTabIndex(elem, index):
    elem.tabIndex = index

