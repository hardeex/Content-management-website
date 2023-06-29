from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 50, unique=True)
    description = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()    
    completed = models.CharField(max_length=150, default='No')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('tasks:tasks_list')
