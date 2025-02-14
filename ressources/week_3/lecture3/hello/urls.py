from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), # Visiting the default view
]