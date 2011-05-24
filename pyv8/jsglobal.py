import PyV8

class FileWrapper(object):
    def __init__(self, fname, mode):
        self.f = open(fname, mode)

    def seek(self, seekto=None):
        if seekto is None:
            return self.f.seek()
        return self.f.seek(seekto)

    def close(self):
        return self.f.close()

    def write(self, bytes):
        return self.f.write(bytes)

    def read(self, bytes=None):
        if bytes is None:
            return self.f.read()
        return self.f.read(bytes)

# Create a python class to be used in the context
class Global(PyV8.JSClass):
    def pyv8_open(self, fname, mode):
        return FileWrapper(fname, mode)

    def pyv8_print_fn(self, arg):
        print arg

    def pyv8_import_module(self, parent_name, module_name):
        #print "pyv8_import_module", parent_name, module_name
        exec "import " + module_name
        return locals()[module_name]
    
    def pyv8_load(self, modules):
        for i in range(len(modules)):
            fname = modules[i]
            fp = open(fname, 'r')
            txt = fp.read()
            fp.close()
            try:
                x = self.__context__.eval(txt)
            except Exception, e:
                print "Failed to load %s: '%s'" % (fname, e)