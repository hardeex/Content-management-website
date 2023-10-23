from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.JobCategory)


@admin.register(models.JobPost)
class JobPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category',  'date')
    list_filter = ('title', 'author', 'category', 'date', 'deadline')
    search_fields = ('author', 'title', 'deadline', 'date')

@admin.register(models.JobComment)
class JobCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'date', 'status')
    list_filter = ('user', 'post', 'date', 'content')
    search_fields = ('user', 'post', 'date', 'content')


@admin.register(models.JobSaveAsDraft)
class SaveAsDraftAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category',  'date')
    list_filter = ('title', 'author', 'category', 'date', 'deadline')
    search_fields = ('author', 'title', 'deadline', 'date')

