from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def HTML_view(request : HttpRequest):

    return render(request,"learning/html.html" )

def CSS_view(request : HttpRequest):
    return render(request,"learning/css.html")


def AI_view(request : HttpRequest):
    return render(request,"learning/ai.html" )


def CV_view(request : HttpRequest):
    return render(request, "learning/cv.html")