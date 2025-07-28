from django.urls import path
from . import views

app_name = "author"

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('app-list', views.app_list, name="app_list"),
    path('collections', views.collections, name="collections"),
    path('manage-app-versions', views.manage_app_versions, name="manage_app_versions")
]