from django.contrib import admin
from django.db import models
from django.forms.widgets import TextInput
from feeds.models import Feed, Post, Section


class FeedAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'45'})}
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
    ordering = ('-section',)
    search_fields = ('url', 'title', 'description', 'section__name')


class PostAdmin(admin.ModelAdmin):

    def _send_status_msg(self, request, rows_updated, success_msg):
        message = "1 post was " if (rows_updated == 1) else "%d posts were " % rows_updated
        message += success_msg
        self.message_user(request, message)

    def mark_as_read(self, request, queryset):
        rows_updated = queryset.update(is_read=True)
        self._send_status_msg(request, rows_updated, "successfuly marked as read.")

    def mark_as_unread(self, request, queryset):
        rows_updated = queryset.update(is_read=False)
        self._send_status_msg(request, rows_updated, "successfuly marked as unread.")

    fieldsets = (
        (None, {
            'fields': ('feed', 'title', 'is_read'),
        }),
        ('Content', {
            'classes': ('collapse',),
            'fields': ('link', 'summary'),
        }),
    )
    list_display = ('title', 'published', 'is_read')
    list_filter = ('published', 'is_read')
    ordering = ('-published',)
    search_fields = ['link', 'title', 'summary', 'feed__url', 'feed__title', 'feed__description']
    actions = [mark_as_read, mark_as_unread]


admin.site.register(Section)
admin.site.register(Feed, FeedAdmin)
admin.site.register(Post, PostAdmin)
