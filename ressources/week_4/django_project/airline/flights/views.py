from django.shortcuts import render
from .models import Flight, Airport

def add_airport(code, city):
    # Create a new Airport instance
    airport = Airport(code=code, city=city)
    
    # Save the Airport instance to the database
    airport.save()

def add_flight(origin_code, destination_code):
    # Get the origin and destination Airport instances
    origin = Airport.objects.get(code=origin_code)
    destination = Airport.objects.get(code=destination_code)
    
    # Create a new Flight instance
    flight = Flight(origin=origin, destination=destination)
    
    # Save the Flight instance to the database
    flight.save()

# Create your views here.
def index(request):
    # Add sample airports
    add_airport('JFK', 'New York')
    add_airport('LAX', 'Los Angeles')
    
    # Add a sample flight
    add_flight('JFK', 'LAX')
    
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })