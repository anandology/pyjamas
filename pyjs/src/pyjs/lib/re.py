def _compile(pat):
    JS(""" return new RegExp(pat);""")

class SRE_Match:
    def __init__(self, mat, pat):
        self.__mat = mat
        self.__pat = pat
    def start(self):
        return self.__start
    def end(self):
        return self.__mat.lastIndex

class SRE_Pattern:
    def __init__(self, pat):
        self.pat = pat
    def match(self, mat):
        rex = _compile(self.pat)
        idx = mat.search(rex)
        if idx == -1:
            return None
        m = SRE_Match(rex, self)
        m.__start = idx

def compile(pat):
    return SRE_Pattern(pat)

