from django.contrib import admin
from .models import Books
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Books)
class BookAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fileds for search,
    and list filters.
    """
    list_display = ('name', 'phone', 'booking_date', 'booking_time')
    search_fields = [ 'name', 'phone' ]
    list_filter = ('booking_date',)