from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'author/dashboard.html')

def app_list(request):
    return render(request, 'author/app_list.html')

def collections(request):
    return render(request, 'author/collections.html')

def manage_app_versions(request):
    return render(request, 'author/manage_app_versions.html')

