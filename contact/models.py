from django.db import models

# Create your models here.
class Contact(models.Model):
    subject = models.CharField(max_length=150)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return str(self.name, self.email)    

    def get_absolute_url(self):
        return reverse('contact:contact_success')
