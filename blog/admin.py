from django.contrib import admin

from .models import BlogPost, BlogCategory, BlogComment

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(BlogCategory)
admin.site.register(BlogComment)
