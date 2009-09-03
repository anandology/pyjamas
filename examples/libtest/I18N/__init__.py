

class I18N(object):
    def example(self):
        return "This is an example"
    def another_example(self):
        return "This is another example"

i18n = I18N()
locale = 'en'
domains = []

import domain
domains.append('domain')
import domain.subdomain
domains.append('domain.subdomain')

def set_locale(loc):
    global i18n
    try:
        path = "I18N.%s" % loc
        c = __import__(path)
    except ImportError, e:
        print "Failed to import %s" % e
    domains.sort()
    for domain in domains:
        try:
            path = "I18N.%s.%s" % (domain, loc)
            __import__(path)
        except ImportError, e:
            print "Failed to import %s" % e

