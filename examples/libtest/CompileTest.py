#This module does no actual work. It simply consists of some tests which may
#cause compile to fail. When you find a new compiler bug, first add the test
#here, in commented-out form. When you've patched the bug, remove the comments.

#issue 432
x, y = 1, 2
del x, y

#issue 433
for x in [1, 2] + [3, 4]:
  pass
