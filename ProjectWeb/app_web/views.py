from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def page_view(request : HttpRequest):
    return render(request , "app_web/page_view.html")

def project_htmlone(request : HttpRequest):
    return render(request , "app_web/project_htmlone.html")

def css_view(request : HttpRequest):
    return render(request , "app_web/css_view.html")

def project_csstwo(request : HttpRequest):
    return render(request , "app_web/project_csstwo.html")

def ai_revolution_project(request : HttpRequest):
    return render(request , "app_web/ai_revolution_project.html")

def cv_project(request : HttpRequest):
    return render(request , "app_web/cv_project.html")