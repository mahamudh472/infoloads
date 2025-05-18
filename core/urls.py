from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('', views.index, name="index"),
    path('apps/<str:slug>', views.app_details, name="app_details"),
    path('download/<str:slug>', views.app_download, name='app_download'),
    path('search', views.search_results, name="search_results"),
    path('category_details/<str:category_name>/<int:platform>', views.category_details, name="category_details")
]

from django.conf import settings
from django.views.static import serve
from django.urls import re_path
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

urlpatterns += [
   re_path(r'^(.*\.js)$', serve, {
    'document_root': os.path.join(BASE_DIR, 'static'),
})
]


