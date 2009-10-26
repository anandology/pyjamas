
exec_order = []

class Imports(object):
    exec_order = exec_order
    def __init__(self):
        self.v = 1

imports = Imports()

overrideme = "not overridden"

from . import cls as loccls
from .imports import cls as upcls
