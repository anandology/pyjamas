""" Pyjamas Django Forms Integration

    Copyright (C) 2009 Luke Kenneth Casson Leighton <lkcl@lkcl.net>

"""

from pyjamas.ui.TextBox import TextBox
from pyjamas.ui.Grid import Grid

class Form:

    def __init__(self, svc):

        self.svc = svc
        self.grid = Grid()
        self.svc({}, {'describe': None}, self)

    def onRemoteResponse(self,  response, request_info):

        method = request_info.method

        if method == 'describe':
            self.describe(response)

    def describe(self, fields):

        self.grid.resize(len(fields), 2)
        idx = 0
        for fname in fields.keys():
            field = fields[fname]
            self.grid.setHTML(idx, 0, field['label'])
