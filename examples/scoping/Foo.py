from pyjamas import Window

def a():
    Window.alert( "in a" )
def b():
    Window.alert( "in b" )

class Foo:
    def __init__(self):
        x = [a, b]       
        for f in x:
            f() 

class Bar:
    def a(self):
        Window.alert( "in bar a" )
    def b(self):
        Window.alert( "in bar b" )

    def __init__(self):
        Window.alert("you should now see 'in bar a', 'in bar b'")
        x = [a, b]       
        for f in x:
            f() 

