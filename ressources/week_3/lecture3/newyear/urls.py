from django.urls import include, path

from . import views 

urlpatterns = [
    # path("", views., name=""),
    path("", views.index, name="index"),
]