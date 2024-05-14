from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Book



class BookList(generic.ListView):
    queryset = Book.objects.all().order_by("booking_date")
    template_name = "home/index.html"
    paginate_by = 6


def booking_detail():
    """
    Display a :model`home.Book`.

    **Context**

    ``book``
        An instance of :model`home.Book`.

    **Template**

    :template:`home/booking_detail.html`
    """

    queryset = Book.objects.all()
    book = get_object_or_404(queryset, name=name)

    return render(
        request,
        "home/booking_detail.html",
        {"name": book},
    )






