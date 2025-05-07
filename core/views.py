from django.shortcuts import render
from downloads.models import App 
# Create your views here.

def index(request):
    apps = App.objects.all()
    context = {
        'apps': apps,
        'page_title': 'Home',
    }
    return render(request, 'index.html', context)

def app_details(request, slug):
    app = App.objects.get(slug=slug)
    return render(request, 'downloads/app_details.html', {'app': app})

def app_download(request, slug):
    pass

def search_results(request):
    q = request.GET.get('q', None)
    apps = App.objects.filter(name__icontains=q)

    context = {
        'q': q,
        'apps': apps
    }
    return render(request, 'core/search_result.html', context)