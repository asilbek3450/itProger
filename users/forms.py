from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import User


# forms for user signup and login views that create users and authenticate users in the database
class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ismingizni kiriting'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Familiyangizni kiriting'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Foydalanuvchi nomini kiriting'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Emailingizni kiriting'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parolni kiriting'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parolni takrorlang'}),
        }


class UserSigninForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Foydalanuvchi nomini kiriting...'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder': 'Foydalanuvchi parolini kiriting...'}))


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'image', 'phone_number', 'website', 'github', 'twitter', 'instagram', 'facebook']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ismingizni kiriting...'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Familiyangizni kiriting...'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon raqamingizni kiriting...'}),
            'website': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Veb-saytingizni kiriting...'}),
            'github': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Githubingizni kiriting...'}),
            'twitter': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Twitteringizni kiriting...'}),
            'instagram': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Instagramingizni kiriting...'}),
            'facebook': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Facebookingizni kiriting...'}),

        }
