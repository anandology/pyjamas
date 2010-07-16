# Module for creating event handlers

class Handler(object):

    def __init__(self, parent, event_type,
                    callback_name=None,
                    on_event_name=None):
        self.parent = parent
        self.event_type = event_type
        self.listeners = {}
        if callback_name:
            self.callback_fnname = callback_name
        else:
            self.callback_fnname = "on%s" % event_type

        # monkey-patch the parent with the callbacks
        add_listener_fnname = "add%sListener" % event_type
        del_listener_fnname = "remove%sListener" % event_type
        listener = "_%sListeners" % event_type
        if on_event_name is None:
            on_event_name = "on%sEvent" % event_type
        setattr(parent, listener, self)
        setattr(parent, add_listener_fnname, self._addListener)
        setattr(parent, del_listener_fnname, self._removeListener)
        setattr(parent, on_event_name, self._onEvent)

    def _addListener(self, listener, *args, **kwargs):
        args = args or ()
        kwargs = kwargs or {}
        self.listeners[listener] = (args, kwargs)

    def _removeListener(self, listener):
        self.listeners.pop(listener)

    def _onEvent(self, sender, *eventargs):
        for listener, args in self.listeners.items():
            fn = getattr(listener, self.callback_fnname, listener)
            (args, kwargs) = args
            args = (sender,) + eventargs + args
            fn(*args, **kwargs)

