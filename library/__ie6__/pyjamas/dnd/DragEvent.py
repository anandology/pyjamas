
class DragEvent:

    def setTarget(self, target=None):
        if target is not None:
            self.srcElement = target
            #self.target = target
        else:
            self.srcElement = DOM.eventGetTarget(self.evt)
            #self.target = target