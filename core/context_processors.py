from downloads.models import Platform

def get_platforms(request):
    return {'platforms': Platform.objects.all()}