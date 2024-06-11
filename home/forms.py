from django import forms 
from .models import Book

class BookingForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['booking_date']
        fields = ['name', 'email', 'number_of_persons', 'booking_date', 'booking_time']
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'}),
            'booking_time': forms.TimeInput(attrs={'type': 'time'})

        }