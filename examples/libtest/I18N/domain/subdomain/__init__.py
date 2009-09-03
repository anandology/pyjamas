

class I18N(object):
    def example(self):
        return "This is a subdomain example"

import I18N.domain as parent
i18n = type('I18N', (I18N, parent.I18N), {})()
