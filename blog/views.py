from django.shortcuts import render, get_list_or_404
from .models import Post

def get_date(post):
    """To get the date of post"""
    return (post['date'])

# Create your views here.
def home_page(request):
    """Home page of blog"""
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/home_page.html",{
        'posts': latest_posts,
    })

def all_posts(request):
    "Present all the posts in collection"
    posts = Post.objects.all().order_by("-date")[:]
    return render(request,"blog/all_posts.html",{
        'posts': posts,
    })

def about(request):
    """About me"""
    return render(request,"blog/about.html")

def post_detail(request, slug):
    """Present a webpage with a selected post in detail."""
    selected_post = Post.objects.get(slug=slug)
    post_tags = selected_post.tags.all()
    return render(request, "blog/post_detail.html", {
        'post': selected_post,
        'post_tags': post_tags
    })
