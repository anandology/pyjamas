# Copyright 2006 James Tauber and contributors
# Copyright 2009 Luke Kenneth Casson Leighton
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

class HasHorizontalAlignment:
    ALIGN_LEFT = "left"
    ALIGN_CENTER = "center"
    ALIGN_RIGHT = "right"

class HasVerticalAlignment:
    ALIGN_TOP = "top"
    ALIGN_MIDDLE = "middle"
    ALIGN_BOTTOM = "bottom"

class HasAlignment:
    ALIGN_BOTTOM = "bottom"
    ALIGN_MIDDLE = "middle"
    ALIGN_TOP = "top"
    ALIGN_CENTER = "center"
    ALIGN_LEFT = "left"
    ALIGN_RIGHT = "right"

class Applier(object):
             
    def __init__(self, **kwargs):
        """ use this to apply properties as a dictionary, e.g.
                x = klass(..., StyleName='class-name')
            will do:
                x = klass(...)
                x.setStyleName('class-name')

            and:
                x = klass(..., Size=("100%", "20px"), Visible=False)
            will do:
                x = klass(...)
                x.setSize("100%", "20px")
                x.setVisible(False)
        """

        self.applyValues(**kwargs)

    def applyValues(self, **kwargs):

        if not kwargs:
            return
        k = kwargs.keys()
        l = len(k)
        i = -1
        while i < l-1:
            i += 1
            prop = k[i]
            fn = getattr(self, "set%s" % prop, None)
            if not fn:
                return
            args = kwargs[prop]
            if isinstance(args, tuple):
                fn(*args)
            else:
                fn(args)

    def retrieveValues(self, *args):
        """ use this function to obtain a dictionary of properties, as
            stored in getXXX functions.
        """

        res = {}
        for prop in args:
            fn = getattr(self, "get%s" % prop, None)
            if not fn:
                continue
            res[prop] = fn()

        return res

