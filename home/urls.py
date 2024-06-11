from . import views
from django.urls import path

urlpatterns = [
    path('', views.BookList.as_view(), name='home'),
    path('<int:book_id>/', views.booking_detail, name='booking_detail'),
    path('booking/new', views.create_booking, name='create_booking'),
    path('edit_booking/<int:book_id>/',
         views.edit_booking, name='edit_booking'),
    path('delete_booking/<int:book_id>/',
         views.delete_booking, name='delete_booking'),
    path('menu/', views.menu_page, name='menu'),
    path('bookings/', views.bookings, name='bookings'),
]
