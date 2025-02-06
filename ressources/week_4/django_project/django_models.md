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

### 1 - APPLYING THE MIGRATION