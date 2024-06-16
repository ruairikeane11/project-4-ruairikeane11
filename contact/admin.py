from django.contrib import admin
from .models import Contact
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Contact)
class AboutAdmin(SummernoteModelAdmin):
    """
    Adds rich-text editing of content in admin
    """
    summernote_fields = ('content',)
