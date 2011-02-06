from django.conf.urls.defaults import patterns
from django.views.generic.list_detail import object_detail


urlpatterns = patterns('apps.feeds.views',
    #(r'^$', 'index'),
    (r'^section/(?P<section_id>[0-9]+)$', 'section'),
    (r'^feed/(?P<feed_id>[0-9]+)$', 'feed'),
    (r'^feed/(?P<feed_id>[0-9]+)/update$', 'update_feed'),
    (r'^update$', 'update_all'),
    (r'^read$', 'mark_as_read'),
)

# url patterns for generic views
urlpatterns += patterns('django.views.generic',
    (r'^$', 'simple.direct_to_template', {'template': 'feeds/index.html'}),
)

# index: use direct_to_template
# section: use object_detail
# feed: use object_detail
