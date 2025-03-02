from django.urls import path 
from . import views

name_app="main"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("html/introduction/", views.introduction_view, name="introduction_view")
]

