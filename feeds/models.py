from django.db.models import *


class Section(Model):
    name = CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Feed(Model):
    url = URLField(unique=True)
    favicon = URLField(blank=True)
    last_update = DateTimeField(auto_now=True)
    title = CharField(unique=True, max_length=50)
    description = CharField(max_length=150, null=True, blank=True)
    section = ForeignKey(Section)

    def __unicode__(self):
        return self.url


class Post(Model):
    feed = ForeignKey(Feed, to_field='title')
    link = URLField(unique=True, verify_exists=False)
    title = CharField(max_length=200)
    summary = TextField(unique=True)
    published = DateTimeField(blank=True)
    is_read = BooleanField()

    def __unicode__(self):
        return self.title

