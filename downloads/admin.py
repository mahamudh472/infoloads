from django.contrib import admin
from .models import App, Category, Review, Download, Platform, AppVersion
# Register your models here.

class AppVersionInline(admin.StackedInline):
    model = AppVersion

@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    inlines = [AppVersionInline]
    extras = 1

admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Download)
admin.site.register(Platform)
