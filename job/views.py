from django.shortcuts import render, get_object_or_404, redirect
from . import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#from . import custom_model_form
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from account.forms import NewCommentForm
from .models import JobPost
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger





# create classes the views
class JobHomeView(ListView):
    model = models.JobPost
    template_name = 'home/job_list.html'
    ordering = ['-pushlished_date']
    


class JobDetailsView(DetailView):
    model = models.JobPost
    template_name = 'home/job_details.html'