from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse



# Create your models here.
class JobPost(models.Model):
    name = models.ForeignKey(User, on_delete = models.CASCADE )
    title = models.CharField(max_length=255)
    pushlished_date = models.DateField()
    deadline = models.DateField()
    location = models.CharField(max_length=50)
    requirement = models.TextField()
    qualification = models.TextField()
    description = models.TextField()
    apply = models.TextField()
   
    def __str__(self):
        return f"Job Position: {self.title} | Published Date: {self.pushlished_date} Deadline: {self.deadline} Post By: {self.name}"

class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    #date = models.DateTimeField()
    content = models.TextField()

    def __str__(self):
        return f"Blog Title: {self.title} | Date Published: { self.date} |  Author: {self.author}"

    def get_absolute_url(self):
        return reverse('index:blog_details', args=[str(self.id)] )
        

   
    