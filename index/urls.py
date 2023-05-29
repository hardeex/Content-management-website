from . import views
from django.urls import path
from . import views
from . views import JobHomeView, JobDetailsView, BlogHomeView, BlogDetailsView, AddPostView

app_name = 'index'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('blog/', BlogHomeView.as_view(), name="blog_list"),
    path('blog/<int:pk>/', BlogDetailsView.as_view(), name='blog_details'),
    path('job/', JobHomeView.as_view(), name="job_list"),
    path('job/<int:pk>/', JobDetailsView.as_view(), name='job_details'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    
]