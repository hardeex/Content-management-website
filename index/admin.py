from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.JobPost)
admin.site.register(models.BlogPost)
admin.site.register(models.BlogCategory)
admin.site.register(models.Profile)
admin.site.register(models.Comment)