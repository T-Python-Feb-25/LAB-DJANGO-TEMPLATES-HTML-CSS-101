from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def introduction_view(request: HttpRequest):
  return render(request, "main/introduction.html/")

def Css_introduction_view(request: HttpRequest):
  return render(request, "main/Css_introduction.html/")

def Article_AI_view(request: HttpRequest):
  return render(request, "main/article_aI.html/")

def Careers_CV_view(request: HttpRequest):
  return render(request, "main/careers-cv.html/")