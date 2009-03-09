function dictobj() {
}

function dict_init(d) {
    var u = new pyjslib.Dict([['goodbye', 2]]);
    this.d = d;
    d.update(u);
}

function dict_get_value(key) {
    return this.d.__getitem__(key)
}

dictobj.prototype.get_value = dict_get_value;
dictobj.prototype.init = dict_init;

