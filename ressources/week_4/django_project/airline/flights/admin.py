from django.contrib import admin

from .models import Flight, Airport

# Those two lines tells Django that I want to use those two models with the admin app
admin.site.register(Airport)
admin.site.register(Flight)