from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('', views.index, name="index"),
    path('apps/<str:slug>', views.app_details, name="app_details"),
    path('download/<str:slug>', views.app_download, name='app_download'),
    path('search', views.search_results, name="search_results")
]
