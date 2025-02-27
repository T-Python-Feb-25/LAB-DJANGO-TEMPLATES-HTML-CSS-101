from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

# Introduction HTML
def introduction(request:HttpRequest):
  return render(request, "main/introduction.html")

# Introduction CSS
def css_introduction(request:HttpRequest):
  return render(request,"main/css_introduction.html")

# Build 
def home_view(request:HttpRequest):
  return render(request, "main/index.html")