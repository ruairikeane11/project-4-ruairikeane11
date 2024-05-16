from django.shortcuts import render
from .models import Contact


def contact_us(request):
    """
    Renders the contact page
    """
    contact = Contact.objects.latest('created_on')

    return render(
        request,
        "contact/contact.html",
        {"contact": contact},
    )