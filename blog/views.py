from datetime import date
from django.shortcuts import render

posts = [
    {
        "slug": 'Mountains',
        "image": "blog/images/mountain_post_image.jpg",
        "date": date.today().strftime("%B %d, %Y"),
        "title": "Mountains",
        "author": "Arshdeep Kaur",
        "excerpt": "I love mountains. Whenever I visit hill side area it makes me feel the beauty of nature.Every nature being welcom with an open arm.",
        "content": """Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sunt, itaque magni minus, error commodi maiores
        natus quo officia sed nisi nesciunt in aspernatur placeat consectetur unde velit architecto mollitia aut.

        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sunt, itaque magni minus, error commodi maiores
        natus quo officia sed nisi nesciunt in aspernatur placeat consectetur unde velit architecto mollitia aut.
        
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sunt, itaque magni minus, error commodi maiores
        natus quo officia sed nisi nesciunt in aspernatur placeat consectetur unde velit architecto mollitia aut."""
    },
    {
        "slug": 'Mountains',
        "image": "blog/images/mountain_post_image.jpg",
        "date": date.today().strftime("%B %d, %Y"),
        "title": "Mountains",
        "author": "Arshdeep Kaur",
        "excerpt": "I love mountains. Whenever I visit hill side area it makes me feel the beauty of nature.Every nature being welcom with an open arm.",
        "content": """Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sunt, itaque magni minus, error commodi maiores
        natus quo officia sed nisi nesciunt in aspernatur placeat consectetur unde velit architecto mollitia aut.

        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sunt, itaque magni minus, error commodi maiores
        natus quo officia sed nisi nesciunt in aspernatur placeat consectetur unde velit architecto mollitia aut.
        
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sunt, itaque magni minus, error commodi maiores
        natus quo officia sed nisi nesciunt in aspernatur placeat consectetur unde velit architecto mollitia aut."""
    },
    {
        "slug": 'Mountains',
        "image": "blog/images/mountain_post_image.jpg",
        "date": date.today().strftime("%B %d, %Y"),
        "title": "Mountains",
        "author": "Arshdeep Kaur",
        "excerpt": "I love mountains. Whenever I visit hill side area it makes me feel the beauty of nature.Every nature being welcom with an open arm.",
        "content": """Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sunt, itaque magni minus, error commodi maiores
        natus quo officia sed nisi nesciunt in aspernatur placeat consectetur unde velit architecto mollitia aut.

        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sunt, itaque magni minus, error commodi maiores
        natus quo officia sed nisi nesciunt in aspernatur placeat consectetur unde velit architecto mollitia aut.
        
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sunt, itaque magni minus, error commodi maiores
        natus quo officia sed nisi nesciunt in aspernatur placeat consectetur unde velit architecto mollitia aut."""
    },
    {
        "slug": 'Mountains',
        "image": "blog/images/mountain_post_image.jpg",
        "date": date.today().strftime("%B %d, %Y"),
        "title": "Mountains",
        "author": "Arshdeep Kaur",
        "excerpt": "I love mountains. Whenever I visit hill side area it makes me feel the beauty of nature.Every nature being welcom with an open arm.",
        "content": """Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sunt, itaque magni minus, error commodi maiores
        natus quo officia sed nisi nesciunt in aspernatur placeat consectetur unde velit architecto mollitia aut.

        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sunt, itaque magni minus, error commodi maiores
        natus quo officia sed nisi nesciunt in aspernatur placeat consectetur unde velit architecto mollitia aut.
        
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sunt, itaque magni minus, error commodi maiores
        natus quo officia sed nisi nesciunt in aspernatur placeat consectetur unde velit architecto mollitia aut."""
    },
    {
        "slug": 'Mountains',
        "image": "blog/images/mountain_post_image.jpg",
        "date": date.today().strftime("%B %d, %Y"),
        "title": "Mountains",
        "author": "Arshdeep Kaur",
        "excerpt": "I love mountains. Whenever I visit hill side area it makes me feel the beauty of nature.Every nature being welcom with an open arm.",
        "content": """Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sunt, itaque magni minus, error commodi maiores
        natus quo officia sed nisi nesciunt in aspernatur placeat consectetur unde velit architecto mollitia aut.

        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sunt, itaque magni minus, error commodi maiores
        natus quo officia sed nisi nesciunt in aspernatur placeat consectetur unde velit architecto mollitia aut.
        
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sunt, itaque magni minus, error commodi maiores
        natus quo officia sed nisi nesciunt in aspernatur placeat consectetur unde velit architecto mollitia aut."""
    }
]

def get_date(post):
    """To get the date of post"""
    return (post['date'])

# Create your views here.
def home_page(request):
    """Home page of blog"""
    sort_posts = sorted(posts, key=get_date)
    latest_posts = sort_posts[-3:]
    return render(request, "blog/home_page.html",{
        'posts': latest_posts
    })

def all_posts(request):
    "Present all the posts in collection"
    sort_posts = sorted(posts, key=get_date)
    return render(request,"blog/all_posts.html",{
        'posts': sort_posts,
    })

def about(request):
    """About me"""
    return render(request,"blog/about.html")

def post_detail(request, slug):
    """Present a webpage with a selected post in detail."""
    selected_post = next(post for post in posts if post['slug'] == slug)
    return render(request, "blog/post_detail.html", {
        'post': selected_post
    })
