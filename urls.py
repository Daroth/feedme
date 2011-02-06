from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

import apps.feeds.urls

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin_tools/', include('admin_tools.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^', include(apps.feeds.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        })
    )
