from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("alice/", views.alice, name="alice"),
    path("bob/", views.bob, name="bob"),
    path("chalie/", views.chalie, name="chalie"),
    # Pluggin the "<str:name>" as route allows
    # python to dynamically leverage any string passed
    # in the url
    path("<str:name>", views.greet, name="greet"),
]