"""Overrides which use the indexOf method of arrays in supported browsers"""

class List:

    @compiler.noSourceTracking
    @compiler.noDebug
    def index(self, value, start=0):
        JS("""
        var result = this.l.indexOf(value, start);
        if (result >= 0)
            return result;
        """)
        raise ValueError("list.index(x): x not in list")

class Tuple:

    @compiler.noSourceTracking
    @compiler.noDebug
    def __contains__(self, value):
        return JS('self.l.indexOf(value)>=0')
