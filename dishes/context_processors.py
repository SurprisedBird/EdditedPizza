from dishes.models import Size


def sizes(request):
    return {
       "sizes": Size.objects.all()
    }
