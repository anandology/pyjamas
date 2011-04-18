import pyjd # this is dummy in pyjs.

# This is more for a unittest than an example...

class Scope:

    def onModuleLoad(self):
        from Foo import Foo, Bar
        f = Foo()
        b = Bar()

if __name__ == '__main__':
    pyjd.setup("Scope.html")
    app = Scope()
    app.onModuleLoad()
    pyjd.run()
