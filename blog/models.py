from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator

# Create your models here.
class Post(models.Model):
    """To create a model of post"""
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=250)
    image_name = models.ImageField(upload_to="images", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True,default="",null=False,db_index=True)
    content = models.TextField(validators=[MinLengthValidator(250)])
    author = models.ForeignKey("Author", null=True,
                               on_delete=models.SET_NULL, related_name="posts")
    tags = models.ManyToManyField("Tag", related_name="posts")

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    def __str__(self):
        return f"{self.title}"

class Author(models.Model):
    """To create a model of author"""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Tag(models.Model):
    """To create a model of tag."""
    tag = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.tag}"
    
class Comment(models.Model):
    """To create a model for collecting comments."""
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)
    text = models.TextField(max_length=400)
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="comments")
    initials = models.CharField(max_length=5,null=True)
    color = models.CharField(max_length=50,null=True)
