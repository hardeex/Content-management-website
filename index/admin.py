from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin


# Register your models here.
admin.site.register(models.JobPost)
#admin.site.register(models.BlogPost)
admin.site.register(models.BlogCategory)
admin.site.register(models.Profile)
admin.site.register(models.Comment, MPTTModelAdmin)

@admin.register(models.BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category',  'date')
    list_filter = ('title', 'author', 'category', 'date')
    search_field = ('author', 'title', 'content', 'category', 'date')

#@admin.register(models.Comment)
#class CommentAdmin(admin.ModelAdmin):
 #   list_display = ("post", "user", "date", "status")
  #  list_filter = ("status", "date")
   # search_field = ("user", "content")