from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm
from django.contrib import messages
 

def contact_us(request):
    """
    Renders the contact page with ContactForm
    """

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            messages.success(request, "Your message has been submitted.")
    else:
        form = ContactForm()

    submitted_contacts = Contact.objects.all().order_by('-created_on')

    return render (
        request,
        "contact/contact.html",
        {"form":form,
        'submitted_contacts': submitted_contacts},
    )
        



def contact_delete(request, contact_id):
    """
    Deletes instance of ContactForm from database
    """
    contact = get_object_or_404(Contact, id=contact_id)
    contact.delete()
    messages.success(request, "Contact form successfully deleted")
    return redirect('contact')
