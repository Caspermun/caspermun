from django.shortcuts import render, get_object_or_404
from caspermun.models import *
from core import settings
import mutagen


def index(request):
    main = Main.objects.first()
    main.views += 1
    main.save()
    about = About.objects.first()
    contacts = Contacts.objects.first()
    albums = Album.objects.all()

    context = {
        'main': main,
        'about': about,
        'contacts': contacts,
        'albums': albums,
    }
    return render(request, 'index.html', context)


def album_detail(request, url):
    album = get_object_or_404(Album, url=url)
    tracks = Track.objects.filter(album=album)
    context = {
        'album': album,
        'tracks': tracks,
    }
    return render(request, 'pages/track_detail.html', context)


def smart_link(request, url):
    album = get_object_or_404(Album, url=url)
    album.views += 1
    album.save()
    main = Main.objects.first()
    contacts = Contacts.objects.first()

    context = {
        'album': album,
        'main': main,
        'contacts': contacts,
    }
    return render(request, 'pages/smart_link.html', context)


def error_404(request, exception):
    return index(request)
