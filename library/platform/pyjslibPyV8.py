def printFunc(objs):
    JS("""
        var s = "";
        for(var i=0; i < objs.length; i++) {
            if(s != "") s += " ";
                s += objs[i];
        }

        print_fn(s);
    """)
