from . import views
from django.urls import path

urlpatterns = [
    path('', views.BookList.as_view(), name='home'),
    path('<name:booking_date>/', views.booking_detail, name='booking_detail'),
]