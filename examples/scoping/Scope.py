from Foo import Foo, Bar

class Scope:

    def onModuleLoad(self):
        f = Foo()
        b = Bar()

