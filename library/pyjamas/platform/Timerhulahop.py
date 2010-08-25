# Implementation for hulahop

# uses xpcom's nsITimer interface
# see pyjd/hula.py for details

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
