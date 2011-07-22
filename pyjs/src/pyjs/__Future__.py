

class __Future__(object):
    division = False

    def import_division(self, translator):
        self.division = True
        translator.op_names2['/'] = 'op_truediv'
