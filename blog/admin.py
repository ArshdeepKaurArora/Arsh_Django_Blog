from django.contrib import admin
from datetime import date
from .models import Post, Author, Tag, Comment

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "author", "date",)
    list_filter = ("author","date","tags",)

class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "text", "post")

# Register your models here.

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)