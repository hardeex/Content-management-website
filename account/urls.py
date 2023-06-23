from django.urls import path
from . views import UserRegisterView, UserEditProfileView, ChangePasswordView, ShowUserProfile, EditProfilePageView, CreateProfilePageVIew, ForgotPasswordView 
from django.contrib.auth import views as auth_views
from . import views


app_name = 'account'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
   
    path('password/', ChangePasswordView.as_view(template_name='registration/change_password.html'), name='password'),
    path('changed_password_successfully/', views.changed_password_successfully, name='changed_password_successfully'),

    path('edit_profile/', UserEditProfileView.as_view(), name='edit_profile'),
    path('<int:pk>/profile', ShowUserProfile.as_view(), name='user_profile'),
    path('<int:pk>/edit_profile_page', EditProfilePageView.as_view(), name='edit_profile_page'),  
    path('create_profile_page/', CreateProfilePageVIew.as_view(), name='create_profile'),

    path('forgot_password/', ForgotPasswordView.as_view(), name='forgot_password'), 
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm'), 
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
]