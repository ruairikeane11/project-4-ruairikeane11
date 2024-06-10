from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Book
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class BookList(generic.ListView):
    """
    queryset = Book.objects.all().order_by("booking_date")
    """
    template_name = "home/index.html"
    paginate_by = 3

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Book.objects.filter(user=self.request.user).order_by("booking_date")
        else:
            return Book.objects.none()


@login_required
def booking_detail(request, book_id):
    """
    Display a :model`home.Book`.

    **Context**

    ``book``
        An instance of :model`home.Book`.

    **Template**

    :template:`home/booking_detail.html`
    """

    book = get_object_or_404(Book, id=book_id, user=request.user)
    return render(
        request,
        "home/booking_detail.html",
        {"book": book},
    )


@login_required
def create_booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('bookings')
    else:
        form = BookingForm()
    return render(request, "home/create_booking.html", {'form': form})


@login_required
def edit_booking(request, book_id):
    book = get_object_or_404(Book, id=book_id, user=request.user)

    if request.method == "POST":
        form = BookingForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookingForm(instance=book)
    return render(request, 'home/edit_booking.html', {'form': form, 'book': book})


@login_required
def delete_booking(request, book_id):
    book = get_object_or_404(Book, id=book_id, user=request.user)
    book.delete()
    return redirect('bookings')

@login_required
def bookings(request):
    paginate_by = 3
    bookings = Book.objects.filter(user=request.user)
    return render (request, 'home/bookings.html', {'book_list':bookings })


def menu_page(request):
    return render(
        request, 
        'home/menu.html',
    )

