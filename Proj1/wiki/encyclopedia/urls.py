from django.urls import path
from django.urls import include
from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.new, name="new"),
    path("search/", views.search, name="search"),
    path("<str:title>", views.entry, name="entry"),
    path("<str:title>/edit", views.edit, name="edit"),
    path("edit/", views.edit, name="edit"),
    path("random_entry/", views.random_entry, name="random_entry")
]
