from django.urls import path
from . import views

urlpatterns = [
    path("",views.HomepageView.as_view(),name="home_page"),
    path("posts", views.AllpostView.as_view(),name="all_posts"),
    path("about",views.AboutView.as_view(),name="about"),
    path("post_detail/<slug:slug>",views.PostdetailView.as_view(),name="post_detail"),
    path("read_later", views.ReadlaterView.as_view(),name="read_later")
]