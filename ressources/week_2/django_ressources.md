## START A DJANGO PROJECT

```bash
django-admin startproject <PROJECT_NAME>
```

```text
manage.py
```

is a file we're going to interact with with the CLI.
Generally, we don't need to toch that file

```text
settings.py
```

is where all the configuration of our web-app is based

```text
urls.py
```

Think of it about a table of content for our web-app

PROJECT vs APP in Django

An app is a sub-component of a project.

For starting the whole project, we need to create an app :

```bash
python manage.py startapp <APP_NAME>
```

After it, we have some code on `settings.py`

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```

Where we need to add our app

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
	"hello", # HERE
]
```

NOTABENE : The order of the apps do not matters most of the time, unless we're dealing wit app dependencies, template loaders or migrations.

Now moving on on the `views.py` of th recently created app :

```python
from django.shortcuts import render

# Create your views here.

```

For creating a view, we need a function :

```python
def index(request):
# The request keyword represent the HTTP request that the client made
```

```python
from django.shortcuts import render
from django.http import HttpResponse # we need to import the ability from django to generate HTTP responses

def index(request):
    return HttpResponse("Hello, World !")
```

For connecting the whole project to the app, we need to create an additional `urls.py` within the app, so the app can manage its own urls

```python
# First we need to import path function
from django.urls import path

# Then import the views.py to leveraling the OOP views.index
from . import views

urlpatterns = [
    path("", views.index, name="index")
	# views.index actually reffers to the index functions in views.py of the same app
	# name="index" is usefull for giving a name to a particular URL pattern for referencing it in others parts of the application later on
]
```


This is what Django project `urls.py` looks like
```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]
```

In order to connect our app to our project, we need to connect the recently created app to the project's `urls.py` file.
This file kinda acts like a router, able to redirect all the routes towards the app route `urls.py` sub-files.

```python
from django.contrib import admin
# Need to import `include`
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello/", include("hello.urls")),
]
```

## LEVERAGING <str::name>

Thanks to the syntax `<str::name>` in the url, we can then dynamically generate names inputs

```python
path("<str:name>", views.greet, name="greet"),
```

```python
def greet(request, name):
    return HttpResponse(f"Hello {name.capitalize()} !")
```

## MAKING HTML PAGES

Consider this

```python
def greet(request):
    return HttpResponse("Hello, World !")
```

At the end of the day, this would be very tedious to generate a whole HTML page in a single string in Python.

Plus, we can ave multiple people working on one side on the Python logic, and the other working let's say on CSS, rearanging the front-end.

Django allows us so to separate multiple logics in multiple files.

We're going to use a `render` function which takes `request` and the path of the `.html` file we want to leverage

```python
def greet(request):
    return render(request, "hello/index.html")
```

In an app, we're going to create an folder called `templates` in which we create another folder called `hello` (the name of the app).

IMPORTANT :
Despite the newly created folder called `templates` is already inside the `hello` folder, we'll still create a subfolder for avoiding conflicts in namespaces.


## DJANGO TEMPLATES :

For leveraging templates, we can plug a `context` (a python `dict`) as last argument, where we can plug variables to be plugged in in the page.

```python
def greet(request, name):
    return render(request, "hello/greet.html", {
        "name" : name.capitalize(),
    })
```

For leveraging this template, we can use `{{ }}` within the HTML for pluggin variables.
```html
<!DOCTYPE html>
<html lang="en">
	<head>
		<title>Hello hehe</title>
	</head>
	<body>
		<h1>Hello, {{ name }}!</h1>
	</body>
</html>
```

We can also use DJango logic statements

```html
<!DOCTYPE html>
<html lang="en">

<head>
	<title> Is it New Year's ?</title>
</head>

<body>
	{% if newyear %}
	<h1> YES </h1>
	{% else %}
	<h1> YES </h1>
	{% endif %}
</body>

</html>
```


## STATIC FILES

Just like templates, Django have a lot of functions and libraries than can leverage static files.

The key here is to access to them quite easily within the app folder.

Here is what the folder organization looks like

```text
my_project/
 |
 |--- app/
 |    |--- __init__.py
 |    |--- admin.py
 |    |--- apps.py
 |    |--- models.py
 |    |--- tests.py
 |    |--- views.py
 |    |
 |    |--- migrations/
 |    |    |--- __init__.py
 |    |
 |    |--- templates/
 |    |    |--- app/
 |    |    |    |--- index.html
 |    |
 |    |--- static/
 |    |    |--- app/
 |    |    |    |--- css/
 |    |    |    |    |--- styles.css
 |    |    |    |--- js/
 |    |    |    |    |--- scripts.js
 |    |    |    |--- images/
 |    |    |    |    |--- logo.png
 |
 |--- manage.py
```

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">

<head>
	<title> Is it New Year's ?</title>
	<link rel="stylesheet" href="{% static 'newyear/styles.css' %}">
</head>
```

After placing css just like the architecture above, we can first `{% load static %}` and then tell Django to load static files dynamically










