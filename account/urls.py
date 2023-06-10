from django.urls import path
from . views import UserRegisterView
#from . forms import registration_form

app_name = 'account'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    #path('account/', registration_form.as_view, name='account'),
]