from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from index.models import Profile
from django.forms import ImageField
from django.core.exceptions import ValidationError
from index.models import Comment
from ckeditor.widgets import CKEditorWidget
from mptt.forms import TreeNodeChoiceField
from contact.models import Contact


class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100,  widget= forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email',  'password1', 'password2')  

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)   

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'




class EditProfileForm(UserChangeForm):   
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100,  widget= forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100,  widget= forms.TextInput(attrs={'class': 'form-control'}))
    last_login = forms.CharField(max_length=100,  widget= forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    #is_superuser = forms.CharField(max_length=100,  widget= forms.CheckboxInput(attrs={'class': 'form-check'}))
    #is_superuser = forms.CharField(max_length=100,  widget= forms.TextInput(attrs={'class': 'form-check', 'readonly': 'readonly'}))
    #is_staff = forms.CharField(max_length=100,  widget= forms.CheckboxInput(attrs={'class': 'form-check'}))
    #is_active = forms.CharField(max_length=100,  widget= forms.CheckboxInput(attrs={'class': 'form-check'}))
    #date_joined = forms.CharField(max_length=100,  widget= forms.TextInput(attrs={'class': 'form-control'}))
    date_joined = forms.CharField(max_length=100,  widget= forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
   

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'last_login', 'date_joined')


class PasswordChangedForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(max_length=100, widget= forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(max_length=100,  widget= forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('username', 'new_password1', 'new_password2')  



MAX_FILE_SIZE = 2 * 1024 * 1024  # 2MB

def validate_file_size(value):
    if value.size > MAX_FILE_SIZE:
        raise ValidationError(f"The maximum file size allowed is {MAX_FILE_SIZE} bytes.")

class ProfilePageForm(forms.ModelForm):
    profile_pic = forms.ImageField(
        validators=[validate_file_size],
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = Profile
        fields = ('profile_pic', 'email_url', 'website_url', 'github_url', 'linkedln_url', 'facebook_url', 'twitter_url', 'instagram_url', 'whatsapp_url', 'bio')

        widgets ={
            'email_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Email'}),                
            'website_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Portfolio Link'}),
            'github_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Your GitHub Repo Link'}),
            'linkedln_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Linkedln Link'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Facebook Profile Link'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Twitter Profile Link'}),
            'whatsapp_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'WhatsApp Link'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Instagram Profile Link'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'About you'}),
        }

class NewCommentForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    parent = TreeNodeChoiceField(queryset=Comment.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
         
        self.fields['parent'].required = False 
        self.fields['parent'].label = ''
        self.fields['parent'].widget.attrs.update({'class': 'd-none'})

    class Meta:
        model = Comment
        fields = ('parent', 'content')


class ContactForm(forms.ModelForm):
    

    class Meta:
        model = Contact
        fields = ('subject', 'name', 'email', 'message')

        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }
