from django.shortcuts import render
from caspermun.models import *


def index(request):
    index = IndexPage.objects.first()
    albums = Album.objects.all()

    context = {
        'index': index,
        'albums': albums,
    }
    return render(request, 'index.html', context)


def smart_link(request, url):
    try:
        album = Album.objects.get(url=url)
    except Album.DoesNotExist:
        album = None
    index = IndexPage.objects.first()

    context = {
        'album': album,
        'index': index,
    }
    return render(request, 'pages/smart_link.html', context)
