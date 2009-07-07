
class List:
    def index(self, value, start=0):
        JS("""
        var result = this.l.indexOf(value, start);
        if (result >= 0)
            return result;
        """)
        raise ValueError("list.index: " + value + " not in list")

class Tuple:
    def index(self, value, start=0):
        JS("""
        var result = this.l.indexOf(value, start);
        if (result >= 0)
            return result;
        """)
        raise ValueError("list.index: " + value + " not in list")
