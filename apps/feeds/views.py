from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from apps.feeds.forms import MarkAsRead
from apps.feeds.models import Feed, Post

from datetime import datetime
from time import mktime

import feedparser


def mark_as_read(request):
    if request.method == 'POST':
        form = MarkAsRead(request.POST)
        if form.is_valid():
            post = get_object_or_404(Post, pk=form.cleaned_data['post_id'])
            if not post.is_read:
                post.is_read = True
                post.save()
    return HttpResponseRedirect('/')

def update_all(request):
    for feed in Feed.objects.all():
        parsed = feedparser.parse(feed.url)
        if parsed.feed.description and (feed.description is None):
            feed.description = parsed.feed.description
            feed.save()
        for entry in parsed.entries:
            try:
                if hasattr(entry, 'updated_parsed'):
                    pubdate = datetime.fromtimestamp(mktime(entry.updated_parsed))
                else:
                    pubdate = None
                post = Post(
                    feed=feed,
                    link=entry.link,
                    title=entry.title,
                    summary=entry.summary,
                    published=pubdate,
                    is_read=False,
                )
                post.save()
            except IntegrityError:
                pass
    return HttpResponseRedirect('/')

def update_feed(request, feed_id):
    return HttpResponseRedirect('/')
