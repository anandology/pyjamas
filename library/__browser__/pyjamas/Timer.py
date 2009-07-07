#Timer().hookWindowClosing()

class Timer:
    MIN_PERIOD = 1
    
    def __init__(self, delay = 0, object = None):
        self.isRepeating = False
        self.timerId = 0

        self.listener = object
        if delay >= Timer.MIN_PERIOD:
            self.schedule(delay)
    
    def clearInterval(self, id):
        JS("""
        $wnd.clearInterval(id);
        """)

    def clearTimeout(self, id):
        JS("""
        $wnd.clearTimeout(id);
        """)

    def createInterval(self, timer, period):
        JS("""
        return $wnd.setInterval(function() { timer.fire(); }, period);
        """)

    def createTimeout(self, timer, delay):
        JS("""
        return $wnd.setTimeout(function() { timer.fire(); }, delay);
        """)

    # TODO - requires Window.addWindowCloseListener
    def hookWindowClosing(self):
        pass
    
    def cancel(self):
        if self.isRepeating:
            self.clearInterval(self.timerId)
        else:
            self.clearTimeout(self.timerId)
        timers.remove(self)

    def run(self):
            self.listener.onTimer(self.timerId)
    
    def schedule(self, delayMillis):
        if delayMillis < Timer.MIN_PERIOD:
            alert("Timer delay must be positive")
        self.cancel()
        self.isRepeating = False
        self.timerId = self.createTimeout(self, delayMillis)
        timers.append(self)

    def scheduleRepeating(self, periodMillis):
        if periodMillis < Timer.MIN_PERIOD:
            alert("Timer period must be positive")
        self.cancel()
        self.isRepeating = True
        self.timerId = self.createInterval(self, periodMillis)
        timers.append(self)

    # TODO: UncaughtExceptionHandler, fireAndCatch
    def fire(self):
        self.fireImpl()

    def fireImpl(self):
        if not self.isRepeating:
            timers.remove(self)
        self.run()

    def getID(self):
        return self.timerId


    
