from django.db import models


class Airport(models.Models):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.code} ({self.city})"


class Flight(models.Model):
    origin = models.CharField(max_length=64)  # This is a char field
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()  # This is an INT field

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
