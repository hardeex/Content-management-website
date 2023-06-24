from django import forms
from . import models



category = models.JobCategory.objects.all().values_list('name', 'name')
category_lists = []
for category_list in category:
    category_lists.append(category_list)

class CustomJobPostForm(forms.ModelForm):
    class Meta:
        model = models.JobPost
        fields = ('title', 'author', 'category', 'location', 'deadline', 'content')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control',  'value': '', 'id':'author', 'type': 'hidden'}),            
            'category': forms.Select(choices= category_lists,  attrs= {'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'deadline': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            
        }
