class rectobj:
    pass
def rect_area(self):
    return self.x * self.y
def rect_add(self, rect):
    self.x += rect.x
    self.y += rect.y
def rect_init(self, x, y):
    self.x = x
    self.y = y
rectobj.__init__ = rect_init
rectobj.add = rect_add
rectobj.area = rect_area

x = rectobj(5, 2)
y = rectobj(2, 7)
print x.area()
x.add(y)
print x.area()
