from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from ckeditor.fields import RichTextField
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.
class Discussion(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    date = models.DateTimeField(auto_now_add=True)    
    content = RichTextField(blank=True, null=True, unique=True)   
    likes = models.ManyToManyField(User, related_name='discuss_posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('discussion:discuss_details', args=[str(self.id)] )

    def total_likes(self):
        return self.likes.count()
        





class Comment(MPTTModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='discuss_user')
    post = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name='discuss_comments')
    content = RichTextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    
    # MPTT implementation
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
 
    
    class MPTTMeta:
        order_insertion_by = ['-date']
    

    
    def __str__(self):
        return f"Comment By: {self.user}"
