from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import User


# forms for user signup and login views that create users and authenticate users in the database
class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserSigninForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Foydalanuvchi nomini kiriting...'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder': 'Foydalanuvchi parolini kiriting...'}))


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'image', 'phone_number', 'website', 'github', 'twitter', 'instagram', 'facebook']

