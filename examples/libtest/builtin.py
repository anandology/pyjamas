# This module is used in builtin test
# It should only be used there! It is to check for conditional
# imports, which will succeed anyway, if the imported module is 
# imported somewhere else

value = 1

def get_value():
    return value
