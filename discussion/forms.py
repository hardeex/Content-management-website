from django import forms
from . import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextField
from mptt.models import MPTTModel, TreeForeignKey
from mptt.forms import TreeNodeChoiceField



class DiscussionForm(forms.ModelForm):
    class Meta:
        model = models.Discussion
        fields = ('title', 'author',  'content')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'author', 'type': 'hidden'}),                    
            'content': forms.Textarea(attrs={'class': 'form-control'}),           
        }




class NewCommentForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())


    class Meta:
        model = models.Comment
        fields = ( 'content',)

        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }