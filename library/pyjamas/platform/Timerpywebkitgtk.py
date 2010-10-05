class Timer:

    def __setTimeout(self, delayMillis):

        return pyjd.gobject.timeout_add(delayMillis)

    def __clearTimeout(self,timer):
        timer.cancel()

    def __setInterval(self, periodMillis):
        mf = get_main_frame()
        return mf.nsITimer(self.__fire, periodMillis, True)

    __clearInterval = __clearTimeout

