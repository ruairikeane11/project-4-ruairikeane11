from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Books(models.Model):
    """
    Stores a single booking request related to :model:`auth.User`.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    number_of_persons_choices = [
        ('1','1'),
        ('2', '2'),
        ('3','3'),
        ('4+','4+'),
    ]
    number_of_persons = models.CharField(max_length=2, choices=number_of_persons_choices)
    booking_date = models.DateField()
    booking_time_choices = [
        ('14:00', '14:00'),
        ('14:30', '14:30'),
        ('15:00', '15:00'),
        ('15:30', '15:30'),
        ('16:00', '16:00'),
        ('16:30', '16:30'),
        ('17:00', '17:00'),
        ('17:30', '17:30'),
        ('18:00', '18:00'),
        ('18:30', '18:30'),
        ('19:00', '19:00'),
        ('19:30', '19:30'),
        ('20:00', '20:00'),
        ('20:30', '20:30'),
        ('21:00', '21:00'),
        ('21:30', '21:30'),
        ('22:00', '22:00'),
        ('22:30', '22:30'),
    ]
    booking_time = models.CharField(max_length=5, choices=booking_time_choices)

    class Meta:
        ordering = ["booking_date"]

    def __str__(self):
        return f"{self.name}|{self.email}"
