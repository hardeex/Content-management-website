from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from ckeditor.fields import RichTextField
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.
class JobPost(models.Model):
    name = models.ForeignKey(User, on_delete = models.CASCADE )
    title = models.CharField(max_length=255)
    #pushlished_date = models.DateTimeField(auto_now_add=True)
    pushlished_date = models.DateField()
    deadline = models.DateField()
    location = models.CharField(max_length=50)
    requirement = models.TextField()
    qualification = models.TextField()
    description = models.TextField()
    apply = models.TextField()
   
    def __str__(self):
        return f"Job Position: {self.title} | Published Date: {self.pushlished_date} Deadline: {self.deadline} Post By: {self.name}"

class BlogCategory(models.Model):
    name = models.CharField(max_length= 150)
    
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index:blog_details', args=[str(self.id)] )


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    #date = models.DateTimeField()
    category = models.CharField(max_length=150, default='uncategorized')
    #category = models.ForeignKey(BlogCategory, on_delete = models.CASCADE)
    #content = models.TextField()
    content = RichTextField(blank=True, null=True, unique=True)
    headline = models.TextField(max_length=255)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def __str__(self):
        return f"Blog Title: {self.title} | Date Published: { self.date} |  Author: {self.author} | {self.category}"

    def get_absolute_url(self):
        return reverse('index:blog_details', args=[str(self.id)] )

    def total_likes(self):
        return self.likes.count()
        

   
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)   
    bio = RichTextField(blank=True, null=True)
    #bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    linkedln_url = models.CharField(max_length=255, blank=True, null=True)
    facebook_url =  models.CharField(max_length=255, blank=True, null=True)
    twitter_url= models.CharField(max_length=255, blank=True, null=True)
    instagram_url =  models.CharField(max_length=255, blank=True, null=True)
    whatsapp_url= models.CharField(max_length=255, blank=True, null=True)
    github_url=  models.CharField(max_length=255, blank=True, null=True)
    website_url= models.CharField(max_length=255, blank=True, null=True)
    email_url= models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return str(self.user)    

    def get_absolute_url(self):
        return reverse('index:home')

class Comment(MPTTModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    content = RichTextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    
    # MPTT implementation
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    #level = models.PositiveIntegerField(default=0)
    #lft = models.PositiveIntegerField(default=0)
    #rght = models.PositiveIntegerField(default=0)
    #tree_id = models.PositiveIntegerField(default=0)  
    
    class MPTTMeta:
        order_insertion_by = ['date']
    
    class Meta:
        ordering = ('date', )
    
    def __str__(self):
        return f"Comment By: {self.user}"


