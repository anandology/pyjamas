
class List:

    def index(self, value, start=0):
        JS("""
        var result = this.l.indexOf(value, start);
        if (result >= 0)
            return result;
        """)
        raise ValueError("list.index(x): x not in list")

class Tuple:

    def __contains__(self, value):
        return JS('self.l.indexOf(value)>=0')
