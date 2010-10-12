
class Timer:

    def __setTimeout(self, delayMillis):

        mf = get_main_frame()
        return mf.get_dom_window().setTimeout(self.__fire, delayMillis)

    def __clearTimeout(self,timer):
        mf = get_main_frame()
        return mf.get_dom_window().clearTimeout(timer)

    def __setInterval(self, periodMillis):
        mf = get_main_frame()
        return mf.get_dom_window().setInterval(self.__fire, periodMillis)

    __clearInterval = __clearTimeout

