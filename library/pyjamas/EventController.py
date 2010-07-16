# Module for creating event handlers

class Handler(object):

    def __init__(self, parent, event_type):
        self.parent = parent
        self.event_type = event_type
        self.listeners = {}
        self.callback_fnname = "on%s" % event_type

        # monkey-patch the parent with the callbacks
        add_listener_fnname = "add%sListener" % event_type
        del_listener_fnname = "remove%sListener" % event_type
        listener = "_%sListeners" % event_type
        on_event_name = "on%sEvent" % event_type
        setattr(parent, listener, self)
        setattr(parent, add_listener_fnname, self.addListener)
        setattr(parent, del_listener_fnname, self.removeListener)
        setattr(parent, on_event_name, self.onEvent)

    def addListener(self, listener, *args, **kwargs):
        args = args or ()
        kwargs = kwargs or {}
        self.listeners[listener] = (args, kwargs)

    def removeListener(self, listener):
        self.listeners.pop(listener)

    def onEvent(self, sender, *eventargs):
        for listener, args in self.listeners.items():
            fn = getattr(listener, self.callback_fnname, listener)
            (args, kwargs) = args
            args = (sender,) + eventargs + args
            fn(*args, **kwargs)

