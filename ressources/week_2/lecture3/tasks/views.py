from django.shortcuts import render

tasks = ["foo", "bar", "baz"]
def index(request):
    # render a list with render tasks
    return render(request, "tasks/index.html", {
        # django template html : code 
        "tasks" : tasks
    })

def add(request):
    return render(request, "tasks/add.html")

