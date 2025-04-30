from django.db import models
from autoslug import AutoSlugField
# Create your models here.

class App(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', unique=True)
    description = models.TextField()
    version = models.CharField(max_length=10)
    file = models.FileField(upload_to='downloads/')
    image = models.ImageField(upload_to='app_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    size = models.CharField(max_length=20)
    downloads = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

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
