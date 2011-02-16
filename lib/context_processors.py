import os

from django.conf import settings

from apps.feeds.models import Section


def static_files(request):
    return {
        'CSS': os.path.join(settings.MEDIA_URL, 'css'),
        'JS': os.path.join(settings.MEDIA_URL, 'js'),
        'MEDIA': os.path.join(settings.MEDIA_URL, 'media'),
    }

def debug_status(request):
    return {
        'DEBUG': settings.DEBUG,
    }

def sections_list(request):
    return {
        'SECTIONS': Section.objects.all(),
    }
