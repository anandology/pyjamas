def othermoduledeco1(f):
    def fn(*args, **kwargs):
        return "a" + f(*args, **kwargs) + "c"
    return fn
