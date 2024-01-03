from django.urls import path

from .views import user_login, user_logout, user_signup

urlpatterns = [

    path('register/', user_signup, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
