"""
* Copyright 2007,2008,2009 John C. Gunther
* Copyright (C) 2009 Luke Kenneth Casson Leighton <lkcl@lkcl.net>
*
* Licensed under the Apache License, Version 2.0 (the
* "License"); you may not use this file except in compliance
* with the License. You may obtain a copy of the License at:
*
*  http:#www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing,
* software distributed under the License is distributed on an
* "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
* either express or implied. See the License for the specific
* language governing permissions and limitations under the
* License.
*
"""



"""
* Allows precise alignment of a text label before the
* exact size of that label is known, by enclosing it
* within a 1x1 grid.
* <p>
*
* The external grid must be larger than the label or requested grid
* alignment won't be realized. But larger that required containing
* grids occlude mouse events from nearby elements. The
* NonoccludingReusableAlignedLabel subclasses this class to solve
* this problem.
*
*
"""

class AlignedLabel(Grid):
    def __init__(self, **kwargs):
        Grid.__init__(self, 1, 1, **kwargs)
        self.getCellFormatter().setWordWrap(0,0,False)
        self.setCellPadding(0)
        self.setCellSpacing(0)
        self.setBorderWidth(0)




