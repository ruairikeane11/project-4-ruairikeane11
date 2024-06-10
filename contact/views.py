from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
 

def contact_us(request):
    """
    Renders the contact page with ContactForm
    """

    submitted_content = None


    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            submitted_content = contact.content
            form = ContactForm()
    else:
        form = ContactForm()

    return render (
        request,
        "contact/contact.html",
        {"form":form, 'submitted_content': submitted_content},
    )
        

