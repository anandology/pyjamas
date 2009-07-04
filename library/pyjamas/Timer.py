# This is the gtk-dependent Timer module.
# For the pyjamas/javascript version, see platform/TimerPyJS.py

import sys
if sys.platform not in ['mozilla', 'ie6', 'opera', 'oldmoz', 'safari']:
    from gobject import timeout_add
else:
    timers = []

class Timer:

    def __init__(self, time, notify):

        self.notify_fn = notify.onTimer
        self.timer_id = timeout_add(time, self.notify)

    def clearInterval(self, timer_id):
        pass

    def clearTimeout(self, timer_id):
        pass

    def createInterval(self, timer, period):
        pass

    def createTimeout(self, timer, delay):
        pass

    # TODO - requires Window.addWindowCloseListener
    def hookWindowClosing(self):
        pass

    def notify(self, *args):
        if self.notify_fn.func_code.co_argcount == 2:
            self.notify_fn(self.timer_id)
        else:
            self.notify_fn()

    def cancel(self):
        print "Timer.cancel: TODO"

    def run(self):
        pass

    def schedule(self, delayMillis):
        pass

    def scheduleRepeating(self, periodMillis):
        pass

    # TODO: UncaughtExceptionHandler, fireAndCatch
    def fire(self):
        pass

    def fireImpl(self):
        pass

    def getID(self):
        return self.timer_id

