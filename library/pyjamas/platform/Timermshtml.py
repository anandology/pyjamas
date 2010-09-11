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

# Implementation of Timer for mshtml using python threading with a
# call into comtypes to make windows happy with python threads.

class Timer:
        
    def __impl_init_hook(self):

        # we need windows to fire the function so it's happy with
        # python threads...so we wrap the function with this call
        def wrap():
            pyjd.add_timer_queue(onTimer)
            
        onTimer = self.__onTimer
        self.__onTimer = wrap

    def __setTimeout(self, delayMillis):
        timer = pyjd.threading.Timer(delayMillis/1000.0, self.__fire)
        timer.start()
        return timer
    
    def __clearTimeout(self, timer):
        timer.cancel()
        
    def __setInterval(self, periodMillis):

        # wrap the call so we can repeat the interval
        def repeat():
            self.__fire()
            self.__tid = self.__setInterval(periodMillis)

        timer = pyjd.threading.Timer(periodMillis/1000.0, repeat)
        timer.start()

        return timer

    # they're the same
    __clearInterval = __clearTimeout
