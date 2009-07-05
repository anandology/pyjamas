from pyjamas.Timer import Timer

deferredCommands = []
timerIsActive = False

class DeferredCommand:
    def add(self, cmd):
        global deferredCommands

        deferredCommands.append(cmd)
        self.maybeSetDeferredCommandTimer()
    
    def flushDeferredCommands(self):
        global deferredCommands
        
        for i in range(len(deferredCommands)):
            current = deferredCommands[0]
            del deferredCommands[0]
            
            if current is None:
                return
            else:
                current.execute()

    def maybeSetDeferredCommandTimer(self):
        global timerIsActive, deferredCommands
        
        if (not timerIsActive) and (not len(deferredCommands)==0):
            Timer(1, self)
            timerIsActive = True
            
    def onTimer(self, t):
        global timerIsActive

        self.flushDeferredCommands()
        timerIsActive = False
        self.maybeSetDeferredCommandTimer()


