from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Books
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class BookList(generic.ListView):
    """
    Displays recorded instances of Books model

    """
    template_name = "home/index.html"
    paginate_by = 3

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Books.objects.filter(user=self.request.user).order_by("booking_date")
        else:
            return Books.objects.none()


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

    book = get_object_or_404(Books, id=book_id, user=request.user)
    return render(
        request,
        "home/booking_detail.html",
        {"book": book},
    )


@login_required
def create_booking(request):
    """
    Add a record of Books to database
    """
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
    """
    Allows user to edit a record of Books and update in database.

    **Context**

    ``book``
        An instance of :model:`home.Books`.
    """
    book = get_object_or_404(Books, id=book_id, user=request.user)

    if request.method == "POST":
        form = BookingForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('bookings')
    else:
        form = BookingForm(instance=book)
    return render(request, 'home/edit_booking.html',
                  {'form': form, 'book': book})


@login_required
def delete_booking(request, book_id):
    """
    Allows user to delete a record of Books from database.

    **Context**

    ``book``
        An instance of :model:`home.Books`.
    """
    book = get_object_or_404(Books, id=book_id, user=request.user)
    book.delete()
    return redirect('bookings')


@login_required
def bookings(request):
    """
    Renders all records of Books.

    **Context**

    ``bookings``
        All records of model:`home.Books`.

    **Template:**

    :template:`blog/bookings.html`
    """
    bookings = Books.objects.filter(user=request.user)
    return render(request, 'home/bookings.html', {'book_list': bookings})


def menu_page(request):
    """
    Renders menu.html and all its content
    """
    return render(
        request,
        'home/menu.html',
    )
