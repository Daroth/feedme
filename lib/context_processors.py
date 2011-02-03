import os

from django.conf import settings


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
