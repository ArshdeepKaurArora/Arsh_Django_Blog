from django.shortcuts import render, get_list_or_404
from .models import Post
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views import View
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def get_date(post):
    """To get the date of post"""
    return (post['date'])

# Create your views here.
class HomepageView(ListView):
    """To return homepage of blog"""
    template_name = "blog/home_page.html"
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        selected_posts = Post.objects.all().order_by("-date")[:3]
        context["posts"] = selected_posts
        return context

class AllpostView(ListView):
    """Return all posts collected in post model"""
    model = Post
    template_name = "blog/all_posts.html"
    ordering = ["-date"]
    context_object_name = "posts"

class AboutView(TemplateView):
    """Return about page on blog"""
    template_name = "blog/about.html"

class PostdetailView(View):
    """Return a page with particular post in detail."""
    def get(self,request,slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id")
        }
        return render(request,"blog/post_detail.html",context)
    
    def post(self,request,slug):
        post = Post.objects.get(slug=slug)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            redirect_path = reverse("post_detail", args=[slug])
            return HttpResponseRedirect(redirect_path)
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by('-id')
        }
        return render(request, "blog/post_detail.html", context)
