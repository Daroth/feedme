from django.contrib.admin import ModelAdmin, site
from django.db.models import CharField
from django.forms.widgets import TextInput

from apps.feeds.models import Section, Feed, Post


class SectionAdmin(ModelAdmin):
    list_display = ('name', 'total_feeds')
    ordering = ('name',)

    def total_feeds(self, obj):
        return obj.feed_set.count()


class FeedAdmin(ModelAdmin):
    formfield_overrides = {
        CharField: {'widget': TextInput(attrs={'size': '45'})},
    }
    fieldsets = (
        (None, {
            'fields': ('url', 'title', 'section'),
        }),
        ('More options', {
            'classes': ('collapse',),
            'fields': ('description', 'favicon'),
        }),
    )
    list_display = ('title', 'url', 'section', 'last_update')
    list_filter = ('section',)
    ordering = ('section',)
    search_fields = ('url', 'title', 'description', 'section__name')
    date_hierarchy = 'last_update'


class PostAdmin(ModelAdmin):
    def mark_as_read(self, request, queryset):
        self._mark(request, queryset, as_read=True)

    def mark_as_unread(self, request, queryset):
        self._mark(request, queryset, as_read=False)

    def _mark(self, request, queryset, as_read):
        rows_updated = queryset.update(is_read=as_read)
        suffix = "read" if as_read else "unread"
        self._send_status_msg(request, rows_updated,
                              "successfuly marked as "+suffix)

    def _send_status_msg(self, request, rows_updated, success_msg):
        message = ("1 post was " if (
            rows_updated == 1
        ) else "%d posts were " % rows_updated)
        message += success_msg
        self.message_user(request, message)

    fieldsets = (
        (None, {
            'fields': ('feed', 'title', 'is_read'),
        }),
        ('Details', {
            'classes': ('collapse',),
            'fields': ('link', 'summary'),
        }),
    )
    list_display = ('title', 'published', 'is_read', 'feed')
    list_filter = ('published', 'is_read')
    ordering = ('-published',)
    search_fields = ('link', 'title', 'summary', 'feed__url',
                     'feed__title', 'feed__description')
    actions = (mark_as_read, mark_as_unread)


site.register(Section, SectionAdmin)
site.register(Feed, FeedAdmin)
site.register(Post, PostAdmin)
