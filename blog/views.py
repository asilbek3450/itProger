from django.http import HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from blog.forms import CommentForm, CreateBlogForm, CreateCategoryForm, UpdateBlogForm
from blog.models import BlogPost, BlogComment, BlogCategory


# Create your views here.
def index(request):
    blog_posts = BlogPost.objects.all().order_by('-created_at')
    categories = BlogCategory.objects.all()
    context = {
        'blog_posts': blog_posts,
        'categories': categories,
    }
    return render(request, 'blog/index.html', context)


def blog_detail(request, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug)
    categories = BlogCategory.objects.all()
    latest_posts = BlogPost.objects.all().order_by('-created_at')[:3]
    comments = BlogComment.objects.filter(post=blog_post)
    add_comment_form = CommentForm(request.POST)

    # count of views this post by users and session will be expired after one week
    if not request.session.get('has_viewed_%s' % blog_post.id):
        blog_post.view_count += 1
        blog_post.save()
        request.session['has_viewed_%s' % blog_post.id] = True

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
        'categories': categories,
        'comments': comments,
        'add_comment_form': add_comment_form,
        'latest_posts': latest_posts,
    }
    return render(request, 'blog/blog_detail.html', context)


def categories_list(request):
    categories = BlogCategory.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'blog/categories.html', context)


def single_category(request, slug):
    categories = BlogCategory.objects.all()
    category = get_object_or_404(BlogCategory, slug=slug)
    blog_posts = BlogPost.objects.filter(category=category).order_by('-created_at')
    context = {
        'categories': categories,
        'blog_posts': blog_posts,
        'category': category,
    }
    return render(request, 'blog/single_category.html', context)


def create_blog_post(request):
    if request.method == 'POST':
        form = CreateBlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.save()
            return redirect('blog_list')
    else:
        form = CreateBlogForm()
    context = {
        'form': form,
    }
    return render(request, 'blog/create_blog.html', context)


def update_blog_post(request, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug)
    if request.method == 'POST':
        form = UpdateBlogForm(request.POST, request.FILES, instance=blog_post)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = UpdateBlogForm(instance=blog_post)
    context = {
        'form': form,
    }
    return render(request, 'blog/update_blog.html', context)


def create_category(request):
    if request.method == 'POST':
        form = CreateCategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('blog_list')
    else:
        form = CreateCategoryForm()
    context = {
        'form': form,
    }
    return render(request, 'blog/create_category.html', context)

