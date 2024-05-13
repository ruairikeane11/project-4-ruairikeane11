from django.shortcuts import render
from django.views import generic
from .models import Book



class BookList(generic.ListView):
    queryset = Book.objects.all().order_by("booking_date")
    template_name = "home/index.html"
    paginated_by = 4



