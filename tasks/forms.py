from .models import Tasks
from django import forms




class TaskForm(forms.ModelForm):
    due_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    start_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    
    completed_choices = [
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('In-Progress', 'In-Progress'),
        ('Yet to start', 'Yet to start')
    ]

    completed = forms.ChoiceField(choices=completed_choices, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Tasks
        fields = ('name', 'description', 'completed', 'start_date', 'due_date')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
