from django.shortcuts import render
from downloads.models import App 
# Create your views here.

def index(request):
    apps = App.objects.all()
    context = {
        'apps': apps
    }
    return render(request, 'index.html', context)

def app_details(request, slug):
    return render(request, 'downloads/app_details.html')

def app_download(request, slug):
    pass