from pyjamas.Timer import Timer

deferredCommands = []
timerIsActive = False


def add(cmd):
    deferredCommands.append(cmd)
    maybeSetDeferredCommandTimer()


def flushDeferredCommands():
    for i in range(len(deferredCommands)):
        current = deferredCommands[0]
        del deferredCommands[0]
        if current:
            current.execute()


def maybeSetDeferredCommandTimer():
    global timerIsActive

    if (not timerIsActive) and (not len(deferredCommands) == 0):
        Timer(1, onTimer)
        timerIsActive = True


def onTimer(t):
    global timerIsActive

    flushDeferredCommands()
    timerIsActive = False
    maybeSetDeferredCommandTimer()


# a simple object to implement a deferred function/method call
class DPC_Obj():
    def __init__(self, func):
        self._func = func

    # the execute method is called by DeferredComand
    def execute(self):
        self._func()


# a simple DPC mechanism
# calls the specified routine (with no args)
# after event stack is cleared
def queue_Call(func):
    add(DPC_Obj(func))
