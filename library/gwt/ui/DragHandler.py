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

from pyjamas import DOM
from pyjamas.ui import Event

DRAG_EVENTS = [ "dragstart", "drag", "dragend"]

def fireDragEvent(listeners, event):
    etype = DOM.eventGetType(event)
    if etype == "dragstart":
        for listener in listeners:
            listener.onDragStart(event)
        return True
    elif etype == "drag":
        for listener in listeners:
            listener.onDrag(event)
        return True
    elif etype == "dragend":
        for listener in listeners:
            listener.onDragEnd(event)
        return True
    return False

class DragHandler(object):

    def __init__(self):
        self._dragListeners = []
        self.sinkEvents(Event.DRAGEVENTS)

    def onBrowserEvent(self, event):
        event_type = DOM.eventGetType(event)
        if event_type in DRAG_EVENTS:
            return fireDragEvent(self._dragListeners, event)
        return False

    def addDragListener(self, listener):
        self._dragListeners.append(listener)

    def removeDragListener(self, listener):
        self._dragListeners.remove(listener)

    def onDragStart(self, event):
        """
        Store data into the DataTransfer object and set the allowed effects.

        Set data into the event's dataTransfer with a content-type and some
        string data.

        Some native dataTransfer objects will only set content-type of "Text"
        and/or "URL".

        allowedEffects is one of:
            'none', 'copy', 'copyLink', 'copyMove', 'link', 'linkMove', 'move',
            or 'all'

        an example:

         dt = event.dataTransfer
         dt.setData('text/plain','Hello, World!')
         dt.allowedEffects = 'copyMove'
        """
        pass

    def onDrag(self, event):
        """
        this happens periodically while the drag is in progress.
        use DOM.eventPreventDefault(event) to cancel drag operation
        """
        pass

    def onDragEnd(self, event):
        """
        This happens on the initiating widget after the dragging mouse
        is released.
        """
        pass

