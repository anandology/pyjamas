

class I18N(object):
    def example(self):
        return "This is a domain en_US example"

import I18N.en_US as parent
import I18N.domain as dom
dom.i18n = type('I18N', (I18N, dom.I18N, parent.I18N), {})()
