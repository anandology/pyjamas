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

def makeDraggable(widget):
    element = widget.getElement()
    DOM.setAttribute(element, 'draggable', True)

# getTypes is provided to get around some of the
# various flavors dataTransfer.type objects.

def getTypes(event):
    types = []
    dt = event.dataTransfer
    try:
        dt_types = dt.types
        if isinstance(dt_types, str):
            return dt_types.split(',')
        ct = 0
        try:
            type_i = dt_types.item(ct)
            while type_i:
                types.append(type_i)
                ct += 1
                type_i = dt_types.item(ct)
        except:
            try:
                type_i = dt_types[ct]
                while type_i:
                    types.append(type_i)
                    ct += 1
                    type_i = dt_types[ct]
            except:
                for item in ['Text', 'URL', 'File','HTML', 'Image', 'String']:
                    try:
                        if len(dt.getData(item)):
                            types.append(item)
                    except:
                        pass
    except:
        for item in ['Text', 'URL', 'File','HTML', 'Image']:
            try:
                if len(dt.getData(item)):
                    types.append(item)
            except:
                pass
    return types
