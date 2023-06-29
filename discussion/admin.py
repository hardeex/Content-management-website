from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin


# Register your models here.
admin.site.register(models.Comment, MPTTModelAdmin)

@admin.register(models.Discussion)
class DiscussionAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    list_filter = ('title', 'author',  'date')
    search_fields = ('author', 'title', 'date', 'content')
