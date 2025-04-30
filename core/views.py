from django.shortcuts import render
from downloads.models import App 
# Create your views here.
def index(request):
    apps = App.objects.all()
    context = {
        'apps': apps
    }
    return render(request, 'index.html', context)