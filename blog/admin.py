from django.contrib import admin
from datetime import date

from .models import Post, Author, Tag

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


# Register your models here.

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Tag)