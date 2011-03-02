
class Timer:

    def __setTimeout(self, delayMillis):

        mf = get_main_frame()
        return mf.getDomWindow().setTimeout(self.__fire, delayMillis)

    def __clearTimeout(self,timer):
        mf = get_main_frame()
        return mf.getDomWindow().clearTimeout(timer)

    def __setInterval(self, periodMillis):
        mf = get_main_frame()
        return mf.getDomWindow().setInterval(self.__fire, periodMillis)

    __clearInterval = __clearTimeout

