from pyjamas import DOM

class DragEvent(object):
    """
    emulates a drag event.
    http://dev.w3.org/html5/spec/dnd.html#dragevent
    """
    relatedTarget = None
    detail = 0
    returnValue = True
    def __init__(self, evt, type, dataTransfer, target=None):
        self.evt = evt
        self.type = type
        self.setTarget(target)
        self.dataTransfer = dataTransfer
        self.canBubble = True
        if self.type in ['dragleave', 'dragend']:
            self.cancelable = False
        else:
            self.cancelable = True

    def setTarget(self, target=None):
        if target is not None:
            self.target = target
        else:
            self.target = DOM.eventGetTarget(self.evt)

    # rather than copying a bunch of attributes on init, we provide a bunch
    # of property statements.  These properties hardly ever get looked at
    # during dnd events anyway, but they're there if we need them.

    def stopPropagation(self):
        self.evt.stopPropagation()

    @property
    def screenX(self):
        return self.evt.screenX

    @property
    def screenY(self):
        return self.evt.screenY

    @property
    def pageX(self):
        return self.evt.pageX

    @property
    def pageY(self):
        return self.evt.pageY

    @property
    def clientX(self):
        return self.evt.clientX

    @property
    def clientY(self):
        return self.evt.clientY

    @property
    def altKey(self):
        return self.evt.altKey

    @property
    def ctrlKey(self):
        return self.evt.ctrlKey

    @property
    def shiftKey(self):
        return self.evt.shiftKey

    @property
    def metaKey(self):
        return self.evt.metaKey

    @property
    def button(self):
        return self.evt.button

    def preventDefault(self):
        """
        ie6 sets returnValue to False, so we do, too.
        """
        self.returnValue = False

    def initDragEvent(self, type, canBubble, cancelable, dummy, detail, screenX,
                      screenY, clientX, clientY, ctrlKey, altKey, shiftKey,
                      metaKey, button, relatedTarget, dataTransfer):
        """
        Just raise NotImplemented.  Provided only for completeness with the
        Interface.
        """
        raise NotImplemented("Instanciate this class with a mouse event.")
#        self.type = type
#        self.canBubble = canBubble
#        self.cancelable = cancelable
#        self.dummy = dummy
#        self.detail = detail
#        self.screenX = screenX
#        self.screenY = screenY
#        self.clientX = clientX
#        self.clientY = clientY
#        self.ctrlKey = ctrlKey
#        self.altKey = altKey
#        self.shiftKey = shiftKey
#        self.metaKey = metaKey
#        self.button = button
#        self.relatedTarget = relatedTarget
#        self.dataTransfer = dataTransfer

