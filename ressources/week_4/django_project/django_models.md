FROM QUENTIN :
Voir les interfaces utilisateurs de django (classes abstraites) 


# DJANGO MODELS

Models in Django world are a way of creating a python class which represent data I want django to store inside of a databse

When creating a model, Django figured out what SQL syntax to use from creating `TABLES` and manipulating `TABLES`.

Inside each Django App, we got a file named `models.py` where we're going to going to define what models are going to exists for out application.


- Every model (so every SQL tables) is going to a **python class**

```python
from django.db import models

# Create your models here.
class Flight(models.Model):
    origin = models.CharField(max_length=64) # This is a char field 
    destination = models.CharField(max_length=64)
    duration = models.IntegerField() # This is an INT field
```

At this point of creating a table in our `models.py`, Django didn't actually created anything.

```bash
ls
```

output:
```text
airline  flights  manage.py
```
At this point, we can't see anything created.

We need to tell Django to **UPDATE** the database to include those new informations about the model we've just created.

This manipulation is called a :

## DJANGO MIGRATION

A Django Migration is a two-steps process :

### 1 - CREATING THE MIGRATION

```bash
python3 manage.py makemigrations
```

After making a migrations as seen in the console
```text
Migrations for 'flights':
  flights/migrations/0001_initial.py
    + Create model Flight
```

We can see under the migrations folder a file called `0001_initial.py`

```python
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Flight",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("origin", models.CharField(max_length=64)),
                ("destination", models.CharField(max_length=64)),
                ("duration", models.IntegerField()),
            ],
        ),
    ]
```

This file is a set of python auto-generated instructions on how to manipulate the DB based on the changes we've made.


### 2 - APPLYING THE MIGRATION

```bash
python3 manage.py migrate
```

... and we'll see an output like this :

```text
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, flights, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying flights.0001_initial... OK
  Applying sessions.0001_initial... OK
```

And we can clearly identify our database 
```
  Applying flights.0001_initial... OK
```
within the logs.

Now we can see a new file `db.sqlite3` has been created !

## MANAGIN SQL with PYTHON SHELL

The python shell command which can be called with :

```bash
python3 manage.py shell
```

is usefull to interact with the web-app through the python interpreter.

Within this shell envirnoment, we can type straight python code 

```python
from flights.models import Flight
f = Flight(origin="New York", destination="London", duration="415")
f.save()
Flight.objects.all()
```
> [!NOTE]
> `f.save()` does actually saves with a SQL `insert` command throught Python interpreter
>  `Flight.objects.all()` is the SQL equivalent to `SELECT * FROM flights`


Querying the name actually outputs :
```text
Out[4]: <QuerySet [<Flight: Flight object (1)>]>
```

Which is not very usefull. Instead, we can define a `__str__` inside our model like

```python
    # This method returns a human-readable string representation of the current object instance
    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
```
*(which acts like a function which returns basics string representation of the class,and can now ask the shell back again)*

```python
from flights.models import Flight
flights = Flight.objects.all()
flights
```

```text
<QuerySet [<Flight: 1: New York to London>]>
```

We can push the logic further with typing within the shell

```python
flights = Flight.objects.all()
flight = flights.first()

# and then
# Outputs the `id` of the first flights
flight.id
# Outputs the `origin` of the first flights
flight.origin
# Outputs the `destination` of the first flights
flight.destination

# Then delete the current selected flight
flight.delete()
```

Once we want to implement a new model let's say `Airport` :

```python
class Airport(models.Models):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.code} ({self.city})"
```

We'll need to change out base model

```python
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
```

In order to finish this change, we need to make a migration once again

```bash
python3 manage.py makemigrations
```

```text
Migrations for 'flights':
  flights/migrations/0002_airport_alter_flight_destination_alter_flight_origin.py
    - Create model Airport
    - Alter field destination on flight
    - Alter field origin on flight
```
```bash
python3 manage.py migrate
```


## DJANGO SUPERUSER

```bash
python3 manage.py createsuperuser
```

After creating a superuser, we need to take those models and add them to the file `admin.py`

```python
from django.contrib import admin

from .models import Flight, Airport

# Those two lines tells Django that I want to use those two models with the admin app
admin.site.register(Airport)
admin.site.register(Flight)
```

Then we can register to the current admin page by typing the url

```bash
http://localhost:8000/admin/
```
(if port 8000 is our default port by Django server)


## CREATING CUSTOM FLIGHT PAGE

The goal here is to create an url like

```bash
http://localhost:8000/admin/flight/1
```

To have such result we need first another url

```python
    path("<int:flight_id>", views.flight, name="flight")
```

Then write the said function

```python
def flight(request, flight_id):
    # pk stands for primary key
    flight = Flight.objects.get(pk=flight_id)

    return render(request, "flights/flight.html", {
        "flight":flight
    })
```

Then write the custom HTML

```html
{% extends "flights/layout.html" %}

{% block body %}
<h1>Flight {{ flight.id }}</h1>

<ul>
	<li>Origin: {{ flight.origin }}</li>
	<li>Destination: {{ flight.destination }}</li>
	<li>Duration: {{ flight.duration }}</li>
</ul>
{% endblock %}
```

## CREATING A PASSENGER CLASS

```python
class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
	# The blank attribute is here to tell Django : The passenger can exists without necessary having a flight
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first}, {self.last}"
```
















```python

```

```python

```