from django.shortcuts import render, get_object_or_404, redirect
from downloads.models import App, Platform, Category, Download
from django.http import JsonResponse
from django.core.paginator import Paginator
from core.models import Blog
from ipware import get_client_ip


# Create your views here.

def cron_job_trigger(request):
    return JsonResponse({'status': 'success'})
def index(request):
    trending_apps = App.objects.filter(app_type="app")[:6]
    trending_games = App.objects.filter(app_type="game")[:6]
    context = {
        'trending_apps': trending_apps,
        'trending_games': trending_games,
        'page_title': 'Home',
    }
    return render(request, 'index.html', context)

def app_details(request, slug):
    app = get_object_or_404(App, slug=slug)
    suggestions = App.objects.exclude(id=app.id).order_by('?')[:10]
    print(get_client_ip(request)[0])
    return render(request, 'downloads/app_details.html', {
        'app': app,
        'suggestions': suggestions,
    })

def app_download(request, slug):
    app = get_object_or_404(App, slug=slug)
    app.downloads += 1
    app.save()

    # Add download history
    Download.objects.create(
        app=app,
        user_ip=get_client_ip(request)[0]
    )

    return redirect(app.file_url)


def search_results(request):
    q = request.GET.get('q', None)
    apps = App.objects.filter(name__icontains=q)

    paginator = Paginator(apps, 10)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(int(page_num))
    context = {
        'q': q,
        'page_obj': page_obj
    }
    return render(request, 'core/search_result.html', context)

def category_details(request, category_name, platform=0):
    if category_name == "apps":
        apps = App.objects.filter(app_type='app')
        category_name = ""
        app_type = 'Apps'
    elif category_name == "games":
        apps = App.objects.filter(app_type="game")
        category_name = ""
        app_type = 'Games'
    elif bool(platform):
        category = Platform.objects.get(name=category_name)
        apps = App.objects.filter(platform=category)
        app_type = False
    else:
        category = Category.objects.get(name=category_name)
        apps = Category.objects.filter(category=category)
        app_type = False

    paginator = Paginator(apps, 10)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(int(page_num))
    context = {
        'category_name': category_name,
        'page_obj': page_obj,
        'app_type': app_type
    }
    return render(request, 'downloads/category_details.html', context)

def blog_list(request):
    blogs = Blog.objects.all()

    context = {
        'blogs': blogs
    }
    return render(request, 'news/blog_list.html', context)

def blog_details(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    context = {
        'blog': blog
    }
    return render(request, 'news/blog_details.html', context)