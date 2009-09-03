
class I18N(object):
    def example(self):
        return "This is an en_US example"
    def another_example(self):
        return "This is en_US another example"

import I18N as parent
parent.i18n = type('I18N', (I18N, parent.I18N), {})()
