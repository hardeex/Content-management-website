from django import forms
from . import models



category = models.BlogCategory.objects.all().values_list('name', 'name')
category_lists = []
for category_list in category:
    category_lists.append(category_list)

class CustomBlogPostForm(forms.ModelForm):
    class Meta:
        model = models.BlogPost
        fields = ('title', 'author', 'category', 'content', 'headline')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Blog Title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Blog Title', 'value': '', 'id':'author', 'type': 'hidden'}),        
            'category': forms.Select(choices= category_lists,  attrs= {'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Blog Content'}),
            'headline': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'A snippet of your post that captures readers mind to read your post '}),
        }
