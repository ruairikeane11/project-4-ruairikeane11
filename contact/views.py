from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
 

def contact_us(request):
    """
    Renders the contact page with ContactForm
    """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()

    return render (
        request,
        "contact/contact.html",
        {"form":form},
    )
        

