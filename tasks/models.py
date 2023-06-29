from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100, unique=True)
    description = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('tasks:tasks_list')
