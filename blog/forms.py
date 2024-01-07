from django import forms

from .models import BlogComment, BlogPost, BlogCategory


class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': '5', 'placeholder': 'Comment'})
        }
        labels = {
            'text': 'Comment'
        }


class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'description', 'short_description', 'image', 'category']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Maqola nomi'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Maqola haqida'}),
            'short_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Maqola haqida qisqacha'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Maqola rasmi'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Maqola kategoriyasi'}),
        }

        labels = {
            'title': 'Maqola nomi',
            'description': 'Maqola haqida',
            'short_description': 'Maqola haqida qisqacha',
            'image': 'Maqola rasmi',
            'category': 'Maqola kategoriyasi',
        }


class UpdateBlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'description', 'short_description', 'image', 'category']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Maqola nomi'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Maqola haqida'}),
            'short_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Maqola haqida qisqacha'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Maqola rasmi'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Maqola kategoriyasi'}),
        }

        labels = {
            'title': 'Maqola nomi',
            'description': 'Maqola haqida',
            'short_description': 'Maqola haqida qisqacha',
            'image': 'Maqola rasmi',
            'category': 'Maqola kategoriyasi',
        }


class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = BlogCategory
        fields = ['name', 'description']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kategoriya nomi'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Kategoriya haqida'}),
        }

        labels = {
            'name': 'Kategoriya nomi',
            'description': 'Kategoriya haqida',
        }
