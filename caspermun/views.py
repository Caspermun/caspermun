from django.shortcuts import render, get_object_or_404
from caspermun.models import *
from core import settings


def index(request):
    main = Main.objects.first()
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


def smart_link(request, url):
    album = get_object_or_404(Album, url=url)
    album.views = album.views + 1
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
