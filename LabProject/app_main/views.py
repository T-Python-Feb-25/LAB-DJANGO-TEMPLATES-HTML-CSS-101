from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.



def first_html_page(request : HttpRequest):
    return render(request, "app_main/myِ_best_anime.html")

def css_view(request: HttpRequest):
    return render(request, "app_main/myِ_best_anime2.html")

def Ai_view(request : HttpRequest):
    return render(request, "app_main/Ai.html")


def cv_view(request : HttpRequest):
    return render(request, "app_main/cv.html")

def cafee_view(request : HttpRequest):
    return render(request, "app_main/index.html")


def menu_view(request : HttpRequest):
    return render(request, "app_main/menu.html")


def det_view(request : HttpRequest):
    return render(request, "app_main/details.html")


def caffee(request : HttpRequest):
    return render(request, "app_main/try_cafee.html")

def store_view(request : HttpRequest):
    return render(request, "app_main/try.html")

