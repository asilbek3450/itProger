from django.shortcuts import render, get_object_or_404, redirect

from blog.forms import CommentForm
from blog.models import BlogPost, BlogComment


# Create your views here.
def index(request):
    blog_posts = BlogPost.objects.all()
    context = {
        'blog_posts': blog_posts,
    }
    return render(request, 'blog/index.html', context)


def blog_detail(request, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug)
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
        'add_comment_form': add_comment_form
    }
    return render(request, 'blog/detail.html', context)
