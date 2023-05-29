from django.shortcuts import render, get_object_or_404
from . import models
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

# create classes the views
class JobHomeView(ListView):
    model = models.JobPost
    template_name = 'home/job_list.html'
    


class JobDetailsView(DetailView):
    model = models.JobPost
    template_name = 'home/job_details.html'


class BlogHomeView(ListView):
    model = models.BlogPost
    template_name = 'home/blog_list.html'


class BlogDetailsView(DetailView):
    model = models.BlogPost
    template_name = 'home/blog_details.html'
    

class AddPostView(CreateView):
    model = models.BlogPost
    template_name = 'home/add_post.html'
    fields = '__all__'

# Create your views here.
def home(request):
    jobs = models.JobPost.objects.all()[:5]
    blogs = models.BlogPost.objects.all()[:5]
    return render(request, 'home/home.html',{
        'jobs': jobs,
        'blogs': blogs
    })


