from django import forms 
from .models import Book

class BookingForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'email', 'number_of_persons', 'booking_date', 'booking_time']