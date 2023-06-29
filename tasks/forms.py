from . import models
from django import forms



class TaskForm(forms.ModelForm):
    due_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    start_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    


    class Meta:
        model = models.Tasks
        fields = ('name', 'description', 'start_date', 'due_date')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            #'user': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'task_user', 'type': 'hidden'}),        
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
