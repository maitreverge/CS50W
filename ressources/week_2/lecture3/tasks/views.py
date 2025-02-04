from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


class NewTaskForm(forms.Form):
    task = forms.CharField(label="new_task")


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

def add(request):
    if request.method == "POST":
        # request.POST contains all the data the user submited
        form = NewTaskForm(request.POST)
        # Checking if the form is valid is making both a server side check even
        # if the client-side check seems to be valid
        # Imagine changing a form validation while client have the old html client-side checking
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form,
            })

    return render(request, "tasks/add.html", {
        "form" : NewTaskForm(),
    })

