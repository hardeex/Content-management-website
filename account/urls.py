from django.urls import path
from . views import UserRegisterView, UserEditProfileView, ChangePasswordView
from django.contrib.auth import views as auth_views
from . import views


app_name = 'account'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditProfileView.as_view(), name='edit_profile'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html'), name='password')
    path('password/', ChangePasswordView.as_view(template_name='registration/change_password.html'), name='password'),
    path('changed_password_successfully/', views.changed_password_successfully, name='changed_password_successfully'),
]