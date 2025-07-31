from django.urls import path
from . import views
from django.conf import settings
from django.views.static import serve
from django.urls import re_path
import os
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from .sitemaps import AppDetailSitemap, AppDownloadSitemap, CategoryDetailSitemap, StaticViewSitemap

app_name = "core"

sitemaps_dict = {
    'static': StaticViewSitemap,
    'apps': AppDetailSitemap,
    'downloads': AppDownloadSitemap,
    'categories': CategoryDetailSitemap,
}

urlpatterns = [
    path('', views.index, name="index"),
    path('refresh/', views.cron_job_trigger, name="refresh"),
    path('apps/<str:slug>', views.app_details, name="app_details"),
    path('download/<str:slug>/<str:version>', views.app_download, name='app_download'),
    path('search', views.search_results, name="search_results"),
    path('category_details/<str:category_name>/<int:platform>', views.category_details, name="category_details"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps_dict}, name="sitemap"),
    path('blog', views.blog_list, name="blogs"),
    path('blog/<str:slug>', views.blog_details, name='blog_details')
]


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

urlpatterns += [
   re_path(r'^(.*\.js)$', serve, {
    'document_root': os.path.join(BASE_DIR, 'static'),
}),
    re_path(r'^ads.txt$', serve, {
        'path': 'ads.txt',
        'document_root': settings.STATIC_ROOT,
    }),
]


