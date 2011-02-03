from django.db import models


class Section(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Feed(models.Model):
    url = models.URLField(unique=True)
    favicon = models.URLField(blank=True)
    last_update = models.DateTimeField(auto_now=True)
    title = models.CharField(unique=True, max_length=50)
    description = models.CharField(max_length=150, blank=True, null=True)
    section = models.ForeignKey(Section)

    def __unicode__(self):
        return self.url


class Post(models.Model):
    feed = models.ForeignKey(Feed, to_field='title')
    link = models.URLField(unique=True, verify_exists=False)
    title = models.CharField(max_length=150)
    summary = models.TextField(unique=True)
    published = models.DateTimeField(blank=True)
    is_read = models.BooleanField()

    def __unicode__(self):
        return self.title
