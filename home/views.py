from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
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
            







