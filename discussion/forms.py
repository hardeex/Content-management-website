from django import forms
from . import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextField
from mptt.models import MPTTModel, TreeForeignKey
from mptt.forms import TreeNodeChoiceField
from . models import Comment



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
    parent = TreeNodeChoiceField(queryset=Comment.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
         
        self.fields['parent'].required = False 
        self.fields['parent'].label = ''
        self.fields['parent'].widget.attrs.update({'class': 'd-none'})

    class Meta:
        model = models.Comment
        fields = ('parent', 'content')

        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }