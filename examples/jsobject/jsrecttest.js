function rectobj() {
}

function rect_init(x, y) {
    this.x = x;
    this.y = y;
}

function rect_area() {
    return this.x * this.y;
}

function rect_add(rect) {
    this.x += rect.x;
    this.y += rect.y;
}

rectobj.prototype.area = rect_area;
rectobj.prototype.add = rect_add;
rectobj.prototype.init = rect_init;

