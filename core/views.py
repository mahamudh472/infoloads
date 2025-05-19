from django.shortcuts import render, get_object_or_404, redirect
from downloads.models import App, Platform, Category
from django.http import JsonResponse


# Create your views here.

def cron_job_trigger(request):
    return JsonResponse({'status': 'success'})
def index(request):
    apps = App.objects.all()
    context = {
        'apps': apps,
        'page_title': 'Home',
    }
    return render(request, 'index.html', context)

def app_details(request, slug):
    app = get_object_or_404(App, slug=slug)
    suggestions = App.objects.exclude(id=app.id).order_by('?')[:10]
    return render(request, 'downloads/app_details.html', {
        'app': app,
        'suggestions': suggestions,
    })

def app_download(request, slug):
    app = get_object_or_404(App, slug=slug)
    app.downloads += 1
    app.save()

    return redirect(app.file_url)


def search_results(request):
    q = request.GET.get('q', None)
    apps = App.objects.filter(name__icontains=q)

    context = {
        'q': q,
        'apps': apps
    }
    return render(request, 'core/search_result.html', context)

def category_details(request, category_name, platform=0):
    if bool(platform):
        category = Platform.objects.get(name=category_name)
        apps = App.objects.filter(platform=category)
        context = {
            'category_name': category_name, 'apps': apps
        }
        return render(request, 'downloads/category_details.html', context)

    category = Category.objects.get(name=category_name)
    apps = Category.objects.filter(category=category)
    context = {
        'category_name': category_name, 'apps': apps
    }
    return render(request, 'downloads/category_details.html', context)
