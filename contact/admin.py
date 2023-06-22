from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
   list_display = ("name", "name")
   list_filter = ("name", "email", "message")
   search_field = ("name", "email", "message")
