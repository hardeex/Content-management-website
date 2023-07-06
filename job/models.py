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
    deadline = models.DateTimeField()
    location = models.CharField(max_length=150)    
    category = models.CharField(max_length=150)    
    content = RichTextField(blank=True, null=True, unique=True)    

    def __str__(self):
        return f" {self.title}"

    def get_absolute_url(self):
        return reverse('jobs:job_details', args=[str(self.id)] )

    def delete_expired_posts(self):
        expired_posts = JobPost.objects.filter(deadline__lt=timezone.now())
        expired_posts.delete()
        


class JobCategory(models.Model):
    name = models.CharField(max_length= 150, unique=True)
    
    class Meta:
        verbose_name_plural = 'Job Category'


    def __str__(self):
        return self.name

    #def get_absolute_url(self):
     #   return reverse('jobs:job_details', args=[str(self.id)] )

    def get_absolute_url(self):
        return reverse('jobs:job_list' )


   


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
