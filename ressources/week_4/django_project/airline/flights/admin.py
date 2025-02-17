from django.contrib import admin

from .models import Flight, Airport, Passenger

# Those two lines tells Django that I want to use those two models with the admin app
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

# Horizontal filter gives us the ability to drop something from
# the left to the right
class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)

admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)
