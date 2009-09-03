
import I18N.domain.subdomain as parent

class I18N(parent.I18N):
    def example(self):
        return "This is a subdomain en_US example"

parent.i18n = I18N()
