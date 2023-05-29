from django import forms
from . import models

class CustomBlogPostForm(forms.forms):
    class Meta:
        model = models.BlogPost
        fields = ('title', 'author', 'content')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.Textarea(attrs={'class': 'form-control'}),
        }