

class MultiListener(object):
    # The combinations that are coupled. E.g., if onFocus is defined, then
    # onLostFocus should also be defined. The set method will substitute the 
    # missing methods with the ignore method.
    # See also pyjamas.builder.Builder.eventListeners
    combinations = dict(
        onFocus = ["onLostFocus"],
        onLostFocus = ["onFocus"],
        onKeyDown = ["onKeyUp", "onKeyPress"],
        onKeyUp = ["onKeyPress", "onKeyDown"],
        onKeyPress = ["onKeyDown", "onKeyUp"],
        onMouseMove = ["onMouseDown","onMouseUp","onMouseEnter","onMouseLeave"],
        onMouseDown = ["onMouseUp","onMouseEnter","onMouseLeave","onMouseMove"],
        onMouseUp = ["onMouseEnter","onMouseLeave","onMouseMove","onMouseDown"],
        onMouseEnter = ["onMouseLeave","onMouseMove","onMouseDown","onMouseUp"],
        onMouseLeave = ["onMouseMove","onMouseDown","onMouseUp","onMouseEnter"],
        onTabSelected = ["onBeforeTabSelected"],
        onBeforeTabSelected = ["onTabSelected"],
    )

    def __init__(self, obj, **kwargs):
        self.set(obj, **kwargs)

    def set(self, obj, **kwargs):
        """Check for missing event functions and substitute these with """
        """the ignore method"""
        ignore = getattr(self, "ignore")
        for k, v in kwargs.iteritems():
            setattr(self, k, getattr(obj, v))
            if k in self.combinations:
                for k1 in self.combinations[k]:
                    if not hasattr(self, k1):
                        setattr(self, k1, ignore)

    def ignore(self, *args, **kwargs):
        """Ignore event"""
        # The methods returns True, which is only needed for the method
        # onBeforeTabSelected.
        return True
