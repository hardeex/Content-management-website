from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.JobPost)
admin.site.register(models.BlogPost)
admin.site.register(models.BlogCategory)
admin.site.register(models.Profile)

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "user", "date", "status")
    list_filter = ("status", "date")
    search_field = ("user", "content")