from django.http import HttpResponse

from lib.helpers import render_to


@render_to('feeds/index.html')
def index(request):
    return {'content': "Hello World!"}
