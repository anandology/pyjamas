from pyjamas.__pyjamas__ import JS

def time():
    JS(" return new Date().getTime() / 1000.0; ")
