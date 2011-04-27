# Copyright 2006 James Tauber and contributors
# Copyright (C) 2009 Luke Kenneth Casson Leighton <lkcl@lkcl.net>
# Copyright (C) 2010 Serge Tarkovski <serge.tarkovski@gmail.com>
# Copyright (C) 2010 Rich Newpol (IE override) <rich.newpol@gmail.com>
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

# This IE-specific override is required because IE doesn't allow
# empty element to generate events. Therefore, when the mouse moves
# (or clicks) happen over *only* the GlassWidget (which is empty)
# they stop flowing. however, IE does provide setCapture/releaseCapture
# methods on elements which can be used to same effect as a regular
# GlassWidget.

# This file implements the IE version of GlassWidget simply by mapping
# the GlassWidget API to the use of setCapture/releaseCapture

# we re-use the global 'mousecapturer' to prevent GlassWidget.hide()
# from releasing someone else's capture

def show(mousetarget, **kwargs):
    global mousecapturer
    # get the element that wants events
    target_element = mousetarget.getElement()
    # insure element can capture events
    if hasattr(target_element,"setCapture"):
        # remember it
        mousecapturer = target_element
        # start capturing
        DOM.setCapture(target_element)

def hide():
    global mousecapturer
    if hasattr(mousecapturer,"releaseCapture"):
        DOM.releaseCapture(mousecapturer)
    mousecapturer = None
