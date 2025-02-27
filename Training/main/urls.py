from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
  path("html/introduction/", views.introduction, name= "introduction"),
  path("css/introduction/", views.css_introduction, name="css_introduction")
]