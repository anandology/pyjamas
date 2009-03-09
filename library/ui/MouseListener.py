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

class MouseListener:
    def fireMouseEvent(self, listeners, sender, event):
        x = DOM.eventGetClientX(event) - DOM.getAbsoluteLeft(sender.getElement())
        y = DOM.eventGetClientY(event) - DOM.getAbsoluteTop(sender.getElement())

        type = DOM.eventGetType(event)
        if type == "mousedown":
            for listener in listeners:
                listener.onMouseDown(sender, x, y)
        elif type == "mouseup":
            for listener in listeners:
                listener.onMouseUp(sender, x, y)
        elif type == "mousemove":
            for listener in listeners:
                listener.onMouseMove(sender, x, y)
        elif type == "mouseover":
            from_element = DOM.eventGetFromElement(event)
            if not DOM.isOrHasChild(sender.getElement(), from_element):
                for listener in listeners:
                    listener.onMouseEnter(sender)
        elif type == "mouseout":
            to_element = DOM.eventGetToElement(event)
            if not DOM.isOrHasChild(sender.getElement(), to_element):
                for listener in listeners:
                    listener.onMouseLeave(sender)


