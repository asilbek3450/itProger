from django.urls import path

from .views import index, blog_detail, single_category, create_blog_post, create_category, update_blog_post

urlpatterns = [

    path('', index, name='blog_list'),
    path('create_blog/', create_blog_post, name='create_blog_post'),
    path('update_blog/<str:slug>/', update_blog_post, name='update_blog_post'),
    path('create_category/', create_category, name='create_category'),
    path('<str:slug>/', blog_detail, name='blog_detail'),
    path('category/<str:slug>/', single_category, name='single_category'),
]
