
exec_order = []

class Imports(object):
    exec_order = exec_order
    def __init__(self):
        self.v = 1

imports = Imports()

overrideme = "not overridden"

from . import cls as loccls
from .imports import cls as upcls

def conditional_func():
    return "not overridden"

if True:
    def conditional_func():
        return "overridden"
