
exec_order = []

class Imports(object):
    exec_order = exec_order
    def __init__(self):
        self.v = 1

imports = Imports()

overrideme = "not overridden"

from . import cls as loccls

# TODO: Generate an ImportError
# This is not valid since Python 2.6!
#try:
#    from .imports import cls as upcls
#except ImportError:
#    upcls = loccls
upcls = loccls

def conditional_func():
    return "not overridden"

if True:
    def conditional_func():
        return "overridden"

# Import all
all_masked = False
all_override = False
from allwith__all__ import *
from allsimple import *
