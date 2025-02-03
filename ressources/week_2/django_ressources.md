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

For creating a view, we type :
``` python
def index(request):
# The request keyword represent the HTTP request that the client made
```

