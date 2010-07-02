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

from pyjamas import DOM

class InnerText(object):

    def setText(self, text):
        DOM.setInnerText(self.getElement(), text)

    def getText(self):
        return DOM.getInnerText(self.getElement())

