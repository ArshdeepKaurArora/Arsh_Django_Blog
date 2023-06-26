from django.urls import path
from . import views

urlpatterns = [
    path("",views.home_page,name="home_page"),
    path("posts", views.all_posts,name="all_posts"),
    path("about",views.about,name="about"),
    path("post_detail/<slug:slug>",views.post_detail,name="post_detail")
]