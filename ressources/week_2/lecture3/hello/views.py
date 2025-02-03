from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "hello/index.html")

def alice(request):
    return HttpResponse("Hello alice !")

def bob(request):
    return HttpResponse("Hello bob !")

def chalie(request):
    return HttpResponse("Hello chalie !")

def greet(request, name):
    return HttpResponse(f"Hello {name.capitalize()} !")
    
