from . import views
from django.urls import path
from . import views
from . views import JobHomeView, JobDetailsView, BlogHomeView, BlogDetailsView, AddPostView, EditPostView, DeletePostView, AddCategoryView
from  django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage


app_name = 'index'

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('images/favicon.ico'))),
    
    path('', views.home, name = 'home'),

    path('blog/', BlogHomeView.as_view(), name="blog_list"),
    path('blog/<int:pk>/', BlogDetailsView.as_view(), name='blog_details'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('blog/edit/<int:pk>', EditPostView.as_view(), name='edit_post' ),
    path('blog/<int:pk>/delete', DeletePostView.as_view(), name='delete_post' ),
    path('like/<int:pk>', views.LikeView, name='like_post'),
    
    path('job/', JobHomeView.as_view(), name="job_list"),
    path('job/<int:pk>/', JobDetailsView.as_view(), name='job_details'),

    
    path('add_category/', AddCategoryView.as_view(), name='add_category'),       
    path('category/<str:category_name>/', views.CategoryView, name='category_list'), 
    path('view_category/', views.ListCategory, name='view_category'), 

    path('<int:pk>/add_comment/', views.add_comment, name='add_comment')

]