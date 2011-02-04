from django.conf.urls.defaults import patterns

urlpatterns = patterns('apps.feeds.views',
    (r'^$', 'index'),
    (r'^section/(?P<section_id>[0-9]+)$', 'section'),
    (r'^feed/(?P<feed_id>[0-9]+)$', 'feed'),
    (r'^feed/(?P<feed_id>[0-9]+)/update$', 'update_feed'),
    (r'^update$', 'update_all'),
    (r'^read$', 'mark_as_read'),
)
