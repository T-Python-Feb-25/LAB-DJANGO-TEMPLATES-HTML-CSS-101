from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.


def introToHTML(request: HttpRequest):

    return render(request, "main/html/introtohtml.html")


def introToCSS(request: HttpRequest):

    return render(request, "main/css/introduction.html")


def articleAi(request: HttpRequest):

    return render(request, "main/articleai.html")


def careercv(request: HttpRequest):

    return render(request, "main/careercv.html")
