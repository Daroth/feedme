from django.forms import *
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from feeds.models import Feed, Post, Section

from datetime import datetime
from time import mktime

import feedparser


class MarkAsRead(Form):
    post_id = IntegerField()


def index(request):
    feeds_list = Feed.objects.all()
    sections_list = Section.objects.all()
    return render_to_response('feeds/index.html', {
        'feeds_list': feeds_list,
        'sections_list': sections_list,
    })

def update(request):
    for feed in Feed.objects.all():
        parsed = feedparser.parse(feed.url)
        if (not feed.description) and (parsed.feed.description != ''):
            feed.description = parsed.feed.description
        for post in parsed.entries:
            try:
                post_update = datetime.fromtimestamp(mktime(post.updated_parsed))
                new_post = Post(
                    feed=feed,
                    link=post.link,
                    title=post.title,
                    summary=post.summary,
                    published=post_update,
                    is_read=False,
                )
                new_post.save()
            except IntegrityError:
                pass
        feed.save()
    return HttpResponseRedirect('/')

def section(request, section_id):
    section = get_object_or_404(Section, pk=section_id)
    feeds_list = Feed.objects.filter(section=section_id)
    sections_list = Section.objects.all()
    return render_to_response('feeds/section.html', {
        'section': section,
        'feeds_list': feeds_list,
        'sections_list': sections_list,
    })

def feed(request, feed_id):
    feed = get_object_or_404(Feed, pk=feed_id)
    feeds_list = Feed.objects.all()
    sections_list = Section.objects.all()
    return render_to_response('feeds/feed.html', {

        'feeds_list': feeds_list,
        'sections_list': sections_list,
    })

def mark_as_read(request):
    if request.method == "POST":
        form = MarkAsRead(request.POST)
        if form.is_valid():
            post_id = form.cleaned_data['post_id']
            post = get_object_or_404(Post, pk=post_id)
            if not post.is_read:
                post.is_read = True
                post.save()
    return HttpResponseRedirect('/')
