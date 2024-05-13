from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Contact(models.Model):
    name = models.CharField("Name", max_length=100)
    email = models.EmailField("E-mail")
    website = models.URLField("Website (optional)")
    message = models.TextField("Message")
    date = models.DateTimeField("Date Sent", auto_now_add=True)


class Location(models.Model):
    username = models.CharField("Username", max_length=100)
    lat = models.FloatField("Latitude")
    lng = models.FloatField("Longitude")
    date = models.DateTimeField("Date & Time", auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.date}"

