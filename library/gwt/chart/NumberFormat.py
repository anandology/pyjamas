class NF:
    def __init__(self, fmt):
        self.fmt = fmt

    def format(self, num):
        """ cheerfully ignore the number format requested
            and just return the number converted to a string
        """
        # To speedup int when not compiled with --number-classes
        # (or with --strict)
        from __pyjamas__ import INT
        return str(INT(num))

def getFormat(fmt):
    return NF(fmt)

