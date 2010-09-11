# Module for creating event handlers

######################
## EventGenerator - mixin notification support class
#
# An EventGenerator mixin keeps multiple listener lists for custom events,
# and can fire notifications for the events
#
# To use this class, simply add the mixin class to the derived class definition:
## class myClass(somebaseclass, EventGenerator):
# The derived class can define any number of custom events with a single call:
## self.addListenedEvent("Foo")
# which will add the usual listener management methods to the class:
## def addFooListener(self, listener)      # add a listener
## def removeFooListener(self, listener)   # remove a listener
# as well as a method to send a custom event notification to the listeners:
## def dispatchFooEvent(self, parms*)   # call listeners
# Listeners use this class in the usual way:
## fooObj.addFooListener(self)      # will call self.onFoo() if I have one
# OR
## fooObj.addFooListener(self.myFooHandler)      # will call self.myFooHandler()
#
# R. Newpol - 2009
#########################################

class EventGenerator():
    def _get_add_listener_func_name(self, ev):
        return "add"+ev+"Listener"
    def _get_remove_listener_func_name(self, ev):
        return "remove"+ev+"Listener"
    def _get_dispatch_func_name(self, ev):
        return "dispatch"+ev+"Event"
    def addListenedEvent(self, ev):
        # create the EventListener with event-specific lists and funcs
        el = EventListener(ev)
        # add the "addXXXListener() method to ourself
        attr_add = self._get_add_listener_func_name(ev)
        setattr(self,attr_add,el.add_listener)
        # add the "removeXXXListener()" method to ourself
        attr_rem = self._get_remove_listener_func_name(ev)
        setattr(self,attr_rem,el.rem_listener)
        # add the "dispatchXXXEvent() method to ourself
        attr_dsp = self._get_dispatch_func_name(ev)
        setattr(self,attr_dsp,el.dispatch)

# EventListener objects provide event-specific listener list,
# as well as event-specific methods to add/remove listeners to the list,
# and dispatch event notifications
# This class is not instantiated directly; it is used by the EventGenerator class
class EventListener():
    def __init__(self, ev):
        self.ev = ev
        self.listeners = []
    def add_listener(self, listener):
        self.listeners.append(listener)
    def rem_listener(self, listener):
        self.listeners.remove(listener)
    # listener objects should have a "onXX" event method
    def dispatch(self, *args):
        ev = "on"+self.ev
        for listener in self.listeners:
            if hasattr(listener,ev):
                getattr(listener,ev)(*args)
            else:
                listener(*args)


# original Handler event class (unrelated to EventGenerator)
class Handler(object):

    def __init__(self, parent, event_type, *args, **kwargs):
        self.parent = parent
        self.event_type = event_type
        self.listeners = {}
        self.callback_fnname = "on%s" % event_type
        self.extra_args = args
        self.extra_kwargs = kwargs

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
        args = self.extra_args + args 
        kwargs.update(self.extra_kwargs)
        self.listeners[listener] = (args, kwargs)

    def removeListener(self, listener):
        self.listeners.pop(listener)

    def onEvent(self, sender, *eventargs):
        for listener, args in self.listeners.items():
            fn = getattr(listener, self.callback_fnname, listener)
            (args, kwargs) = args
            args = (sender,) + args + eventargs
            fn(*args, **kwargs)

