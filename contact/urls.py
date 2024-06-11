from . import views
from django.urls import path

urlpatterns = [
    path('', views.contact_us, name='contact'),
    path('contact/delete/<int:contact_id>/',
         views.contact_delete, name='contact_delete'),
]
