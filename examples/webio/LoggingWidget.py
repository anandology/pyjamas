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

import logging
from pyjamas import DOM
from pyjamas.ui.Widget import Widget

class LoggingWidget(Widget):
    def __init__(self, log='webio', level=logging.DEBUG):
        super(LoggingWidget, self).__init__(Element=DOM.createElement('ul'))
        logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s",
                            level=level)
        stream_handler = logging.StreamHandler(self)
        logger = logging.getLogger(log)
        logger.addHandler(stream_handler)
        self.setStyleAttribute('overflow', 'auto')
        self.setStyleAttribute('list-style-type', 'none')

    def write(self, data):
        e = self.getElement()
        d = DOM.createElement('li')
        DOM.setInnerHTML(d, data[:-1])
        DOM.appendChild(e, d)

    def flush(self):
        pass
