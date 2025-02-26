from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

# Introduction
def introduction(request:HttpRequest):
  return render(request, "main/introduction.html")