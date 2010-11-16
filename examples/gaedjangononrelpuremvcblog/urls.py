from django.conf.urls.defaults import *
import os
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media/output')

urlpatterns = patterns('',
    (r'^$', 'post.views.index'),
    (r'^services/$', 'post.views.service'),
    (r'^(?P<path>.*)$', 'django.views.static.serve',
			{'document_root': MEDIA_ROOT,
             'show_indexes': True}),
)
