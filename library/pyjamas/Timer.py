from pyjamas import Window
from __pyjamas__ import JS, get_main_frame
import pyjd

class Timer:

    '''
    Timer() a re-implementation of GWT's Timer class.  This class has
    the same interface as GWT's with two minor enhancements in the
    constructor which changes what gets fired when the timer goes off.

    In addition to the constructor, there are four public methods:

       run() -- the method that gets fired when the timer goes off.
       The base class raises a NotImplementedError if it is not
       overridden by a subclass or if Timer isn't instantiated with
       the notify keyword arguement.

       schedule(delayMillis) -- schedule the timer to fire delayMillis
       milliseconds into the future.

       scheduleRepeating(periodMillis) -- schedule the timer to fire
       periodMillis milliseconds into the future and after execution
       (but not until execution is over), automatically reschedule the
       timer.  This is identical to an implementation of run() that
       calls schedule() on itself as its last action.

       cancel() -- cancel a timer.
       
    '''

    __timers = set()

    class __WindowCloseListener:
        ## window closing events
        # cancel all the timers when window is closed
        def onWindowClosed(self):
            for timer in list(Timer.__timers):
                timer.cancel()

        def onWindowClosing(self):
            pass

    def __init__(self, delayMillis=0, notify=None):

        '''Called with no arguments, create a timer that will call its
        run() method when it is scheduled and fired.  This is GWT's
        interface and behaviour.  There are two enhancements to
        pyjamas' implementation when specified with special keyword
        arguments:

            timer = Timer(delayMillis=ms)

        is identical to:

            timer = Timer()
            timer.schedule(ms)

        and:

            timer = Timer(notify=object_or_func)

        is the same as:

            timer = Timer()
            run = getattr(object_or_func, 'onTimer', object_or_func)
            if not callable(run): raise ValueError, msg
            timer.run = run

        i.e., the value passed to notify is checked to see if it has
        an onTimer attribute; if so, it is used as run(), if not the
        object itself is used as run()

        NOTE: there are no positional arguments!
        '''

        # initialize a few house keeping vars
        self.tid = None
        Window.addWindowCloseListener(Timer.__WindowCloseListener())

        # check notify
        if notify is not None:
            run = getattr(notify, 'onTimer', notify)
            if not callable(run):
                raise ValueError, 'Programming error: notify must be callable'
            self.run = run

        # schedule?
        if delayMillis != 0:
            self.schedule(delayMillis)

    def cancel(self):
        'Cancel the timer.'

        if self.tid is None:
            return

        if self.is_repeating:
            self.__clearInterval(self.tid)
        else:
            self.__clearTimeout(self.tid)

        self.tid = None
        Timer.__timers.discard(self)
    
    def run(self):
        'Run when fired...needs to be overridden.'
        raise NotImplementedError, ('''Timer.run() must be overridden or Timer
                                       must be instantiated with notify keyword
                                       argument''')

    def schedule(self, delayMillis):
        '''Schedule this timer to fire in delayMillis milliseconds.
        Calling this method cancels (for this instance only) any
        previously scheduled timer.'''

        if delayMillis <= 0:
            raise ValueError, 'delay must be positive'
        
        self.cancel()
        self.is_repeating = False
        self.tid = self.__setTimeout(delayMillis)
        Timer.__timers.add(self)
        

    def scheduleRepeating(self, periodMillis):
        '''Schedule this timer to fire forever (or until cancelled)
        every periodMillis milliseconds.  Calling this method cancels
        (for this instance only) any previously scheduled timer.'''

        if periodMillis <= 0:
            raise ValueError, 'period must be positive'
        
        self.cancel()
        self.is_repeating = True
        self.tid = self.__setInterval(periodMillis)
        Timer.__timers.add(self)

    # fire the timer
    def __fire(self):
        # if not repeating, remove it from the list of active timers
        if not self.is_repeating:
            Timer.__timers.discard(self)
        self.run()

    ######################################################################
    # Platforms need to implement the following four methods
    ######################################################################
        
    def __setTimeout(self, delayMillis):
        raise NotImplementedError, 'Timer is not fully implemented for your platform'

    def __clearTimeout(self,tid):
        raise NotImplementedError, 'Timer is not fully implemented for your platform'

    def __setInterval(self, periodMillis):
        raise NotImplementedError, 'Timer is not fully implemented for your platform'

    def __clearInterval(self, tid):
        raise NotImplementedError, 'Timer is not fully implemented for your platform'
