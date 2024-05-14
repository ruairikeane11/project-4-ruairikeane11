from . import views
from django.urls import path

urlpatterns = [
    path('', views.BookList.as_view(), name='home'),
    path('<int:book_id>/', views.booking_detail, name='booking_detail'),
]