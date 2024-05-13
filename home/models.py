from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    number_of_persons = models.PositiveIntegerField(default=1)
    booking_date = models.DateField()
    booking_time = models.TimeField()

    class Meta:
        ordering = ["booking_date"]

    def __str__ (self):
        return f"{self.name } | {self.booking_date} | {self.booking_time}"
