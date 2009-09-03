
class I18N(object):
    def example(self):
        return "This is a domain example"

import I18N as parent
i18n = type('I18N', (I18N, parent.I18N), {})()
