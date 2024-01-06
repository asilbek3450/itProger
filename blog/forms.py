from django import forms

from .models import BlogComment


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

