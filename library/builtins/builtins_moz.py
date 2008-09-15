def __print(*objs):
    ___tojs___("""
    var s = "";
    for(var i=0; i < objs.length; i++) {
        if(s != "") s += " ";
        s += objs[i];
    }
    try {
        console.debug(s);
    } catch(e) {
        alert(s);
    }
    //print(s);
    """)
