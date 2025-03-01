from django.shortcuts import render
from django.http import HttpRequest

def favourite_team_view(requset:HttpRequest):
    return render(requset,"main/FavouriteTeam.html")
def learn_view(requset:HttpRequest):
    return render(requset,"main/Learn.html")
def form_practice_view(request:HttpRequest):
    return render(request,"main/Form.html")
def ccs_practice_view(request:HttpRequest):
    return render(request,"main/LearnCSS.html")
def css_introduction_view(request:HttpRequest):
    return render(request,"main/FavouriteTeamWithCSS.html")
def ai_revolution_view(request:HttpRequest):
    return render(request,"main/AIRevolution.html")

def careers_cv_view(request:HttpRequest):
    return render(request,"main/cv.html")

def theme_store_view(request:HttpRequest):
    return render(request,"main/themestore.html")