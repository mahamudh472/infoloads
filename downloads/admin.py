from django.contrib import admin
from .models import App, Category, Review, Download
# Register your models here.

admin.site.register(App)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Download)
