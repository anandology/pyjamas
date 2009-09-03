

class I18N(object):
    def example(self):
        return "This is a subdomain en_US example"

import I18N.domain as parent
import I18N.domain.subdomain as dom
dom.i18n = type('I18N', (I18N, dom.I18N, parent.I18N), {})()
