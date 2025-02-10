from django.db import models

# Create your models here.

class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.code} ({self.city})"

    

class Flight(models.Model):
    # origin = models.CharField(max_length=64)
    # Now origin needs to be connected to the Airport Models
    
    # Defines a foreign key relationship to the Airport model, representing the origin airport.
    # If the referenced Airport is deleted, all related Flight instances will also be deleted (CASCADE).
    # The related_name 'departures' allows reverse lookup from Airport to its departing flights.
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures')

    # destination = models.CharField(max_length=64)
    '''
    The related_name attribute in a Django ForeignKey field is used to specify
    the name of the reverse relation from the related model back to the modelthat defines the ForeignKey.
    This allows you to access related objects in a more readable and convenient way.
    
    EX : airport.departures.all()
    '''
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')

    duration = models.IntegerField()

    # This method returns a human-readable string representation of the current object instance
    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first}, {self.last}"