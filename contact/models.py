from django.db import models

# Create your models here.
class Contact(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    content = models.TextField()

    def __str__(self):
        return self.title

