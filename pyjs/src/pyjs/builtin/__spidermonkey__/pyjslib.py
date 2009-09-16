
def printFunc(objs, newline):
    JS("""
    print.apply(this, objs);
    """)

@compiler.noSourceTracking
def debugReport(msg):
    JS("""
    print(msg);
    """)

