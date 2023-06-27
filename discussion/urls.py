from . import views
from django.urls import path
from . views import  DiscussionHomeView, DiscussionDetailsView, CreateDiscussionView, EditDiscussionPostView, DeleteDiscussionPostView
#from  django.views.generic.base import RedirectView




app_name = 'discussion'

urlpatterns = [
    path('discussion/', DiscussionHomeView.as_view(), name="discuss_list"),
    path('discussion/<int:pk>/', DiscussionDetailsView.as_view(), name='discuss_details'),
    path('create_discussion/', CreateDiscussionView.as_view(), name='create_discussion'),
    path('blog/edit/<int:pk>', EditDiscussionPostView.as_view(), name='edit_discussion_post' ),
    path('blog/<int:pk>/delete', DeleteDiscussionPostView.as_view(), name='delete_discussion_post' ),
    
    path('like/<int:pk>', views.DiscussionLikeView, name='like_post'),
     

    path('<int:pk>/add_comment/', views.add_discussion_comment, name='add_comment'),
]