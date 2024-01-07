from django.urls import path

from .views import index, blog_detail, single_category

urlpatterns = [

    path('', index, name='blog_list'),
    path('<str:slug>/', blog_detail, name='blog_detail'),
    path('category/<str:slug>/', single_category, name='single_category'),
]
