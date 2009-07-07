
def printFunc(objs, newline):
    JS("""
    print.apply(this, objs);
    """)
