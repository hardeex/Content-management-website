from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.JobCategory)


@admin.register(models.JobPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category',  'date')
    list_filter = ('title', 'author', 'category', 'date', 'deadline')
    search_field = ('author', 'title', 'deadline', 'date')

