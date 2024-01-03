from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserSignupForm, UserSigninForm
from .models import User
from django.contrib import messages


# user signup and save user to database
def user_signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            user = User.objects.create_user(username=username, email=email, password1=password1, password2=password2)

            user.set_password(password1)
            user.save()

            if user is not None:
                print('user created successfully')
            else:
                print('user not created')

            return redirect('login')
    else:
        form = UserSignupForm()
    context = {
        'form': form
    }
    return render(request, 'auth/register.html', context)


def user_login(request):
    if request.method == 'POST':
        form = UserSigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            print(username, password)
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Username or password is incorrect')
                return redirect('login')
    else:
        form = UserSigninForm()
    context = {
        'form': form
    }
    return render(request, 'auth/login.html', context)


@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')
