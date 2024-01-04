from django.shortcuts import render, get_object_or_404

from blog.models import BlogPost


# Create your views here.
def index(request):
    blog_posts = BlogPost.objects.all()
    context = {
        'blog_posts': blog_posts,
    }
    return render(request, 'blog/index.html', context)


def blog_detail(request, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug)
    context = {
        'blog_post': blog_post
    }
    return render(request, 'blog/detail.html', context)
