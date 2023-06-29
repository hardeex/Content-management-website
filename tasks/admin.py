from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'description',  'due_date')
    list_filter = ('user', 'name',   'due_date', )
    search_fields = ('user', 'name',   'due_date')