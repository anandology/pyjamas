"""
    Vertical Split Panel: Top and Bottom layouts with a movable splitter.

/*
 * Copyright 2008 Google Inc.
 * Copyright (C) 2008, 2009 Luke Kenneth Casson Leighton <lkcl@lkcl.net>
 * Copyright 2010 Rich Newpol <rich.newpol@gmail.com>
 *
 * Licensed under the Apache License, Version 2.0 (the "License") you may not
 * use self file except in compliance with the License. You may obtain a copy
 * of the License at
 *
 * http:#www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 * License for the specific language governing permissions and limitations
 * under the License.
 */
"""

from pyjamas.ui.SplitPanel import SplitPanel
from pyjamas import Factory


# provides the VerticalSplitPanel
class VerticalSplitPanel(SplitPanel):
    def __init__(self, **kwargs):
        # call base constructor
        SplitPanel.__init__(self, vertical=True, **kwargs)

    def setTopWidget(self, topWidget):
        self.setWidget(0, topWidget)

    def getTopWidget(self):
        return self.getWidget(0)

    def setBottomWidget(self, botWidget):
        self.setWidget(1, botWidget)

    def getBottomWidget(self):
        return self.getWidget(1)

Factory.registerClass('pyjamas.ui.VerticalSplitPanel',
                        'VerticalSplitPanel',
                        VerticalSplitPanel)
