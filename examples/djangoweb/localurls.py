from django.conf.urls.defaults import *
from django.conf import settings

import os

STATIC = str(os.path.join(os.path.dirname(__file__), 'media/output/fckeditor').replace('\\','/'))

urlpatterns = patterns('',
		(r'^services/pages/$', 'djangoweb.webpages.views.service'),
		(r'^fckeditor/(?P<path>.*)$', 'django.views.static.serve',
			{'document_root': STATIC,
             'show_indexes': True}),
		(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
			{'document_root': settings.STATIC,
             'show_indexes': True}),
)
