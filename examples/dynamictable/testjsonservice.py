#!/usr/bin/env python
from pprint import pprint

import jsonrpclib
s = jsonrpclib.ServerProxy("http://127.0.0.1/examples/dynamictable/output/SchoolCalendarService.php",
                           verbose=0)
try:
    reply = s.getPeople(0, 10)
except jsonrpclib.ProtocolError, e:
    print e, e.errcode, e.errmsg, e.message, e.args, e.response

pprint(reply['result'])

