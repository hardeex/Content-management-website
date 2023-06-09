from django import forms
from . import models

category = models.BlogCategory.objects.all().values_list('name', 'name')
category_lists = []
for category_list in category:
    category_lists.append(category_list)

class CustomBlogPostForm(forms.ModelForm):
    class Meta:
        model = models.BlogPost
        fields = ('title', 'author', 'category', 'content')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Blog Title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Blog Title', 'value': '', 'id':'author', 'type': 'hidden'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices= category_lists,  attrs= {'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Blog Content'}),
        }