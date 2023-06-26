from django.db import models
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    """Create a table for posts."""
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=250)
    image_name = models.CharField(max_length=100)
    date = models.CharField(max_length=20)
    slug = models.CharField(max_length=100)
    content = models.CharField(max_length=500)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)
