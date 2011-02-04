from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from lib.helpers import render_to
from apps.feeds.forms import MarkAsRead
from apps.feeds.models import Section, Feed, Post

from datetime import datetime
from time import mktime

import feedparser


@render_to('feeds/index.html')
def index(request):
    feeds = Feed.objects.all()
    sections = Section.objects.all()
    return {
        'feeds': feeds,
        'sections': sections,
    }

@render_to('feeds/section.html')
def section(request, section_id):
    section = get_object_or_404(Section, pk=section_id)
    feeds = Feed.objects.filter(section=section_id)
    sections = Section.objects.all()
    return {
        'section': section,
        'feeds': feeds,
        'sections': sections,
    }

@render_to('feeds/feed.html')
def feed(request, feed_id):
    feed = get_object_or_404(Feed, pk=feed_id)
    feeds = Feed.objects.all()
    sections = Section.objects.all()
    return {
        'feeds': feeds,
        'sections': sections,
    }

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
                pubdate = datetime.fromtimestamp(mktime(entry.updated_parsed))
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
