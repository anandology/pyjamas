from pyjamas import Window

def a():
    Window.alert( "in a" )
def b():
    Window.alert( "in b" )

class Foo:
    def __init__(self):
        Window.alert("Next you should see 'in a', 'in b'")
        x = [a, b]       
        for f in x:
            f() 


class Bar:
    def a():
        Window.alert( "in Bar a" )
    def b():
        Window.alert( "in Bar b" )

    Window.alert("Next you should see 'in Bar a', 'in Bar b'")
    x = [a, b]       
    for f in x:
        f() 

    def __init__(self):

        def a():
            Window.alert( "in bar a" )
        def b():
            Window.alert( "in bar b" )

        Window.alert("you should now see 'in bar a', 'in bar b'")
        x = [a, b]       
        for f in x:
            f() 
