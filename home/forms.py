from django import forms 
from .models import Books

class BookingForm(forms.ModelForm):
    """
    Form class for users to make a booking
    """
    class Meta:
        model = Books
        fields = ['name', 'email', 'number_of_persons', 'booking_date', 'booking_time']
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'}),
        }