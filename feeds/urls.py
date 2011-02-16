from django.conf.urls.defaults import *

urlpatterns = patterns('feeds.views',
    (r'^$', 'index'),
    (r'^update/$', 'update'),
    (r'^section/(?P<section_id>[0-9]+)$', 'section'),
    (r'^feed/(?P<feed_id>[0-9]+)$', 'feed'),
    (r'^read$', 'mark_as_read'),
)
