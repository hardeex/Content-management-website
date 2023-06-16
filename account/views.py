from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import RegisterForm, EditProfileForm, PasswordChangedForm, ProfilePageForm, CommentForm
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView, CreateView
from index.models import Profile
from django.conf import settings
from django.contrib.auth.decorators import login_required
from index.models import BlogPost


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

    def form_valid(self, form):
        profile = form.instance
        if not profile.profile_pic:  # Check if profile_pic field is empty
            profile.profile_pic = settings.DEFAULT_PROFILE_PIC_URL  # Assign default profile picture URL
        return super().form_valid(form)


class ChangePasswordView(PasswordChangeView):
    form_class = PasswordChangedForm
    #form_class = PasswordChangedForm
    success_url = reverse_lazy('account:changed_password_successfully') 

def changed_password_successfully(request):
    return render(request, 'registration/changed_password_successfully.html')

class ShowUserProfile(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'


    def get_context_data(self, *args, **kwargs):
        #users = Profile.objects.all()
        context = super(ShowUserProfile, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context


class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    #fields = '__all__'
    form_class = ProfilePageForm
    success_url = reverse_lazy('index:home')


class CreateProfilePageVIew(CreateView):
    model = Profile
    template_name = 'registration/create_user_profile.html'
    #fields = '__all__'
    form_class = ProfilePageForm
    

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


