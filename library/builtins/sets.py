# TODO: __hash__
class Set:
    def __init__(self, data=None):
        JS("""
        this.d = {};
        this.update(data);
        """)

    def add(self, value):
        JS("""    this.d[pyjslib_hash(value)] = value;""")

    def clear(self):
        JS("""    this.d = {};""")

    def __contains__(self, value):
        JS("""    return (this.d[pyjslib_hash(value)]) ? true : false;""")

    def discard(self, value):
        JS("""    delete this.d[pyjslib_hash(value)];""")

    def issubset(self, items):
        JS("""
        for (var i in this.d) {
            if (!items.__contains__(i)) return false;
            }
        return true;
        """)

    def issuperset(self, items):
        JS("""
        for (var i in items) {
            if (!this.__contains__(i)) return false;
            }
        return true;
        """)

    def __iter__(self):
        JS("""
        var items=new pyjslib_List();
        for (var key in this.d) items.append(this.d[key]);
        return items.__iter__();
        """)

    def __len__(self):
        JS("""
        var size=0;
        for (var i in this.d) size++;
        return size;
        """)

    def pop(self):
        JS("""
        for (var key in this.d) {
            var value = this.d[key];
            delete this.d[key];
            return value;
            }
        """)

    def remove(self, value):
        self.discard(value)

    def update(self, data):
        JS("""
        if (pyjslib_isArray(data)) {
            for (var i in data) {
                this.d[pyjslib_hash(data[i])]=data[i];
            }
        }
        else if (pyjslib_isIteratable(data)) {
            var iter=data.__iter__();
            var i=0;
            try {
                while (true) {
                    var item=iter.next();
                    this.d[pyjslib_hash(item)]=item;
                }
            }
            catch (e) {
                if (e != StopIteration) throw e;
            }
        }
        """)
