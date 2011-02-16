from django.conf.urls.defaults import patterns
from django.views.generic.list_detail import object_detail

from apps.feeds.models import Post, Feed, Section


urlpatterns = patterns('apps.feeds.views',
    (r'update$', 'update_all'),
    (r'read$', 'mark_as_read'),
)

# url patterns for generic views
urlpatterns += patterns('django.views.generic',
    (r'^$', 'simple.direct_to_template', {
        'template': 'feeds/index.html',
    }),
    (r'section/(?P<object_id>[0-9]+)$', 'list_detail.object_detail', {
        'queryset': Section.objects.all(),
        'template_object_name': 'section',
    }),
    (r'feed/(?P<object_id>[0-9]+)$', 'list_detail.object_detail', {
        'queryset': Feed.objects.all(),
        'template_object_name': 'feed',
    }),
    (r'post/(?P<object_id>[0-9]+)$', 'list_detail.object_detail', {
        'queryset': Post.objects.all(),
        'template_object_name': 'post',
    }),
)
