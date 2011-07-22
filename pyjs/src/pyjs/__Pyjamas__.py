
import re
from lib2to3.pytree import Node, Leaf


class __Pyjamas__(object):

    def __init__(self, translator):
        self.translator = translator

    def add_lines(self, *args, **kwargs):
        lineno = None
        if len(args) > 0:
            if isinstance(args[0], Leaf):
                lineno = args[0].lineno
            elif isinstance(args[0], Node):
                for n in args[0].children:
                    if isinstance(args[0], Leaf):
                        lineno = n.lineno
                        break;
        self.add_lines(self.js(*args, **kwargs), lineno=lineno, split=False)


class JS(__Pyjamas__):

    re_escaped_subst = re.compile('@{{(!?[ a-zA-Z0-9_\.$-]*)}}')
    re_number = re.compile('^.*[^\d](\d+)$')

    def js(self, translator, code):
        def subs(m):
            name = m.group(1)
            if name[0] == '!':
                return name[1:]
            jsname = self.translator.get_jsname(name)
            return jsname
        for k, v in translator.const_str.iteritems():
            if v == code:
                # Remove the string constant
                translator.const_str[k] = None
                n = self.re_number.match(v)
                if n:
                    n = eval(n.group(1))
                    if len(translator.const_str) == n + 1:
                        del translator.const_str[k]
                return self.re_escaped_subst.sub(subs, k)
        raise translator.TranslationError("Lookup failure in JS")


class debugger(__Pyjamas__):

    def js(self, translator):
        return 'debugger'


class wnd(__Pyjamas__):

    def js(self, translator):
        return '$wnd'


class doc(__Pyjamas__):

    def js(self, translator):
        return '$doc'


class setCompilerOptions(__Pyjamas__):

    def js(self, *args):
        return


class INT(__Pyjamas__):

    def js(self, translator, value):
        return value


class get_main_frame(__Pyjamas__):

    def js(self, translator):
        return 'null'
