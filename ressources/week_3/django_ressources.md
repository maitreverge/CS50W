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

## EXTENDS and BLOCKS

```html
{% extends "tasks/layout.html" %}

{% block body %}

<body>
	<form action="">
		<input type="text", name="task">
		<input type="submit">
	</form>
</body>
<a href="{% url 'index' %}"> Back to list tasks</a>

{% endblock %}
```

```html
<!-- base HTML -->
<!DOCTYPE html>
<html lang="en">

<head>
	<title>Tasks</title>
</head>

<body>
	<!-- presence of blocks which can be extended -->
	{% block body %}
	{% endblock %}
</body>

</html>
```


## DYNAMICS URLS and route collisions

```html
<a href="{% url 'index' %}"> Back to list tasks</a>
```

When working with urls, we can dynamically insert links, but problem can be that we have differents pages named `index` in `urls.py` files.

To avoid collisions, we can specify in each app :

```python
from django.urls import path
from . import views

##############################
# We can specify that this name is called tasks
app_name = "tasks"
##############################
urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
]
```

... and when it's time to specify urls we can insert `tasks:index` to avoid collision
```html
<a href="{% url 'tasks:index' %}"> Back to list tasks</a>
```

## CSFR

## CSRF (Cross-Site Request Forgery)

CSRF is an attack that tricks the user into performing actions they didn't intend to. Django provides built-in protection against this.

When creating forms in Django, it's important to include a CSRF token to ensure the form is submitted from your site.

Here's an example of a form with CSRF protection:

```html
<form action="/submit/" method="post">
	{% csrf_token %}
	<input type="text" name="task">
	<input type="submit" value="Add Task">
</form>
```

The `{% csrf_token %}` tag generates a unique token for the form, which Django checks when the form is submitted. This helps prevent malicious sites from submitting forms on behalf of your users.

Always include `{% csrf_token %}` in your forms to maintain good security practices.

When viewing the source code of such forms, we can see for example :
```html

<body>
	<form action="/tasks/add" method="post">
		<input type="hidden" name="csrfmiddlewaretoken" value="yjaVM5SOJNSdSw6g6RjhLBYRWQdEPZSPxJ0Ah063mHT14kyRNoojiABzOfqCQe">
		<input type="text" , name="task">
		<input type="submit">
	</form>
</body>
```

## FORMS IN DJANGO

Because Forms in web-app is so commonly used, Django comes with `forms`

```python
from django import forms
```

First we start by creating a new form :

```python
class NewTaskForm(forms.Form):
    task = forms.CharField(label="new_task")
```

... then we pass a new object as context
```python
def add(request):
    return render(request, "tasks/add.html", {
        "form" : NewTaskForm(),
    })
```

... to finally plug it into 
```html
	<form action="{% url 'tasks:add' %}" method="post">
		{% csrf_token %}
		<!-- HERE -->
		{{ form }}
		<!-- HERE -->
		<input type="submit">
	</form>
```

## GET vs POST methods

Within a webpage with a form, we can either `GET` the webpage and also `POST` let's say a form.

Problem is, we need to differenciate the method that arrives from the client.

```python
def add(request):
    if request.method == "POST":
        # request.POST contains all the data the user submited
		# And we put it 
        form = NewTaskForm(request.POST)

        # Checking if the form is valid is making both a server side check even
        # if the client-side check seems to be valid.
		#! NEVER TRUST THE CLIENT
        # Imagine changing a form validation while client have the old html client-side checking
        if form.is_valid():
			# Extract the field named "task"
            task = form.cleaned_data["task"]
			# and appending it to the list
            tasks.append(task)
        else:
            return render(request, "tasks/add.html", {
				# If the form in invalid, we pass to the client the same form he tried to sumbit
				# So he can actually see what mistakes he made
                "form": form,
            })

    return render(request, "tasks/add.html", {
        "form" : NewTaskForm(),
    })
```

At this point, after submitting the form, we actually posted our stuff on the list.

Problem is, it is not obvious to the user what we actually posted.

We can then redirect the user to a page quite elegantely :

```python
return HttpResponseRedirect(reverse("tasks:index"))
```

`HttpResponseRedirect`: This is a class provided by Django that generates an HTTP response which redirects the user to a specified URL. When a user accesses a view that returns an `HttpResponseRedirect`, their browser is instructed to navigate to the new URL.

`reverse`("tasks:index"): The `reverse` function is used to look up the URL for a given view by its name.

## DJANGO SESSIONS

Problem is right now, we have another problem : We face having some sort of same rendering accross different clients.

We do not want our to-do list to be shared with others people's todolists.

So instead of storing data in a global variable like

```python
tasks = []
```

We not enable the creation of empty table for the current connected user

```python
# Store the data inside user session instead of globally
# tasks = []

def index(request):
    # render a list with render tasks
    if "tasks" not in request.session:
        # If the user does not have already a list of tasks, give it an empty list to him
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        # django template html : code 
        # "tasks" : tasks
        
        # Now that we have a session, we need to render the "tasks" from the session
        "tasks": request.session["tasks"]
    })
```

Just doing this is not enough, because we moved the storage from a `global_variable` to a session, which do not exists yet if we just refresh the page.

We might get something like this :

```text
OperationalError at /tasks/

no such table: django_session
```

For creating such table, we need to run the command

```bash
python3 manage.py migrate
```

Migration includes everything that was in memory in a database for sure.






