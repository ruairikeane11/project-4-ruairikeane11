from django.shortcuts import render
from .models import Contact


def contact_us(request):
    """
    Renders the contact page
    """
    contact = Contact.objects.all()

    return render(
        request,
        "contact/contact.html",
        {"contact": contact},
    )