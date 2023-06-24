from django.shortcuts import render, redirect
from . import views
from django.urls import path
from . views import JobHomeView, JobDetailsView


app_name = 'jobs'
urlpatterns = [
    path('job/', JobHomeView.as_view(), name="job_list"),
    path('job/<int:pk>/', JobDetailsView.as_view(), name='job_details'),
]