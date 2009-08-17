# WARNING: the use of javascript pretty much trashes all chance of using
# pyjamas-desktop.  give serious consideration to doing something OTHER
# than including random bits of javascript off the internet in a pyjamas
# application.  the larger the random bit of javascript, the more chance
# there is that it will interact in some horrendous way with the pyjamas
# infrastructure.
#
# if you ABSOLUTELY MUST use javascript, here's how to do it.
#

from pyjamas import log

# this simply tells the compiler that the two names are to be dropped
# into the javascript global namespace
from __javascript__ import examplevar, get_examplevar

# the default behaviour of jsimport is to include the javascript file
# "inline" - unmodified - direct into the compiler output
from __pyjamas__ import jsimport

jsimport("example.js")

log.writebr(examplevar)
examplevar = 'Altered'
log.writebr( get_examplevar() )

