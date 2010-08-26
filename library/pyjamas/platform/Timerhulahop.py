# Copyright (C) 2010, Daniel Popowich <danielpopowich@gmail.com>
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

# Implementation of Timer for hulahop using xpcom's nsITimer interface
# see pyjd/hula.py for details.

class Timer:

    def __setTimeout(self, delayMillis):

        mf = get_main_frame()
        return mf.nsITimer(self.__fire, delayMillis)

    def __clearTimeout(self,timer):
        timer.cancel()

    def __setInterval(self, periodMillis):
        mf = get_main_frame()
        return mf.nsITimer(self.__fire, periodMillis, True)

    # all xpcom timers are the same...
    __clearInterval = __clearTimeout
