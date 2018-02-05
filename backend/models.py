from django.db import models

# Create your models here.
class Story(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='story_images',blank=True)
    
