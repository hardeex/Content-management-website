from . import views
from django.urls import path
from . import views
from . views import JobHomeView, JobDetailsView, BlogHomeView, BlogDetailsView, AddPostView, EditPostView, DeletePostView
from  django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

app_name = 'index'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('blog/', BlogHomeView.as_view(), name="blog_list"),
    path('blog/<int:pk>/', BlogDetailsView.as_view(), name='blog_details'),
    path('job/', JobHomeView.as_view(), name="job_list"),
    path('job/<int:pk>/', JobDetailsView.as_view(), name='job_details'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('images/favicon.ico'))),
    path('blog/edit/<int:pk>', EditPostView.as_view(), name='edit_post' ),
    path('blog/<int:pk>/delete', DeletePostView.as_view(), name='delete_post' ),
    
]