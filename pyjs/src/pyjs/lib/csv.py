#
# This is an incomplete start of csv module
# The current contents should in fact go to _csp.py
#

class CSVReader(object):
    def __init__(self, lines, dialect = None, **kwargs):
        self.__values = []
        self.__inString = False
        self.delimeter = kwargs.get('delimeter', ',')
        self.quotechar = kwargs.get('quotechar', '"')
        self.dialect = dialect
        self.line_num = 0

        lineno = 0
        for line in lines:
            lineno += 1
            self.addNewline(lineno)
            cols = line.split(self.delimeter)
            if len(cols) > 0:
                self.addValue(cols[0], True)
                for col in cols[1:]:
                    self.addValue(col, False)

    def addNewline(self, lineno):
        if self.__inString:
            self.__values[-1][0] = lineno
        else:
            if len(self.__values) > 0:
                row = self.__values[-1]
                if len(row) > 1 and len(row[-1]) > 0:
                    if row[-1][-1] == '\n':
                        row[-1] = row[-1][:-1]
            self.__values.append([lineno])

    def addValue(self, v, isFirst):
        if self.__inString:
            # Check for end of string
            sv = v.rstrip()
            idx0 = idx = len(sv)-1
            while idx > 0 and sv[idx] == self.quotechar:
                idx -= 1
            if (idx0 - idx) % 2:
                v = sv[:-1]
                self.__inString = False
            v = v.replace(self.quotechar + self.quotechar, self.quotechar)
            if isFirst:
                self.__values[-1][-1] += v
            else:
                self.__values[-1][-1] += self.delimeter + v
        else:
            sv = v.lstrip()
            if len(sv) > 0 and sv[0] == self.quotechar:
                self.__inString = True
                v = sv[1:]
                sv = v.rstrip()
                idx0 = idx = len(sv)-1
                while idx > 0 and sv[idx] == self.quotechar:
                    idx -= 1
                if (idx0 - idx) % 2:
                    v = sv[:-1]
                    self.__inString = False
            if isFirst:
                if len(sv) > 0 and sv[-1] == self.quotechar:
                    if len(sv) == 1 or sv[-2] != self.quotechar:
                        v = sv[:-1]
                        self.__inString = False
            v = v.replace(self.quotechar + self.quotechar, self.quotechar)
            self.__values[-1].append(v)

    def __iter__(self):
        self.__iter = self.__values.__iter__()
        return self

    def next(self):
        v = self.__iter.next()
        self.line_num = v[0]
        return v[1:]


def reader(lines, **kwargs):
    return CSVReader(lines, **kwargs)

