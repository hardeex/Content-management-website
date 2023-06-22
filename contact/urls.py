from . import views
from django.urls import path

app_name = 'contact'

urlpatterns = [
    path('contact/', views.Contact, name='contact'),
    path('contact_success/', views.Contact_success, name='contact_success')    
]