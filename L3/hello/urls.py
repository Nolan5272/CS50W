from django.urls import path

from . import views

urlpatterns = [

    path("", views.index, name="index"),
    path("nolgy", views.nolgy, name="nolgy"),
    path("<str:name>", views.greet, name="greet")

]