from django.urls import path
from . import views
from django.conf import settings
from django.views.static import serve
from django.urls import re_path
import os
from django.contrib.sitemaps.views import sitemap
from .sitemaps import AppDetailSitemap, AppDownloadSitemap, CategoryDetailSitemap, StaticViewSitemap

app_name = "core"

sitemaps_dict = {
    'static': StaticViewSitemap,
    'apps': AppDetailSitemap,
    'downloads': AppDownloadSitemap,
    'categories': CategoryDetailSitemap,
}
from django.views.decorators.http import require_GET

@require_GET
def sitemap_view(request):
    return sitemap(request, sitemaps=sitemaps_dict, content_type="application/xml")

urlpatterns = [
    path('', views.index, name="index"),
    path('refresh', views.cron_job_trigger, name="refresh"),
    path('apps/<str:slug>', views.app_details, name="app_details"),
    path('download/<str:slug>', views.app_download, name='app_download'),
    path('search', views.search_results, name="search_results"),
    path('category_details/<str:category_name>/<int:platform>', views.category_details, name="category_details"),
    path("sitemap.xml", sitemap_view, name="sitemap"),
]


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

urlpatterns += [
   re_path(r'^(.*\.js)$', serve, {
    'document_root': os.path.join(BASE_DIR, 'static'),
})
]


