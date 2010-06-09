

class MultiListener(object):
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
    )

    def __init__(self, obj, **kwargs):
        self.set(obj, **kwargs)

    def set(self, obj, **kwargs):
        ignore = getattr(self, "ignore")
        for k, v in kwargs.iteritems():
            setattr(self, k, getattr(obj, v))
            if k in self.combinations:
                for k1 in self.combinations[k]:
                    if not hasattr(self, k1):
                        setattr(self, k1, ignore)

    def ignore(self, *args, **kwargs):
        pass
