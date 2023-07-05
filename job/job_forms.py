from django import forms
from . import models
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.models import User




category = models.JobCategory.objects.all().values_list('name', 'name')
category_lists = []
for category_list in category:
    category_lists.append(category_list)

class CustomJobPostForm(forms.ModelForm):
    deadline = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:
        model = models.JobPost
        fields = ('title', 'author', 'category', 'location', 'deadline', 'content')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control',  'value': '', 'id':'author', 'type': 'hidden'}),            
            'category': forms.Select(choices= category_lists,  attrs= {'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),            
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            
        }


class NewCommentForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())


    class Meta:
        model = models.JobComment
        fields = ( 'content',)

        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }