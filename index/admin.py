from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin


# Register your models here.
admin.site.site_header = 'JDD WEBMASTER LIMITED'
admin.site.register(models.BlogCategory)
admin.site.register(models.Profile)
admin.site.register(models.Comment, MPTTModelAdmin)

@admin.register(models.BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category',  'date')
    list_filter = ('title', 'author', 'category', 'date')
    search_fields = ('author', 'title', 'content', 'category', 'date')


@admin.register(models.SaveAsDraft)
class SaveAsDraftAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category',  'date')
    list_filter = ('title', 'author', 'category', 'date')
    search_fields = ('author', 'title', 'content', 'category', 'date')






