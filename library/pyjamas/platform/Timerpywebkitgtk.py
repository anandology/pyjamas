class Timer:

    def __setTimeout(self, delayMillis):

        return pyjd.gobject.timeout_add(delayMillis, self.__fire)

    def __clearTimeout(self,timer):
        timer.cancel()

    __clearInterval = __clearTimeout

