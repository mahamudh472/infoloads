from django.contrib import admin
from .models import App, Category, Review, Download, Platform, AppVersion
from django.utils.translation import gettext_lazy as _
from django.db.models import Q
# Register your models here.

class HasImageFilter(admin.SimpleListFilter):
    title = _('has image URL')
    parameter_name = 'has_image_url'
    def lookups(self, request, model_admin):
        return (
            ('yes', _('Yes')),
            ('no', _('No')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'yes':
            return queryset.exclude(image_url__isnull=True).exclude(image_url__exact='')
        if self.value() == 'no':
            return queryset.filter(Q(image_url__isnull=True) | Q(image_url__exact=''))

@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    list_filter = [HasImageFilter]
    search_fields = ['name']

admin.site.register(AppVersion)

admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Download)
admin.site.register(Platform)
