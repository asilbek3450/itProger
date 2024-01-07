from django.shortcuts import render, get_object_or_404, redirect

from blog.forms import CommentForm
from blog.models import BlogPost, BlogComment, BlogCategory


# Create your views here.
def index(request):
    blog_posts = BlogPost.objects.all()
    categories = BlogCategory.objects.all()
    context = {
        'blog_posts': blog_posts,
        'categories': categories,
    }
    return render(request, 'blog/index.html', context)


def blog_detail(request, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug)
    latest_posts = BlogPost.objects.all().order_by('-created_at')[:3]
    comments = BlogComment.objects.filter(post=blog_post)
    add_comment_form = CommentForm(request.POST)
    if request.method == 'POST':
        if add_comment_form.is_valid():
            if not request.user.is_authenticated:
                return redirect('login')
            comment = add_comment_form.save(commit=False)
            comment.post = blog_post
            comment.user = request.user
            comment.save()
            return redirect('blog_detail', slug=slug)
    else:
        add_comment_form = CommentForm()

    context = {
        'blog_post': blog_post,
        'comments': comments,
        'add_comment_form': add_comment_form,
        'latest_posts': latest_posts,
    }
    return render(request, 'blog/detail.html', context)


def create_blog_post(request):
    pass


def categories_list(request):
    categories = BlogCategory.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'blog/categories.html', context)


def single_category(request, slug):
    categories = BlogCategory.objects.all()
    category = get_object_or_404(BlogCategory, slug=slug)
    blog_posts = BlogPost.objects.filter(category=category)
    context = {
        'categories': categories,
        'blog_posts': blog_posts,
        'category': category,
    }
    return render(request, 'blog/single_category.html', context)
