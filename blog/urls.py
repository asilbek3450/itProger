from django.urls import path

from .views import index, blog_detail

urlpatterns = [

    path('', index, name='blog_list'),
    path('<slug:slug>/', blog_detail, name='blog_detail'),

]
