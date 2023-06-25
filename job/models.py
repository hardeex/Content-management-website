from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from ckeditor.fields import RichTextField




# Create your models here.
class JobPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    deadline = models.CharField(max_length=150, default='Not specified')
    location = models.CharField(max_length=150)    
    category = models.CharField(max_length=150, default='uncategorized')    
    content = RichTextField(blank=True, null=True, unique=True)    

    def __str__(self):
        return f" {self.title}"

    def get_absolute_url(self):
        return reverse('jobs:job_details', args=[str(self.id)] )

        


class JobCategory(models.Model):
    name = models.CharField(max_length= 150, unique=True)
    
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('jobs:job_details', args=[str(self.id)] )


   


class JobComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(JobPost, on_delete=models.CASCADE, related_name='job_comments')
    content = RichTextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    
    
    class Meta:
        ordering = ('-date', )
    
    def __str__(self):
        return f"Comment By: {self.user}"
