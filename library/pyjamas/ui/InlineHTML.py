# Copyright 2010, Daniel Popowich <danielpopowich@gmail.com>
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
from pyjamas import Factory
from HTML import HTML

class InlineHTML(HTML):
    '''An HTML, but using <span> instead of <div>'''
    
    def __init__(self, html=None, wordWrap=True, **kwargs):
        kwargs['StyleName'] = kwargs.get('StyleName', "gwt-InlineHTML")
        kwargs['Element'] = DOM.createSpan()
        HTML.__init__(self, html, wordWrap, **kwargs)
        
Factory.registerClass('pyjamas.ui.InlineHTML', InlineHTML)
