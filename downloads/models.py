from django.db import models
from autoslug import AutoSlugField
# Create your models here.

class Platform(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):

        return f"/platforms/{self.slug}/"



class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' → '.join(full_path[::-1])

    def get_ancestors(self):
        ancestors = []
        category = self
        while category:
            ancestors.insert(0, category)  # insert at beginning
            category = category.parent
        return ancestors
    
class App(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', unique=True)
    description = models.TextField()
    version = models.CharField(max_length=10)
    file_url = models.URLField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    platform = models.ForeignKey(Platform, on_delete=models.SET_NULL, blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)
    license = models.CharField(max_length=50, blank=True, null=True)
    os = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    size = models.CharField(max_length=20)
    downloads = models.IntegerField(default=0)
    category = models.ForeignKey(Category, related_name="apps", blank=True, null=True, on_delete=models.SET_NULL)
    app_type = models.CharField(max_length=50, choices=[('app', 'app'), ('game', 'game')])

    def __str__(self):
        return self.name
    
class Download(models.Model):
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    user_ip = models.GenericIPAddressField()
    date_downloaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.app.name} downloaded by {self.user_ip}"
    
class Review(models.Model):
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    user_ip = models.GenericIPAddressField()
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.app.name} by {self.user_ip}"
