from django.shortcuts import render
from django.http import HttpRequest, HttpResponse



def introduction(request:HttpRequest):
    return render(request,"introduction.html")

def style_intro(request:HttpRequest):
    return render(request,"style_introduction.html")

def article_ai(request:HttpRequest):
    return render(request,"article_ai.html")

def cv (request:HttpRequest):
    return render(request,"cv.html")


