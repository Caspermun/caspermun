from django.shortcuts import render, get_object_or_404
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
    album = get_object_or_404(Album, url=url)
    album.views = album.views + 1
    album.save()
    index = IndexPage.objects.first()

    context = {
        'album': album,
        'index': index,
    }
    return render(request, 'pages/smart_link.html', context)
