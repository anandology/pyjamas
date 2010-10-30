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

DROP_EVENTS = [ "dragenter", "dragover", "dragleave", "drop"]

def fireDropEvent(listeners, event):
    etype = DOM.eventGetType(event)
    if etype == "dragenter":
        for listener in listeners:
            listener.onDragEnter(event)
        return True
    elif etype == "dragover":
        for listener in listeners:
            listener.onDragOver(event)
        return True
    elif etype == "dragleave":
        for listener in listeners:
            listener.onDragLeave(event)
        return True
    elif etype == "drop":
        for listener in listeners:
            listener.onDrop(event)
        return True
    return False


class DropHandler(object):

    def __init__(self):
        self._dropListeners = []
        self.sinkEvents(Event.DROPEVENTS)

    def onBrowserEvent(self, event):
        event_type = DOM.eventGetType(event)
        if event_type in DROP_EVENTS:
            return fireDropEvent(self._dropListeners, event)
        return False

    def addDropListener(self, listener):
        self._dropListeners.append(listener)

    def removeDropListener(self, listener):
        self._dropListeners.remove(listener)

    def onDragEnter(self,event):
        """
        Decide whether to accept the drop.

        You may inspect the event's dataTransfer member.

        You may get the types using pyjamas.dnd.getTypes(event).

        This event is used to determine whether the drop target may
        accept the drop. If the drop is to be accepted, then this event has
        to be canceled using DOM.eventPreventDefault(event).
        """
        pass

    def onDragOver(self,event):
        """
        This event determines what feedback is to be shown to the user. If
        the event is canceled, then the feedback (typically the cursor) is
        updated based on the dropEffect attribute's value, as set by the event
        handler; otherwise, the default behavior (typically to do nothing)
        is used instead.

        Setting event.dataTransfer.dropEffect may affect dropping behavior.

        Cancel this event with DOM.eventPreventDefault(event) if you want the
        drop to succeed.

        """
        pass

    def onDragLeave(self,event):
        """
        This event happens when the mouse leaves the target element.
        """
        pass

    def onDrop(self,event):
        """allows the actual drop to be performed. This event also needs to be
        canceled, so that the dropEffect attribute's value can be used by the
        source (otherwise it's reset).
        """
        pass
