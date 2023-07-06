from django.shortcuts import render, get_list_or_404
from .models import Post
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views import View
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from random import randint


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
    def initials(self, comment):
        name_splits = comment.name.split()
        initials = ""
        for split in name_splits:
            initials += split[0].upper()
        return initials
    
    def random_color(self):
        color = f"rgb{randint(0,255),randint(0,255),randint(0,255)}"
        return color

    def get(self,request,slug):
        post = Post.objects.get(slug=slug)
        read_later_posts = request.session.get("read_later_posts")
        comments= post.comments.all().order_by("-id")
        print(self.random_color())
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": comments,
            "read_later": True,
        }
        if read_later_posts:
            if post.id in read_later_posts:
                context['read_later'] = False
        return render(request,"blog/post_detail.html",context)
    
    def post(self,request,slug):
        post = Post.objects.get(slug=slug)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.initials = self.initials(comment)
            comment.color = self.random_color()
            comment.save()
            redirect_path = reverse("post_detail", args=[slug])
            return HttpResponseRedirect(redirect_path)
        comments = post.comments.all().order_by('-id')
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": comments,
        }
        return render(request, "blog/post_detail.html", context)
    
class ReadlaterView(View):
    """Return all posts collected in Readlater list"""
    def get(self, request):
        read_later_posts = request.session.get("read_later_posts")
        if not read_later_posts is None and len(read_later_posts) != 0:
            posts = Post.objects.filter(id__in=read_later_posts)
            context = {
                "posts": posts,
                "not_null": True
            }
        else:
            context = {
                "not_null": False
            }
        return render(request, "blog/read_later.html", context)

    def post(self, request):
        read_later_posts = request.session.get("read_later_posts")

        if read_later_posts is None:
            read_later_posts = []

        post_id = int(request.POST["post_id"])
        if post_id not in read_later_posts:
            read_later_posts.append(post_id)
        else:
            read_later_posts.remove(post_id)
        request.session["read_later_posts"] = read_later_posts
        redirect_path = reverse("read_later")
        return HttpResponseRedirect(redirect_path)

class ContactView(View):
    """Return contact page on blog"""
    def get(self,request):
        return render(request, "blog/contact.html")
