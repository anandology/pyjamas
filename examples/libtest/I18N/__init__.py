

class I18N(object):
    def example(self):
        return "This is an example"
    def another_example(self):
        return "This is another example"

i18n = I18N()
locale = 'en'
domains = []

def add_domain(domain_name):
    global domains
    domains.append(domain_name)

import domain
add_domain('domain')
import domain.subdomain
add_domain('domain.subdomain')

def set_locale(loc):
    global i18n
    try:
        path = "I18N.%s" % loc
        m = __import__(path)
        m = getattr(m, loc)
        i18n = getattr(m, 'I18N')()
    except ImportError, e:
        print "Failed to import %s" % e
    domains.sort()
    for domain in domains:
        try:
            path = "I18N.%s.%s" % (domain, loc)
            __import__(path)
        except ImportError, e:
            print "Failed to import %s" % e
#set_locale("en_US")

