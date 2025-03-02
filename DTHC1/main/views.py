from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def home_view(request:HttpRequest):
    
    return render(request, "main/index.html")


def ctsv_view(request:HttpRequest):
    
    return render(request, "main/Fpage.html")

def Ctsv2_view(request:HttpRequest):
    
    return render(request, "main/Spage.html")

def Ai_view(request:HttpRequest):
    
    return render(request, "main/Aipage.html")

def cv_view(request:HttpRequest):
    
    return render(request, "main/cvpage.html")