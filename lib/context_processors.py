import os

from django.conf import settings


def static_files(request):
    return {
        'CSS': os.path.join(settings.MEDIA_ROOT, 'css'),
        'JS': os.path.join(settings.MEDIA_ROOT, 'js'),
        'MEDIA': os.path.join(settings.MEDIA_ROOT, 'media'),
    }

def debug_status(request):
    return {
        'DEBUG': settings.DEBUG,
    }
