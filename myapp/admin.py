from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    readonly_fields = ['user_agent']

admin.site.register(Comment)
