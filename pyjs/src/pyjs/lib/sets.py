from __pyjamas__ import JS

class Set:
    def __init__(self, data=None):
        JS("""
        self.d = {};
        self.update(data);
        """)

    def add(self, value):
        JS("""    self.d[pyjslib.hash(value)] = value;""")

    def clear(self):
        JS("""    self.d = {};""")

    def __contains__(self, value):
        JS("""    return (self.d[pyjslib.hash(value)]) ? true : false;""")

    def discard(self, value):
        JS("""    delete self.d[pyjslib.hash(value)];""")

    def issubset(self, items):
        JS("""
        for (var i in self.d) {
            if (!items.__contains__(i)) return false;
            }
        return true;
        """)

    def issuperset(self, items):
        JS("""
        for (var i in items) {
            if (!self.__contains__(i)) return false;
            }
        return true;
        """)

    def __iter__(self):
        JS("""
        var items=new pyjslib.List();
        for (var key in self.d) items.append(self.d[key]);
        return items.__iter__();
        """)

    def __len__(self):
        JS("""
        var size=0;
        for (var i in self.d) size++;
        return pyjslib['int'](size);
        """)

    def pop(self):
        JS("""
        for (var key in self.d) {
            var value = self.d[key];
            delete self.d[key];
            return value;
            }
        """)

    def remove(self, value):
        self.discard(value)

    def update(self, data):
        JS("""
        if (pyjslib.isArray(data)) {
            for (var i in data) {
                self.d[pyjslib.hash(data[i])]=data[i];
            }
        }
        else if (pyjslib.isIteratable(data)) {
            var iter=data.__iter__();
            var i=0;
            try {
                while (true) {
                    var item=iter.next();
                    self.d[pyjslib.hash(item)]=item;
                }
            }
            catch (e) {
                if (e != pyjslib.StopIteration) throw e;
            }
        }
        """)
