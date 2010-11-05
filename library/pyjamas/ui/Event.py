# Copyright 2006 James Tauber and contributors
# Copyright (C) 2009 Luke Kenneth Casson Leighton <lkcl@lkcl.net>
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

"""
    This module contains flags and integer values used by the event system.
"""

BUTTON_LEFT   = 1
BUTTON_MIDDLE = 4
BUTTON_RIGHT  = 2

ONBLUR        = 0x01000
ONCHANGE      = 0x00400
ONCLICK       = 0x00001
ONCONTEXTMENU = 0x20000
ONDBLCLICK    = 0x00002
ONERROR       = 0x10000
ONFOCUS       = 0x00800
ONKEYDOWN     = 0x00080
ONKEYPRESS    = 0x00100
ONKEYUP       = 0x00200
ONLOAD        = 0x08000
ONLOSECAPTURE = 0x02000
ONMOUSEDOWN   = 0x00004
ONMOUSEMOVE   = 0x00040
ONMOUSEOUT    = 0x00020
ONMOUSEOVER   = 0x00010
ONMOUSEUP     = 0x00008
ONMOUSEWHEEL  = 0x40000
ONSCROLL      = 0x04000
ONINPUT       = 0x80000
DRAGEVENTS    = 0x100000
DROPEVENTS    = 0x200000

FOCUSEVENTS   = 0x01800 # ONFOCUS | ONBLUR
KEYEVENTS     = 0x00380 # ONKEYDOWN | ONKEYPRESS | ONKEYUP
MOUSEEVENTS   = 0x0007C # ONMOUSEDOWN | ONMOUSEUP | ONMOUSEMOVE | ONMOUSEOVER | ONMOUSEOUT

eventbits = {
    # bit    :  name, sinkEvents
    0x000001 : ("click", ["click"]),
    0x000002 : ("dblclick", ["dblclick"]),
    0x000004 : ("mousedown", ["mousedown"]),
    0x000008 : ("mouseup", ["mouseup"]),
    0x000010 : ("mouseover", ["mouseover"]),
    0x000020 : ("mouseout", ["mouseout"]),
    0x000040 : ("mousemove", ["mousemove"]),
    0x000080 : ("keydown", ["keydown"]),
    0x000100 : ("keypress", ["keypress"]),
    0x000200 : ("keyup", ["keyup"]),
    0x000400 : ("change", ["change"]),
    0x000800 : ("focus", ["focus"]),
    0x001000 : ("blur", ["blur"]),
    0x002000 : ("losecapture", ["losecapture"]),
    0x004000 : ("scroll", ["scroll"]),
    0x008000 : ("load", ["load"]),
    0x010000 : ("error", ["error"]),
    0x020000 : ("contextmenu", ["contextmenu"]),
    0x040000 : ("mousewheel", ["mousewheel"]),
    0x080000 : ("input", ["input"]),
    0x010000 : ("dragevents", ["drag", "dragstart", "dragend"]),
    0x020000 : ("dropevents", ["drop", "dragenter", "dragover", "dragleave"]),
}
# eventmap will be filled in init(), but some names
# will be added manually for interoperability
# (duplicate names for bit)
eventmap = {
    "mousewheel": 0x040000,
    "mousescroll": 0x040000,
    "DOMMouseScroll": 0x040000,
    "input": 0x080000,
    "propertychange": 0x080000,
}

def _create_eventmap():
    for bit, bitmap in eventbits.iteritems():
        eventmap[bitmap[0]] = bit

def init():
    _create_eventmap()

init()
