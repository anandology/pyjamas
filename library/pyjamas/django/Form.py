""" Pyjamas Django Forms Integration

    Copyright (C) 2009 Luke Kenneth Casson Leighton <lkcl@lkcl.net>

"""

from pyjamas.ui.TextBox import TextBox
from pyjamas.ui.Grid import Grid
from pyjamas.ui.Composite import Composite
from pyjamas.log import writebr

class FormDescribeGrid:

    def __init__(self, grid):
        self.grid = grid

    def onRemoteResponse(self,  response, request_info):

        method = request_info.method

        writebr(repr(response))

        self.do_describe(response)

    def do_describe(self, fields):

        self.grid.resize(len(fields), 2)
        idx = 0
        for fname in fields.keys():
            field = fields[fname]
            self.grid.setHTML(idx, 0, field['label'])

class Form(Composite):

    def __init__(self, svc, **kwargs):

        Composite.__init__(self, **kwargs)
        self.svc = svc
        self.grid = Grid()
        self.initWidget(self.grid)
        self.describe = FormDescribeGrid(self.grid)
        self.svc({}, {'describe': None}, self.describe)

