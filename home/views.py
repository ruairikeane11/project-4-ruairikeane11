from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Book
from .forms import BookingForm



class BookList(generic.ListView):
    queryset = Book.objects.all().order_by("booking_date")
    template_name = "home/index.html"
    paginate_by = 6



def booking_detail(request, book_id):
    """
    Display a :model`home.Book`.

    **Context**

    ``book``
        An instance of :model`home.Book`.

    **Template**

    :template:`home/booking_detail.html`
    """

    book = get_object_or_404(Book, id=book_id)

    return render(
        request,
        "home/booking_detail.html",
        {"book": book},
    )



def create_booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookingForm()
    return render(request, "home/create_booking.html", {'form': form})

def edit_booking(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        form = BookingForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookingForm(instance=book)
    return render(request, 'home/edit_booking.html', {'form': form, 'book': book})


def delete_booking(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('home')

def menu_page(request):
    return render(
        request, 
        'home/menu.html',
    )







            







