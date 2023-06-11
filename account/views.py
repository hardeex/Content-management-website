from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import RegisterForm, EditProfileForm, PasswordChangedForm
from django.contrib.auth.views import PasswordChangeView
from . import models


class UserRegisterView(generic.CreateView):
    #form_class = UserCreationForm
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditProfileView(generic.UpdateView):
    #form_class = UserCreationForm
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('index:home')    

    def get_object(self):
        return self.request.user

class ChangePasswordView(PasswordChangeView):
    form_class = PasswordChangedForm
    #form_class = PasswordChangedForm
    success_url = reverse_lazy('account:changed_password_successfully') 

def changed_password_successfully(request):
    return render(request, 'registration/changed_password_successfully.html')
