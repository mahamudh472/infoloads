from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from downloads.models import App, Category, Platform

# Static URLs
class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return ["core:index", "core:search_results"]

    def location(self, item):
        return reverse(item)


# App Detail URLs
class AppDetailSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return App.objects.all().order_by('id')

    def location(self, obj):
        return reverse("core:app_details", args=[obj.slug])


# Category + Platform URLs
class CategoryDetailSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        # Only include entries where both category and platform exist
        return App.objects.exclude(category__isnull=True).exclude(platform__isnull=True).values_list(
            'category__name', 'platform__id'
        ).distinct()

    def location(self, item):
        category_name, platform_id = item
        return reverse("core:category_details", args=[category_name, platform_id])
