from caspermun.models import *


def base(request):
    main = Main.objects.first()

    context = {
        'main': main,
    }

    return context
