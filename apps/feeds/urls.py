from django.conf.urls.defaults import patterns

urlpatterns = patterns('apps.feeds.views',
    (r'^$', 'index'),
)
