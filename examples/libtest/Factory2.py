global gclasses
gclasses = {}

def gregister(className, classe):
    gclasses[className] = classe
def ggetObject(className, *args, **kargs):
    classe = gclasses[className]
    return classe(*args, **kargs)


