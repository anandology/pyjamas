import os
import sys

#Calculate the path based on the location of the WSGI script.
apache_configuration= os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)
#workspace = os.path.dirname(project)
sys.path.append(project)
sys.path.append(apache_configuration)


os.environ['DJANGO_SETTINGS_MODULE'] = 'djangowanted.formssettings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
