from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Flight, Passenger
# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights" : Flight.objects.all()
    })

def flight(request, flight_id):
    # pk stands for primary key
    flight = Flight.objects.get(pk=flight_id)

    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers" : flight.passengers.all(),
        "non_passengers" : Passenger.objects.exclude(flights=flight).all()
    })

def book(request, flight_id):
    if request.method == "POST":
        # Get the flight object based on the primary key (flight_id)
        flight = Flight.objects.get(pk=flight_id)
        
        # Get the passenger object based on the ID from the POST request
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        
        # Add the flight to the passenger's list of flights
        passenger.flights.add(flight)
        
        # Redirect to the flight page after booking
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))
