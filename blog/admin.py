from django.contrib import admin
from .models import Article

from tinymce.widgets import TinyMCE
from django.db import models
class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title", {'fields': ["title"]}),
        ("Content", {"fields": ["content"]})
    ]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }

admin.site.register(Article,ArticleAdmin)

